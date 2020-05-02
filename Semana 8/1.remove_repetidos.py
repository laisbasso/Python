def remove_repetidos(lista):
    lista.sort()
    lista_atualizada = []
    for i in (lista):
        if (lista_atualizada == [] or lista_atualizada[-1] != i):
            lista_atualizada.append(i)
    return lista_atualizada
