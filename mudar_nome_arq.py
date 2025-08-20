import os

os.chdir('C:\\Teste')
print(f'Diretorio atual: {os.getcwd()}')

padrao_nome = input('Qual o padrao de nomes de arquivos a usar (sem a extensáo)?')

# for contador, arq in enumerate(os.listdir()):
#     if os.path.isfile(arq):
#         nome_arq, exten_arq = os.path.splitext(arq)
#         nome_arq = padrao_nome + ' ' + arq
        
#         nome_novo = f'{nome_arq}{exten_arq}'
#         os.rename(arq, nome_novo)
#         print(f'\nArquivos renomeados.')


for contador, arq in enumerate(os.listdir()):
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrao_nome
        
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)
        print(f'\nArquivos renomeados.')