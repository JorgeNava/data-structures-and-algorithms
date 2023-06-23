def contarPalabras(listaDePalabras):
    contador = {}

    for palabra in listaDePalabras:
        palabraInversa = palabra[::-1]
        
        if(palabraInversa in contador):
            contador[palabraInversa] += 1
            if(palabra not in contador):
                contador[palabra] = contador[palabraInversa]
        if(palabra not in contador):
          contador[palabra] = 1
    return contador

listaDePalabras = ['Jorge', 'Ana', 'egroJ', 'anA', 'Carlos']
respuesta = contarPalabras(listaDePalabras)
print(respuesta)
