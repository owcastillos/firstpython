def AutoPartes(ventas: list) -> list:
    resultado = []
    for venta in ventas:
        resultado.append({
            'idProducto': venta[0],
            'dProducto': venta[1],
            'pnProducto': venta[2],
            'cvProducto': venta[3],
            'sProducto': venta[4],
            'nComprador': venta[5],
            'cComprador': venta[6],
            'fVenta': venta[7]
        })
    return resultado


def consultaRegistro(ventas, idProducto):
    resultado = ""
    for venta in ventas:
        if(venta['idProducto'] == idProducto):
            resultado += "Producto consultado " + str(venta['idProducto']) + " Descripción " + venta['dProducto'] + " #Parte " + venta['pnProducto'] + " Cantidad vendida " + str(
                venta['cvProducto']) + " Stock " + str(venta['sProducto']) + " Comprador " + venta['nComprador'] + " Documento " + str(venta['cComprador']) + " Fecha Venta " + venta['fVenta'] + "\n\n"
    if(len(resultado) == 0):
        resultado = "No hay registro de venta de ese producto\n\n"
    print(resultado)


"""
Producto consultado : {idProducto} Descripción {dProducto}
#Parte {pnProducto} Cantidad vendida {cvProducto} Stock
{sProducto} Comprador {nComprador} Documento
{cComprador} Fecha Venta {fVenta}
"""
"""
TEST
consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
print()
"""
l1 = [(2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
      (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'),
      (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
      (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
      (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020')]

l2 = [(5489, 'tornillo', 'RS8512', 2, 33, 'Julio Perez', 3654213, '13/06/2020'),
      (3215, 'zocalo', 'UM8587', 2, 125, 'Laura Macias', 1256321, '13/06/2020'),
      (3698, 'biela', 'PT3218', 1, 78, 'Luis Peña', 14565487, '13/06/2020'),
      (8795, 'cilindro', 'AZ8794', 2, 96, 'Carlos Casio', 5612405, '13/06/2020')]

l3 = [(9852, 'Culata', 'XC9875', 2, 165, 'Luis Molero', 3455846, '14/06/2020'),
      (9852, 'Culata', 'XC9875', 2, 165, 'Jose Mejia', 1355846, '14/06/2020'),
      (2564, 'Cárter', 'PT29872', 2, 32, 'Peter Cerezo', 8545436, '14/06/2020'),
      (5412, 'válvula', 'AZ8798', 2, 11, 'Juan Peña', 568975, '14/06/2020')]

todos = [(2001, 'rosca', 'PT29872', 2, 45, 'Luis Molero', 3456, '12/06/2020'),
         (2010, 'bujía', 'MS9512', 4, 15, 'Carlos Rondon', 1256, '12/06/2020'),
         (2010, 'bujía', 'ER6523', 9, 36, 'Pedro Montes', 1243, '12/06/2020'),
         (3578, 'tijera', 'QW8523', 1, 128, 'Pedro Faria', 1456, '12/06/2020'),
         (9251, 'piñón', 'EN5698', 2, 8, 'Juan Peña', 565, '12/06/2020'),
         (5489, 'tornillo', 'RS8512', 2, 33, 'Julio Perez', 3654213, '13/06/2020'),
         (3215, 'zocalo', 'UM8587', 2, 125, 'Laura Macias', 1256321, '13/06/2020'),
         (3698, 'biela', 'PT3218', 1, 78, 'Luis Peña', 14565487, '13/06/2020'),
         (8795, 'cilindro', 'AZ8794', 2, 96, 'Carlos Casio', 5612405, '13/06/2020'),
         (9852, 'Culata', 'XC9875', 2, 165, 'Luis Molero', 3455846, '14/06/2020'),
         (9852, 'Culata', 'XC9875', 2, 165, 'Jose Mejia', 1355846, '14/06/2020'),
         (2564, 'Cárter', 'PT29872', 2, 32, 'Peter Cerezo', 8545436, '14/06/2020'),
         (5412, 'válvula', 'AZ8798', 2, 11, 'Juan Peña', 568975, '14/06/2020')]

consultaRegistro(AutoPartes(l1), 2010)
consultaRegistro(AutoPartes(l2), 2001)
consultaRegistro(AutoPartes(l3), 9852)
