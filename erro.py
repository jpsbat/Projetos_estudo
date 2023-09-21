# Cálculo de erro

medido = float(input("\nDigite o valor medido. Use . como separação \n"))
lido = float(input("\nDigite o valor lido. Use . como separação \n"))

erro = float(abs((lido - medido)/lido) * 100)

print("\nErro: {}%\n".format(erro))