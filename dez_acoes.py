import http.client, urllib.parse

conn = http.client.HTTPSConnection('api.stockdata.org')

params = urllib.parse.urlencode({
    'api_token': 'ujmUaTYeAdRGe5MyEPbIrvF4mevABivctOt1CrgU',
    'symbols': 'AAPL,TSLA',
    'limit': 50,
    })

conn.request('GET', '/v1/news/all?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))