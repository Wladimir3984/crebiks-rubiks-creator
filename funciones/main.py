from calculadorCubo import calcularPiezas

#total,cara,sup_inf,aristas_centrales,centro

piezas = calcularPiezas(3,3,3) #[26, 9, 18, 6, 1]
print(piezas)

piezas = calcularPiezas(4,4,4) #[56, 16, 32, 16, 4]
print(piezas)

piezas = calcularPiezas(3,2,3) #False
print(piezas)

piezas = calcularPiezas(3,9,4) #False
print(piezas)
