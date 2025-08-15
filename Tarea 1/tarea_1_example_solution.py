# Definimos códigos de retorno únicos para que coincidan con las pruebas
CODIGO_EXITO = 0
ERROR_NO_STRING = -100
ERROR_CADENA_INVALIDA = -200
ERROR_CARACTER_INVALIDO = -300


def count_char(cadena, caracter):
    """
    Cuenta cuántas veces aparece un carácter en una cadena, con validaciones.

    Parámetros:
        cadena (str): Cadena de texto donde buscar el carácter.
        caracter (str): Carácter único a buscar.

    Retorna:
        tuple: (codigo_retorno, cantidad_o_None)
            - codigo_retorno: entero (0 = éxito, otro valor = error)
            - cantidad_o_None: entero con cantidad o None en caso de error
    """

    # a) Verificar que cadena sea string
    if not isinstance(cadena, str):
        return ERROR_NO_STRING, None

    # b) Verificar que cadena solo contenga letras y números 0-9
    if not cadena.isalnum():
        return ERROR_CADENA_INVALIDA, None

    # c) Verificar que caracter sea un único carácter y válido
    if (not isinstance(caracter, str) or len(caracter) != 1 or
            not caracter.isalnum()):
        return ERROR_CARACTER_INVALIDO, None

    # Contar ocurrencias del caracter en la cadena
    cantidad = cadena.count(caracter)

    # Retornar código de éxito y cantidad
    return CODIGO_EXITO, cantidad


def multiplo_2(base, multiplo):
    """
    Calcula base multiplicada por un múltiplo usando corrimiento de bits.
    Múltiplo debe ser 1, 2, 4, 8 o 16.
    """

    # Validación de tipo y valor (enteros positivos)
    if not isinstance(base, int) or not isinstance(multiplo, int):
        return -400, None  # Cuando los datos no son números enteros

    if base < 0 or multiplo < 0:
        return -400, None  # Para números no positivos

    # Validación del múltiplo
    if multiplo not in [1, 2, 4, 8, 16]:
        return -500, None  # "multiplo" debe estar entre los valores

    # Cálculo del producto empleando corrimiento de bits <<
    if multiplo == 1:
        result = base
    elif multiplo == 2:
        # base * 2
        result = base << 1
    elif multiplo == 4:
        # base * 4
        result = base << 2
    elif multiplo == 8:
        # base * 8
        result = base << 3
    elif multiplo == 16:
        # base * 16
        result = base << 4

    return 0, result
