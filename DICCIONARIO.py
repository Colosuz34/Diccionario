meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL': 'Una respuesta a una broma',
            'CREEPY': 'aterrador, siniestro',
            'AGGRO': 'ponerse agresivo/enojado',
            'CHILL': 'Estar relajado',
            'CRUSH': 'Persona que te gusta o que te atrae',
            'MOOD': 'Estado de animo actual'
            }

print('Muy buenos dias y bienvenidos al diccionario de los millenials para los boomers')

for i in range(5):
    palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
                
    if palabra in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[palabra])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print('no se encontro la palabra')
