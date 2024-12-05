import http.client
import urllib.parse
import json
import pandas as pd  # Importando pandas

# Função para fazer a requisição e retornar o DataFrame
def get_data(symbols, limit):
    conn = http.client.HTTPSConnection('api.stockdata.org')

    # Definindo os parâmetros
    params = urllib.parse.urlencode({
        'api_token': 'ujmUaTYeAdRGe5MyEPbIrvF4mevABivctOt1CrgU',
        'symbols': symbols,
        'limit': limit,
    })

    # Requisição GET para a API
    conn.request('GET', '/v1/data/quote?' + params)

    # Obtendo a resposta
    res = conn.getresponse()
    data = res.read()

    # Convertendo os dados JSON
    json_data = json.loads(data.decode('utf-8'))

    # Normalizando os dados JSON em um DataFrame do Pandas
    df = pd.json_normalize(json_data['data'])

    return df

# Requisições e concatenando os DataFrames
df_1_3 = get_data('AAPL,TSLA,MSFT', 3)
df_4_6 = get_data('AMZN,ABEV3,ITUB4', 3)
df_7_9 = get_data('MCDC34,BALL,PETR4', 3)
df10 = get_data('NVDC34', 1)

# Exibindo os DataFrames
print(df_1_3)
print(df_4_6)
print(df_7_9)
print(df10)
