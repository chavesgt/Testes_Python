#Código da Questão 2 Feito em Python

def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

# Número a ser verificado
numero = 21

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")