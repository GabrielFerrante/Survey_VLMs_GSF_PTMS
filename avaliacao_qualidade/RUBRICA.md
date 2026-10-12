# Rubrica da avaliação de qualidade

Escopo: a aba **FASE 2 - SELEÇÃO FINAL** da planilha do Google já corrigida (exportada em 2026-10-04), com 791 linhas e 606 artigos distintos. Distribuição por categoria: **VQA 89, Text-Image 71, Image-Text 259, Retrieval 226, Generate 146**. Um artigo pode estar em mais de uma categoria, mas não repete dentro da mesma. Cada planilha `Avaliacao_Qualidade_<Tarefa>.xlsx` traz, por linha, **Nota + Conceito + Justificativa** para cada critério. "Linha na Fase 2" é a linha dessa versão da planilha.

## Critérios do protocolo (aba *Protocolo*)

| Critério | Nota máx. | Conceitos |
|---|---|---|
| Cenários desfavoráveis de dados | 2 | 2 Plenamente atende · 1 Parcialmente atende · 0 Não atende |
| Fundamentação teórica ("bem fundamentada") | 3 | 3 Excelente · 2 Bom · 1 Regular · 0 Insuficiente |
| Clareza dos resultados | 3 | 3 Excelente · 2 Bom · 1 Regular · 0 Insuficiente |
| Ilustrações relevantes | 2 | 2 Plenamente · 1 Parcialmente · 0 Não atende |
| Repositórios acessíveis | 1 | 1 Disponível · 0 Indisponível |
| **TOTAL (0–11)** | 11 | 9–11 Alta · 7–8 Boa · 5–6 Moderada · 0–4 Baixa |
| Critério 6 do protocolo: "Responder 4 questões principais" | 2 | calculado a partir da coluna de QPs da Fase 2 (só QP1–QP7): ≥4 → 2, senão 0 |
| **TOTAL protocolo (0–13)** | 13 | TOTAL/11 + critério 6 |

O `CLAUDE.md` descreve a escala como 0–11 (cinco critérios); o protocolo da planilha e o `readme.md` usam 0–13 (com o critério 6). As duas colunas estão nas planilhas.

## Âncoras de pontuação (aplicadas a todos os trabalhos)

**Cenários desfavoráveis (0–2)**
- 2: experimentos dedicados a regime desfavorável (poucos rótulos, few/zero-shot, ruído, OOD/shift, supervisão fraca, domínio ou língua com poucos dados) como eixo principal da proposta.
- 1: escassez/ruído/shift aparece só como motivação ou em avaliação pontual/secundária.
- 0: nenhum.

**Fundamentação teórica (0–3)**
- 3: formulação formal (equações/objetivo) + justificativa por ablação, análise ou teoria + related work substantivo.
- 2: formulação clara, mas com pouca ablação/análise ou poucas equações.
- 1: descrição operacional (pipeline) sem formalização.
- 0: ausente.

**Clareza dos resultados (0–3)**
- 3: benchmarks padrão + baselines fortes + ablações + análise extra (qualitativa, variância, falhas).
- 2: comparações claras, mas sem ablação/análise adicional.
- 1: poucas comparações ou métricas.
- 0: sem resultados.

**Ilustrações relevantes (0–2)**
- 2: ≥2 ilustrações distintas e relevantes (arquitetura/pipeline + exemplos, resultados ou aplicação).
- 1: apenas uma. 0: nenhuma.

**Repositórios acessíveis (0–1)**
- 1: link **próprio** (código, modelo ou dados), gratuito, **ativo e com conteúdo**, verificado online em 2026-10-04.
- 0: ausente; só de terceiros; "será liberado" sem repositório utilizável; HTTP 404; repositório vazio ou só com placeholder.

## Como a nota foi obtida

1. **Texto completo**: 513 trabalhos únicos lidos online via arXiv; 112 (IEEE/ACM/ScienceDirect de acesso fechado) lidos a partir dos PDFs da biblioteca local do projeto (`E:\Doutorado - UFSCAR\RevisãoSistemática`); **5 apenas pelo resumo** (confiança "Baixa": P181, P190, P202, P365, P377).
2. **Evidência extraída por trabalho**: resumo, títulos de seções, legendas de figuras/tabelas, equações numeradas, ocorrências de ablação/baseline/variância, links de repositório, termos de poucos dados. Casos duvidosos foram conferidos com buscas no texto.
3. **Pontuação** pelas âncoras acima, com justificativa por critério.
4. **Mesmo artigo em várias categorias**: recebe a mesma pontuação em cada categoria em que aparece. A Fase 2 corrigida não tem artigo repetido na mesma categoria.
5. **Repositórios**: todo link candidato foi aberto online; o conteúdo da raiz do repositório foi inspecionado (README, arquivos, diretórios).

## Colunas de apoio

- **Confiança da evidência**: Alta (texto completo ≥20 mil caracteres extraídos), Média (texto completo curto), Baixa (só resumo).
- **Alertas para a revisão**: possivelmente fora do escopo (não texto-imagem / não VLM); dataset/benchmark como contribuição central; estudo/análise sem método novo; domínio de agentes/robótica; só resumo; PDF local; repositório citado porém inacessível. Os alertas de escopo e tipo de contribuição são **heurísticos** e servem para triagem, não para exclusão automática.
- **Ajustes de validação**: mudanças feitas após a primeira passada (ver `RELATORIO_VALIDACAO.md`).
