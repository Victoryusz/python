###### Função NOME
def solicitar_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if not nome.replace(" ", "").isalpha():
            print("Insira um nome válido")
        else:
            return nome.title()

##### Função CPF ######
def solicitar_cpf(mensagem):
    while True:
        num = input(mensagem).strip().replace(".", "").replace("-", "").replace(" ", "")
        if not (num.isdigit() and len(num) == 11):
            print("Insira um CPF válido (11 dígitos).")
            continue
        return f"{num[:3]}.{num[3:6]}.{num[6:9]}-{num[9:11]}"
