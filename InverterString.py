#Questao 5 Código feito em Python

def inverter_string(s):
    invertida = ''
    for char in s:
        invertida = char + invertida
    return invertida

# String a ser invertida
string = "Exemplo"
print(f"String invertida: {inverter_string(string)}")
