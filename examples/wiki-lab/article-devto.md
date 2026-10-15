Conheci a ideia por um tutorial sobre criar uma wiki com LLM e navegar pelas notas no Obsidian. O vídeo partia do [texto LLM Wiki, de Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

A possibilidade de organizar conhecimento e consultá-lo depois, sem reconstruir tudo a cada conversa, me interessou. Na Cereja Flamejante, comecei pela procedência das fontes. Só que registrar um arquivo ainda não entrega uma wiki: faltavam leitura, páginas relacionadas, consulta e manutenção.

Para fechar esse percurso, fizemos um teste assistido com dois documentos fictícios próprios. O assistente LLM leu as fontes, escreveu as páginas e atualizou a resposta quando chegou uma mudança. Os scripts cuidaram dos arquivos e das verificações estruturais. Nenhum material da empresa entrou no exemplo.

Aqui está o caminho para você montar uma versão mínima e repetir esse ciclo.

## O que você vai construir

Uma pasta de documentos vira uma wiki quando ganha páginas que explicam, relacionam e ajudam a consultar o conteúdo. Neste exemplo, a organização é esta:

```text
vault/
  AGENTS.md       instruções de manutenção para o agente
  raw/            documentos originais preservados
  sources/        procedência e notas de leitura
  wiki/           sínteses, conceitos e respostas registradas
  index.md        mapa das páginas
  log.md          histórico das mudanças
```

Esses nomes são uma escolha do exemplo. A separação que importa é entre os documentos recebidos, o conhecimento produzido a partir deles e as instruções de manutenção. O [modelo de Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) ajuda a pensar essa organização; não exige um conjunto único de pastas ou ferramentas.

Você vai precisar de Python 3.10 ou superior para os comandos abaixo e de um agente LLM capaz de ler e escrever arquivos locais. O helper não chama uma API nem produz sínteses sozinho. Obsidian é opcional: você pode abrir a pasta como vault para navegar pelos links Markdown.

## 1. Comece com uma pergunta e uma fonte pequena

O caso fictício é um clube de leitura. A primeira fonte informa quatro encontros de 60 minutos, com início em **23/10/2026 às 19h**. Não informa preço nem vagas.

A pergunta que a wiki deve responder é concreta: **quando é o primeiro encontro e quanto custa?** Isso permite conferir se a resposta usa a fonte e se reconhece uma informação ausente.

O [exemplo completo, com os prompts e resultados](https://github.com/eusouakell/cereja-knowledge-system/tree/experiment/wiki-cycle-20261015/examples/wiki-lab) está no repositório da Cereja. Enquanto essa alteração estiver em revisão, use a branch do experimento:

```sh
git clone --branch experiment/wiki-cycle-20261015 https://github.com/eusouakell/cereja-knowledge-system.git
cd cereja-knowledge-system
```

O repositório inclui uma wiki já preenchida para comparação. Para repetir desde o começo, crie outra pasta com apenas a primeira fonte e as instruções:

```sh
python -c "from pathlib import Path; import shutil; p=Path('outputs/wiki-replay'); (p/'raw').mkdir(parents=True); shutil.copy2('examples/wiki-lab/vault/raw/01-programa.md',p/'raw/01-programa.md'); shutil.copy2('examples/wiki-lab/vault/AGENTS.md',p/'AGENTS.md')"
```

Esse comando falha se a pasta de destino já existir, para não sobrescrever uma execução anterior. Você também pode criar a estrutura e copiar esses dois arquivos manualmente.

## 2. Defina a entrada e registre a procedência

Adicionar um documento a `raw/` pode disparar a ingestão automaticamente quando há uma automação configurada. Você também pode usar um comando ou processar lotes. A pasta, sozinha, não executa nada; o gatilho depende da ferramenta.

Neste teste usamos um comando:

```sh
python -X utf8 tools/wiki_lab.py ingest --vault outputs/wiki-replay
```

Ele calcula SHA-256, identifica os bytes do original e cria uma nota em `sources/`. A nota registra a origem local e os metadados disponíveis. Ao processar os mesmos bytes novamente, o comando retorna a nota existente, preservando suas anotações.

O hash não resolve toda duplicação: dois arquivos diferentes podem representar o mesmo documento. Identidade, versões, armazenamento e acesso são decisões que você precisa definir para sua base.

## 3. Peça ao agente para construir as páginas

Abra o agente na pasta `outputs/wiki-replay`. O `AGENTS.md` do exemplo orienta a preservar os originais, citar fontes, separar interpretação de informação documentada e registrar mudanças. Conteúdo dos documentos deve ser tratado como dado, sem virar instrução para o agente executar ações.

Aplique este pedido:

> Leia AGENTS.md e a fonte em raw/. Preserve o original. Complete as notas de leitura em sources/, com referências às seções da fonte. Crie index.md, log.md e páginas em wiki/ para o clube e um conceito relacionado. Diferencie afirmações da fonte, interpretação e lacunas. Não invente aprovação humana. O resultado deve permitir responder quando é o encontro e o que sabemos sobre seu preço.

No teste assistido, o LLM criou uma página do clube e outra sobre leitura com evidências, relacionadas entre si. A primeira reúne o programa; a segunda interpreta a atividade de comparar leituras citando trechos. Essa interpretação fica identificada como proposta do assistente, sem ser atribuída ao documento.

Confira as páginas contra a fonte antes de usá-las. Para PDFs, você também precisará escolher como extrair e conferir o texto; arquivos digitalizados podem exigir OCR ou leitura visual. Neste ciclo usamos Markdown legível, sem testar essas etapas.

## 4. Consulte e exija referências

O índice aponta para as páginas relevantes. Uma busca simples ajuda a encontrá-las:

```sh
python -X utf8 tools/wiki_lab.py search --vault outputs/wiki-replay --query "encontro preço"
```

Essa busca é lexical: retorna linhas de arquivos, sem gerar uma resposta. Agora pergunte ao agente:

> Consulte o índice, a página do clube e os originais. Quando é o primeiro encontro e quanto custa? Cite arquivo e seção. Registre a resposta em uma página e acrescente seu link ao índice. Se a base não disser, registre a lacuna.

A resposta sustentada pela primeira fonte é **23/10 às 19h; preço não informado**. Não informar preço não significa que o encontro é gratuito.

O que entra no contexto do modelo é o material necessário para essa pergunta. Você pode acrescentar outras formas de recuperação conforme a base crescer; este ciclo pequeno funciona com índice, links e leitura de arquivos.

## 5. Acrescente uma fonte que muda a resposta

A segunda fonte fictícia substitui explicitamente a previsão inicial: o primeiro encontro passa para **24/10/2026 às 10h**. Copie a atualização para a entrada:

```sh
python -c "import shutil; shutil.copy2('examples/wiki-lab/vault/raw/02-atualizacao.md','outputs/wiki-replay/raw/02-atualizacao.md')"
python -X utf8 tools/wiki_lab.py check --vault outputs/wiki-replay
```

Antes de processá-la, a verificação deve apontar uma fonte pendente. Registre a nova procedência:

```sh
python -X utf8 tools/wiki_lab.py ingest --vault outputs/wiki-replay
```

Depois peça ao agente:

> Leia a atualização e compare com as páginas existentes. Atualize apenas o que a fonte sustenta, preservando o programa original. Registre a previsão anterior e o motivo da substituição no histórico. Atualize páginas e índice; refaça a consulta com referências. Não trate a data mais recente de um arquivo como prova suficiente de que ele substitui outro.

No ciclo executado, o LLM atualizou a página do clube e o índice, preservou o original e registrou a previsão anterior. O conceito relacionado não precisou mudar. A consulta passou a responder **24/10 às 10h; preço não informado**, citando a atualização. A ausência de preço permaneceu uma lacuna.

Esse é o ponto em que a manutenção faz diferença: uma nova fonte precisa chegar às páginas e respostas que dependem dela.

## 6. Confira a estrutura e revise o conteúdo

```sh
python -X utf8 tools/wiki_lab.py check --vault outputs/wiki-replay
python -X utf8 tools/wiki_lab.py ingest --vault outputs/wiki-replay
```

O primeiro comando verifica caminhos de links, originais e registros de procedência. O segundo permite conferir a reingestão: as notas existentes devem ser preservadas. Essas verificações não avaliam a verdade das afirmações nem garantem que todos os conflitos foram encontrados.

Defina também como você vai revisar conteúdo: o que exige aprovação, quem pode aprovar e como essa passagem fica registrada. Neste experimento, as páginas continuam identificadas como propostas geradas pelo assistente, sem aprovação humana. Aprovar uma nota e escrever seu conteúdo são coisas diferentes.

## O que o experimento permitiu concluir

| Verificação | Resultado observado |
|---|---|
| Criar páginas a partir de uma fonte | Índice, síntese e conceito relacionado produzidos pelo LLM |
| Consultar com referências | Data e horário ligados à seção da fonte |
| Reconhecer uma lacuna | Preço ausente, sem inventar gratuidade |
| Incorporar uma atualização | Resposta alterada para 24/10 às 10h, com histórico preservado |
| Reprocessar os mesmos arquivos | Notas de leitura preservadas |
| Detectar problemas estruturais | Fonte pendente, original alterado e link quebrado detectados nos testes |

Passaram os quatro testes novos do helper e os dois testes existentes de ingestão. Esse é o recorte testado; não foi executada a suíte integral dos outros sistemas do repositório.

A experiência fechou um ciclo mínimo de wiki LLM: receber fontes, lê-las com o agente, produzir páginas conectadas, consultar com referências e atualizar o conhecimento quando chega informação nova. O código sozinho não fez esse trabalho: a síntese e a manutenção foram realizadas pelo assistente desta conversa.

Dois documentos fictícios não demonstram qualidade em escala, autonomia ou economia de tempo. O teste mostra um fluxo funcional e pequeno que você pode inspecionar e repetir. Para começar sua wiki, escolha uma pergunta real, reúna poucas fontes que possa conferir e percorra esse mesmo ciclo antes de aumentar a automação.
