from funciones.calculadorCubo import calcularPiezas
import pytest

@pytest.mark.parametrize(
    "alto, ancho, profundidad, esperado",
    [
    #tests cubos cuadrados
   (10, 10, 10, {'cubo': '10x10x10', 'piezas': 488, 'front_plus_back': 200, 'aristas_centrales': 32, 'centro_left_plus_right': 256, 'centro_up_plus_down':0}) ,
   (4, 4, 4, {'cubo': '4x4x4', 'piezas': 56, 'front_plus_back': 32, 'aristas_centrales': 8, 'centro_left_plus_right': 16, 'centro_up_plus_down':0}) ,
   (3, 3, 3, {'cubo': '3x3x3', 'piezas': 26, 'front_plus_back': 18, 'aristas_centrales': 4, 'centro_left_plus_right': 4, 'centro_up_plus_down':0}) ,
   (2, 2, 2, {'cubo': '2x2x2', 'piezas': 8, 'front_plus_back': 8, 'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down':0}) ,
   (1, 1, 1, {'cubo': '1x1x1', 'piezas': 1, 'front_plus_back': 0, 'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down':0}) ,
    #tests cubos rectangulares
   (7, 3, 3, {'cubo': '7x3x3', 'piezas': 58, 'front_plus_back': 42, 'aristas_centrales': 4, 'centro_left_plus_right': 10, 'centro_up_plus_down':2}) ,
    ]
)
def test_calculadorCubo(alto, ancho, profundidad, esperado):
    assert calcularPiezas(alto, ancho, profundidad) == esperado
    
