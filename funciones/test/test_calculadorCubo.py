from funciones.calculadorCubo import calcularPiezas,    get_cube_details
import pytest


@pytest.mark.parametrize(
    "alto, ancho, profundidad, esperado",
    [
        # tests cubos cuadrados
        (10, 10, 10, {'cubo': '10x10x10', 'piezas': 488, 'front_plus_back': 200,
         'aristas_centrales': 32, 'centro_left_plus_right': 256, 'centro_up_plus_down': 0}),
        (4, 4, 4, {'cubo': '4x4x4', 'piezas': 56, 'front_plus_back': 32,
         'aristas_centrales': 8, 'centro_left_plus_right': 16, 'centro_up_plus_down': 0}),
        (3, 3, 3, {'cubo': '3x3x3', 'piezas': 26, 'front_plus_back': 18,
         'aristas_centrales': 4, 'centro_left_plus_right': 4, 'centro_up_plus_down': 0}),
        (2, 2, 2, {'cubo': '2x2x2', 'piezas': 8, 'front_plus_back': 8,
         'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down': 0}),
        (1, 1, 1, {'cubo': '1x1x1', 'piezas': 1, 'front_plus_back': 0,
         'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down': 0}),
        # tests cubos rectangulares, si los lados no estan de mayor a menor no se calcula bien,usar solo para test
        (7, 3, 3, {'cubo': '7x3x3', 'piezas': 58, 'front_plus_back': 42,
         'aristas_centrales': 4, 'centro_left_plus_right': 10, 'centro_up_plus_down': 2}),
        (6, 3, 3, {'cubo': '6x3x3', 'piezas': 50, 'front_plus_back': 36,
         'aristas_centrales': 4, 'centro_left_plus_right': 8, 'centro_up_plus_down': 2})

    ]
)
def test_calculadorCubo(alto, ancho, profundidad, esperado):
    # si los lados no estan de mayor a menor no se calcula bien,usar solo para test
    assert calcularPiezas(alto, ancho, profundidad) == esperado


@pytest.mark.parametrize(
    "alto, ancho, profundidad, esperado",
    [
        # Esta funcion ordena los lados de mayor a menor por lo que se corrige el error de la funcion base(calcularPiezas)
        # al reordenar los lados, el cubo no se armara en la orientacion correcta dada por el usuario, pero si se calcula bien

        # testing mutabilidad de lados(ordenados de mayor a menor en funcion get_cube_details, siempre se calculan despues de ordenar)
        (3, 3, 7, {'cubo': '7x3x3', 'piezas': 58, 'front_plus_back': 42,
                   'aristas_centrales': 4, 'centro_left_plus_right': 10, 'centro_up_plus_down': 2}),
        (3, 7, 3, {'cubo': '7x3x3', 'piezas': 58, 'front_plus_back': 42,
                   'aristas_centrales': 4, 'centro_left_plus_right': 10, 'centro_up_plus_down': 2}),
        (3, 3, 6, {'cubo': '6x3x3', 'piezas': 50, 'front_plus_back': 36,
                   'aristas_centrales': 4, 'centro_left_plus_right': 8, 'centro_up_plus_down': 2}),
        (3, 6, 3, {'cubo': '6x3x3', 'piezas': 50, 'front_plus_back': 36,
                   'aristas_centrales': 4, 'centro_left_plus_right': 8, 'centro_up_plus_down': 2}),
        # tests especificos funcionamiento interno de calcularPiezas
        (7, 7, 2, {'cubo': '7x7x2', 'piezas': 98, 'front_plus_back': 98,
                   'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down': 0}),
        (2, 7, 7, {'cubo': '7x7x2', 'piezas': 98, 'front_plus_back': 98,
                   'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down': 0}),
        (5, 3, 1, {'cubo': '5x3x1', 'piezas': 15, 'front_plus_back': 0,
                   'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down': 0}),
        (5, 2, 1, {'cubo': '5x2x1', 'piezas': 10, 'front_plus_back': 10,
                   'aristas_centrales': 0, 'centro_left_plus_right': 0, 'centro_up_plus_down': 0}),
        # Manejo de errores
        (0, 4, 3, False),
        (5, 2, "hello", False),
        (5, -5, 5, False),
        (3.2, 5, 5, False),
        ([1, 2, 3], 5, 5, False),
        ((1, 2, 3), 5, 5, False),
    ]
)
def test_get_cube_details(alto, ancho, profundidad, esperado):
    assert get_cube_details(alto, ancho, profundidad) == esperado
