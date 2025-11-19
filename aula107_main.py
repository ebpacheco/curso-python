import importlib
import aula107

print(aula107.variavel)

for i in range(10):
    importlib.reload(aula107)
print('Fim')