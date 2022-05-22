"""
*La función debe recibir como parámetro un diccionario con la siguiente estructura:

    informacion = {
        'id_cliente': 0,
        'nombre': '',
        'edad': 0,
        'primer_ingreso': False
        
    }
*La función debe retornar un diccionario con la siguiente estructura:
    respuesta = {
        'nombre': '',
        'edad': 0,
        'atraccion': '',
        'primer_ingreso': False,
        'total_boleta': 0,
        'apto' False
        
    }
*apto -> verdadero solo si el cliente está dentro del rango de edad de la tabla
*atraccion y total_boleta -> 'N/A' si no está dentro del rango de edad
*Si es el primer ingreso se aplica un descuento
"""


def cliente(informacion: dict) -> dict:
    # obtener edad
    edad = informacion['edad']
    atraccion = 'N/A'
    valor_boleta = 'N/A'
    apto = True
    con_descuento = 0
    # Evaluar la edad dentro de los rangos descritos
    if edad > 18:
        atraccion = 'X-Treme'
        valor_boleta = 20000
        con_descuento = 0.95
    elif edad >= 15:
        atraccion = 'Carro chocones'
        valor_boleta = 5000
        con_descuento = 0.93
    elif edad >= 7:
        atraccion = 'Sillas voladoras'
        valor_boleta = 10000
        con_descuento = 0.95
    else:
        apto = False
    # Evaluar si tiene descuento y aplicar si se cumple la condición
    if informacion['primer_ingreso'] & apto:
        valor_boleta = valor_boleta * con_descuento

    respuesta = {
        'nombre': informacion['nombre'],
        'edad': informacion['edad'],
        'atraccion': atraccion,
        'primer_ingreso': informacion['primer_ingreso'],
        'total_boleta': valor_boleta,
        'apto': apto
    }
    return respuesta


# Testear la función
informacion = [{
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True
}, {
    'id_cliente': 1,
    'nombre': 'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': False
}, {
    'id_cliente': 2,
    'nombre': 'Gloria Suarez',
    'edad': 3,
    'primer_ingreso': True
}, {
    'id_cliente': 3,
    'nombre': 'Tatiana Suarez',
    'edad': 17,
    'primer_ingreso': True
}, {
    'id_cliente': 3,
    'nombre': 'Tatiana Suarez',
    'edad': 17,
    'primer_ingreso': False
}, {
    'id_cliente': 4,
    'nombre': 'Tatiana Ruiz',
    'edad':  8,
    'primer_ingreso': True
}, {
    'id_cliente': 4,
    'nombre': 'Tatiana Ruiz',
    'edad': 8,
    'primer_ingreso': False
}]

for info in informacion:
    print(cliente(info))
