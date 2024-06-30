import os
import glob

def listar_arquivos_xlsx():
    # Obtém o diretório atual
    diretorio_atual = os.getcwd()
    
    # Lista todos os arquivos .xlsx no diretório atual
    arquivos_xlsx = glob.glob(os.path.join(diretorio_atual, '*.xlsx'))
    
    return arquivos_xlsx

# Listar arquivos .xlsx no diretório atual
arquivos_xlsx = listar_arquivos_xlsx()

# Verifica se encontrou arquivos
if not arquivos_xlsx:
    print("Nenhum arquivo .xlsx encontrado no diretório atual.")
else:
    # Exibir os arquivos encontrados
    print("Arquivos .xlsx encontrados no diretório atual:")
    for idx, arquivo in enumerate(arquivos_xlsx, start=1):
        print(f"{idx}. {os.path.basename(arquivo)}")

    # Permitir que o usuário escolha um arquivo
    escolha = int(input("Escolha o número do arquivo que deseja usar: ")) - 1
    arquivo_escolhido = arquivos_xlsx[escolha]

    print(f"Você escolheu: {os.path.basename(arquivo_escolhido)}")
