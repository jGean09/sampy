import sympy as sp

# Definindo a variável simbólica
x = sp.Symbol('x')

# Definindo a função
y = (x**3 - x**2 - 1) / (x - 1)

# Calculando o limite
limite = sp.limit(y, x, 1)

# Corrigindo a impressão
print(f"O limite da função é {limite}")
