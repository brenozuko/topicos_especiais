import json
import requests

navegador = {
    "User-Agent": "Chrome"
}
urll = "https://parallelum.com.br/fipe/api/v1/carros/marcas"

data = requests.get(url=urll, headers=navegador)
print(data.json())

# for marca in data:
#     print(marca)
