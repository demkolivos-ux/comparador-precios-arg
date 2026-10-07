import requests
import json
import os

# Sucursales de ejemplo en Zona Norte / San Fernando (Coto, Carrefour, Vea, Día, Jumbo)
# Estas son los IDs de sucursal típicos en el sistema Precios Claros
SUCURSALES_OBJETIVO = [
    {"id": "12-1-12", "nombre": "Coto - San Fernando"},
    {"id": "10-1-140", "nombre": "Carrefour - San Fernando"},
    {"id": "9-1-204", "nombre": "Día - San Fernando"},
    {"id": "10-3-601", "nombre": "Vea - San Fernando"}
]

# Lista de productos de prueba (EAN / Código de barras o búsqueda por término)
PRODUCTOS_BUSQUEDA = [
    "leche entera 1l",
    "aceite de girasol 1.5l",
    "galletitas chocolinas",
    "coca cola 2.25",
    "yerba playadito 500g"
]

def buscar_precios_sepa():
    print("--- Iniciando búsqueda de precios en Argentina ---")
    resultados = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for producto in PRODUCTOS_BUSQUEDA:
        print(f"Buscando: {producto}...")
        url = f"https://buscadordeprecios.produccion.gob.ar/api/productos?string={producto}&limite=5"
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                productos_encontrados = data.get("productos", [])
                for item in productos_encontrados:
                    resultados.append({
                        "ean": item.get("id"),
                        "nombre": item.get("nombre"),
                        "marca": item.get("marca"),
                        "precio_lista": item.get("precio_lista"),
                        "precio_promocion": item.get("precio_promocion")
                    })
            else:
                print(f"No se obtuvieron resultados para {producto} (Status {response.status_code})")
        except Exception as e:
            print(f"Error al consultar {producto}: {e}")

    # Guardar resultados en un archivo JSON local
    with open("precios_hoy.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    print(f"¡Éxito! Se guardaron {len(resultados)} registros en precios_hoy.json")

if __name__ == "__main__":
    buscar_precios_sepa()
