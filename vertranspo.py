import os
import xml.etree.ElementTree as ET
import shutil

# Função para procurar a string em um arquivo XML
def procurar_em_xml(arquivo, alvo):
    try:
        tree = ET.parse(arquivo)  # Analisa o arquivo XML
        root = tree.getroot()  # Obtém o elemento raiz do XML

        # Itera sobre todas as linhas no XML
        for elem in root.iter():
            if elem.text is not None and alvo in elem.text:
                return True  # Encontrou a linha
    except ET.ParseError:
        pass  # Ignora arquivos XML inválidos

    return False  # Não encontrou a linha

# Diretório de origem contendo os arquivos XML
diretorio_origem = r'C:\Users\User\Desktop\XML\arquivos' # Alterar o User

# Diretório de destino para os arquivos que contêm a string
diretorio_destino = r'C:\Users\User\Desktop\XML\resultado'  # Alterar o User

# Diretório de destino para os arquivos que **não** contêm a string
diretorio_destino_nao_encontrados = r'C:\Users\User\Desktop\XML\outros'  # Alterar o User

# String que você deseja procurar nos arquivos XML
alvo = 'EMPRESA DE LOGISTICA LTDA'

# Lista para armazenar os arquivos que contêm a string
arquivos_com_alvo = []

# Lista para armazenar os arquivos que **não** contêm a string
arquivos_sem_alvo = []

# Itera sobre todos os arquivos na pasta de origem
for arquivo in os.listdir(diretorio_origem):
    caminho_arquivo_origem = os.path.join(diretorio_origem, arquivo)
    if procurar_em_xml(caminho_arquivo_origem, alvo):
        arquivos_com_alvo.append(arquivo)
        caminho_arquivo_destino = os.path.join(diretorio_destino, arquivo)
    else:
        arquivos_sem_alvo.append(arquivo)
        caminho_arquivo_destino = os.path.join(diretorio_destino_nao_encontrados, arquivo)
    
    # Move o arquivo para o diretório de destino correspondente
    shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)

# Exibe os arquivos que foram movidos para os diretórios de destino
if arquivos_com_alvo:
    print(f"{len(arquivos_com_alvo)} arquivos contêm '{alvo}' e foram movidos para o diretório de destino.")
if arquivos_sem_alvo:
    print(f"{len(arquivos_sem_alvo)} arquivos **não** contêm '{alvo}' e foram movidos para o diretório de destino de não encontrados.")
