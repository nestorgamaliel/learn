import pandas as pd

# Cargar el archivo Excel
archivo = '20250407 - prestamos.xlsx'
xls = pd.ExcelFile(archivo)
df = xls.parse('Prestamos')

# Lista para almacenar scripts INSERT
inserts = []

# Recorrer columnas de persona cada 6 columnas
for start_col in range(1, df.shape[1], 6):
    try:
        nombres = df.iloc[0, start_col]
        apellidos = df.iloc[1, start_col]
        sexo = df.iloc[2, start_col]
        persona_id = df.iloc[3, start_col]

        # Validar que haya datos mínimos para crear el INSERT
        if pd.notnull(persona_id) and pd.notnull(nombres):
            # Preparar valores
            nombres = str(nombres).replace("'", "''")  # Escapar comillas
            apellidos = str(apellidos).replace("'", "''") if pd.notnull(apellidos) else ''
            sexo = str(sexo).strip() if pd.notnull(sexo) else ''

            insert = f"""INSERT INTO public.persona (
    persona_id, nombres, apellidos, fecha_nacimiento, sexo, telefono, direccion, municipio_id, departamento_id)
VALUES (
    {int(persona_id)}, '{nombres}', '{apellidos}', 'NULL', '{sexo}', NULL, NULL, NULL, NULL);"""

            inserts.append(insert)
    except Exception as e:
        print(f"Error en columna {start_col}: {e}")

# Guardar los scripts en un archivo .sql
with open('insert_personas.sql', 'w', encoding='utf-8') as f:
    for sql in inserts:
        f.write(sql + '\n')

print(f"Se generaron {len(inserts)} scripts INSERT en el archivo 'insert_personas.sql'")
