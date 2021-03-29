import os
from utils import formata_tamanho

print('INFO ARQUIVO')
print('-'*29)
caminho_procura = input('Digite um caminho do arquivo: ')
termo_procura = input('Digite o nome do arquivo: ')

conta = 0

for root, dirs, files in os.walk(caminho_procura):
    for file in files:
        if termo_procura in file:
            try:
                conta += 1
                file_abspath = os.path.join(root, file)
                file_name, file_ext = os.path.splitext(file)
                file_size = os.path.getsize(file_abspath)
                print()
                print('Encontrei o arquivo: ', file)
                print('Caminho: ', file_abspath)
                print('Nome: ', file_name)
                print('Extensão: ', file_ext)
                print('Tamanho: ', file_size)
                print('Tamanho formatado: ', formata_tamanho(file_size))
            except PermissionError as e:
                print('Sem premissão neste aruqivo. ')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido: ', e)

print()
print(f'{conta} arquivo(s) encontrado(s)')