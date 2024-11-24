import os

# Obtém a lista de arquivos .xlsx no diretório atual
xlsx_files = [f for f in os.listdir() if f.endswith('.xlsx')]

# Verifica se há arquivos .xlsx no diretório
if xlsx_files:
    print("Arquivos encontrados:")
    for i, file in enumerate(xlsx_files, 1):
        print(f"{i}. {file}")

    # Pergunta ao usuário qual arquivo escolher
    try:
        choice = int(input(f"Escolha o número do arquivo que você deseja selecionar (1-{len(xlsx_files)}): "))
        if 1 <= choice <= len(xlsx_files):
            chosen = xlsx_files[choice - 1]
            print(f"Você escolheu o arquivo: {chosen}")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida, por favor insira um número.")
else:
    print("Nenhum arquivo .xlsx encontrado no diretório.")
