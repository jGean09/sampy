import sympy as sp

# Variáveis simbólicas
x = sp.Symbol('x')
t = sp.Symbol('t')
p = sp.Symbol('p')
h = sp.Symbol('h')

# Funções e os pontos de cálculo do limite
f_a = (x**3 - 5*x**2 + 8*x - 4) / (x**4 - 5*x - 6)  # a) Lim x → 2
p_a = 2

f_b = sp.tan(t - p) / (t**2 - p**2)  # b) Lim t → p
p_b = p

f_c = (sp.sin(x**2 + 1/x) - sp.sin(1/x)) / x  # c) Lim x → 0
p_c = 0

f_d = sp.sin(sp.pi * x) / (x - 1)  # d) Lim x → 1
p_d = 1

f_e = (sp.sin(x + h) - sp.sin(x)) / h  # e) Lim h → 0
p_e = 0

f_f = (sp.sec(x + h) - sp.sec(x)) / h  # f) Lim h → 0
p_f = 0

f_g = ((x + 2) / (x + 1))**x  # g) Lim x → ∞
p_g = sp.oo

f_h = (x**2 - 4) / (x**2 - 4*x + 4)  # h) Lim x → 2
p_h = 0

f_i = (1 + x)**(2/x)  # i) Lim x → 0
p_i = 0

f_j = sp.sin(t) / (t - sp.pi)  # j) Lim t → π
p_j = sp.pi

# Calculando e exibindo os limites
print("a) Lim x → 2 =", sp.limit(f_a, x, p_a))
print("b) Lim t → p =", sp.limit(f_b, t, p_b))
print("c) Lim x → 0 =", sp.limit(f_c, x, p_c))
print("d) Lim x → 1 =", sp.limit(f_d, x, p_d))
print("e) Lim h → 0 =", sp.limit(f_e, h, p_e))
print("f) Lim h → 0 =", sp.limit(f_f, h, p_f))
print("g) Lim x → ∞ =", sp.limit(f_g, x, p_g))
print("h) Lim x → 2 =", sp.limit(f_h, x, p_h))
print("i) Lim x → 0 =", sp.limit(f_i, x, p_i))
print("j) Lim t → π =", sp.limit(f_j, t, p_j))
