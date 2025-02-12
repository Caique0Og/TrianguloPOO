# 2. Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
f = float(input("Quantos graus farenrraits ta fazendo aí patrão? "))

def c_pa_f (f):
    c = (f - 32) * (5/9)
    print(f"Está fazendo aproximadamente {c:.2f} graus céuços ")

c_pa_f (f)