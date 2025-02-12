# 3. Faça um Programa que pergunte quanto você ganha por hora e o número
# de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês, sabendo-se que são descontados 11% para o Imposto de
# Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
# dê:

# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

fazMeRir = float(input("Fala quanto tu ganha por time, patrão: "))

def perdeuOtario(fazMeRir):

    SalarioBruto = fazMeRir * (8*20)
    rouboGoverno = (SalarioBruto * 0.011)
    INSS = (SalarioBruto * 0.08)
    VAGABUNDOS = (SalarioBruto * 0.05)
    resto = SalarioBruto - INSS - VAGABUNDOS - rouboGoverno
    print(f"O que te restou pra parar as pensões: {resto:.3f} \n Roubado pelo governo: {rouboGoverno:.3f} \n Roubado pelo INSS: {INSS:.3f} \n Roubado pelos VAGABUNDOS do sindicato: {VAGABUNDOS:.3f}")

perdeuOtario(fazMeRir)