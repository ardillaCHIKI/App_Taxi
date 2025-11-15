import folium

# Lista de coordenadas que representan la ruta (latitud, longitud)
ruta = [
    (40.416775, -3.703790),  # Madrid, España
    (40.418056, -3.713056),  # Puerta del Sol
    (40.419556, -3.692556),  # Parque del Retiro
    (40.423333, -3.712222),  # Templo de Debod
]

# Crear un mapa centrado en el primer punto de la ruta
mapa = folium.Map(location=ruta[0], zoom_start=14)

# Dibujar la ruta usando una polyline
folium.PolyLine(
    ruta,  # Coordenadas de la ruta
    color="blue",  # Color de la línea
    weight=5,  # Grosor de la línea
    opacity=0.8,  # Opacidad de la línea
).add_to(mapa)

# Colocar un marcador en el punto inicial
folium.Marker(
    location=ruta[0],
    popup="Inicio de la ruta",
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(mapa)

# Colocar un marcador en el punto final
folium.Marker(
    location=ruta[-1],
    popup="Fin de la ruta",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(mapa)

# Guardar el mapa como un archivo HTML
mapa.save("ruta_interactiva.html")

# Mensaje para el usuario
print("El mapa con la ruta ha sido guardado como 'ruta_interactiva.html'. Ábrelo en tu navegador para visualizarlo.")