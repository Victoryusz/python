print("=== Seja bem vindo ao caixa. ===")

conseguiu_numero = False
conseguiu_gorjeta = False

# Verificar se digitou número válido antes de converter
while not conseguiu_numero:
    try:
        numero = float(input("⭐ Valor da conta: "))
        if numero < 0:
            print("Insira um número válido.❌")
        else:
            conseguiu_numero = True
            print(f"Valor da conta: ${numero}✔️")
    except:
        print("VALOR INVÁLIDO.❌")

# Verificar se digitou número válido antes de converter
while not conseguiu_gorjeta:
    try:
        gorjeta = float(input(f"Quanto % de gorjeta? "))
        if gorjeta < 0:
            print("Insira um número válido.❌")
        else:
            conseguiu_gorjeta = True
            print(f"Valor da Gorjeta: ${gorjeta}✔️")
    except:
        print("GORJETA INVÁLIDA.❌")

# Calcular e mostre o valor da gorjeta e o total a pagar
resultado = (gorjeta * numero) / 100
valor_final = resultado + numero

print(f"=== {gorjeta}% de ${numero} é ${resultado}, TOTAL A PAGAR = ${valor_final} ===")
