
salarioB = float(input("Digite o salário: "))
vale =  input("Descontar o Vale Transporte? ")
if salarioB <1302.00:
if salarioB <1320.01:
    inss = salarioB*0.075
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <2571.29:
    inss = salarioB*0.09
elif salarioB > 1320.00 and salarioB <2571.30:
    inss = (salarioB - 1320)*0.09 + 99
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <3856.94:
    inss = salarioB*0.12
elif salarioB > 2571.29 and salarioB < 3856.95:
    inss = (salarioB - 2571.29) * 0.12 + 99 + 112.62
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <7507.49:
    inss = salarioB*0.14
elif salarioB > 3856.94 and salarioB < 7507.50:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB >7507.50:
    inss = salarioB-876.95
elif salarioB >7507.49:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
else:
    print("Sem comentários!")
#print(salarioB, "  ", salarioL)
    print("Ops! Algo deu errado contacte seu programador!")
if vale == "s" or vale == "S":
    valVale = salarioL*0.06
    valVale = (salarioB-inss)*0.06
    print (f"Desconto do vale transporte é de R${valVale}")
    salarioL = salarioB - valVale
    salarioL = (salarioB-inss) - valVale
    print ("Seu salário liquído é de: R$", salarioL)