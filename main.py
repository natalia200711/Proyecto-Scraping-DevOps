import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

def ejecutar_scraping_estatico():
    # URL del artículo elegido en tu Evidencia 1
    url_producto = "https://www.amazon.com/dp/B0HFMCH32K"

    # Encabezados para simular un navegador real
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9"
    }

    print("Iniciando proceso de web scraping estático con BeautifulSoup...")
    inicio_bs = time.time()

    titulo_bs = "No encontrado"
    precio_bs = "No disponible"
    estado_bs = "Fallido"

    try:
        # Realizamos la petición GET a la página
        response = requests.get(url_producto, headers=headers, timeout=15)

        if response.status_code == 200:
            print("Petición exitosa con BeautifulSoup")
            soup = BeautifulSoup(response.content, "html.parser")

            # Extraemos el título y el precio de forma segura
            title_element = soup.find("span", id="productTitle")
            titulo_bs = title_element.get_text(strip=True) if title_element else "No encontrado"

            price_element = soup.find("span", class_="a-offscreen")
            precio_bs = price_element.get_text(strip=True) if price_element else "No disponible"

            estado_bs = "Exitoso"
        else:
            print(f"Aviso: La página respondió con el código HTTP: {response.status_code}")
            estado_bs = "Bloqueado o Restringido"

    except Exception as e:
        print(f"Ocurrió un error durante la petición: {e}")
        estado_bs = "Excepción"

    tiempo_bs = time.time() - inicio_bs

    # Mostramos los resultados en la consola del pipeline o terminal local
    print("\n========================================")
    print("        RESULTADO BEAUTIFULSOUP         ")
    print("========================================")
    print("Título:", titulo_bs)
    print("Precio:", precio_bs)
    print("Estado:", estado_bs)
    print("Tiempo:", round(tiempo_bs, 4), "segundos")
    print("========================================")

    # Retornamos True para asegurar que el script finalice de forma correcta ante el CI/CD
    return True

if __name__ == "__main__":
    ejecutar_scraping_estatico()