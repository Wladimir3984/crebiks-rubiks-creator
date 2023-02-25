from calculadorCubo import calcularPiezas

#total,cara,sup_inf,aristas_centrales,centro

piezas = calcularPiezas(3,3,3) #[26, 9, 18, 4, 4]
print(piezas)

piezas = calcularPiezas(4,4,4) #[56, 16, 32, 8, 16]
print(piezas)

piezas = calcularPiezas(4,3,3) #
print(piezas)

piezas = calcularPiezas(7,3,3) #58
print(piezas)

piezas = calcularPiezas(1,1,1) # 1 0 0 0 0
print(piezas)

piezas = calcularPiezas(2,3,3) # 18 9 18 0 0
print(piezas)

piezas = calcularPiezas(3,3,2) # 18 9 18 0 0
print(piezas)
