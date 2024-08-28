notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB)/2

#verifivação
if mediafinal >=7.0:
     print("Media %.1f - Aprovado "% mediafinal)
else:
     print("A media %.1f - Reprovado "% mediafinal)