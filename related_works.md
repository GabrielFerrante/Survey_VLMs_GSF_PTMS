# Trabalhos Relacionados — Surveys sobre VLMs e Métodos de Aprendizado

Este documento apresenta os surveys e trabalhos relacionados identificados durante a revisão sistemática sobre métodos de aprendizado para Vision-Language Models (VLMs) com foco em cenários de dados rotulados limitados.

---

## 1. Visual Tuning

**Autores:** Bruce X.B. Yu, Jianlong Chang, Haixin Wang et al.
**Venue/Ano:** ACM Computing Surveys, Vol. 56, No. 12, July 2024
**DOI:** https://doi.org/10.1145/3657632

**Escopo:** Primeiro survey abrangente sobre *visual tuning* — técnicas para reutilizar modelos foundation pré-treinados via ajuste eficiente de parâmetros (PETL). Categoriza as técnicas em cinco grupos: fine-tuning, prompt tuning, adapter tuning, parameter tuning e remapping tuning.

**Relevância:** Cobre estratégias de adaptação de modelos visuais que são centrais para VLMs em cenários com dados limitados, onde o full fine-tuning é inviável. Aborda LoRA, adapters e prompt tuning — métodos frequentemente encontrados nos artigos da nossa revisão.

---

## 2. Multi-modal Misinformation Detection: Approaches, Challenges and Opportunities

**Autores:** Sara Abdali, Sina Shaham, Bhaskar Krishnamachari
**Venue/Ano:** ACM Computing Surveys, Vol. 57, No. 3, November 2024
**DOI:** https://doi.org/10.1145/3697349

**Escopo:** Survey sobre detecção de desinformação multimodal, classificando a pesquisa em três direções: estudo de dados multimodais, estudo de features multimodais e estudo de modelos multimodais. Cobre fusão cross-modal, VQA, image captioning e técnicas de detecção de fake news.

**Relevância:** Demonstra aplicação direta de VLMs em tarefas de verificação de conteúdo, utilizando alinhamento texto-imagem e aprendizado contrastivo — métodos centrais na nossa revisão.

---

## 3. Foundations and Trends in Multimodal Machine Learning: Principles, Challenges, and Open Questions

**Autores:** Paul Pu Liang, Amir Zadeh, Louis-Philippe Morency
**Venue/Ano:** ACM Computing Surveys, Vol. 56, No. 10, June 2024
**DOI:** https://doi.org/10.1145/3656580

**Escopo:** Survey fundacional que define três princípios-chave do aprendizado multimodal — heterogeneidade, conexões e interações entre modalidades — e propõe uma taxonomia de seis desafios: representação, alinhamento, raciocínio, geração, transferência e quantificação.

**Relevância:** Fornece o arcabouço teórico fundamental para compreender os desafios de VLMs. A taxonomia de seis desafios complementa nossa análise baseada em questões de pesquisa (QP1-QP7).

---

## 4. Analyzing the Robustness of Vision & Language Models

**Autores:** Alexander Shirnin, Nikita Andreev, Sofia Potapova, Ekaterina Artemova
**Venue/Ano:** IEEE/ACM Transactions on Audio, Speech, and Language Processing, Vol. 32, 2024
**DOI:** 10.1109/TASLP.2024.3399061

**Escopo:** Estudo empírico sobre robustez de modelos V&L (LXMERT, VisualBERT, OFA) sob perturbações de imagem e texto na tarefa de VQA. Avalia 5 perturbações visuais e 9 textuais, analisando mecanismos de atenção cross-modal.

**Relevância:** Diretamente conectado à QP5 (explicabilidade) e QP7 (avaliação multimodal). Revela que modelos V&L tendem a sobreajustar em modalidades individuais, questionando a eficácia do alinhamento cross-modal.

---

## 5. Progress and Thinking on Self-Supervised Learning Methods in Computer Vision: A Review

**Autores:** Zhihua Chen, Bo Hu, Zhongsheng Chen, Jiarui Zhang
**Venue/Ano:** IEEE Sensors Journal, Vol. 24, No. 19, October 2024
**DOI:** 10.1109/JSEN.2024.3443885

**Escopo:** Review sobre métodos de aprendizado auto-supervisionado (SSL) em visão computacional, classificados em quatro categorias: baseados em contexto, aprendizado contrastivo (CL), algoritmos generativos e masked image modeling (MIM). Cobre evolução de 2010 a 2024.

**Relevância:** Diretamente alinhado à QP1 (métodos de aprendizado) e QP3 (semi-supervisionado). SSL é uma estratégia fundamental para treinar VLMs sem dados rotulados em larga escala.

---

## 6. When Multitask Learning Meets Partial Supervision: A Computer Vision Review

**Autores:** Maxime Fontana, Michael Spratling, Miaojing Shi
**Venue/Ano:** Proceedings of the IEEE, Vol. 112, No. 6, June 2024
**DOI:** 10.1109/JPROC.2024.3435012

**Escopo:** Primeiro survey focado em aprendizado multitarefa (MTL) com supervisão parcial em visão computacional. Aborda compartilhamento de parâmetros, desafios de otimização multi-objetivo, agrupamento de tarefas e métodos parcialmente supervisionados (self-supervised, semi-supervised, few-shot).

**Relevância:** Conecta MTL a cenários de supervisão limitada — exatamente o foco da nossa revisão. Aborda como o compartilhamento de representações entre tarefas pode reduzir a dependência de dados rotulados.

---

## 7. A Survey of Label-Efficient Deep Learning for 3D Point Clouds

**Autores:** Aoran Xiao, Xiaoqin Zhang, Ling Shao, Shijian Lu
**Venue/Ano:** IEEE TPAMI, Vol. 46, No. 12, December 2024
**DOI:** 10.1109/TPAMI.2024.3416302

**Escopo:** Survey sobre aprendizado eficiente em rótulos para nuvens de pontos 3D, com taxonomia baseada em quatro abordagens: data augmentation, domain transfer, weakly-supervised learning e pretrained foundation models (incluindo VLMs). Fortemente cita aprendizado ativo.

**Relevância:** Paralelo direto com nossa revisão — foco em label-efficient learning, incluindo semi-supervisionado, auto-supervisionado e modelos foundation. Destaca a integração de VLMs (CLIP) em cenários 3D com dados escassos.

---

## 8. A Survey on Self-Supervised Learning: Algorithms, Applications, and Future Trends

**Autores:** Jie Gui, Tuo Chen, Jing Zhang et al.
**Venue/Ano:** IEEE TPAMI, Vol. 46, No. 12, December 2024
**DOI:** 10.1109/TPAMI.2024.3415112

**Escopo:** Survey extenso sobre SSL cobrindo algoritmos (context-based, CL, generativos, contrastivos), aplicações em processamento de imagens, visão computacional e NLP, e três tendências principais. Google Scholar reporta ~18.900 papers SSL somente em 2021.

**Relevância:** Complementa diretamente QP1 e QP3. Cobre a pipeline geral SSL (pre-training → downstream fine-tuning) que é fundamental para VLMs. Diferencia SSL de paradigmas supervisionados e não-supervisionados.

---

## 9. A Survey on Open-Vocabulary Detection and Segmentation: Past, Present, and Future

**Autores:** Chaoyang Zhu, Long Chen
**Venue/Ano:** IEEE TPAMI, Vol. 46, No. 12, December 2024
**DOI:** 10.1109/TPAMI.2024.3413013

**Escopo:** Survey sobre detecção e segmentação open-vocabulary (OVD/OVS), com taxonomia baseada em sinais de supervisão fraca: visual-semantic space mapping, novel visual feature synthesis, region-aware training, pseudo-labeling, knowledge distillation e transfer learning via VLMs (CLIP).

**Relevância:** Demonstra como VLMs habilitam generalização para classes não vistas usando supervisão fraca (image-text pairs). Diretamente ligado a QP1 (métodos de aprendizado) e aborda cenários de dados limitados.

---

## 10. An Overview of Text-Based Person Search: Recent Advances and Future Directions

**Autores:** Kai Niu, Yanyi Liu, Yuzhou Long et al.
**Venue/Ano:** IEEE TCSVT, Vol. 34, No. 9, September 2024
**DOI:** 10.1109/TCSVT.2024.3376373

**Escopo:** Survey sobre busca de pessoas baseada em texto (TBPS), cobrindo extração de features (visual e textual) e alinhamento semântico cross-modal (atenção cross-modal, alinhamentos não-atencionais, objetivos de treinamento e abordagens generativas).

**Relevância:** Aplicação específica de retrieval text-image com alinhamento fino entre modalidades. Relevante para a categoria Retrieval e demonstra desafios de correspondência cross-modal em granularidade fina.

---

## 11. Toward Label-Efficient Emotion and Sentiment Analysis

**Autores:** Sicheng Zhao, Xiaopeng Hong, Jufeng Yang et al.
**Venue/Ano:** Proceedings of the IEEE, Vol. 111, No. 10, October 2023
**DOI:** 10.1109/JPROC.2023.3309299

**Escopo:** Introduz label-efficient emotion and sentiment analysis (LeESA), com taxonomia hierárquica de sete paradigmas: não-supervisionado, semi-supervisionado, weakly-supervised, low-shot, incremental, domain-adaptive e domain-generalizable.

**Relevância:** Survey-chave para QP3 e QP4. Taxonomia de sete paradigmas de aprendizado eficiente em rótulos é diretamente análoga ao escopo da nossa revisão. Multimodal (texto, imagem, vídeo, fisiológico).

---

## 12. How to Practice VQA on a Resource-limited Target Domain

**Autores:** Mingda Zhang, Rebecca Hwa, Adriana Kovashka
**Venue/Ano:** IEEE/CVF WACV 2023
**DOI:** 10.1109/WACV56688.2023.00443

**Escopo:** Investigação sistemática de transferência de conhecimento para VQA em domínios com dados limitados. Compara estratégias sob cenários não-supervisionado, auto-supervisionado, semi-supervisionado e totalmente supervisionado. Conclui que adaptação semi-supervisionada é mais eficaz quando recursos são limitados.

**Relevância:** Artigo-chave para nossa revisão — aborda diretamente VQA com dados escassos, QP1, QP3, QP4, QS3. Demonstra experimentalmente que semi-supervised learning é a melhor estratégia para VQA em domínios com recursos limitados.

---

## 13. Diffusion Models: A Comprehensive Survey of Methods and Applications

**Autores:** Ling Yang, Zhilong Zhang, Yang Song et al.
**Venue/Ano:** ACM Computing Surveys, 2023
**DOI:** https://doi.org/10.1145/3626235

**Escopo:** Survey abrangente de 58 páginas sobre modelos de difusão, cobrindo fundamentos (DDPMs, SGMs, Score SDEs), amostragem eficiente, likelihood melhorada, aplicações em CV, NLP, geração multimodal (text-to-image, text-to-3D, text-to-video) e aplicações interdisciplinares (drug design, medical imaging).

**Relevância:** Cobre a categoria Generate da nossa revisão. Modelos de difusão condicionados por texto representam a fronteira da geração text-to-image. Relevante para QP1 e QP7.

---

## 14. Multimodality Representation Learning: A Survey on Evolution, Pretraining and Its Applications

**Autores:** Muhammad Arslan Manzoor, Sarah AlBarri, Ziting Xian et al.
**Venue/Ano:** ACM, 2023
**DOI:** https://arxiv.org/abs/2302.00389

**Escopo:** Survey sobre aprendizado de representação multimodal cobrindo a evolução de métodos task-specific para pretraining unificado. Aborda tipos de pretraining (supervisionado, semi-supervisionado, auto-supervisionado), objetivos de pretext tasks, arquiteturas e downstream tasks (VQA, retrieval, classificação).

**Relevância:** Complementa diretamente nosso survey cobrindo a pipeline de pretraining multimodal. Aborda fusão de modalidades, alinhamento e evolução de arquiteturas — temas transversais às nossas categorias de tarefa.

---

## 15. A Survey on Safe Multi-Modal Learning Systems

**Autores:** Tianyi Zhao, Liangliang Zhang, Yao Ma, Lu Cheng
**Venue/Ano:** ACM SIGKDD (KDD '24), August 2024
**DOI:** https://doi.org/10.1145/3637528.3671462

**Escopo:** Primeira taxonomia para segurança de sistemas multimodais (MMLS), estruturada em quatro pilares: robustez (distributional shift, adversarial), alinhamento (jailbreaking, misalignment), monitoramento (anomaly detection, calibração) e controlabilidade (explicabilidade, privacidade, fairness).

**Relevância:** Aborda aspectos de robustez e confiabilidade de VLMs — complementar à QP5 (explicabilidade) e importante para deployment real de modelos treinados com dados limitados.

---

## 16. Heterogeneous Contrastive Learning for Foundation Models and Beyond

**Autores:** Lecheng Zheng, Baoyu Jing, Zihao Li et al.
**Venue/Ano:** ACM SIGKDD (KDD '24), August 2024
**DOI:** https://doi.org/10.1145/3637528.3671454

**Escopo:** Survey sobre aprendizado contrastivo heterogêneo para modelos foundation, cobrindo heterogeneidade de visão (multi-view) e de tarefa. Categoriza métodos para pretraining (pretext tasks, supervised, auxiliary) e downstream (prompting, multi-task, task reformulation). Cobre CLIP e variantes.

**Relevância:** Aprendizado contrastivo é o método dominante em VLMs (CLIP, ALIGN). Diretamente ligado a QP1. Aborda como CL habilita aprendizado auto-supervisionado cross-modal — fundamental para cenários com dados limitados.

---

## 17. Rethinking Benchmarks for Cross-modal Image-text Retrieval

**Autores:** Weijing Chen, Linli Yao, Qin Jin
**Venue/Ano:** ACM SIGIR '23, July 2023
**DOI:** https://doi.org/10.1145/3539618.3591758

**Escopo:** Propõe novos benchmarks para retrieval imagem-texto (MSCOCO-FG, Flickr30K-FG) que exigem compreensão semântica fine-grained, revelando que modelos SOTA que atingem performance quase perfeita em benchmarks atuais falham em cenários mais desafiadores com imagens similares.

**Relevância:** Diretamente relevante para a categoria Retrieval. Questiona a adequação dos benchmarks existentes — conectado à QP6 (documentação de datasets) e QP7 (critérios de avaliação).

---

## 18. Recent Advances of Foundation Language Models-based Continual Learning: A Survey

**Autores:** Yutao Yang, Jie Zhou, Xuanwen Ding et al.
**Venue/Ano:** ACM (ArXiv), 2024

**Escopo:** Survey sobre aprendizado contínuo (CL) baseado em modelos foundation de linguagem (PLMs, LLMs, VLMs). Taxonomia divide em offline CL (domain/task/class-incremental) e online CL (hard/blurry task boundary). Aborda catastrophic forgetting, parameter-efficient tuning e instruction-based methods.

**Relevância:** Aprendizado contínuo é essencial quando VLMs precisam se adaptar a novos domínios sem esquecer conhecimento anterior — relevante para cenários de dados limitados e QP1.

---

## 19. A Comprehensive Survey of AI-Generated Content (AIGC): A History of Generative AI from GAN to ChatGPT

**Autores:** Yihan Cao, Siyu Li, Yixin Liu et al.
**Venue/Ano:** J. ACM, Vol. 37, No. 4, 2023

**Escopo:** Survey sobre conteúdo gerado por IA (AIGC), cobrindo a evolução de GANs a ChatGPT e DALL-E 2. Aborda geração unimodal (texto, imagem) e multimodal (text-to-image, text-to-video, text-to-audio), fundamentos técnicos e aplicações.

**Relevância:** Cobre a categoria Generate da nossa revisão. Contextualiza a evolução dos modelos generativos e sua integração com VLMs para geração cross-modal.

---

## 20. A Comprehensive Survey of Vision-Language Models: Pretrained Models, Fine-tuning, Prompt Engineering, Adapters, and Benchmark Datasets

**Autores:** Sufyan Danish, Abolghasem Sadeghi-Niaraki, Samee Ullah Khan et al.
**Venue/Ano:** Information Fusion, Vol. 126, 2026
**DOI:** https://doi.org/10.1016/j.inffus.2025.103623

**Escopo:** Survey sistemático de 115 artigos (2018-2025) sobre componentes-chave de VLMs: fine-tuning (LoRA, BitFit, domain-specific), prompt engineering (discrete, continuous, zero/few-shot), adapters (fusion, non-fusion, multi-modal), modelos pré-treinados e datasets de benchmark. Primeiro survey a integrar todos esses componentes em um trabalho coeso.

**Relevância:** O survey mais próximo ao nosso em escopo — cobre VLMs de forma abrangente. Porém, foca em técnicas de otimização (fine-tuning, prompting, adapters) enquanto nossa revisão foca especificamente em métodos de aprendizado para cenários com dados limitados.

---

## Análise Comparativa com Nossa Abordagem de Survey

### Posicionamento da Nossa Revisão

| Dimensão | Surveys Existentes | Nossa Revisão |
|----------|-------------------|---------------|
| **Foco principal** | Arquiteturas, técnicas de otimização, ou domínios específicos | Métodos de aprendizado para VLMs em cenários com dados rotulados limitados |
| **Métodos de aprendizado** | Geralmente cobrem 1-2 paradigmas (ex: SSL ou CL) | Cobre sistematicamente semi-supervisionado, auto-supervisionado, ativo e cross-modal |
| **Questões de pesquisa** | Geralmente sem protocolo estruturado | 7 QPs + 4 QSs com avaliação quantitativa de 599 artigos |
| **Categorias de tarefa** | Foco em 1-2 tarefas (ex: só VQA, só retrieval) | 5 categorias simultâneas (VQA, Text-Image, Image-Text, Retrieval, Generate) |
| **Período** | Variável, frequentemente sem corte temporal definido | Mai/2020 – Mai/2025, com protocolo de busca reprodutível |
| **Metodologia** | Majoritariamente revisões narrativas | Revisão sistemática com protocolo, critérios de inclusão/exclusão e avaliação de qualidade (0-11 pts) |

### Lacunas Cobertas pela Nossa Revisão

1. **Aprendizado ativo em VLMs (QP4):** Apenas 18 dos 599 artigos abordam active learning — os surveys existentes (Xiao et al., 2024; Zhao et al., 2023) mencionam AL apenas para domínios específicos (point clouds, emoções), enquanto nossa revisão mapeia sistematicamente sua escassez em VLMs de forma transversal.

2. **Grafos para relações texto-imagem (QP2):** Nenhum survey existente trata grafos como elemento central para modelar relações cross-modais em VLMs. Nossa revisão identifica 163 artigos que empregam estruturas de grafos — um eixo ainda não consolidado na literatura.

3. **Cenários de dados limitados de forma transversal:** Surveys como Gui et al. (2024) ou Chen et al. (2024) cobrem SSL/semi-supervised para domínios unimodais (CV). Nossa revisão é específica para o cenário multimodal texto-imagem, onde a escassez de dados rotulados é amplificada pela necessidade de alinhar duas modalidades.

4. **Avaliação de qualidade estruturada:** Os 20 surveys analisados utilizam revisões narrativas ou semi-estruturadas. Nossa revisão aplica uma escala de 11 pontos com critérios quantitativos reprodutíveis, alinhando-se às diretrizes de revisões sistemáticas.

5. **Cobertura de múltiplas tarefas simultaneamente:** Enquanto Danish et al. (2026) cobrem VLMs de forma ampla, focam em otimização (fine-tuning, adapters). Nossa revisão cruza 5 categorias de tarefa com 4 eixos de aprendizado (semi-supervisionado, auto-supervisionado, ativo, cross-modal), revelando padrões e lacunas por combinação.

### Complementaridade

Nossa revisão se complementa com os trabalhos existentes da seguinte forma:

- **Fundamentos teóricos:** Liang et al. (2024) fornece a base conceitual (heterogeneidade, alinhamento, transferência) que nossa revisão aplica empiricamente aos 599 artigos.
- **Técnicas específicas:** Yu et al. (2024) detalha visual tuning; Zheng et al. (2024) detalha contrastive learning — técnicas que aparecem nos artigos da nossa revisão, mas que analisamos sob a ótica de eficiência de dados.
- **Domínios de aplicação:** Xiao et al. (2024) e Zhao et al. (2023) cobrem domínios específicos (3D, emoções) onde label-efficient learning é aplicado; nossa revisão analisa o fenômeno de forma transversal em VLMs.
- **Avaliação e benchmarks:** Chen et al. (2023) questiona benchmarks de retrieval; nossa QP6 e QP7 avaliam sistematicamente a documentação e adequação de datasets/métricas nos 599 artigos selecionados.
