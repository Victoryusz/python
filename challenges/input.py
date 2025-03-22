# Criar um script que pergunte o nome e a idade do usuário, usando a função input()
# Depois Exibir " Olá, [nome]! Você tem [idade] anos."

# Váriaveis
first_name = input('Please write your name: ')   # String.
age = int(input('Now write your age: '))         # Integer.


print(type(first_name))                           # Exibição do type
print(type(age))                                  # Exibição do type

print('Hi,', first_name,'! You are', age, 'old.')        # Exibição de informações coletadas do usuário.
print(f'Hi, {first_name}! You are {age} old.')           # Exibição de informações coletadas do usuário. f string
print('Hi, {}! You are {} old.'.format(first_name, age)) # Exbição escrita de forma diferente.