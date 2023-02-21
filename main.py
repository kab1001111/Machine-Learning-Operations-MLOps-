
#Instalamos e importamos la librerias Fastapi y Pandas .
#Instalamos  la libreria uvicorn para usar el servidor.

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd




app = FastAPI(title='Proyecto Streaming plataforms - FastAPI',
            version="0.0.1",
            contact={
            "name": "Bernardo Mantilla",
            "url": "https://github.com/kab1001111",
            "email": "nzberman@gmail.com",},
            description = "En esta Api pueden realizar distintas consultas con respecto a las plataformas Amazon, Disney, Hulu y netflix."
            )


#http://127.0.0.1:8000

# Consulta 3: Cantidad de películas por plataforma con filtro de PLATAFORMA.
@app.get("/get_count_platform/{platform}")


#Consulta 4: Actor que mas se repite por plataforma y ano.
@app.get("/get_actor/{platform}/{year}")


# Consulta 1: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
@app.get("/get_max_duration/{year}/{plataform}/{duration_type}")



# Consulta 2: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
@app.get("/get_score_count/{plataform}/{scored}/{year}")
def get_score_count(platform: str, scored: float, year: int):
    df =pd.read_csv('plaforms_final.csv')

    platform_dict = {}
    for plat, combos in {'netflix': ['n', 'ne', 'net', 'netf', 'netfl', 'netfli', 'netflix'],
                            'disney': ['d', 'di', 'dis', 'disn', 'disne', 'disney'],
                            'hulu': ['h', 'hu', 'hul', 'hulu'],
                            'amazon': ['a', 'am', 'ama', 'amaz', 'amazo', 'amazon']}.items():
        for combo in combos:
            platform_dict[combo] = plat

    # Buscar la plataforma correspondiente en el diccionario
    platform_full = platform_dict.get(platform, platform)

    # Cargar el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv()

