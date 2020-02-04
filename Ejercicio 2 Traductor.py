
lista = ['oscreem', 'ueq', 'la', 'óncodificaci', 'ñaense', 'eshabilidad', 'eld', 'losig', '21', 'osusam', 'la', 
         'óncodificaci', 'moco', 'nau', 'taherramien', 'rapa', 'armostr', 'moco'] #Listsa original
def traductor(arg):
    """ La funcion que va a traducir los codigos """
    letra = list(arg) #Se hace un array de las letras de la palabra tomada
    try:
        for i in range (0,2): #El loop va a mandar la primera letra al fondo y desplazar todas las demas a la izq
            letra.append( letra[0] )
            letra.pop(0)
        resultado = ''.join(letra) #Cuando se termina el loop se une de nuevo las letras para retornar la palabra traducida    
        return resultado

    except len(letra) <2: #si son 2 letras el loop no afecta, si es 1 letra se retorna identicamente
        return arg        

       

for i in range(0, len(lista) ): #se hace el loop para traducir todas las palabras de la lista, se une para tener la oracion y se imprime
    lista [i] = traductor( lista[i] )
oracion = ' '.join(lista)
print(oracion)


        




