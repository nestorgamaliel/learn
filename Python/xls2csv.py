import pandas as pd
import os
from datetime import datetime

def procesar_excel_a_csv(ruta_excel, ruta_salida_40, ruta_salida_60):
    """
    Procesa un archivo Excel con hojas mensuales y genera dos archivos CSV consolidados
    para las planillas 40% y 60%.
    
    Args:
        ruta_excel: Ruta al archivo Excel
        ruta_salida_40: Ruta donde guardar el CSV para planilla 40%
        ruta_salida_60: Ruta donde guardar el CSV para planilla 60%
    """
    # Leer todas las hojas del Excel
    xl = pd.ExcelFile(ruta_excel)
    
    # Listas para almacenar los dataframes
    dfs_40 = []
    dfs_60 = []
    
    # Procesar cada hoja (cada mes)
    for nombre_hoja in xl.sheet_names:
        try:
            print(f"Procesando hoja: {nombre_hoja}")
            
            # Intentar extraer mes y año del nombre de la hoja
            fecha = None
            try:
                # Asumiendo que el nombre de la hoja tiene formato como "Enero 2019"
                fecha = datetime.strptime(nombre_hoja, "%B %Y")
                mes_anio = fecha.strftime("%m-%Y")
            except:
                # Si el formato es diferente, usar el nombre de la hoja como está
                mes_anio = nombre_hoja
            
            print(f"  Mes y año identificado: {mes_anio}")
            
            # Leer la hoja completa
            df_completo = pd.read_excel(xl, sheet_name=nombre_hoja, header=None)
            
            # Buscar los encabezados que separan las dos secciones
            idx_40 = None
            idx_60 = None
            
            for i, fila in enumerate(df_completo.values):
                # Convertir la fila a string y buscar los identificadores
                fila_str = str(fila)
                if "PLANILLA DE SALARIO ADMON 40%" in fila_str:
                    idx_40 = i
                    print(f"  Encontrado encabezado 40% en fila {i}")
                elif "PLANILLA DE SALARIO ADMON 60%" in fila_str:
                    idx_60 = i
                    print(f"  Encontrado encabezado 60% en fila {i}")
            
            # Si encontramos ambos encabezados, dividir el dataframe
            if idx_40 is not None and idx_60 is not None:
                # Sección 40%: desde idx_40+1 hasta idx_60-1
                df_40 = df_completo.iloc[idx_40+1:idx_60].copy()
                # La primera fila contiene los encabezados reales
                if len(df_40) > 1:
                    nuevos_encabezados = df_40.iloc[0].tolist()
                    # Asegurarse de que no haya nombres de columnas duplicados
                    encabezados_unicos = []
                    for i, encabezado in enumerate(nuevos_encabezados):
                        if pd.isna(encabezado):
                            encabezado = f"Sin_Nombre_{i}"
                        # Si ya existe este encabezado, añadir un sufijo
                        if encabezado in encabezados_unicos:
                            contador = 1
                            while f"{encabezado}_{contador}" in encabezados_unicos:
                                contador += 1
                            encabezado = f"{encabezado}_{contador}"
                        encabezados_unicos.append(encabezado)
                    
                    df_40 = df_40.iloc[1:]
                    df_40.columns = encabezados_unicos
                    # Añadir columna mes-año - ASEGURANDO QUE SE INCLUYA
                    df_40['Mes_Anio'] = mes_anio  # Cambiado a mayúsculas para consistencia
                    # Verificar que la columna fue añadida correctamente
                    if 'Mes_Anio' not in df_40.columns:
                        print("  ¡ADVERTENCIA! No se pudo añadir columna Mes_Anio a df_40")
                    else:
                        print(f"  Columna Mes_Anio añadida correctamente a df_40: {df_40['Mes_Anio'].iloc[0] if len(df_40) > 0 else 'No hay datos'}")
                    
                    dfs_40.append(df_40)
                    print(f"  Extraídos {len(df_40)} registros para 40%")
                
                # Sección 60%: desde idx_60+1 hasta el final
                df_60 = df_completo.iloc[idx_60+1:].copy()
                # La primera fila contiene los encabezados reales
                if len(df_60) > 1:  # Verificar que hay datos
                    nuevos_encabezados = df_60.iloc[0].tolist()
                    # Asegurarse de que no haya nombres de columnas duplicados
                    encabezados_unicos = []
                    for i, encabezado in enumerate(nuevos_encabezados):
                        if pd.isna(encabezado):
                            encabezado = f"Sin_Nombre_{i}"
                        # Si ya existe este encabezado, añadir un sufijo
                        if encabezado in encabezados_unicos:
                            contador = 1
                            while f"{encabezado}_{contador}" in encabezados_unicos:
                                contador += 1
                            encabezado = f"{encabezado}_{contador}"
                        encabezados_unicos.append(encabezado)
                    
                    df_60 = df_60.iloc[1:]
                    df_60.columns = encabezados_unicos
                    # Añadir columna mes-año - ASEGURANDO QUE SE INCLUYA
                    df_60['Mes_Anio'] = mes_anio  # Cambiado a mayúsculas para consistencia
                    # Verificar que la columna fue añadida correctamente
                    if 'Mes_Anio' not in df_60.columns:
                        print("  ¡ADVERTENCIA! No se pudo añadir columna Mes_Anio a df_60")
                    else:
                        print(f"  Columna Mes_Anio añadida correctamente a df_60: {df_60['Mes_Anio'].iloc[0] if len(df_60) > 0 else 'No hay datos'}")
                    
                    dfs_60.append(df_60)
                    print(f"  Extraídos {len(df_60)} registros para 60%")
            
            # Si solo encontramos un encabezado, puede ser que la hoja solo tenga una sección
            elif idx_40 is not None:
                df_40 = df_completo.iloc[idx_40+1:].copy()
                if len(df_40) > 1:
                    nuevos_encabezados = df_40.iloc[0].tolist()
                    # Asegurarse de que no haya nombres de columnas duplicados
                    encabezados_unicos = []
                    for i, encabezado in enumerate(nuevos_encabezados):
                        if pd.isna(encabezado):
                            encabezado = f"Sin_Nombre_{i}"
                        if encabezado in encabezados_unicos:
                            contador = 1
                            while f"{encabezado}_{contador}" in encabezados_unicos:
                                contador += 1
                            encabezado = f"{encabezado}_{contador}"
                        encabezados_unicos.append(encabezado)
                    
                    df_40 = df_40.iloc[1:]
                    df_40.columns = encabezados_unicos
                    df_40['Mes_Anio'] = mes_anio  # Cambiado a mayúsculas para consistencia
                    # Verificar que la columna fue añadida correctamente
                    if 'Mes_Anio' not in df_40.columns:
                        print("  ¡ADVERTENCIA! No se pudo añadir columna Mes_Anio a df_40")
                    
                    dfs_40.append(df_40)
                    print(f"  Extraídos {len(df_40)} registros para 40% (única sección)")
            
            elif idx_60 is not None:
                df_60 = df_completo.iloc[idx_60+1:].copy()
                if len(df_60) > 1:
                    nuevos_encabezados = df_60.iloc[0].tolist()
                    # Asegurarse de que no haya nombres de columnas duplicados
                    encabezados_unicos = []
                    for i, encabezado in enumerate(nuevos_encabezados):
                        if pd.isna(encabezado):
                            encabezado = f"Sin_Nombre_{i}"
                        if encabezado in encabezados_unicos:
                            contador = 1
                            while f"{encabezado}_{contador}" in encabezados_unicos:
                                contador += 1
                            encabezado = f"{encabezado}_{contador}"
                        encabezados_unicos.append(encabezado)
                    
                    df_60 = df_60.iloc[1:]
                    df_60.columns = encabezados_unicos
                    df_60['Mes_Anio'] = mes_anio  # Cambiado a mayúsculas para consistencia
                    # Verificar que la columna fue añadida correctamente
                    if 'Mes_Anio' not in df_60.columns:
                        print("  ¡ADVERTENCIA! No se pudo añadir columna Mes_Anio a df_60")
                    
                    dfs_60.append(df_60)
                    print(f"  Extraídos {len(df_60)} registros para 60% (única sección)")
                
        except Exception as e:
            print(f"Error procesando la hoja {nombre_hoja}: {e}")
    
    # Concatenar todos los dataframes para crear los consolidados
    if dfs_40:
        print(f"Consolidando {len(dfs_40)} hojas para planilla 40%...")
        # Verificar que todos los dataframes tengan columnas con nombres únicos
        for i, df in enumerate(dfs_40):
            if df.columns.duplicated().any():
                print(f"¡Alerta! El dataframe {i} tiene columnas duplicadas: {df.columns[df.columns.duplicated()]}")
                # Renombrar columnas duplicadas
                cols = pd.Series(df.columns)
                for dup in cols[cols.duplicated()].unique():
                    cols[cols[cols == dup].index.values.tolist()] = [f"{dup}_{i}" if i != 0 else dup for i in range(sum(cols == dup))]
                df.columns = cols
            
            # ASEGURARSE de que la columna Mes_Anio exista en cada dataframe
            if 'Mes_Anio' not in df.columns:
                print(f"  ¡ADVERTENCIA! Dataframe {i} no tiene columna Mes_Anio. Intentando recuperar...")
                # Intentar identificar a qué mes pertenece este dataframe si es posible
                if i < len(xl.sheet_names):
                    df['Mes_Anio'] = xl.sheet_names[i]
                else:
                    df['Mes_Anio'] = f"Desconocido_{i}"
        
        # IMPORTANTE: Asegurarse de que 'Mes_Anio' está en essential_columns
        essential_columns = ['Mes_Anio']  # Comenzar con Mes_Anio
        
        # Verificar qué columnas están en todos los dataframes
        if len(dfs_40) > 1:
            common_columns = set.intersection(*[set(df.columns) for df in dfs_40])
            # Añadir las columnas comunes a essential_columns
            for col in common_columns:
                if col not in essential_columns:
                    essential_columns.append(col)
        else:
            # Si solo hay un dataframe, usar todas sus columnas
            essential_columns = list(dfs_40[0].columns)
        
        # Si hay pocas columnas comunes, buscar las más frecuentes
        if len(essential_columns) < 3:  # Asumimos que al menos necesitamos algunas columnas clave
            print("No hay suficientes columnas comunes. Usando solo columnas esenciales...")
            
            # Encontrar las columnas más comunes entre todos los dataframes
            column_counts = {}
            for df in dfs_40:
                for col in df.columns:
                    if col not in column_counts:
                        column_counts[col] = 0
                    column_counts[col] += 1
            
            # Usar las columnas que aparecen en al menos la mitad de los dataframes
            threshold = len(dfs_40) / 2
            for col, count in column_counts.items():
                if count >= threshold and col not in essential_columns:
                    essential_columns.append(col)
        
        # ASEGURARSE de que Mes_Anio esté en essential_columns
        if 'Mes_Anio' not in essential_columns:
            essential_columns.insert(0, 'Mes_Anio')
        
        print(f"Columnas que se incluirán en el CSV 40%: {essential_columns}")
        
        # Asegurarnos de que todos los dataframes tengan estas columnas
        for i, df in enumerate(dfs_40):
            for col in essential_columns:
                if col not in df.columns:
                    df[col] = None
            
            # Reordenar para que Mes_Anio sea la primera columna
            cols = [c for c in df.columns if c != 'Mes_Anio']
            df = df[['Mes_Anio'] + cols]
            dfs_40[i] = df  # Actualizar el dataframe en la lista
        
        # Intentar la concatenación
        try:
            df_consolidado_40 = pd.concat(dfs_40, ignore_index=True)
            # Limpiar datos (eliminar filas completamente vacías)
            df_consolidado_40 = df_consolidado_40.dropna(how='all')
            
            # ASEGURARSE de que Mes_Anio está en el dataframe final
            if 'Mes_Anio' not in df_consolidado_40.columns:
                print("¡ERROR CRÍTICO! La columna Mes_Anio no está en el dataframe consolidado 40%")
            else:
                print(f"Valores únicos de Mes_Anio en el dataframe 40%: {df_consolidado_40['Mes_Anio'].unique()}")
            
            # Guardar a CSV
            df_consolidado_40.to_csv(ruta_salida_40, index=False)
            print(f"Archivo 40% guardado en: {ruta_salida_40}")
        except Exception as e:
            print(f"Error al consolidar datos 40%: {e}")
            # Intentar guardar cada hoja como un CSV separado
            print("Intentando guardar cada hoja como CSV separado...")
            for i, df in enumerate(dfs_40):
                df.to_csv(f"{ruta_salida_40.replace('.csv', '')}_hoja_{i}.csv", index=False)
    else:
        print("No se encontró información para Planilla 40%")
    
    # REPETIR EL MISMO PROCESO PARA LA PLANILLA 60%
    if dfs_60:
        print(f"Consolidando {len(dfs_60)} hojas para planilla 60%...")
        # Verificar que todos los dataframes tengan columnas con nombres únicos
        for i, df in enumerate(dfs_60):
            if df.columns.duplicated().any():
                print(f"¡Alerta! El dataframe {i} tiene columnas duplicadas: {df.columns[df.columns.duplicated()]}")
                # Renombrar columnas duplicadas
                cols = pd.Series(df.columns)
                for dup in cols[cols.duplicated()].unique():
                    cols[cols[cols == dup].index.values.tolist()] = [f"{dup}_{i}" if i != 0 else dup for i in range(sum(cols == dup))]
                df.columns = cols
            
            # ASEGURARSE de que la columna Mes_Anio exista en cada dataframe
            if 'Mes_Anio' not in df.columns:
                print(f"  ¡ADVERTENCIA! Dataframe {i} no tiene columna Mes_Anio. Intentando recuperar...")
                # Intentar identificar a qué mes pertenece este dataframe si es posible
                if i < len(xl.sheet_names):
                    df['Mes_Anio'] = xl.sheet_names[i]
                else:
                    df['Mes_Anio'] = f"Desconocido_{i}"
        
        # IMPORTANTE: Asegurarse de que 'Mes_Anio' está en essential_columns
        essential_columns = ['Mes_Anio']  # Comenzar con Mes_Anio
        
        # Verificar qué columnas están en todos los dataframes
        if len(dfs_60) > 1:
            common_columns = set.intersection(*[set(df.columns) for df in dfs_60])
            # Añadir las columnas comunes a essential_columns
            for col in common_columns:
                if col not in essential_columns:
                    essential_columns.append(col)
        else:
            # Si solo hay un dataframe, usar todas sus columnas
            essential_columns = list(dfs_60[0].columns)
        
        # Si hay pocas columnas comunes, buscar las más frecuentes
        if len(essential_columns) < 3:  # Asumimos que al menos necesitamos algunas columnas clave
            print("No hay suficientes columnas comunes. Usando solo columnas esenciales...")
            
            # Encontrar las columnas más comunes entre todos los dataframes
            column_counts = {}
            for df in dfs_60:
                for col in df.columns:
                    if col not in column_counts:
                        column_counts[col] = 0
                    column_counts[col] += 1
            
            # Usar las columnas que aparecen en al menos la mitad de los dataframes
            threshold = len(dfs_60) / 2
            for col, count in column_counts.items():
                if count >= threshold and col not in essential_columns:
                    essential_columns.append(col)
        
        # ASEGURARSE de que Mes_Anio esté en essential_columns
        if 'Mes_Anio' not in essential_columns:
            essential_columns.insert(0, 'Mes_Anio')
        
        print(f"Columnas que se incluirán en el CSV 60%: {essential_columns}")
        
        # Asegurarnos de que todos los dataframes tengan estas columnas
        for i, df in enumerate(dfs_60):
            for col in essential_columns:
                if col not in df.columns:
                    df[col] = None
            
            # Reordenar para que Mes_Anio sea la primera columna
            cols = [c for c in df.columns if c != 'Mes_Anio']
            df = df[['Mes_Anio'] + cols]
            dfs_60[i] = df  # Actualizar el dataframe en la lista
        
        # Intentar la concatenación
        try:
            df_consolidado_60 = pd.concat(dfs_60, ignore_index=True)
            # Limpiar datos (eliminar filas completamente vacías)
            df_consolidado_60 = df_consolidado_60.dropna(how='all')
            
            # ASEGURARSE de que Mes_Anio está en el dataframe final
            if 'Mes_Anio' not in df_consolidado_60.columns:
                print("¡ERROR CRÍTICO! La columna Mes_Anio no está en el dataframe consolidado 60%")
            else:
                print(f"Valores únicos de Mes_Anio en el dataframe 60%: {df_consolidado_60['Mes_Anio'].unique()}")
            
            # Guardar a CSV
            df_consolidado_60.to_csv(ruta_salida_60, index=False)
            print(f"Archivo 60% guardado en: {ruta_salida_60}")
        except Exception as e:
            print(f"Error al consolidar datos 60%: {e}")
            # Intentar guardar cada hoja como un CSV separado
            print("Intentando guardar cada hoja como CSV separado...")
            for i, df in enumerate(dfs_60):
                df.to_csv(f"{ruta_salida_60.replace('.csv', '')}_hoja_{i}.csv", index=False)
    else:
        print("No se encontró información para Planilla 60%")

# Ejemplo de uso
if __name__ == "__main__":
    ruta_excel = "C:\\Devs\\Plycem\\PLANILLA 2019 A 2023.xlsx"
    ruta_salida_40 = "planilla_40_consolidada.csv"
    ruta_salida_60 = "planilla_60_consolidada.csv"
    
    procesar_excel_a_csv(ruta_excel, ruta_salida_40, ruta_salida_60)