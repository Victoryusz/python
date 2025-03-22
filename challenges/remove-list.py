# Primeiro remova a "Manga" da lista usando o método remove(). Depois remova o último item da lista usando o comando del. 
# Por fim, imprima a lista modificada na tela.

frutas = ['Maçã', 'Morango', 'Manga', 'Uva', "Abacaxi"]  # Lista fonte.

print(f'A origem é: {frutas}')                # Exibição da fonte original.

frutas.remove('Manga')                        # Remoção de item específico, com o método remove().

print(f'Remoção Manga: {frutas}')             # Exibição da lista com a remoção.

del frutas[-1]                                # Remoção de item em posição específica, usando comando del.

print(f'Remoção do último item: {frutas}')    # Exibição da lista sem a Manga e sem o Abacaxi