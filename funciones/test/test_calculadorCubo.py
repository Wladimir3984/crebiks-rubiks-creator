from funciones.calculadorCubo import calcularPiezas
import pytest

@pytest.mark.parametrize(
    "alto, ancho, profundidad, esperado",
    [
    #tests cubos cuadrados
   (10, 10, 10, {'cubo': '10x10x10', 'piezas': 488, 'superior_mas_inferior': 200, 'aristas_centrales': 32, 'centro': 256}) ,
   (4, 4, 4, {'cubo': '4x4x4', 'piezas': 56, 'superior_mas_inferior': 32, 'aristas_centrales': 8, 'centro': 16}) ,
   (3, 3, 3, {'cubo': '3x3x3', 'piezas': 26, 'superior_mas_inferior': 18, 'aristas_centrales': 4, 'centro': 4}) ,
   (2, 2, 2, {'cubo': '2x2x2', 'piezas': 8, 'superior_mas_inferior': 8, 'aristas_centrales': 0, 'centro': 0}) ,
   (1, 1, 1, {'cubo': '1x1x1', 'piezas': 1, 'superior_mas_inferior': 0, 'aristas_centrales': 0, 'centro': 0}) ,
    #tests cubos rectangulares
    ]
)
def test_calculadorCubo(alto, ancho, profundidad, esperado):
    assert calcularPiezas(alto, ancho, profundidad) == esperado
    
