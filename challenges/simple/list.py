# Criar uma lista chamada Frutas que contenha os seguintes itens: maçã, banana, manga e uva.

# Lista com itens armazenados

frutas = ['Maçã', 'Banana', 'Manga', 'Uva']  # Lista: Serão armazenados dentro da váriavel "frutas" {index: começa na posição 0}

# Entendendo a localização das váriaveis. 
# Da esquerda para a direita (0,1,2,3) e da Direita para a esquerda (-1,-2,-3)

#print(f'A primeira fruta é: {frutas[0]}') # Exibição index [0]
#print(f'A última fruta é: {frutas[-1]}')  # Exibição index [-1]

# Desafio: Alterar o segundo elemento da lista, depois disso adicionar outra fruta ao final da lista.

#frutas[1:3] = ['Abacaxi', 'Abacate'] # Do 1 ao 3 , mas não incluindo ele no caso 1,2 apenas.
#frutas.insert(2, 'Abacate')

frutas[1] = 'Morango'       # Alterando a váriavel do local [1].
frutas.append('Abacaxi')    # Função append, insere sempre no final.

print(frutas) 