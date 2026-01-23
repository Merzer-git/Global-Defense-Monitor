"""
Módulo que contiene el diccionario de códigos ISO-3 de países del mundo.
Las claves son los nombres de países en inglés.
Incluye manejo de países históricos que ya no existen en la lista ISO-3 actual.
"""

import pycountry
import pandas as pd

# Mapeo manual de países históricos o nombres alternativos que no están en pycountry
PAISES_HISTORICOS = {
    'Soviet Union': 'SUN',
    'USSR': 'SUN',
    'Czechoslovakia': 'CSK',
    'Yugoslavia': 'YUG',
    'East Germany': 'DDR',
    'German Democratic Republic': 'DDR',
    'Serbia and Montenegro': 'SCG',
    'Netherlands Antilles': 'ANT',
    'Eritrea and Ethiopia': 'ETH',  # O podría ser ERI
    'Taiwan': 'TWN',
    'Palestine': 'PSE',
}


def generar_diccionario_iso3(df=None):
    diccionario_iso3 = {}
    
    # Primero, agregar todos los países de pycountry
    for country in pycountry.countries:
        diccionario_iso3[country.name] = country.alpha_3
    
    # Luego, agregar los países históricos/especiales
    diccionario_iso3.update(PAISES_HISTORICOS)
    
    # Si se proporciona un dataframe, filtrar solo los países del dataframe
    if df is not None:
        paises_df = set(df['Country'].unique())
        diccionario_iso3 = {k: v for k, v in diccionario_iso3.items() if k in paises_df}
    
    return diccionario_iso3


def cargar_iso3_desde_df(df):
    """
    Carga el diccionario ISO-3 basado en los países presentes en el dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe con columna 'Country'
        
    Returns:
        dict: Diccionario con códigos ISO-3 para los países del dataframe
    """
    return generar_diccionario_iso3(df)


# Diccionario pre-generado con códigos ISO-3 de todos los países
PAISES_ISO3_TODOS = generar_diccionario_iso3()


def obtener_iso3(nombre_pais, paises_iso3=None):
    """
    Obtiene el código ISO-3 de un país dado su nombre en inglés.
    
    Args:
        nombre_pais (str): Nombre del país en inglés
        paises_iso3 (dict, optional): Diccionario de países ISO-3. 
                                      Si no se proporciona, usa PAISES_ISO3_TODOS
        
    Returns:
        str: Código ISO-3 del país, o None si no se encuentra
    """
    if paises_iso3 is None:
        paises_iso3 = PAISES_ISO3_TODOS
    
    return paises_iso3.get(nombre_pais)


def obtener_nombre_pais(codigo_iso3, paises_iso3=None):
    """
    Obtiene el nombre del país dado su código ISO-3.
    
    Args:
        codigo_iso3 (str): Código ISO-3 del país
        paises_iso3 (dict, optional): Diccionario de países ISO-3.
                                      Si no se proporciona, usa PAISES_ISO3_TODOS
        
    Returns:
        str: Nombre del país en inglés, o None si no se encuentra
    """
    if paises_iso3 is None:
        paises_iso3 = PAISES_ISO3_TODOS
    
    for nombre, codigo in paises_iso3.items():
        if codigo == codigo_iso3.upper():
            return nombre
    return None


def agregar_iso3_a_df(df, columna_origen='Country', columna_destino='ISO3'):
    """
    Agrega una columna con códigos ISO-3 a un dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe con columna de país
        columna_origen (str): Nombre de la columna con nombres de países
        columna_destino (str): Nombre de la nueva columna con códigos ISO-3
        
    Returns:
        pd.DataFrame: Dataframe con la nueva columna ISO-3
    """
    paises_iso3_df = cargar_iso3_desde_df(df)
    df = df.copy()  # Evitar SettingWithCopyWarning
    df[columna_destino] = df[columna_origen].map(paises_iso3_df)
    return df


# if __name__ == '__main__':
#     # Ejemplo de uso
#     print(f"Total de países en la lista ISO-3: {len(PAISES_ISO3_TODOS)}")
#     print("\nPrimeros 10 países:")
#     for nombre, iso3 in list(PAISES_ISO3_TODOS.items())[:10]:
#         print(f"  {nombre}: {iso3}")
    
#     # Buscar un país específico
#     print(f"\nEjemplos de búsqueda:")
#     print(f"  Spain: {obtener_iso3('Spain')}")
#     print(f"  Argentina: {obtener_iso3('Argentina')}")
#     print(f"  China: {obtener_iso3('China')}")
#     print(f"  Soviet Union: {obtener_iso3('Soviet Union')}")
    
#     # Ejemplo con dataframe
#     print(f"\n--- Ejemplo con dataframe ---")
#     df = pd.read_parquet("data/datos_militares_final.parquet")
#     print(f"Países únicos en el dataframe: {df['Country'].nunique()}")
    
#     paises_df_iso3 = cargar_iso3_desde_df(df)
#     print(f"Países mapeados a ISO-3: {len(paises_df_iso3)}")
    
#     # Mostrar algunos ejemplos
#     print("\nEjemplos de mapeo:")
#     for pais in list(df['Country'].unique())[:5]:
#         iso3 = obtener_iso3(pais, paises_df_iso3)
#         print(f"  {pais}: {iso3}")
