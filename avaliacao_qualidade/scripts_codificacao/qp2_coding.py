"""Codificação integral dos 100 artigos com QP2 quanto ao papel do grafo.

G1: grafo no pré-treinamento ou no aprendizado de representações visão-linguagem de propósito geral
G2: grafo como módulo, entrada ou objetivo de um modelo de tarefa específica (raciocínio, fusão, alinhamento)
G3: grafo de conhecimento externo como fonte de conhecimento para a tarefa
G4: grafo como saída (geração de grafo de cena ou de ambiente)
G5: grafo apenas em dados, pré-processamento ou análise, ou fora da modelagem texto-imagem
G0: uso de grafo não identificado no texto disponível (nota da planilha ou resumo)
Fonte: trecho QP2 das notas da aba FASE 1 (74) ou resumo do arXiv/Crossref (26).
"""
import json, os
from collections import Counter

C = {
 'P004': 'G3', 'P010': 'G2', 'P011': 'G2', 'P013': 'G4', 'P014': 'G1', 'P015': 'G3', 'P017': 'G3', 'P019': 'G5',
 'P021': 'G2', 'P022': 'G2', 'P023': 'G2', 'P029': 'G2', 'P031': 'G3', 'P037': 'G3', 'P038': 'G2', 'P040': 'G2',
 'P041': 'G5', 'P043': 'G5', 'P044': 'G2', 'P055': 'G5', 'P056': 'G3', 'P075': 'G2', 'P087': 'G2', 'P092': 'G2',
 'P095': 'G3', 'P096': 'G2', 'P100': 'G2', 'P101': 'G2', 'P103': 'G3', 'P109': 'G2', 'P110': 'G2', 'P115': 'G1',
 'P131': 'G3', 'P132': 'G1', 'P135': 'G5', 'P140': 'G2', 'P141': 'G3', 'P143': 'G1', 'P144': 'G2', 'P155': 'G5',
 'P156': 'G3', 'P161': 'G1', 'P175': 'G2', 'P183': 'G3', 'P185': 'G2', 'P186': 'G3', 'P187': 'G2', 'P189': 'G3',
 'P193': 'G5', 'P203': 'G3', 'P205': 'G4', 'P210': 'G1', 'P225': 'G2', 'P227': 'G2', 'P248': 'G2', 'P261': 'G0',
 'P274': 'G5', 'P275': 'G5', 'P281': 'G2', 'P297': 'G1', 'P306': 'G1', 'P307': 'G5', 'P311': 'G2', 'P316': 'G2',
 'P323': 'G5', 'P333': 'G0', 'P334': 'G3', 'P341': 'G3', 'P353': 'G2', 'P366': 'G2', 'P367': 'G2', 'P370': 'G2',
 'P394': 'G3', 'P395': 'G3', 'P399': 'G2', 'P403': 'G4', 'P411': 'G4', 'P422': 'G0', 'P442': 'G0', 'P444': 'G0',
 'P461': 'G0', 'P483': 'G1', 'P488': 'G5', 'P528': 'G0', 'P542': 'G3', 'P549': 'G0', 'P551': 'G4', 'P555': 'G1',
 'P556': 'G2', 'P576': 'G2', 'P577': 'G3', 'P580': 'G5', 'P595': 'G2', 'P606': 'G2', 'P611': 'G0', 'P613': 'G5',
 'P614': 'G5', 'P618': 'G0', 'P624': 'G0', 'P631': 'G0',
}
D = os.path.dirname(os.path.abspath(__file__))
assert len(C) == 100
data = json.load(open(os.path.join(D, 'notes606.json'), encoding='utf-8'))
cnt = Counter(C.values())
print(sorted(cnt.items()))
for g in sorted(cnt):
    print(g, [k for k, v in C.items() if v == g])
# por categoria de tarefa (atribuicoes)
bycat = {}
for k, g in C.items():
    for c in [x.strip() for x in data[k]['cats'].split('|')]:
        bycat.setdefault(c, Counter())[g] += 1
for c, v in bycat.items():
    print(c, sorted(v.items()))
json.dump(C, open(os.path.join(D, 'qp2_coding.json'), 'w'), indent=0)
