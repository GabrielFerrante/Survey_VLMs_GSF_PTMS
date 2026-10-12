# Survey: Learning Methods for Vision-Language Models

Systematic literature review on learning methods for Vision-Language Models (VLMs), focusing on scenarios with limited labeled data — including semi-supervised, self-supervised, active, and cross-modal learning approaches.

## Researchers

- Gabriel Souto Ferrante
- Priscila Tiemi Maeda Saito

## Scope

- **Period:** May 2020 – May 2025
- **Sources:** IEEE Xplore, ArXiv, Science Direct, ACM Digital Library
- **Search results retrieved:** 6,989 (counting results repeated across queries)
- **Phase 1 records (task level):** 1,649 (1,145 unique titles)
- **Selected papers (Phase 2):** 606 unique (791 category assignments)
- **Quality assessment:** all 606 papers scored on a 0–13 scale; no paper is excluded by score

## Research Questions

| Code | Question |
|------|----------|
| QP1 | Which learning methods are explored? |
| QP2 | Does training employ graphs to map text-image relationships? |
| QP3 | Does training leverage semi-supervised learning? |
| QP4 | Does training incorporate active learning? |
| QP5 | Does architecture include vision modules for explainability? |
| QP6 | Are datasets thoroughly documented and appropriate? |
| QP7 | Do evaluation criteria assess multiple multimodal tasks? |
| QS1 | Are open repositories available? |
| QS2 | Is dataset access provided publicly? |
| QS3 | Is limited domain-specific data availability mentioned? |
| QS4 | Do benchmarks include medical imaging data? |

### Research Questions Coverage

Counted over the 606 unique papers; for each paper, the questions registered in any of its categories are considered.

| Question | Papers | Coverage |
|----------|--------|----------|
| QP1 | 605 | 99.8% |
| QP2 | 100 | 16.5% |
| QP3 | 99 | 16.3% |
| QP4 | 14 | 2.3% |
| QP5 | 261 | 43.1% |
| QP6 | 603 | 99.5% |
| QP7 | 442 | 72.9% |
| QS1 | 248 | 40.9% |
| QS2 | 428 | 70.6% |
| QS3 | 183 | 30.2% |
| QS4 | 94 | 15.5% |

## Task Categories

The selected papers are organized across five VLM task categories:

| Category | Papers | Focus |
|----------|--------|-------|
| VQA | 89 | Visual Question Answering |
| Text-Image | 71 | Cross-modal retrieval and semantic alignment |
| Image-Text | 259 | Pre-training and transfer learning |
| Retrieval | 226 | Cross-modal information retrieval and ranking |
| Generate | 146 | Image/caption generation, diffusion models |

> **Note:** A paper may appear in more than one category, but never twice in the same one. Among the 606 unique papers, 450 appear in one category, 128 in two, 27 in three and 1 in four. Total: 791 category assignments.

## Search Strings

### IEEE Xplore / Science Direct / ACM

All queries follow the same template, varying the **task** and **learning method**:

```
("Vision-Language Models" OR "VLM") AND ("<TASK>") AND ("<LEARNING_METHOD>") AND ("Deep Learning")
NOT ("Survey" OR "Review") NOT ("Video" OR "Audio")
```

**Tasks:** VQA, Text-Image, Image-Text, Retrieval, Generate

**Learning methods:** Active Learning, Semi-supervised Learning, Cross-modal Learning, Multimodal Learning, Self-supervised Learning

### ArXiv

Queries use the ArXiv advanced search API with the following template:

```
order: -announced_date_first
size: <50–200>
date_range: from 2020-05-01 to 2025-05-01
classification: Computer Science (cs), Electrical Engineering and Systems Science (eess)
include_cross_list: True
terms: AND all=Vision-Language Models OR VLM
       AND all=<TASK>
       AND all=<LEARNING_METHOD>
       NOT all=Survey OR Review
```

### Results per task and source

| Task | IEEE | ArXiv | Science Direct | ACM | Total |
|------|------|-------|----------------|-----|-------|
| VQA | 443 | 116 | 0 | 6 | 565 |
| Text-Image | 466 | 752 | 1 | 4 | 1,223 |
| Image-Text | 1,052 | 781 | 5 | 54 | 1,892 |
| Retrieval | 972 | 367 | 3 | 40 | 1,382 |
| Generate | 720 | 1,134 | 7 | 66 | 1,927 |
| **Total** | **3,653** | **3,150** | **16** | **170** | **6,989** |

Share of the total: IEEE Xplore 52.3%, ArXiv 45.1%, ACM 2.4%, Science Direct 0.2%.

> **Search limitations:** the strings require the literal terms "VLM" / "Vision-Language Models" and "Deep Learning"; few-shot, zero-shot, weak supervision, prompt tuning, distillation and noisy supervision were not searched, only counted afterwards (see `avaliacao_qualidade/codificacao_QP1_paradigmas_por_categoria.csv`). Data-curation work such as DataComp is not retrieved. ACL Anthology, OpenReview, CVF, PMLR and Scopus were not queried, and no snowballing was performed.

## Selection Process

PRISMA flow (figure: `figures/fig_prisma_flow.png`, Portuguese version `fig_prisma_flow_PTBR.png`):

| Stage | Records |
|-------|---------|
| Search results retrieved | 6,989 |
| Not carried to Phase 1 (repeated results across queries/tasks and title/abstract screening; not itemized) | 5,340 |
| **Phase 1 — Initial selection** (task-level records) | **1,649** |
| Excluded by CE1 | 852 |
| &nbsp;&nbsp;— at title/abstract (insufficient information) | 527 |
| &nbsp;&nbsp;— answered fewer than 3 questions | 304 |
| &nbsp;&nbsp;— other inclusion criteria | 21 |
| **Phase 2 — Final selection** (records retained) | **797** |
| Removed: repeated entries of the same paper in the same category | 6 |
| **Included** | **791 assignments / 606 unique papers** |

All 606 papers are then quality-scored. The Top 10 per category is a descriptive presentation, not a filter.

### Quality Assessment Scale (0–13 points)

| Criterion | Max Points |
|-----------|-----------|
| Unfavorable scenarios coverage | 2 |
| Theoretical grounding | 3 |
| Result clarity | 3 |
| Relevant illustrations | 2 |
| Accessible repositories (verified online) | 1 |
| Answers 4 or more primary questions (QP1–QP7) | 2 |
| **Total** | **13** |

Scoring was performed with the support of a language model operating on the full text (489 papers from ArXiv, 112 from closed-access PDFs, 5 from the abstract only), with author review. The anchors are in `avaliacao_qualidade/RUBRICA.md` and the validation in `avaliacao_qualidade/RELATORIO_VALIDACAO.md`. A blind re-evaluation of 11 papers gave 51 of 55 identical criterion scores; it measures stability of the procedure, not inter-rater agreement. Two of the six criteria measure adherence to the review topic, and the scale does not assess risk of bias, data leakage, baseline fairness or variance.

### Quality Assessment Results

Per category assignment (the sixth criterion depends on the questions registered in each category):

| Category | Scored | Mean | Median | Min | Max | With 13/13 |
|----------|--------|------|--------|-----|-----|------------|
| VQA | 89 | 9.42 | 10 | 5 | 13 | 6 |
| Text-Image | 71 | 9.46 | 10 | 3 | 13 | 8 |
| Image-Text | 259 | 9.87 | 10 | 2 | 13 | 20 |
| Retrieval | 226 | 9.47 | 10 | 3 | 13 | 16 |
| Generate | 146 | 9.47 | 10 | 3 | 13 | 8 |

Top 10 ordering: total score, then number of questions answered (QPs + QSs), then Phase 2 order. In Image-Text and Retrieval the Top 10 is a selection among papers with equal scores.

### Inclusion Criteria

- CI1: Answers at least two primary questions in the initial phase and three questions (primary or secondary) in the final phase
- CI2: Indicated by an expert
- CI3: Computer science or related fields
- CI4: Full paper or short paper
- CI5: Published in the stipulated period
- CI6: Multimodal models integrating text and image
- CI7: Clear description of the architecture
- CI8: Conference or journal paper

### Exclusion Criteria

- CE1: Does not meet the inclusion criteria
- CE2: Does not match the task query
- CE3: Text not available
- CE4: Not written in Portuguese or English
- CE5: White paper
- CE6: Does not use VLMs
- CE7: No architecture description

> CI2 is not reproducible, and CI4/CI8 were relaxed to admit preprints (387 of the 606 papers have ArXiv as their only recorded venue). There is no explicit "limited supervision" criterion: 161 papers (26.6%) show no sign of it, so the corpus is a mapping of learning methods in VLMs in which limited supervision is an analysis axis, not an inclusion filter.

## Key Findings

- **Learning paradigms (QP1 mentions):** contrastive learning is the most mentioned paradigm (44.1% of papers), followed by fine-tuning/transfer (42.2%), few-/zero-shot (28.4%) and self-supervised learning (27.4%). Contrastive learning dominates Image-Text (63.7%) and Retrieval (50.9%), but not VQA (27.0%) or Generate (26.7%).
- **QP4 (Active Learning)** is the most underexplored question: 14 papers (2.3%). Three are outside VLMs and three use "active" in another sense, leaving 8 in scope, of which only 3 select samples for human annotation. In all 8, the component acts in adaptation/fine-tuning, never in general-purpose pre-training.
- **QP3 (Semi-supervised)** is registered in 99 papers (16.3%), but only 29 (4.8% of the corpus) are semi-supervised in the strict sense (labeled + unlabeled data of the task). The rest are noisy/weak supervision, self-supervision or model-generated synthetic data.
- **QP2 (Graphs)** appears in 100 papers (16.5%). Only 10 integrate the graph into pre-training or general-purpose representation learning; 37 use it as a task-specific module and 21 as an external knowledge graph.
- **Combinations are rare:** 406 papers (67.0%) record none of QP2, QP3 and QP4; none records all three.
- **Medical domain:** 6 of the Top 10 in Image-Text register QS4, against 18.1% of the category. QS3 is mentioned in 60.6% of papers with medical benchmarks versus 24.6% of the others.
- **Quality scale:** category means range only from 9.42 to 9.87, and 58 assignments reach 13/13, so the scale discriminates little at the top. Associations between QP3/QS3 and the score are partly mechanical.

## Repository Structure

```
├── .claude/                      # Claude Code configuration and custom skills
│   └── commands/
│       ├── read-paper.md         # Skill: structured paper analysis (QPs, quality score)
│       └── write-paper.md        # Skill: academic writing for survey sections
├── avaliacao_qualidade/          # Quality assessment deliverables
│   ├── Avaliacao_Qualidade_*.xlsx            # One workbook per task category (score + concept + justification per criterion)
│   ├── avaliacao_por_artigo_unico.csv        # Scores for the 606 unique papers
│   ├── verificacao_repositorios.csv          # Online verification of repository links
│   ├── codificacao_QP1_paradigmas_por_categoria.csv
│   ├── codificacao_QP2_papel_do_grafo.csv
│   ├── codificacao_QP3_operacional.csv
│   ├── codificacao_QP4.csv
│   ├── scripts_codificacao/      # Scripts and inputs that generate the codings
│   ├── RUBRICA.md                # Scoring anchors
│   └── RELATORIO_VALIDACAO.md    # Validation report
├── scripts/                      # Python scripts for generating figures (EN and *_PTBR)
│   ├── style.py
│   ├── fig_documents_per_source.py
│   ├── fig_selected_per_category.py
│   ├── fig_research_questions.py      # reads avaliacao_qualidade/avaliacao_por_artigo_unico.csv
│   ├── fig_year_distribution.py       # reads the review spreadsheet
│   ├── fig_prisma_flow.py
│   └── fig_quality_scores.py          # reads avaliacao_qualidade/*.xlsx
├── figures/                      # Generated figures (PDF + PNG, 300 DPI)
├── latex/                        # Manuscript sections (Portuguese)
│   ├── PaperCompleto.tex         # Full manuscript (Springer Nature template)
│   ├── introducao.tex, metodologia.tex, resultados.tex, discussao.tex, conclusao.tex
│   └── referencias_novas.bib     # New references (with DOI) not in the main .bib
├── GSF e PTMS - Revisão Sistemática ... .xlsx   # Review spreadsheet (Phase 1 and Phase 2 tabs)
├── acm_artigos_fase1.csv         # ACM records, Phase 1
├── google_cheat.json             # Link to the live Google Sheet
├── related_works.md              # Analysis of 20 related surveys
├── CLAUDE.md                     # Project context for Claude Code
└── readme.md                     # This file
```

## Reproducing the figures

```bash
cd scripts
python fig_prisma_flow.py          # and the other fig_*.py scripts; *_PTBR.py for Portuguese labels
```

The Google Sheet is the live source of the review data; the repository workbook can lag behind it.
