# Survey: Learning Methods for Vision-Language Models

Systematic literature review on learning methods for Vision-Language Models (VLMs), focusing on scenarios with limited labeled data — including semi-supervised, self-supervised, active, and cross-modal learning approaches.

## Researchers

- Gabriel Souto Ferrante
- Priscila Tiemi Maeda Saito

## Scope

- **Period:** May 2020 – May 2025
- **Sources:** IEEE Xplore, ArXiv, Science Direct
- **Documents retrieved:** 6,854
- **Eligible papers (Phase 2):** 599 unique (775 category assignments)
- **Selection phases:** 3 (Initial Screening → Full-text Eligibility → Quality Assessment)

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

| Question | Papers | Coverage |
|----------|--------|----------|
| QP1 | 589 | 98.3% |
| QP2 | 163 | 27.2% |
| QP3 | 119 | 19.9% |
| QP4 | 18 | 3.0% |
| QP5 | 332 | 55.4% |
| QP6 | 589 | 98.3% |
| QP7 | 389 | 64.9% |
| QS1 | 233 | 38.9% |
| QS2 | 334 | 55.8% |
| QS3 | 189 | 31.6% |
| QS4 | 117 | 19.5% |

## Task Categories

The selected papers are organized across five VLM task categories:

| Category | Papers | Focus |
|----------|--------|-------|
| VQA | 84 | Visual Question Answering |
| Text-Image | 68 | Cross-modal retrieval and semantic alignment |
| Image-Text | 249 | Pre-training and transfer learning |
| Retrieval | 225 | Cross-modal information retrieval and ranking |
| Generate | 149 | Image/caption generation, diffusion models |

> **Note:** A paper may appear in more than one category. Total unique papers: 599 (775 category assignments total).

## Search Strings

### IEEE Xplore / Science Direct

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

**Tasks:** VQA, Text-Image, Image-Text, Retrieval, Generate

**Learning methods:** Active Learning OR AL, Semi-supervised Learning, Cross-modal Learning, Multimodal Learning, Self-supervised Learning

### Results per task and source

| Task | IEEE | ArXiv | Science Direct | Total |
|------|------|-------|----------------|-------|
| VQA | 443 | 122 | 0 | 565 |
| Text-Image | 466 | 781 | 1 | 1,248 |
| Image-Text | 1,052 | 781 | 5 | 1,838 |
| Retrieval | 972 | 367 | 3 | 1,342 |
| Generate | 720 | 1,134 | 7 | 1,861 |
| **Total** | **3,653** | **3,185** | **16** | **6,854** |

## Selection Process

The selection follows a three-phase PRISMA protocol:

1. **Phase 1 — Initial Screening:** Title + abstract review applying inclusion (CI1–CI4) and exclusion (CE1–CE4) criteria
2. **Phase 2 — Full-text Eligibility:** Full-text evaluation against 11 research questions (QP1–QP7, QS1–QS4), minimum 2–3 QPs required → **599 eligible papers**
3. **Phase 3 — Quality Assessment:** Scoring on 0–11 scale (pending)

### Quality Assessment Scale (0–13 points)

| Criterion | Max Points |
|-----------|-----------|
| Unfavorable scenarios coverage | 2 |
| Theoretical grounding | 3 |
| Result clarity | 3 |
| Relevant illustrations | 2 |
| Accessible repositories | 1 |
| Quality | 2 |
| **Total** | **11** |

### Inclusion Criteria

- CI1: Study addresses multimodal text-image models
- CI2: Study provides clear architecture/method description
- CI3: Published in peer-reviewed conference or journal
- CI4: Answers minimum 2–3 research questions

### Exclusion Criteria

- CE1: Not available in English or Portuguese
- CE2: White papers, technical reports, or non-peer-reviewed documents
- CE3: Does not use VLMs or lacks architecture description
- CE4: Focused exclusively on video, audio, or non-text/image modalities

## Repository Structure

```
├── .claude/              # Claude Code configuration and custom skills
│   ├── commands/
│   │   ├── read-paper.md   # Skill: structured paper analysis (QPs, quality score)
│   │   └── write-paper.md  # Skill: academic writing for survey sections
│   └── settings.json
├── latex/                # LaTeX source files for the survey paper
│   ├── introduction.tex
│   ├── related_work.tex
│   ├── methodology.tex
│   └── references.bib
├── scripts/              # Python scripts for generating figures
│   ├── style.py
│   ├── fig_documents_per_source.py
│   ├── fig_selected_per_category.py
│   ├── fig_research_questions.py
│   ├── fig_year_distribution.py
│   └── fig_prisma_flow.py
├── figures/              # Generated figures (PDF + PNG, 300 DPI)
├── related_works.md      # Analysis of 20 related surveys
├── CLAUDE.md             # Project context for Claude Code
└── readme.md             # This file
```

