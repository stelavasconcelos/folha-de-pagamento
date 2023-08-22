salarioB = float(input("Digite o salário: "))
vale =  input("Descontar o Vale Transporte? ")
if salarioB <1320.01:
    inss = salarioB*0.075
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)

elif salarioB > 1320.00 and salarioB <2571.30:
    inss = (salarioB - 1320)*0.09 + 99
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
  
elif salarioB > 2571.29 and salarioB < 3856.95:
    inss = (salarioB - 2571.29) * 0.12 + 99 + 112.62
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    
elif salarioB > 3856.94 and salarioB < 7507.50:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    
elif salarioB >7507.49:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    
else:
     print("Ops! Algo deu errado contacte seu programador!")
if vale == "s" or vale == "S":
 valVale = (salarioB-inss)*0.06
 print (f"Desconto do vale transporte é de R${valVale}")
salarioL = (salarioB-inss) - valVale
print ("Seu salário liquído é de: R$", salarioL)
