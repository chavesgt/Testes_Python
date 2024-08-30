#Questao 3 Código feito em Python

import json

# Exemplo de dados em formato JSON
faturamento_json = '''
{
    "faturamento_diario": [0, 1500, 2000, 0, 3000, 1000, 0, 2000, 0, 2500]
}
'''

dados = json.loads(faturamento_json)
faturamento = [valor for valor in dados['faturamento_diario'] if valor > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")
