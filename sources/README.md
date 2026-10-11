# Fontes para curadoria

Registros de procedência e notas de leitura. Não são conhecimento aprovado por terem sido gerados.

Execute na raiz:

```sh
python tools/ingest_source.py raw/estudo.pdf --title "Título do estudo" --resource "https://example.org/estudo" --rights "Conferir licença; original somente local" --public-note
```

`--public-note` confirma que nomes e metadados podem ser públicos. Não concede direitos sobre o original. O comando calcula SHA-256, preserva o arquivo, cria `draft` e retorna a nota existente ao reprocessar os mesmos bytes. Metadados corrigidos devem ser editados em revisão: reexecutar não sobrescreve notas. Não há watcher, extração, OCR ou síntese automática nesta versão.

Leia a fonte e preencha método, escopo, limitações e afirmações sustentadas conforme [evidence/schema.md](../evidence/schema.md). Notas revisadas alimentam evidência e perguntas do [thesis graph](../thesis-graph/README.md); o Editorial Engine consome esse contexto. Promoção canônica e publicação exigem os gates existentes.

## Navegação no Obsidian

Abra a pasta do checkout como vault. Use os links do README para navegar; as relações adicionadas às notas aparecem no grafo. Configuração do Obsidian e sincronização não são automatizadas por este fluxo. O grafo representa links, não valida evidência.

## Exemplo reproduzível

```sh
python tools/ingest_source.py examples/wiki-ingestion/source-demo.md --title "Exemplo de coleta da Cereja" --author "Cereja Flamejante" --rights "Material demonstrativo próprio" --public-note
python -m unittest discover -s tests
```

O exemplo é próprio e didático; não é um estudo científico nem um resultado de curadoria. O formato não foi certificado como conforme ao OKF.

