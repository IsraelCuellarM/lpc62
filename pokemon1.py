import requests

#Pruba de hacer cambios al archivo subido desde la carpeta clonada en windows.
#Nombre: Israel Cuéllar Méndez.
#Matricula: 2077688.

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    
    response = requests.get(url)
    if response.status_code == 200 :
        payload = response.json()
        results = payload.get('results',[])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
