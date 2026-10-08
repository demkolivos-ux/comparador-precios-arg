import json
import pandas as pd

# Datos extraídos (aquí va tu lógica de extracción)
datos_precios = [
    {"EAN": "7790001001", "Producto": "Leche Entera La Serenísima 1L", "Marca": "La Serenísima", "Supermercado": "Coto", "Precio": 1250},
    {"EAN": "7790001001", "Producto": "Leche Entera La Serenísima 1L", "Marca": "La Serenísima", "Supermercado": "Carrefour", "Precio": 1190},
    {"EAN": "7790001002", "Producto": "Galletitas Toddy 210g", "Marca": "Toddy", "Supermercado": "Día", "Precio": 1400},
]

# Convertir a DataFrame de Pandas
df = pd.DataFrame(datos_precios)

# Guardar en archivo Excel y CSV
df.to_excel("precios_hoy.xlsx", index=False)
df.to_csv("precios_hoy.csv", index=False, encoding='utf-8-sig')

print("¡Archivos precios_hoy.xlsx y precios_hoy.csv generados con éxito!")
