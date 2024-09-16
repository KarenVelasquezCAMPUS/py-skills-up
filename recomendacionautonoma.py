# Lista de ciudades con clima y ubicación específica Autonomo

def recomendacion_autonomo(caracteristica, tipo):
    clima = {
        "Bogota": "frio",
        "Monteria": "calido",
        "Medellin": "templado"
    }

    ubicacion = {
        "Guajira": "norte",
        "Leticia": "sur",
        "Santander": "este",
        "Antioquia": "oeste"
    }

    turismo = {
        "Santa Marta": "mar",
        "Villavicencio": "llano",
        "Riohacha": "desierto",
        "Quindio": "valle"
    }

    if tipo == "clima":
        for ciudad, clima_ciudad in clima.items():
            if clima_ciudad == caracteristica:
                return ciudad
        return "No se encontro la caracteristica"
    elif tipo == "ubicacion":
        for ciudad, ubicacion_ciudad in ubicacion.items():
            if ubicacion_ciudad == caracteristica:
                return ciudad
        return "No se encontro la caracteristica"
    elif tipo == "turismo":
        for ciudad, turismo_ciudad in turismo.items():
            if turismo_ciudad == caracteristica:
                return ciudad
        return "No se encontro la caracteristica"
    else:
        return "Tipo no valido"


print(recomendacion_autonomo("norte", "ubicacion"))
