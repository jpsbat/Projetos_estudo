# Cálculo de média da Facens

AC1_str = input("\nDigite sua nota da AC1. Use . como separação \n")
AC2_str = input("\nDigite sua nota da AC2. Use . como separação \n")
AG_str = input("\nDigite sua nota da AG. Use . como separação \n")
AF_str = input("\nDigite sua nota da AF. Use . como separação \n")

AC1 = float(AC1_str)
AC2 = float(AC2_str)
AG = float(AG_str)
AF = float(AF_str)

media_str = abs((0.15 * AC1) + (0.3 * AC2) + (0.1 * AG) + (0.45 * AF))
media = float(media_str)

falta_str = abs(5 - media)
falta = float(falta_str)

print("\nSua média: {:.2f}\n".format(media))

if (media <= 5):
    print("Falta {:.2f} pra passar\n".format(falta))

notas = [AC1, AC2, AG, AF]
menor_nota = float(min(notas))
nota_substitutiva = (5.0 - (media - menor_nota)) / 0.45

print("A menor nota é {:.2f}".format(menor_nota))
print("Precisa tirar {:.2f} na sub para passar".format(nota_substitutiva))
