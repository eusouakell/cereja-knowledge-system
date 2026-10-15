# Uma wiki LLM mínima, do original à consulta atualizada

Experimento concluído em 15/10/2026. Dois documentos fictícios próprios; nenhum dado empresarial. O assistente LLM desta conversa gerou e atualizou as páginas. Os scripts fazem procedência, busca lexical e verificação estrutural, sem chamadas a modelos.

## Obter e conferir o exemplo concluído

Python 3.10+ e um agente capaz de ler/escrever arquivos locais. Obsidian é opcional: abra a pasta `vault` como vault para navegar por links Markdown. Instalação, sincronização e grafo do Obsidian não foram testados nesta execução.

Enquanto o PR não for incorporado a main, use a branch do experimento:

```sh
git clone --branch experiment/wiki-cycle-20261015 https://github.com/eusouakell/cereja-knowledge-system.git
cd cereja-knowledge-system
python -X utf8 tools/wiki_lab.py ingest --vault examples/wiki-lab/vault
python -X utf8 tools/wiki_lab.py search --vault examples/wiki-lab/vault --query "encontro preço"
python -X utf8 tools/wiki_lab.py check --vault examples/wiki-lab/vault
python -X utf8 -m unittest discover -s tests -p "test_*ingestion.py" -v
python -X utf8 -m unittest discover -s tests -p "test_wiki_lab.py" -v
```

A primeira operação retorna `created: false` para as duas fontes porque o snapshot final já contém as notas. O check retorna PASS; a busca encontra a data atualizada e a ausência de preço. Não há geração automática de respostas por esse comando.

## Repetir o ciclo desde o começo

Na raiz do checkout, crie outra pasta com apenas o primeiro original e as instruções. O comando abaixo falha se a pasta `raw` de destino já existir, para não sobrescrever uma execução anterior:

```sh
python -c "from pathlib import Path; import shutil; p=Path('outputs/wiki-replay'); (p/'raw').mkdir(parents=True); shutil.copy2('examples/wiki-lab/vault/raw/01-programa.md',p/'raw/01-programa.md'); shutil.copy2('examples/wiki-lab/vault/AGENTS.md',p/'AGENTS.md')"
python -X utf8 tools/wiki_lab.py ingest --vault outputs/wiki-replay
```

Abra o agente nessa nova pasta. Aplique o primeiro prompt:

> Leia AGENTS.md e a fonte em raw/. Preserve o original. Complete as notas de leitura em sources/, com referências às seções da fonte. Crie index.md, log.md e páginas em wiki/ para o clube e um conceito relacionado. Diferencie afirmações da fonte, interpretação e lacunas. Não invente aprovação humana. O resultado deve permitir responder quando é o encontro e o que sabemos sobre seu preço.

Confira a síntese contra o documento. Para consultar:

```sh
python -X utf8 tools/wiki_lab.py search --vault outputs/wiki-replay --query "encontro preço"
python -X utf8 tools/wiki_lab.py check --vault outputs/wiki-replay
```

Pergunte ao agente:

> Consulte o índice, a página do clube e os originais. Quando é o primeiro encontro e quanto custa? Cite arquivo e seção. Registre a resposta em uma página e acrescente seu link ao índice. Se a base não disser, registre a lacuna.

Antes da atualização, a resposta sustentada é **23/10/2026 às 19h; preço não informado**. A ausência de preço não permite concluir gratuidade.

Adicione a segunda fonte:

```sh
python -c "import shutil; shutil.copy2('examples/wiki-lab/vault/raw/02-atualizacao.md','outputs/wiki-replay/raw/02-atualizacao.md')"
python -X utf8 tools/wiki_lab.py check --vault outputs/wiki-replay
python -X utf8 tools/wiki_lab.py ingest --vault outputs/wiki-replay
```

Antes da ingestão, o check deve falhar por fonte não processada. Isso é intencional. Depois, peça ao agente:

> Leia a atualização e compare com as páginas existentes. Atualize apenas o que a fonte sustenta, preservando o programa original. Registre a previsão anterior e o motivo da substituição no histórico. Atualize páginas e índice; refaça a consulta com referências. Não trate a data mais recente de um arquivo como prova suficiente de que ele substitui outro.

Agora a resposta sustentada é **24/10/2026 às 10h; preço não informado**. A nova fonte declara explicitamente a substituição. Repita busca, check e ingestão; a reingestão deve preservar as notas de leitura. O snapshot em `vault/` serve como comparação, não como resposta que o agente precisa copiar.

## O que fica pronto

```text
vault/
  AGENTS.md       instruções de manutenção para o agente
  raw/            originais imutáveis
  sources/        procedência e leitura de cada fonte
  wiki/           sínteses, conceitos e consulta registrada
  index.md        mapa de navegação
  log.md          histórico de atualização
```

Você decide o gatilho (pasta monitorada, comando ou lote), extração/OCR, identificadores e política de revisão. Neste teste usamos comando, Markdown legível e SHA-256; as notas permanecem propostas geradas. Não é necessário implementar watcher ou embeddings para esse ciclo pequeno.

## Resultado e limites

O ciclo fonte → leitura pelo LLM → páginas relacionadas → consulta → nova fonte → atualização foi executado. O original e a previsão anterior foram preservados. O agente reconheceu o preço ausente. Quatro testes novos e os dois testes existentes de ingestão passaram no recorte local. Não foi executada a suíte integral de Flame; os comandos acima selecionam somente os testes deste fluxo.

O check verifica caminhos de links, cobertura de procedência e integridade dos originais. Não verifica a existência de âncoras, qualidade da síntese, validade das evidências ou todas as contradições possíveis. Dois documentos fictícios não demonstram desempenho em escala, economia de tempo ou autonomia. Não houve aprovação humana das páginas nem teste de OCR/PDF, vigilância de pasta, recuperação vetorial ou conformidade OKF. A documentação e os arquivos do experimento seguem a política de direitos do repositório; não se presume uma nova licença aberta.
