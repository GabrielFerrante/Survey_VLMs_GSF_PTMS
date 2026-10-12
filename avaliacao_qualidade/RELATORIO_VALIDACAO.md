# Relatório de validação da avaliação de qualidade

Fase 2 usada: a planilha do Google com as suas correções, exportada em 2026-10-04 (791 linhas, 606 artigos distintos). O xlsx que está no repositório ficou desatualizado (262 linhas em Image-Text, títulos abreviados em Generate) e não foi usado. Verificação online dos repositórios: 2026-10-04.

## 1. Números gerais

| Tarefa | Linhas na Fase 2 | Média /11 | Mediana | Alta | Boa | Moderada | Baixa | Média /13 |
|---|---|---|---|---|---|---|---|---|
| VQA | 89 | 8.74 | 9 | 55 | 21 | 13 | 0 | 9.42 |
| Text-Image | 71 | 8.68 | 9 | 41 | 23 | 4 | 3 | 9.46 |
| Image-Text | 259 | 9.02 | 9 | 185 | 57 | 11 | 6 | 9.87 |
| Retrieval | 226 | 8.62 | 9 | 139 | 61 | 18 | 8 | 9.47 |
| Generate | 146 | 8.84 | 9 | 93 | 41 | 11 | 1 | 9.47 |
| **Total** | 791 | 8.81 | 9 | | | | | 9.60 |

Distribuição final por categoria: **VQA 89, Text-Image 71, Image-Text 259, Retrieval 226, Generate 146 (total 791)**. Um mesmo artigo aparece em mais de uma categoria em 156 dos 606 artigos (normal); nenhum artigo aparece duas vezes na mesma categoria.

Médias por critério (606 artigos): cenários 1.07/2, fundamentação 2.57/3, resultados 2.73/3, ilustrações 1.94/2, repositório 0.45/1.

Fonte da evidência (606 artigos): 489 online (arXiv), 112 PDFs locais (acesso fechado), 5 apenas resumo.

## 2. Validações feitas

### 2.1 Repositórios (critério 1 ponto)

Todos os links candidatos foram abertos online. Dos 606 artigos, **272 ficaram com repositório disponível** (HTTP 200 e conteúdo na raiz). A verificação mudou **22 notas de 1→0** e **15 de 0→1**.

Motivos dos 1→0 (repositório citado no artigo, mas inutilizável):

- P082 — MLP Architectures for Vision-and-Language Modeling: An Empirical Study — README: "Code will be released soon"
- P127 — Exploring Curriculum Learning for Vision-Language Tasks: A Study on S… — sem repositório próprio (apenas baselines do BabyLM)
- P159 — Dissecting Deep Metric Learning Losses for Image-Text Retrieval — repositório com apenas 1 arquivo README, sem código
- P182 — Learning from Inside: Self-driven Intra-modality Siamese Knowledge Ge… — repositório GitHub inexistente (HTTP 404)
- P212 — AttriPrompter: Auto-Prompting With Attribute Semantics for Zero-Shot … — link incompleto (github.com/AttriPrompter) e "will be released"
- P249 — CMAL: A Novel Cross-Modal Associative Learning Framework for Vision-L… — repositório GitHub inexistente (HTTP 404)
- P268 — Weakly Supervised Vision-and-Language Pre-training with Relative Repr… — repositório GitHub inexistente (HTTP 404)
- P285 — VLMixer: Unpaired Vision-Language Pre-training via Cross-Modal CutMix — repositório GitHub inexistente (HTTP 404)
- P307 — Behind the Scene: Revealing the Secrets of Pre-trained Vision-and-Lan… — repositório GitHub inexistente (HTTP 404)
- P329 — MEDBind: Unifying Language and Multimodal Medical Data Embeddings — "code release under preparation"; repositório inexistente (404)
- P381 — Knowledge-Aided Momentum Contrastive Learning for Remote-Sensing Imag… — repositório GitHub inexistente (404)
- P385 — ViLNM: Visual-Language Noise Modeling for Text-to-Image Person Retrie… — repositório com 1 arquivo (apenas placeholder; "will be available")
- P393 — Globetrotter: Connecting Languages by Connecting Images — página do projeto inexistente (404); "will be released"
- P420 — Boosting Weak Positives for Text Based Person Search — link anônimo de revisão (4open.science), não verificável (401)
- P429 — Bridging Vision and Language Spaces with Assignment Prediction — README: "Official code will be available soon"
- P453 — SCOT: Self-Supervised Contrastive Pretraining For Zero-Shot Compositi… — repositório GitHub inexistente (404)
- P489 — SAND: Enhancing Open-Set Neuron Descriptions through Spatial Awareness — repositório GitHub inexistente (404)
- P501 — Solving Token Gradient Conflict in Mixture-of-Experts for Large VLM — repositório com 1 arquivo ("will be publicly available")
- P505 — Development of Compositionality and Generalization through Interactiv… — repositório GitHub inexistente (404)
- P519 — Weakly supervised one-stage vision and language disease detection — repositório de anotações inexistente (404)
- P601 — Composing Ensembles of Pre-trained Models via Iterative Consensus — página do projeto inexistente (404)
- P611 — Labeled Data Generation with Inexact Supervision — repositório vazio ("This repository is empty")

Mudanças 0→1 (link próprio achado no texto ou no campo de comentário do arXiv, verificado ativo):

- P021 — Comprehensive Visual Question Answering on Point Clouds through Compo… — https://github.com/yanx27/CLEVR3D
- P048 — Surgical-VQLA: Transformer with Gated Vision-Language Embedding for V… — https://github.com/longbai1006/Surgical-VQLA
- P069 — Surgical-VQLA++: Adversarial Contrastive Learning for Calibrated Robu… — https://github.com/longbai1006/Surgical-VQLAPlus
- P163 — Vision-Language Pre-Training for Boosting Scene Text Detectors — https://github.com/CVI-SZU/STKM
- P205 — LLaVA-SpaceSGG: Visual Instruct Tuning for Open-Vocabulary Scene Grap… — https://github.com/Endlinc/LLaVA-SpaceSGG
- P309 — Distilled Dual-Encoder Model for Vision-Language Understanding — https://github.com/kugwzk/DiDE
- P328 — RAR: Retrieving And Ranking Augmented MLLMs for Visual Recognition — https://github.com/Liuziyu77/RAR
- P338 — LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedi… — https://github.com/microsoft/LLaVA-Med
- P386 — Sketch Less for More: On-the-Fly Fine-Grained Sketch-Based Image Retr… — https://github.com/AyanKumarBhunia/on-the-fly-FGSBIR
- P397 — CLIP for All Things Zero-Shot Sketch-Based Image Retrieval, Fine-Grai… — https://aneeshan95.github.io/Sketch_LVM/
- P413 — HELPER-X: A Unified Instructable Embodied Agent to Tackle Four Intera… — https://helper-agent-llm.github.io
- P438 — Position-guided Text Prompt for Vision-Language Pre-training — https://github.com/sail-sg/ptp
- P478 — MixGen: A New Multi-Modal Data Augmentation — https://github.com/amazon-science/mix-generation
- P527 — Describe Anything: Detailed Localized Image and Video Captioning — https://describe-anything.github.io
- P580 — Dr-LLaVA: Visual Instruction Tuning with Symbolic Clinical Grounding — https://github.com/AlaaLab/Dr-LLaVA

Links mal extraídos de PDFs (quebra de linha, hífens) foram reconstruídos manualmente antes de contar como inexistentes. Repositórios com README "coming soon" só para parte do material, mas com código na raiz, mantiveram 1 ponto. Detalhes em `verificacao_repositorios.csv`.

### 2.2 Consistência interna

- **Ajustes de fundamentação (ft)**: 22 notas 3→2 (≤2 equações numeradas e sem sinais de formalização) e 5 notas 2→3 (≥5 equações + ablação + related work). Lista nas colunas "Ajustes de validação".
- Verificação cruzada de ablação/baselines/equações/figuras contra as notas atribuídas: 10 trabalhos com discrepância forte (≥2 níveis) foram relidos; mantidas as notas, exceto as de ft acima.
- **Repetição na Fase 2**: conferida por título normalizado, arXiv e similaridade; na versão corrigida não há nenhum artigo duas vezes na mesma categoria.

### 2.3 Reavaliação cega por amostragem

11 trabalhos (sorteio com semente fixa, texto online) foram pontuados de novo sem olhar a nota anterior: **51 de 55 notas de critério idênticas (93%)**; as 4 diferenças foram de 1 ponto: três em fundamentação (3 vs 2 em artigos com poucas equações) e uma em cenários. Isso levou ao ajuste de ft descrito acima.

### 2.4 Comparação com as pontuações antigas (`scores_*.csv` do histórico git)

Em 479 títulos em comum, as notas novas são em média **0,9 ponto mais altas no total /11** (7,91 → 8,83), com correlação de **0,46**; exatidão exata 22% e dentro de ±1 ponto 56%. A diferença vem de fundamentação (+0,34) e resultados (+0,40). Cenários (+0,14), ilustrações (+0,09) e repositório (−0,05) são próximos. Não sei como as notas antigas foram atribuídas; as novas se baseiam em texto completo e âncoras explícitas. No agregado /13, as médias novas por tarefa (9,42–9,87) ficam na mesma faixa das do `readme.md` (8,8–9,9).

## 3. Limitações e pontos que pedem decisão humana

- **Leitura assistida, não linha a linha**: as notas vêm de texto completo, mas apoiadas por extração automática de evidências e buscas pontuais. Não foi feita a análise de 9 seções do `/read-paper` por artigo.
- **Efeito teto**: clareza dos resultados = 3 em 78% dos artigos e ilustrações = 2 em 95%; a nota discrimina pouco nesses dois critérios. Se quiserem mais separação, endurecer a âncora de "análise extra" para o 3.
- Equações contadas só quando numeradas; artigos biomédicos e curtos podem estar subestimados em fundamentação.
- Repositórios divulgados só na página do arXiv/GitHub e não citados no PDF (ou em hyperlinks ocultos) podem ter sido perdidos; os campos de comentário do arXiv foram consultados.
- 5 trabalhos avaliados só pelo resumo; 112 por PDF local de acesso fechado.
- Critério 6 usa apenas a lista de QPs da Fase 2, sem reavaliar se o trabalho realmente responde às QPs.
- Inconsistências na própria Fase 2 (QPs ausentes ou código inexistente): P065 (linha 67). Estão sinalizadas nas planilhas.
- Os alertas abaixo são heurísticos; a decisão de excluir é dos pesquisadores.

## 4. Listas para triagem

### Mudanças da Fase 2 corrigida em relação à versão anterior

- Image-Text: removidas 3 linhas que repetiam o mesmo artigo na mesma categoria (P161, P209 e P227 estavam duas vezes); Image-Text passou de 262 para 259.
- Generate: removida a segunda linha de "A Multimodal Automated Interpretability Agent" e incluído "AIGeN: An Adversarial Approach for Instruction Generation in VLN" (novo, avaliado agora: total 9/11); Generate continua com 146.
- Generate: títulos abreviados foram trocados pelos títulos completos; nenhum artigo mudou por isso.

### Possivelmente fora do escopo (texto-imagem / VLM) (21)

- P464 — Exploring the Meaningfulness of Nearest Neighbor Search in High-Dimen… — análise de NNS em alta dimensão (não específica de VLMs) — RETRIEVAL
- P477 — TVLT: Textless Vision-Language Transformer — fusão de sensores, sem texto — RETRIEVAL
- P481 — Analyzing Local Representations of Self-supervised Vision Transformers — análise de ViTs só de visão — RETRIEVAL
- P487 — Visual Representation Learning with Self-Supervised Attention for Low… — ViTs auto-supervisionados só de visão — RETRIEVAL
- P488 — On the Use of Graph Neural Networks for Virtual Network Embedding — virtual network embedding (5G), não é VLM — GENERATE
- P490 — CAFuser: Condition-Aware Multimodal Fusion for Robust Semantic Percep… — fusão multimodal de sensores, sem texto — GENERATE
- P499 — Sensor2Text: Enabling Natural Language Interactions for Daily Activit… — sensores vestíveis — GENERATE
- P505 — Development of Compositionality and Generalization through Interactiv… — ação-linguagem em robótica sem imagem-texto estrito — GENERATE
- P509 — A Knowledge-Driven Cross-view Contrastive Learning for EEG Representa… — sinais EEG, não texto-imagem — GENERATE
- P510 — Active Learning for Classifying 2D Grid-Based Level Completability — níveis de jogos (aprendizado ativo), não é VLM — GENERATE
- P520 — Generation Of Colors using Bidirectional LSTM Networks — nomeação de cores com BiLSTM — GENERATE
- P521 — Deep Active Learning with Noise Stability — aprendizado ativo genérico, não multimodal — GENERATE
- P540 — MambaTron: Efficient Cross-Modal Point Cloud Enhancement — imagem + nuvem de pontos, sem texto — GENERATE
- P577 — Optimus-1: Hybrid Multimodal Memory Empowered Agents — agente Minecraft (texto-imagem apenas indireto) — GENERATE
- P610 — StorSeismic: A new paradigm in deep learning for seismic processing — dados sísmicos — GENERATE
- P611 — Labeled Data Generation with Inexact Supervision — geração de dados rotulados (texto e imagem separados) — GENERATE
- P612 — Efficiency-oriented approaches for self-supervised speech representat… — survey de aprendizado auto-supervisionado para fala — GENERATE
- P613 — GOFA: A Generative One-For-All Model for Joint Graph Language Modeling — grafos com atributos de texto — GENERATE
- P614 — BatchSampler: Sampling Mini-Batches for Contrastive Learning — aprendizado contrastivo unimodal/grafos — GENERATE
- P625 — Align-IQA: Aligning Image Quality Assessment Models with Diverse Huma… — avaliação de qualidade de imagem (IQA) — IMAGE-TEXT
- P630 — Internal Embeddings of Multi-modal LLMs as Generalizable Representati… — avaliação de qualidade de imagem (IQA) — GENERATE

### Dataset/benchmark como contribuição central (10)

- P021 — Comprehensive Visual Question Answering on Point Clouds through Compo… — dataset CLEVR3D (+ método) — VQA
- P122 — Insect-Foundation: A Foundation Model and Large Multimodal Dataset fo… — dataset multimodal de insetos (+ modelo) — TEXT-IMAGE
- P135 — FINEMATCH: Aspect-based Fine-grained Image and Text Mismatch Detectio… — benchmark/tarefa FineMatch (+ modelo) — IMAGE-TEXT, TEXT-IMAGE
- P203 — Knowledge-Routed Visual Question Reasoning: Challenges for Deep Repre… — dataset/benchmark KRVQR — IMAGE-TEXT
- P207 — Exploring Synthetic Captions for Remote Sensing Vision-Text Foundatio… — dataset de legendas sintéticas RS (+ modelos) — IMAGE-TEXT
- P210 — Construction and Applications of Billion-Scale Pre-Trained Multimodal… — OpenBG (grafo de conhecimento + benchmark) — IMAGE-TEXT
- P235 — Derm1M: A Million-scale Vision-Language Dataset Aligned with Clinical… — dataset Derm1M (+ modelo DermLIP) — IMAGE-TEXT
- P321 — VISTA: A Visual and Textual Attention Dataset for Interpreting Multim… — dataset VISTA de atenção — IMAGE-TEXT
- P532 — STING-BEE: VLM for Real-World X-ray Baggage Security Inspection — dataset STCray (+ modelo STING-BEE) — GENERATE
- P561 — Taking Notes Brings Focus? Multi-Turn Multimodal Dialogue Learning — dataset MMDiag (+ DiagNote) — GENERATE

### Estudo/análise sem método novo (13)

- P082 — MLP Architectures for Vision-and-Language Modeling: An Empirical Study — estudo empírico — VQA
- P083 — An Empirical Study of Training End-to-End Vision-and-Language Transfo… — estudo empírico — VQA
- P126 — Understanding the Limits of Vision Language Models Through the Lens o… — estudo de limites dos VLMs — TEXT-IMAGE
- P127 — Exploring Curriculum Learning for Vision-Language Tasks: A Study on S… — estudo (BabyLM) — TEXT-IMAGE
- P270 — Probing the Role of Positional Information in Vision-Language Models — análise (probing) — IMAGE-TEXT
- P431 — Enhancing Image Retrieval : A Comprehensive Study on Photo Search usi… — estudo/revisão do CLIP sem experimentos próprios — RETRIEVAL
- P434 — An Empirical Study of CLIP for Text-based Person Search — estudo empírico — RETRIEVAL
- P437 — An Empirical Study of Multimodal Model Merging — estudo empírico — GENERATE, RETRIEVAL
- P459 — Identifying Implicit Social Biases in Vision-Language Models — análise de vieses sem método novo — RETRIEVAL
- P464 — Exploring the Meaningfulness of Nearest Neighbor Search in High-Dimen… — análise de NNS em alta dimensão (não específica de VLMs) — RETRIEVAL
- P465 — Shaking Up VLMs: Comparing Transformers and Structured State Space Mo… — comparação de arquiteturas — RETRIEVAL
- P467 — Exploring the Spectrum of Visio-Linguistic Compositionality and Recog… — estudo de avaliação — RETRIEVAL
- P513 — Language with Vision: a Study on Grounded Word and Sentence Embeddings — estudo — GENERATE

### Tipo de documento (white paper, desafio, plataforma) (3)

- P485 — VL: Leveraging Vision and Vision-language Models into Large-scale Pro… — Solução de desafio — RETRIEVAL
- P522 — Designing Ecosystems of Intelligence from First Principles — White paper conceitual (CE5) — GENERATE
- P583 — LEGENT: Open Platform for Embodied Agents — Plataforma/ferramenta (não método) — GENERATE

### Domínio de agentes/robótica (verificar aderência) (7)

- P155 — Vision-Language Navigation with Random Environmental Mixup — verificar aderência a texto-imagem — IMAGE-TEXT
- P556 — Graph based Environment Representation for Vision-and-Language Naviga… — verificar aderência a texto-imagem — GENERATE
- P578 — LLARVA: Vision-Action Instruction Tuning Enhances Robot Learning — verificar aderência a texto-imagem — GENERATE
- P582 — A Self-Correcting Vision-Language-Action Model for Fast and Slow Syst… — verificar aderência a texto-imagem — GENERATE
- P588 — PlayFusion: Skill Acquisition via Diffusion from Language-Annotated P… — verificar aderência a texto-imagem — GENERATE
- P590 — Octopus: Embodied Vision-Language Programmer from Environmental Feedb… — verificar aderência a texto-imagem — GENERATE
- P631 — AIGeN: An Adversarial Approach for Instruction Generation in VLN — verificar aderência a texto-imagem — GENERATE

### Avaliados só pelo resumo (5)

- P181 — A Mutually Textual and Visual Refinement Network for Image-Text Match… — texto completo indisponível — IMAGE-TEXT
- P190 — Language Guided Local Infiltration for Interactive Image Retrieval — texto completo indisponível — IMAGE-TEXT, RETRIEVAL
- P202 — Semantic Threads Enabling Image-Text Retrieval via VQA Transformers — texto completo indisponível — IMAGE-TEXT
- P365 — ChangeCLIP: Remote sensing change detection with multimodal vision-la… — texto completo indisponível — IMAGE-TEXT
- P377 — TinyCMR: A Lightweight Learning Framework for Efficient Cross-Modal R… — texto completo indisponível — RETRIEVAL

Vídeo apenas: nenhum trabalho identificado como exclusivamente de vídeo (busca no título/resumo); P499 (Sensor2Text, sensores vestíveis) está listado como fora do escopo.
