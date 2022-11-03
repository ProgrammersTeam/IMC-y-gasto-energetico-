def imc(total):
    if (total < 18.4):
        print("Su IMC esta en bajo peso", + total)
    elif (18.5 <= total <= 24.9):
        print("Su IMC esta en normal", + total)
    elif (25 <= total <= 29.9):
        print("su IMC esta en sobrepeso", total)
    elif (30 <= total <= 34.9):
        print("su IMC esta en Obesidad I", total)
    elif (35 <= total <= 39.9):
        print("su IMC esta en Obesidad II", total)
    else:
        print("su IMC esta en Obesidad III", total)
    return total

def gasto_calorico(genero, acm, edad, peso):
    if (genero == "femenino"):
        gc = 655 + (9.6 * peso) + (5 * acm) - (4.7 * edad)
    else:
        gc = 66 + (13.7 * peso) + (5 * acm) - (6.5 * edad)
    return gc

try:
  print("Este programa es para a medir tu indice de masa coorporal actual (IMC)")
  altura = float(input("Tu altura (metros) actual es: "))
  peso = float(input("Tu peso corporal (kilogramos) es: "))
  edad = float(input("Ingrese su edad actual: "))
  total = peso / (altura * altura)
  imct = imc(total)

  #Gasto_Calorico
  print("En esta parte se calculará el gasto calórico que tiene, si desea continuar coloque su género, de lo contrario un no")
  genero = input("Ingrese su género (femenino, masculino): ")
  if (genero == "masculino" or genero == "femenino"):
    acm = altura * 100
    gc = gasto_calorico(genero, acm, edad, peso)
    print("Su gasto calórico es: ", gc)
except:
  print("Error")