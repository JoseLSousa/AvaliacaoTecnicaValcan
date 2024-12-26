import os
import shutil
from datetime import datetime, timedelta

# Caminho para o diretório onde os arquivos para backup estão
directory = './Problema 1/home/valcann/backupsForm/'

# Verifica se o caminho para o diretório está acessível
if not os.path.exists(directory):
    print('Caminho do diretório inválido.')
    exit()  # Se o diretório não existir, encerrar o programa

# Obtém a data e hora de hoje
today = datetime.today()

# Lista os arquivos no diretório
files = os.listdir(directory)

destinationPath = './Problema 1/home/valcann/backupsTo'

for item in files:
    # Caminho completo do arquivo
    filePath = os.path.join(directory, item)
    
    # Verifica se é um arquivo (pode ser um diretório também)
    if os.path.isfile(filePath):
        fileSize = os.path.getsize(filePath)
        createdAt = datetime.fromtimestamp(os.path.getctime(filePath))  # Data de criação
        lastModification = datetime.fromtimestamp(os.path.getmtime(filePath))  # Última modificação

        # Comparar a data de criação com a data de hoje
        if today - createdAt >= timedelta(days=3):
            # Verifica se o arquivo existe antes de excluir
            if os.path.exists(filePath):
                os.remove(filePath)
                print(f"Arquivo {filePath} excluído")
            else:
                print(f"Arquivo {filePath} não existe")
        else:
            # Verifica se o destino existe e se não cria a pasta antes de copiar 
            if os.path.exists(destinationPath):
                shutil.copy(filePath, destinationPath)
            else:
                os.mkdir(destinationPath)
                shutil.copy(filePath, destinationPath)
                
        # Escreve as informações no arquivo de log
        with open('./Problema 1/home/valcann/BackupsForm.log', 'a') as file:
            file.write(f"Nome do arquivo: {item} Tamanho: {fileSize}, Criado em: {createdAt.strftime('%d/%m/%Y, %H:%M:%S')}, Ultima modificacao: {lastModification.strftime('%d/%m/%Y, %H:%M:%S')}\n")
        
print("Operação concluída com sucesso.")
