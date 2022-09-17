#TEA
print("Este programa es para a medir tu indice de masa coorporal actual (IMC)")
Altura = input("Tu altura (metros) actual es: ")
Peso = input("Tu peso corporal (Kilogramos) es: ")
Total = float(Peso)/(float(Altura)*float(Altura))
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
