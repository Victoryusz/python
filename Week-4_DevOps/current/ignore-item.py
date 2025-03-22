# Criar um script que copia um arquivo de um diretório para outro, mas que ignora um arquivo específico.

import shutil                                                    # importa a biblioteca shutil

def ignore_specific_files(directory, files):                     # função que recebe um diretório e uma lista de arquivos
    print(f"Verificando pasta: {directory}, arquivos: {files}")  # imprime a pasta e os arquivos
    return [f for f in files if f == 'logs.txt']                 # retorna o arquivo 'logs.txt' se ele existir

shutil.copytree('source_dir', dst='dev_dir', ignore=ignore_specific_files)  # copia o diretório 'source_dir' para 'dev_dir' ignorando o arquivo 'logs.txt'

