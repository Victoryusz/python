from funcoes import solicitar_nome, solicitar_cpf

nome = solicitar_nome("Digite seu nome: ")
cpf = solicitar_cpf("Digite seu cpf:")

print("=== BEM VINDO ===")
print(f"Seu nome: {nome}\nSeu CPF: {cpf}")
