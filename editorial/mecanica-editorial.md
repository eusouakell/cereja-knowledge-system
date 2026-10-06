# Mecânica editorial do Núcleo

Decisão de Kell em 06/10/2026: adotar guias, guardas, verificações e sensores, com flexibilidade por contexto. Escopo atual: português brasileiro. Inglês e espanhol ficam fora desta implementação. Este documento define governança; não afirma que ferramentas ou monitoramento já foram implementados.

## Contexto antes da execução

Registrar leitor, objetivo, canal, formato, fontes, autoria disponível e ação esperada, quando existir. Selecionar o perfil pertinente. Exceções precisam de motivo e escopo; não revogam princípios de precisão, acessibilidade ou autoria.

| Perfil | Aplicação |
|---|---|
| Newsletter | Preservar costura autoral, oralidade, humor e variedade de ritmo. Apresentar contexto para acompanhar as conexões. |
| Site | Atender intenção de busca e descoberta; aplicar SEO e GEO com conteúdo útil, fontes e estrutura acessível. |
| Interface | Explicitar ação, condição, estado e consequência. Botão de assinatura: Assinar Newsletter. |
| Texto social | Aplicar clareza e voz. Estratégia, carrossel e direção de arte seguem o fluxo especialista do canal. |

Frases de 15 a 20 palavras são uma meta de revisão. Quando um briefing exigir limite máximo, conferir esse limite e dividir sem perder relações ou qualificadores. Citações literais, nomes e exceções necessárias devem ser identificados, nunca adulterados para caber. Cada parágrafo desenvolve uma ideia central. Converter blocos densos em listas quando contiverem passos ou itens paralelos; preservar relações narrativas.

## Camadas

| Camada | Responsabilidade | Registro esperado |
|---|---|---|
| Guias | Manter voz, linguagem simples, exemplos aprovados e perfis contextuais. | Fonte, versão, escopo e decisão vigente. |
| Guardas | Impedir fatos, experiências, citações ou permissões inventadas; preservar significado e autoria. | Problema, trecho afetado e condição para resolver. |
| Verificações | Examinar fontes, links, gramática, estrutura, alt text e legibilidade. | Evidência, método, alcance, resultado e pendências. |
| Sensores | Aprender com compreensão, respostas, cliques e dificuldades após publicação. | Observação real, período, contexto e proposta de melhoria. |

Fluxo: consultar guias → produzir → verificar → revisar → aprovação de Kell → publicar → aprender. Publicação exige autorização aplicável ao pedido. Parecer de agente não substitui aprovação de Kell nem teste com leitores.

Verificações podem registrar aprovado no escopo, revisão necessária, bloqueado ou não avaliado. Ausência de ferramenta, acesso ou teste gera não avaliado, nunca aprovação automática. Bloquear a entrega diante de invenção, alteração de significado ou direito de uso não resolvido. Questões de ritmo e preferência seguem revisão editorial.

## Linguagem e referências

Aplicar os quatro princípios da ISO 24495-1 como referência: relevância, facilidade de encontrar, compreensão e uso da informação. Utilizável significa atender a necessidade do leitor; nem todo texto exige ação imediata. Nosso registro de avaliação é próprio, não um schema oficial ISO nem certificação. A parte 3 orienta comunicação sobre ciência para públicos diversos.

Preferir voz ativa com responsável conhecido. Se o responsável não está informado, preservar a incerteza. Remover gerundismo e burocratês sem alterar tempo ou condição: vamos estar analisando → vamos analisar; conquanto → embora, quando equivalente. Explicar termos indispensáveis.

As referências legais da administração pública brasileira orientam a adaptação; não constituem obrigação automaticamente aplicável à newsletter. A Portaria CNJ 191/2025 regulamenta o Selo Linguagem Simples 2025. AP Stylebook não foi adotado como padrão da Cereja. Aspas, pontuação, tratamento de nomes e cargos seguem contexto e uso correto em português, sem substituições cegas.

Direitos de uso seguem seu próprio guardrail. Citar uma marca não autoriza reproduzir suas fotos, obras ou logotipos. Não presumir uma licença internacional genérica de fair use. Verificar fonte, atribuição, licença ou permissão pertinente ao uso.

## Site com SEO e GEO

GEO designa aqui o objetivo de tornar conteúdo compreensível e descobrível em experiências de busca com IA. Práticas variam por serviço e devem ter fonte e data. Não prometer indexação, posição ou citação por um sistema.

- Escrever títulos e descrições fiéis ao conteúdo e à intenção do leitor. Evitar repetição artificial de palavras-chave.
- Organizar headings, links internos e nomes descritivos de links. Disponibilizar informação essencial como texto, com alternativas para imagens.
- Identificar autora, fontes, datas relevantes e entidades sem inventar autoridade ou atualização. Explicar conceitos e responder perguntas reais quando isso servir à página.
- Conferir conteúdo visível e dados estruturados juntos. Marcação deve representar informação real; não fabricar FAQ, avaliações ou credenciais para busca.
- Encaminhar indexabilidade, canonical, sitemap e controles de rastreamento à implementação técnica. Registrar o que foi conferido e o que não foi.
- Tratar links pagos conforme orientação atual do mecanismo; no Google, sponsored é preferido e nofollow é aceito. Isso não substitui transparência editorial sobre patrocínio.

No Google, AI Overviews e AI Mode usam os fundamentos de SEO existentes; não exigem arquivo ou schema especial para IA. Essa orientação não é garantia nem regra universal para outros serviços.

## Medição e aprendizagem

Flesch adaptado ao português pode ajudar a localizar carga de leitura. Registrar método de segmentação e contagem de sílabas, versão e limitações. Não inferir compreensão ou escolaridade individual apenas pelo índice. Revisão semântica, editorial e testes com leitores complementam os números.

Sensores usam métricas disponíveis e autorizadas. Distinguir observação de hipótese: cliques não comprovam compreensão; tempo de página não comprova leitura completa. Não declarar abandono por edição sem medição adequada. Acessos vindos de IA precisam de método identificável; Search Console agrega as experiências de IA do Google ao tráfego de busca na Web.

ISO 27001 e ISO 9001 são referências de gestão, não testes unitários de texto. Normas de acessibilidade orientam processos; checagens automatizadas isoladas não comprovam conformidade. Datas e moedas podem ter representação técnica padronizada e apresentação familiar ao leitor; timestamps usados em agendamento devem explicitar fuso.

JSON é uma opção de contrato entre componentes. Definir campos e estados de erro antes de implementar; não restringir toda entrega humana a JSON. Não criar tradução trilíngue, API paga ou automação com base apenas neste documento.

## Fontes consultadas em 06/10/2026

- [ISO e seus princípios, IPLF](https://www.iplfederation.org/iso-standard/).
- [ISO 24495-3:2026, escopo público](https://committee.iso.org/standard/86938.html?browse=tc). Não foi consultado o texto integral pago da norma.
- [Lei 15.263/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15263.htm).
- [Portaria CNJ 191/2025, compilação](https://atos.cnj.jus.br/files/compilado13571220250728688781b886ee5.pdf).
- [Texto descritivo de links, W3C](https://www.w3.org/WAI/WCAG21/Techniques/general/G91).
- [Links pagos, Google](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links).
- [Busca com IA, Google](https://developers.google.com/search/docs/appearance/ai-features).
- [Conteúdo útil, Google](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

Consultar também [Content Design](content-design.md), [linguagem simples](linguagem-simples.md) e [voz e tom](voice-and-tone.md).
