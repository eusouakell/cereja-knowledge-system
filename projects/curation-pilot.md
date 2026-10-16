# Operação da curadoria no D:
Perfil: Research Synthesist sob governance/curation-automation-policy.md.

1. Leia a política e local-curation/index.md.
2. Coleta: python -X utf8 tools/curation_pipeline.py collect
3. Procedência: python -X utf8 tools/curation_pipeline.py ingest-metadata
4. Entrada manual: python -X utf8 tools/curation_pipeline.py inbox
5. Saúde: python -X utf8 tools/curation_pipeline.py health

O script limita a coleta e deduplica registros; não avalia relevância semântica nem produz síntese. Metadados não equivalem à leitura da obra.
Em seguida o curador avalia candidatos por relevância, contribuição nova, procedência e conexão editorial. Pontuação interna, razões e estados selected/deferred/excluded devem ir em local-curation/reviews/, sem apagar os registros originais. Escore não é métrica validada de qualidade.
Com no máximo 6 sínteses/dia, escrever: afirmações da fonte, inferência separada, trecho/seção de apoio, limitações, ligação às notas existentes e revisão pendente.
Se um endpoint falhar, guardar falha e usar pesquisa pública por ferramentas disponíveis para referência; não contornar CAPTCHA, autenticação ou bloqueio. FAPESP/SciELO podem começar com página selecionada; o agente deve procurar material novo relevante nas rodadas seguintes em vez de tratar a mesma URL como novidade.
Smithsonian retornou 403 no piloto; referência pública pode permanecer no catálogo, sem alegar download automático bem-sucedido.
Não instalar skills de terceiros. Não sincronizar Git automaticamente.
Abrir local-curation/index.md no Obsidian. Os dados locais continuam no D:.

## Tutoriais e pesquisas sob demanda
- Livros Cereja: local-curation/tutorials/livros-cereja/README.md e modelos na pasta templates/. Proposta de capítulo piloto; não é pipeline já implementado.
- Repositórios Akita: local-curation/research/akita/README.md. Inventário leve e triagem; não autoriza clonagem integral.
- Procedência pública: references/akita-book-production.md.
Preservar esses artefatos nas manutenções; a regeneração do índice de metadados não deve apagar ou substituir o tutorial.
