"""PRISMA-like selection flow diagram for the systematic review.

Counts come from the review spreadsheet (tabs 'Strings de busca', 'FASE 1 - SELEÇÃO INICIAL'
and 'FASE 2 - SELEÇÃO FINAL'); see avaliacao_qualidade/ for the quality assessment.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from style import apply_style, FIGURES_DIR

apply_style()

# --- Counts ---------------------------------------------------------------------------
RETRIEVED = 6989                       # search results (IEEE 3653, ArXiv 3150, SciDir 16, ACM 170)
PHASE1 = 1649                          # task-level records in the Phase 1 tab (1145 unique titles)
EXCL_NO_ANALYSIS, EXCL_LT3, EXCL_OTHER = 527, 304, 21
EXCLUDED = EXCL_NO_ANALYSIS + EXCL_LT3 + EXCL_OTHER   # 852, all coded CE1
KEPT = PHASE1 - EXCLUDED                              # 797
REPEATED = 6                           # repeated entries of one paper inside the same category
FINAL = KEPT - REPEATED                # 791 category assignments (606 unique papers)
assert (EXCLUDED, KEPT, FINAL) == (852, 797, 791)


def n(v):
    """Thousands separator used in the manuscript (6.989)."""
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
    return y + h / 2 + PAD, y - h / 2 - PAD        # top, bottom (outer edge)


def side_box(y, h, text, **kw):
    kw.setdefault('edge', '#CCCCCC')
    draw_box(SIDE_X, y, SIDE_W, h, text, fontsize=7.8, bold=False, **kw)
    # dashed arrow from the vertical flow line to the side box
    arrow(MAIN_X, y, SIDE_X - SIDE_W / 2 - PAD - 0.02, y, side=True)


# --- main flow (y centre, height) ---
top_id, bot_id = main_box(14.6, 0.9, f'Identification\n{n(RETRIEVED)} search results retrieved',
                          color='#D1E5F0', fontsize=10)
top_src, bot_src = main_box(13.1, 0.9, 'IEEE Xplore: 3.653  |  ArXiv: 3.150\nScience Direct: 16  |  ACM: 170',
                            color='#F7F7F7', fontsize=8.5)
top_p1, bot_p1 = main_box(11.2, 1.3,
                          f'Phase 1 — Initial selection\n{n(PHASE1)} records (task level)\n'
                          '1.145 unique titles; title, abstract\n',
                          color='#FDDBC7', fontsize=9.5)
top_p2, bot_p2 = main_box(8.9, 1.4,
                          f'Phase 2 — Final selection\n{n(KEPT)} records retained\n'
                          'Full-text eligibility (QP1–QP7, QS1–QS4)\nminimum of 3 questions answered',
                          color='#FDDBC7', fontsize=9.5)
top_inc, bot_inc = main_box(6.4, 1.5,
                            f'Included — 606 unique papers\n({n(FINAL)} category assignments)\n'
                            'VQA: 89  |  Text-Image: 71  |  Image-Text: 259\nRetrieval: 226  |  Generate: 146',
                            color='#FFF9C4', edge='#F9A825', fontsize=9)
top_q, bot_q = main_box(4.1, 1.2,
                        'Quality assessment\nAll 606 papers scored (0–13 points)\nNo paper excluded by score',
                        color='#FDDBC7', fontsize=9.5)
top_s, bot_s = main_box(2.0, 1.2,
                        'Synthesis — 606 papers analyzed\n(Top 10 per task shown for presentation only)',
                        color='#B2DF8A', fontsize=9.5)

for upper_bottom, lower_top in [(bot_id, top_src), (bot_src, top_p1), (bot_p1, top_p2),
                                (bot_p2, top_inc), (bot_inc, top_q), (bot_q, top_s)]:
    arrow(MAIN_X, upper_bottom - 0.02, MAIN_X, lower_top + 0.02)

# --- side boxes, vertically centred on the gaps between main boxes ---
side_box((bot_src + top_p1) / 2, 1.55,
         f'Not carried to Phase 1: {n(RETRIEVED - PHASE1)}\n(repeated results across queries\nand tasks, and title/abstract\nscreening; not itemized)',
         color='#F7F7F7')
side_box((bot_p1 + top_p2) / 2, 1.75,
         f'Excluded (CE1): {n(EXCLUDED)}\n'
         f'• {EXCL_NO_ANALYSIS} by title/abstract\n  (insufficient information)\n'
         f'• {EXCL_LT3} answered < 3 questions\n• {EXCL_OTHER} other inclusion criteria',
         color='#FEE0D2')
side_box((bot_p2 + top_inc) / 2, 1.4,
         f'Removed: {REPEATED}\n(repeated entries of the same\npaper in the same category,\nincluding title variants)',
         color='#FEE0D2')

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_prisma_flow.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_prisma_flow.png')
print('Saved: fig_prisma_flow.pdf / .png')
