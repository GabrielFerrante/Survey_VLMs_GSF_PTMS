"""Exporta as codificações de QP1-QP4 para avaliacao_qualidade/ (material suplementar)."""
import json, os, csv, re
D = os.path.dirname(os.path.abspath(__file__))
OUT = 'C:/Repositorios/Survey_VLMs_GSF_PTMS/avaliacao_qualidade/'
data = json.load(open(os.path.join(D, 'notes606.json'), encoding='utf-8'))
extra = json.load(open(os.path.join(D, 'abs_extra.json'), encoding='utf-8'))

L2 = {'G1': 'Pré-treinamento ou representações VL de propósito geral', 'G2': 'Módulo, entrada ou objetivo de modelo de tarefa específica',
      'G3': 'Grafo de conhecimento externo como fonte de conhecimento', 'G4': 'Grafo como saída', 'G5': 'Apenas dados, pré-processamento, análise ou fora de texto-imagem',
      'G0': 'Uso de grafo não identificado no texto disponível'}
L3 = {'S1': 'Semi-supervisionado em sentido estrito', 'S2': 'Supervisão fraca, ruidosa ou inexata', 'S3': 'Auto-supervisionado registrado como QP3',
      'S4': 'Dados sintéticos ou pseudo-anotações geradas por modelos', 'S5': 'Outros (destilação, UDA, ICL, avaliação com poucos rótulos)', 'S0': 'Não identificável'}
QP4 = {
 'P087': ('A1', 'Seleção para anotação humana sob orçamento', 'Adaptação/treinamento do modelo de recuperação'),
 'P224': ('A1', 'Seleção para anotação humana sob orçamento', 'Adaptação por prompts'),
 'P620': ('A1', 'Seleção para anotação humana sob orçamento', 'Pré-seleção antes do ajuste fino'),
 'P615': ('A2', 'Seleção sem oráculo humano', 'Ajuste fino (amostras sintéticas, RL)'),
 'P621': ('A2', 'Seleção sem oráculo humano', 'Adaptação few-shot (feedback zero-shot de LVLM)'),
 'P233': ('A2', 'Seleção sem oráculo humano', 'Treinamento de alinhamento de VLM médico (mineração de triplas)'),
 'P113': ('A3', 'Estimativa de incerteza sem ciclo de seleção', 'Adaptador pós-hoc sobre modelo congelado'),
 'P508': ('A4', 'Humano no laço', 'Ajuste por instruções'),
 'P510': ('X1', 'Aprendizado ativo fora do escopo de VLMs', 'Níveis de jogos'),
 'P520': ('X1', 'Aprendizado ativo fora do escopo de VLMs', 'Nomeação de cores (BiLSTM)'),
 'P521': ('X1', 'Aprendizado ativo fora do escopo de VLMs', 'Classificação genérica, não multimodal'),
 'P412': ('X2', '"Ativo" em outro sentido', 'Recuperação ativa contra alucinação'),
 'P503': ('X2', '"Ativo" em outro sentido', 'Agente de interpretabilidade'),
 'P590': ('X2', '"Ativo" em outro sentido', 'Retroalimentação do ambiente (agente incorporado)'),
}


def write(name, header, rows):
    with open(OUT + name, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)
    print(name, len(rows))


c2 = json.load(open(os.path.join(D, 'qp2_coding.json')))
write('codificacao_QP2_papel_do_grafo.csv', ['ID', 'Titulo', 'Categorias', 'Codigo', 'Papel do grafo', 'Fonte do texto'],
      [[k, data[k]['title'], data[k]['cats'], g, L2[g], 'nota QP2 (Fase 1)' if re.search(r'QP2\s*-', data[k]['notas'] or '') else 'resumo'] for k, g in sorted(c2.items())])
c3 = json.load(open(os.path.join(D, 'qp3_coding.json')))
write('codificacao_QP3_operacional.csv', ['ID', 'Titulo', 'Categorias', 'Codigo', 'Classe operacional', 'Fonte do texto'],
      [[k, data[k]['title'], data[k]['cats'], g, L3[g], 'nota QP3 (Fase 1)' if re.search(r'QP3\s*-', data[k]['notas'] or '') else 'resumo'] for k, g in sorted(c3.items())])
write('codificacao_QP4.csv', ['ID', 'Titulo', 'Categorias', 'Codigo', 'Tipo', 'Etapa ou contexto'],
      [[k, data[k]['title'], data[k]['cats'], *v] for k, v in sorted(QP4.items())])
assert set(QP4) == {k for k, v in data.items() if 'QP4' in set(re.findall(r'Q[PS]\d', (v['codes'] or '').upper()))}
q1 = json.load(open(os.path.join(D, 'qp1_paradigms.json'), encoding='utf-8'))
cats = ['VQA', 'TEXT-IMAGE', 'IMAGE-TEXT', 'RETRIEVAL', 'GENERATE']
write('codificacao_QP1_paradigmas_por_categoria.csv', ['Paradigma'] + [f'{c} (n={q1["N"][c]})' for c in cats] + ['Artigos unicos (n=606)'],
      [[p] + [q1['hits'][c].get(p, 0) for c in cats] + [n] for p, n in sorted(q1['uniq'].items(), key=lambda x: -x[1])])
