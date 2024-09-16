# Lista de ciudades con clima y ubicación específica Manual

def recomendacionmanual():
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

    seleccion = "clima"

    if seleccion == "clima":
        print([ciudad for ciudad, cl in clima.items() if cl == "frio"])
    elif seleccion == "ubicacion":
        print([ciudad for ciudad, ub in ubicacion.items() if ub == "norte"])
    elif seleccion == "turismo":
        print([ciudad for ciudad, tu in turismo.items() if tu == "valle"])

recomendacionmanual()
