"""Diagrama de fluxo de seleção (PRISMA) da revisão sistemática, versão em português.

As contagens vêm da planilha da revisão (abas 'Strings de busca', 'FASE 1 - SELEÇÃO INICIAL'
e 'FASE 2 - SELEÇÃO FINAL'); a avaliação de qualidade está em avaliacao_qualidade/.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from style import apply_style, FIGURES_DIR

apply_style()

# --- Contagens ------------------------------------------------------------------------
RETRIEVED = 6989                       # resultados da busca (IEEE 3653, ArXiv 3150, SciDir 16, ACM 170)
PHASE1 = 1649                          # registros por tarefa na aba da Fase 1 (1145 títulos únicos)
EXCL_NO_ANALYSIS, EXCL_LT3, EXCL_OTHER = 527, 304, 21
EXCLUDED = EXCL_NO_ANALYSIS + EXCL_LT3 + EXCL_OTHER   # 852, todos com código CE1
KEPT = PHASE1 - EXCLUDED                              # 797
REPEATED = 6                           # repetições do mesmo artigo na mesma categoria
FINAL = KEPT - REPEATED                # 791 atribuições de categoria (606 artigos únicos)
assert (EXCLUDED, KEPT, FINAL) == (852, 797, 791)


def n(v):
    """Separador de milhares usado no manuscrito (6.989)."""
    return f'{v:,}'.replace(',', '.')


PAD = 0.12
MAIN_X, MAIN_W = 3.3, 5.6
SIDE_X, SIDE_W = 8.35, 3.0

fig, ax = plt.subplots(figsize=(7.5, 10.8))
ax.set_xlim(0, 10)
ax.set_ylim(0.9, 15.4)
ax.axis('off')


def draw_box(x, y, w, h, text, color='white', edge='#333333', fontsize=9, bold=True):
    ax.add_patch(mpatches.FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h, boxstyle=f'round,pad={PAD}',
        facecolor=color, edgecolor=edge, linewidth=1.2))
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight='bold' if bold else 'normal', linespacing=1.35)


def arrow(x1, y1, x2, y2, side=False):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#888888' if side else '#555555',
                                lw=1.2 if side else 1.5, linestyle='--' if side else '-'))


def main_box(y, h, text, **kw):
    draw_box(MAIN_X, y, MAIN_W, h, text, **kw)
    return y + h / 2 + PAD, y - h / 2 - PAD        # topo, base (borda externa)


def side_box(y, h, text, **kw):
    kw.setdefault('edge', '#CCCCCC')
    draw_box(SIDE_X, y, SIDE_W, h, text, fontsize=7.8, bold=False, **kw)
    arrow(MAIN_X, y, SIDE_X - SIDE_W / 2 - PAD - 0.02, y, side=True)


# --- fluxo principal (centro y, altura) ---
top_id, bot_id = main_box(14.6, 0.9, f'Identificação\n{n(RETRIEVED)} resultados de busca recuperados',
                          color='#D1E5F0', fontsize=10)
top_src, bot_src = main_box(13.1, 0.9, 'IEEE Xplore: 3.653  |  ArXiv: 3.150\nScience Direct: 16  |  ACM: 170',
                            color='#F7F7F7', fontsize=8.5)
top_p1, bot_p1 = main_box(11.2, 1.3,
                          f'Fase 1 — Seleção inicial\n{n(PHASE1)} registros (por tarefa)\n'
                          '1.145 títulos únicos; título, resumo\ne análise das QP/QS',
                          color='#FDDBC7', fontsize=9.5)
top_p2, bot_p2 = main_box(8.9, 1.4,
                          f'Fase 2 — Seleção final\n{n(KEPT)} registros mantidos\n'
                          'Elegibilidade do texto completo (QP1–QP7, QS1–QS4)\nmínimo de 3 questões respondidas',
                          color='#FDDBC7', fontsize=9.5)
top_inc, bot_inc = main_box(6.4, 1.5,
                            f'Incluídos — 606 artigos únicos\n({n(FINAL)} atribuições de categoria)\n'
                            'VQA: 89  |  Text-Image: 71  |  Image-Text: 259\nRetrieval: 226  |  Generate: 146',
                            color='#FFF9C4', edge='#F9A825', fontsize=9)
top_q, bot_q = main_box(4.1, 1.2,
                        'Avaliação de qualidade\nOs 606 artigos pontuados (0–13 pontos)\nNenhum excluído pela nota',
                        color='#FDDBC7', fontsize=9.5)
top_s, bot_s = main_box(2.0, 1.2,
                        'Síntese — 606 artigos analisados\n(Top 10 por tarefa apenas para apresentação)',
                        color='#B2DF8A', fontsize=9.5)

for upper_bottom, lower_top in [(bot_id, top_src), (bot_src, top_p1), (bot_p1, top_p2),
                                (bot_p2, top_inc), (bot_inc, top_q), (bot_q, top_s)]:
    arrow(MAIN_X, upper_bottom - 0.02, MAIN_X, lower_top + 0.02)

# --- caixas laterais, centradas nos intervalos entre as caixas principais ---
side_box((bot_src + top_p1) / 2, 1.55,
         f'Não levados à Fase 1: {n(RETRIEVED - PHASE1)}\n(resultados repetidos entre consultas\ne tarefas e triagem por título/resumo;\nnão discriminado)',
         color='#F7F7F7')
side_box((bot_p1 + top_p2) / 2, 1.75,
         f'Excluídos (CE1): {n(EXCLUDED)}\n• {EXCL_NO_ANALYSIS} por título/resumo\n  (informação insuficiente)\n'
         f'• {EXCL_LT3} com < 3 questões respondidas\n• {EXCL_OTHER} por outros critérios de inclusão',
         color='#FEE0D2')
side_box((bot_p2 + top_inc) / 2, 1.4,
         f'Removidos: {REPEATED}\n(repetições do mesmo artigo\nna mesma categoria, inclusive\nvariantes de título)',
         color='#FEE0D2')

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_prisma_flow_PTBR.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_prisma_flow_PTBR.png')
print('Saved: fig_prisma_flow_PTBR.pdf / .png')
