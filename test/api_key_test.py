import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Para guardar las variables usamos el comando:
# setx NOMRBE_API_KEY "api_key_aqui"

# Cargar variables desde el archivo .env y leer la apikey
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("API key no definida")

chat = ChatOpenAI(temperature=0)
response = chat.invoke("Sabes español?")
print(response.content)
