import openai
import json

# Asignar la clave API (sustituir "TU_CLAVE_AQUI" por la clave generada)
client = openai.OpenAI(api_key="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")

# JSON de ejemplo
json_data = '{"nombre": "Juan", "edad": 30, "ciudad": "San Salvador"}'

# Crear el prompt para ChatGPT
prompt = f"""
Tengo el siguiente JSON:
{json_data}

Por favor, descomponlo en clave-valor explicando el significado de cada elemento.
"""

# Hacer la solicitud a OpenAI
respuesta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# Mostrar la respuesta generada
print(respuesta.choices[0].message.content)