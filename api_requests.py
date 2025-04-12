import requests
import time
import configuration

def get_alive_characters():

    # Conteo de tiempo de respuesta
    start_time = time.time()
    url_alive = requests.get(configuration.URL_SERVICE + configuration.GET_CHARACTERS_PATH + configuration.ALIVE_PARAMETERS)
    end_time = time.time()
    response_time = end_time - start_time
    assert response_time < 0.5, "Respuesta para personajes vivos tardia"
    #----------------------------------------------------

    # Conteo de número de personajes vivos
    alive_data = url_alive.json()
    for character in alive_data["results"]:
        pass
    total_characters_alive = len(alive_data["results"])
    # ---------------------------------------------------

    # Validación de código de respuesta
    assert url_alive.status_code == 200, "Código de respuesta para personajes vivos incorrecto"
    # ---------------------------------------------------

    # Muestra de código de respuesta y cantidad de personajes vivos
    print("\nCódigo de respuesta para personajes vivos:", url_alive.status_code, "\nNúmero de personajes vivos:",total_characters_alive)
    # ---------------------------------------------------

    # Validación de datos
    for character in alive_data["results"]:
        assert isinstance(character["id"], int), "El ID no es un entero"
        assert isinstance(character["name"], str), "El nombre no es un string"
        assert isinstance(character["status"], str), "El estado no es un string"
        assert isinstance(character["species"], str), "El tipo species no es un string"
        assert isinstance(character["origin"], dict), "Episodios no es un diccionario"
        assert isinstance(character["location"], dict), "La ubicación no es un diccionario"
        assert isinstance(character["image"], str), "La imagen no es un string"
        assert isinstance(character["episode"], list), "El episodio no es una lista"
        assert isinstance(character["url"], str), "La url no es un string"
        assert isinstance(character["created"], str), "El estado creado no es un string"

get_alive_characters()


def get_dead_characters():

    # Conteo de tiempo de respuesta
    start_time = time.time()
    url_dead = requests.get(configuration.URL_SERVICE + configuration.GET_CHARACTERS_PATH + configuration.DEAD_PARAMETERS)
    end_time = time.time()
    response_time = end_time - start_time
    assert response_time < 0.5, "Respuesta para personajes muertos tardia"
    #----------------------------------------------------

    # Conteo de número de personajes muertos
    dead_data = url_dead.json()
    for character in dead_data["results"]:
        pass
    total_characters_dead = len(dead_data["results"])
    # ---------------------------------------------------

    # Validación de código de respuesta
    assert url_dead.status_code == 200, "Código de respuesta para personajes muertos incorrecto"
    # ---------------------------------------------------
    
    # Muestra de código de respuesta y cantidad de personajes muertos
    print("\nCódigo de respuesta para personajes muertos:", url_dead.status_code, "\nNúmero de personajes muertos:",total_characters_dead)
    # ---------------------------------------------------

    # Validación de datos
    for character in dead_data["results"]:
        assert isinstance(character["id"], int), "El ID no es un entero"
        assert isinstance(character["name"], str), "El nombre no es un string"
        assert isinstance(character["status"], str), "El estado no es un string"
        assert isinstance(character["species"], str), "El tipo especies no es un string"
        assert isinstance(character["origin"], dict), "Episodios no es un diccionario"
        assert isinstance(character["location"], dict), "La ubicación no es un diccionario"
        assert isinstance(character["image"], str), "La imagen no es un string"
        assert isinstance(character["episode"], list), "El episodio no es una lista"
        assert isinstance(character["url"], str), "La url no es un string"
        assert isinstance(character["created"], str), "El estado creado no es un string"

get_dead_characters()


