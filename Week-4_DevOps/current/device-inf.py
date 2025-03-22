import shutil      # Importa a biblioteca shutil.

total, used, free = shutil.disk_usage('/')             # Armazena o uso do disco na variável total, used e free.
print('Total: ',total,'Used: ',used,'Free: ',free)     # Exibe 0 uso do disco.