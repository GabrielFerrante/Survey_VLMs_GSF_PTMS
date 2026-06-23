"""PRISMA-like selection flow diagram for the systematic review."""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from style import apply_style, COLORS, FIGURES_DIR

apply_style()

fig, ax = plt.subplots(figsize=(7, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')


def draw_box(ax, x, y, w, h, text, color='white', edge='#333333', fontsize=10):
    rect = mpatches.FancyBboxPatch(
        (x - w / 2, y - h / 2), w, h,
        boxstyle='round,pad=0.15', facecolor=color,
        edgecolor=edge, linewidth=1.2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight='bold', linespacing=1.4)
    return rect


def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#555555',
                                lw=1.5, connectionstyle='arc3,rad=0'))


def draw_side_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#999999',
                                lw=1.2, linestyle='--'))


# --- Identification ---
draw_box(ax, 5, 11, 7, 0.9,
         'Identification\n6,854 documents retrieved',
         color='#D1E5F0', fontsize=10)

draw_arrow(ax, 5, 10.55, 5, 9.95)

# Sources breakdown
draw_box(ax, 5, 9.5, 7, 0.8,
         'IEEE Xplore: 3,653  |  ArXiv: 3,185  |  Science Direct: 16',
         color='#F7F7F7', fontsize=8.5)

draw_arrow(ax, 5, 9.1, 5, 8.3)

# --- Screening Phase 1 ---
draw_box(ax, 5, 7.8, 7, 0.9,
         'Phase 1 — Initial Screening\nTitle + Abstract review',
         color='#FDDBC7', fontsize=10)

draw_side_arrow(ax, 8.5, 7.8, 9.5, 7.0)
draw_box(ax, 9.2, 6.5, 1.8, 0.7,
         'Excluded\n(CI/CE)',
         color='#FEE0D2', edge='#CCCCCC', fontsize=8)

draw_arrow(ax, 5, 7.35, 5, 6.55)

# --- Eligibility Phase 2 ---
draw_box(ax, 5, 6.0, 7, 0.9,
         'Phase 2 — Full-text Eligibility\nResearch questions + Quality assessment',
         color='#FDDBC7', fontsize=10)

draw_side_arrow(ax, 8.5, 6.0, 9.5, 5.2)
draw_box(ax, 9.2, 4.7, 1.8, 0.7,
         'Excluded\n(< 2 QPs)',
         color='#FEE0D2', edge='#CCCCCC', fontsize=8)

draw_arrow(ax, 5, 5.55, 5, 4.75)

# --- Included ---
draw_box(ax, 5, 4.2, 7, 0.9,
         'Included\n599 unique papers (775 category assignments)',
         color='#B2DF8A', fontsize=10)

draw_arrow(ax, 5, 3.75, 5, 3.15)

# --- Task breakdown ---
tasks_text = ('VQA: 84   |   Text-Image: 68   |   Image-Text: 249\n'
              'Retrieval: 225   |   Generate: 149')
draw_box(ax, 5, 2.5, 7, 0.9,
         tasks_text,
         color='#E6F5E6', edge='#66BB6A', fontsize=9)

fig.tight_layout()
fig.savefig(f'{FIGURES_DIR}/fig_prisma_flow.pdf')
fig.savefig(f'{FIGURES_DIR}/fig_prisma_flow.png')
print('Saved: fig_prisma_flow.pdf / .png')
