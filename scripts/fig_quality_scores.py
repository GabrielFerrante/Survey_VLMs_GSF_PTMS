"""Quality scores distribution and Top 10 papers — one chart per category."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from style import apply_style, COLORS, FIGURES_DIR

apply_style()

QUALITY_DIR = '../avaliacao_qualidade'

categories = {
    'VQA': {'file': f'{QUALITY_DIR}/Avaliacao_Qualidade_VQA.xlsx', 'color': COLORS['vqa']},
    'Text-Image': {'file': f'{QUALITY_DIR}/Avaliacao_Qualidade_Text-Image.xlsx', 'color': COLORS['textimg']},
    'Image-Text': {'file': f'{QUALITY_DIR}/Avaliacao_Qualidade_Image-Text.xlsx', 'color': COLORS['imgtxt']},
    'Generate': {'file': f'{QUALITY_DIR}/Avaliacao_Qualidade_Generate.xlsx', 'color': COLORS['generate']},
    'Retrieval': {'file': f'{QUALITY_DIR}/Avaliacao_Qualidade_Retrieval.xlsx', 'color': COLORS['retrieval']},
}


def load_scores(path):
    """One row per paper in the category (Phase 2). Total uses the protocol scale (0-13)."""
    raw = pd.read_excel(path, sheet_name='Avaliação')
    codes = raw['QPs/QSs (Fase 2)'].fillna('')
    return pd.DataFrame({
        'Title': raw['Título'],
        'Total': raw['TOTAL protocolo (0–13)'],
        'QP_count': codes.str.count(r'Q[PS]\d'),  # questions answered (QPs + QSs)
    })


for cat, info in categories.items():
    df = load_scores(info['file'])
    color = info['color']
    slug = cat.replace(' ', '_').replace('-', '_')

    fig, axes = plt.subplots(1, 2, figsize=(14, 5), gridspec_kw={'width_ratios': [1, 1.4]})

    # --- Left: Score distribution histogram ---
    ax1 = axes[0]
    bins = np.arange(df['Total'].min() - 0.5, 14.5, 1)
    ax1.hist(df['Total'], bins=bins, color=color, edgecolor='white',
             linewidth=0.8, alpha=0.85)
    ax1.set_xlabel('Quality Score (0–13)')
    ax1.set_ylabel('Number of Papers')
    ax1.set_title(f'Score Distribution — {cat} (n={len(df)})')
    ax1.set_xticks(range(int(df['Total'].min()), 14))
    ax1.yaxis.grid(True, linestyle='--', alpha=0.3)
    ax1.set_axisbelow(True)

    mean_score = df['Total'].mean()
    ax1.axvline(mean_score, color=COLORS['secondary'], linestyle='--', linewidth=1.5)
    ax1.text(mean_score + 0.15, ax1.get_ylim()[1] * 0.9,
             f'Mean: {mean_score:.2f}', color=COLORS['secondary'], fontsize=9)

    # --- Right: Top 10 papers by score + QP count ---
    ax2 = axes[1]
    # score first, then number of questions answered; remaining ties keep the Phase 2 order
    top10 = df.sort_values(['Total', 'QP_count'], ascending=[False, False],
                           kind='stable').head(10)

    short_names = []
    for t in top10['Title']:
        short_names.append(t[:42] + '...' if len(t) > 45 else t)

    y_pos = np.arange(len(top10))
    ax2.barh(y_pos, top10['Total'].values, color=color,
             height=0.6, edgecolor='white', linewidth=0.5)

    for i, (score, qps) in enumerate(zip(top10['Total'].values, top10['QP_count'].values)):
        ax2.text(score + 0.15, i, f'{score}/13  ({qps} QPs+QSs)',
                 va='center', fontsize=8.5, fontweight='bold')

    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(short_names, fontsize=7.5)
    ax2.set_xlabel('Quality Score')
    ax2.set_title(f'Top 10 Papers — {cat}')
    ax2.set_xlim(0, 15.5)
    ax2.xaxis.grid(True, linestyle='--', alpha=0.3)
    ax2.set_axisbelow(True)
    ax2.invert_yaxis()

    fig.tight_layout()
    fig.savefig(f'{FIGURES_DIR}/fig_quality_scores-{cat}.pdf')
    fig.savefig(f'{FIGURES_DIR}/fig_quality_scores-{cat}.png')
    plt.close(fig)
    print(f'Saved: fig_quality_scores-{cat}.pdf / .png')
