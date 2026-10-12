"""Paradigmas de aprendizado mencionados por artigo (QP1), por categoria de tarefa.

Texto analisado por artigo: título + descrição de QP1 registrada na Fase 1 (quando existe) + resumo.
Um artigo pode mencionar vários paradigmas. Contagem por atribuição de categoria (791) e por artigo único (606).
"""
import json, re, os, csv
from collections import Counter
D = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(D, 'notes606.json'), encoding='utf-8'))
extra = json.load(open(os.path.join(D, 'abs_extra.json'), encoding='utf-8'))

P = [
 ('Contrastivo', r'contrastiv|infonce|\bITC\b'),
 ('Auto-supervisionado', r'self-?supervis|auto-?supervis|autossupervis|masked (language|image|modal)|\bMLM\b|\bMIM\b|mascarament|masked autoencod'),
 ('Semi-supervisionado / pseudo-rótulos', r'semi-?supervis|semissupervis|pseudo-?(label|rótul|r[oó]tul)|pseudolabel|self-train|auto-?treinamento|autotreinamento'),
 ('Supervisão fraca ou ruidosa', r'weakly|weak supervis|fracamente supervis|supervisão fraca|noisy|ruidos'),
 ('Few-shot / zero-shot', r'few-?shot|zero-?shot|poucos exemplos'),
 ('Prompt tuning / aprendizado de prompts', r'prompt[- ](tuning|learning)|aprendizado de prompt|ajuste de prompt|soft prompt|prompt engineering|engenharia de prompt'),
 ('Ajuste por instruções', r'instruction[- ]?(tun|follow)|ajuste (por|com|de) instru|instruction data'),
 ('Destilação de conhecimento', r'distill|destila'),
 ('Adaptadores / PEFT', r'\badapter|adaptador|\blora\b|parameter-efficient|eficiente em parâmetros'),
 ('Aprendizado por reforço', r'reinforcement learning|aprendizado por reforço|\brlhf\b|\bppo\b'),
 ('Aprendizado ativo', r'active learning|aprendizado ativo'),
 ('Ajuste fino / transferência', r'fine-?tun|ajuste fino|transfer learning|aprendizado por transferência|transferência de conhecimento'),
]


def text_of(k, v):
    qp1 = ''
    for part in (v['notas'] or '').split(' || '):
        m = re.search(r'QP1\s*-(.*?)(?=Q[PS]\d\s*-|$)', part, re.S)
        if m and len(m.group(1)) > len(qp1):
            qp1 = m.group(1)
    return ' '.join([v['title'], qp1, v['abstract'] or '', extra.get(k, '')])


CATS = ['VQA', 'TEXT-IMAGE', 'IMAGE-TEXT', 'RETRIEVAL', 'GENERATE']
N = Counter(); hits = {c: Counter() for c in CATS}; uniq = Counter()
for k, v in data.items():
    t = text_of(k, v)
    found = [name for name, rx in P if re.search(rx, t, re.I)]
    for name in found:
        uniq[name] += 1
    for c in [x.strip() for x in v['cats'].split('|')]:
        N[c] += 1
        for name in found:
            hits[c][name] += 1
print('N', dict(N), sum(N.values()))
rows = []
for name, _ in P:
    tot = sum(hits[c][name] for c in CATS)
    cells = [f'{hits[c][name]} ({100*hits[c][name]/N[c]:.1f}%)'.replace('.', ',') for c in CATS]
    rows.append((name, uniq[name], tot, cells))
    print(f'{name:40s} unicos={uniq[name]:3d} ({100*uniq[name]/606:.1f}%) atrib={tot:3d} ({100*tot/791:.1f}%) | ' + ' | '.join(cells))
json.dump({'N': N, 'hits': {c: dict(hits[c]) for c in CATS}, 'uniq': uniq}, open(os.path.join(D, 'qp1_paradigms.json'), 'w', encoding='utf-8'), ensure_ascii=False)
