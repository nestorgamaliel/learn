from funciones import (
    obtener_archivos_json, leer_json, extraer_datos_factura, extraer_detalles_factura,
    conectar_postgresql, guardar_factura, guardar_detalles
)
import pandas as pd


# Configuración de la base de datos
CARPETA_JSON = r"C:\dte"
USUARIO = "lender"
PASSWORD = "lender1$"
HOST = "localhost"
PUERTO = "5432"
DB = "Lender"


def main():
    print("Obteniendo archivos JSON...")
    archivos = obtener_archivos_json(CARPETA_JSON)
    
    if not archivos:
        print("No se encontraron archivos JSON en la carpeta.")
        return
    
    facturas = []
    detalles = []

    print("Procesando archivos JSON...")
    for archivo in archivos:
        json_data = leer_json(archivo)
        if json_data:
            factura = extraer_datos_factura(json_data)
            if factura:
                facturas.append(factura)

            detalles_factura = extraer_detalles_factura(json_data)
            detalles.extend(detalles_factura)

    if not facturas:
        print("No se encontraron datos de facturas válidos.")
        return

    df_facturas = pd.DataFrame(facturas)
    df_detalles = pd.DataFrame(detalles)

    print("Conectando a la base de datos PostgreSQL...")
    engine = conectar_postgresql(USUARIO, PASSWORD, HOST, PUERTO, DB)

    if engine:
        print("Guardando datos en la base de datos...")
        guardar_factura(df_facturas, engine)
        guardar_detalles(df_detalles, engine)
    else:
        print("No se pudo conectar a la base de datos.")


if __name__ == "__main__":
    main()
