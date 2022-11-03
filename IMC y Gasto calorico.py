#TEA
def imc(Total):
    if Total<18.4:
        print("Su IMC esta en bajo peso", +Total)
    elif 18.5 <= Total <= 24.9:
        print("Su IMC esta en normal", +Total)
    elif 25<= Total <=29.9:
        print("su IMC esta en sobrepeso", Total)
    elif 30<= Total <=34.9:
        print("su IMC esta en Obesidad I", Total)    
    elif 35<= Total <=39.9:
        print("su IMC esta en Obesidad II", Total)
    else:
        print("su IMC esta en Obesidad III", Total)
    return Total

def gasto_calorico(genero, acm, Edad, Peso):
    if (genero == "femenino"):
        print("Aqui")
        fem = float(655)+float(9.6*Peso)+float(5*acm)-(4.7*Edad)
        print("su gasto calorico es: ", fem)
    else:
        mas = float(66)+float(13.7*Peso)+float(5*acm)-(6.5*Edad)
        print("su gasto calorico es: ", mas)
    return genero


print("Este programa es para a medir tu indice de masa coorporal actual (IMC)")
Altura = input("Tu altura (metros) actual es: ")
Peso = input("Tu peso corporal (Kilogramos) es: ")
Edad = input("ingrese su edad actual")
Total = float(Peso)/(float(Altura)*float(Altura))
imct = imc(Total)
#Gasto_Calorico
print("En esta parte se calculara el gasto calorico que usted tiene, si desea continuar coloque su sexo, sino, unicamente un no")
Genero = input("ingrese su genero(femenino, masculino): ")
Alturacm = Altura*100
gc = gasto_calorico(Genero, Alturacm, Edad, Peso)
print(gc)

