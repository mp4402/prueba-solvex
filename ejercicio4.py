import requests
from bs4 import BeautifulSoup

# URL de la página de CoinMarketCap
url = 'https://coinmarketcap.com/currencies/bitcoin/'

# Realiza una solicitud GET para obtener el contenido de la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de respuesta 200)

if response.status_code == 200:
    # Analiza el contenido de la página web con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    precio = soup.find(class_='sc-f70bb44c-0 jxpCgO base-text').text

    print(f"El precio actual de Bitcoin es: {precio}")
else:
    print(f'Error al hacer la solicitud. Código de respuesta: {response.status_code}')
