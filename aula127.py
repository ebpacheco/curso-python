# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:

caminho_arquivo = 'aula126.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3 \n', 'Linha 4\n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())

    print('#' * 10)
    arquivo.seek(0,0)
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print()

    print('#' * 10)
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())
    print()

print('#' * 10)


with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())