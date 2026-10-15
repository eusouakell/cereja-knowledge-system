# Histórico do experimento — 15/10/2026

## Etapa 1 — ingestão

O helper Python criou uma nota de procedência para 01-programa.md. Não houve chamada de modelo pelo script.

## Etapa 2 — síntese pelo LLM

O assistente desta conversa leu o programa fictício e escreveu índice, página do clube e conceito relacionado. Prompt aplicado: “Leia o programa preservando o original. Gere uma síntese com afirmações ligadas às seções da fonte; crie um conceito relacionado, atualize o índice e registre lacunas. Não atribua aprovação humana.”

Resultado anterior à atualização: primeiro encontro em 23/10 às 19h. Preço e vagas ausentes. As páginas foram geradas pelo próprio assistente executor; não há avaliação independente.

## Etapa 3 — chegada de nova fonte

02-atualizacao.md foi adicionado a raw/. Antes da ingestão, check retornou FAIL com “Unprocessed source: 02-atualizacao.md”. A ingestão criou uma nota nova e preservou a existente. O helper não atualizou a síntese sozinho.

Prompt aplicado ao assistente: “Leia a nova fonte e compare com as páginas existentes. Atualize apenas o que ela sustenta, preserve a previsão anterior como histórico e registre o motivo da mudança. Não trate novidade como verdade por si só.”

O assistente atualizou o clube e o índice: 24/10 às 10h substitui 23/10 às 19h porque o documento declara a substituição. O conceito de leitura com evidências não mudou, pois a nova fonte não altera essa atividade.

## Etapa 4 — consulta após atualização

Pergunta aplicada ao assistente: “Quando é o primeiro encontro e quanto custa? Consulte o índice, a página do clube e as fontes; responda com referências. Se a base não disser, registre a lacuna.”

Resposta salva em [consulta-encontro.md](wiki/consulta-encontro.md): 24/10 às 10h; preço não informado, sem inferir gratuidade. A busca lexical do helper localiza páginas; a leitura e a resposta foram feitas pelo LLM desta conversa.

## Limites

É um ciclo funcional assistido, com dois documentos pequenos fictícios. Não é benchmark de qualidade, teste de autonomia nem validação em acervo empresarial. Não houve revisão humana das sínteses. O check estrutural confere links e originais, não a verdade das afirmações.
