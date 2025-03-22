# Criar um script que solocite ao usuário dois números.
# Em seguida, seu script deve imprimir a soma, subtração, multiplicação, divisão e a exponenciação.

# Solicitando entrada de dados:
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

#print (type(num1)) # Exibir tipo de váriavel
#print (type(num2))
       
# Fazendo os calculos:
soma = num1 + num2    # Soma +
subt = num1 - num2    # Subtração -
mult = num1 * num2    # Multiplicação *
div  = num1 / num2    # Divisão /
expo = num1 ** num2   # Exponenciação **

# Exibindo os resultados no console.
print(f'A Soma dos dois números é {soma}')
print(f'A Subtração é: {subt}')
print(f'A Multiplicação é: {mult}')
print(f'E a Divisão é: {div}')
print(f'Por ultimo e não menos importante Exponenciação: {expo}')

