import requests
import json

# Substitua pela sua chave da API
api_key = 'GET https://api.stockdata.org/v1/data/intraday/adjusted HTTP/1.1'

# A URL da API para obter dados (aqui estamos usando um exemplo de dados históricos)
url = f'https://api.stockdata.org/v1/data/quote?symbols=AAPL&api_token={api_key}'

# Fazendo a requisição GET para a API
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Convertendo a resposta para um formato JSON
    data = response.json()
    print(json.dumps(data, indent=4))  # Exibindo os dados de maneira formatada
else:
    print(f'Erro ao obter dados: {response.status_code}')
