import os
import json
from sqlalchemy import create_engine


def obtener_archivos_json(carpeta):
    """ Obtiene la lista de archivos JSON en la carpeta """
    return [os.path.join(carpeta, archivo) for archivo in os.listdir(carpeta) if archivo.endswith('.json')]


def leer_json(archivo):
    """ Lee un archivo JSON y lo devuelve como un diccionario """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al leer {archivo}: {e}")
        return None


def extraer_datos_factura(json_data):
    """ Extrae los datos principales de la factura """
    try:
        factura = {
            "numero_control": json_data["identificacion"]["numeroControl"],
            "codigo_generacion": json_data["identificacion"]["codigoGeneracion"],
            "fecha_emision": json_data["identificacion"]["fecEmi"],
            "hora_emision": json_data["identificacion"]["horEmi"],
            "tipo_moneda": json_data["identificacion"]["tipoMoneda"],
            "emisor_nit": json_data["emisor"]["nit"],
            "emisor_nombre": json_data["emisor"]["nombre"],
            "receptor_nit": json_data["receptor"]["nit"],
            "receptor_nombre": json_data["receptor"]["nombre"],
            "total_gravada": json_data["resumen"]["totalGravada"],
            "total_iva": sum(t["valor"] for t in json_data["resumen"]["tributos"] if t["codigo"] == "20"),
            "total_pagar": json_data["resumen"]["totalPagar"]
        }
        return factura
    except KeyError as e:
        print(f"Error extrayendo datos de la factura: {e}")
        return None


def extraer_detalles_factura(json_data):
    """ Extrae los detalles de los productos/servicios vendidos """
    try:
        detalles = []
        numero_control = json_data["identificacion"]["numeroControl"]

        for item in json_data["cuerpoDocumento"]:
            detalles.append({
                "numero_control": numero_control,
                "num_item": item["numItem"],
                "descripcion": item["descripcion"],
                "cantidad": item["cantidad"],
                "precio_unitario": item["precioUni"],
                "monto_descuento": item["montoDescu"],
                "venta_gravada": item["ventaGravada"]
            })
        return detalles
    except KeyError as e:
        print(f"Error extrayendo detalles de factura: {e}")
        return []


def conectar_postgresql(usuario, password, host, puerto, db):
    """ Crea y devuelve una conexión a PostgreSQL usando SQLAlchemy """
    url = f"postgresql://{usuario}:{password}@{host}:{puerto}/{db}"
    try:
        engine = create_engine(url)
        return engine
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def guardar_factura(df_facturas, engine):
    """ Guarda los datos de facturas en PostgreSQL """
    try:
        df_facturas.to_sql('facturas', engine, if_exists='append', index=False)
        print(f"Facturas guardadas correctamente.")
    except Exception as e:
        print(f"Error al guardar facturas en la base de datos: {e}")


def guardar_detalles(df_detalles, engine):
    """ Guarda los detalles de las facturas en PostgreSQL """
    try:
        df_detalles.to_sql('detalle_factura', engine, if_exists='append', index=False)
        print(f"Detalles guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar detalles en la base de datos: {e}")
