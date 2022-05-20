tarefa = {"titulo": "Fazer nada", "descrição": "nada mesmo"}
# print(tarefa['titulo'])

lista = [tarefa, {"titulo": "Daniel", "descrição": "desenvolvedor"}]
print(lista)

lista.append({"titulo": "Batata"})

for tarefa in lista:
    print(tarefa)


def soma(x, y):
    return x + y


print(soma(10, 2))
