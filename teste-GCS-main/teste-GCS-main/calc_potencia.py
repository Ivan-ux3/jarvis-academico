# Calculo de potencia e raiz quadrada

# Módulo B - Operações de Potência

# Autor: Laura Santa Cruz Rodrigues

# Branch: feature/modulo-potencia

def potencia(base, expoente):
    ''' Cacula a potência de um número, dado uma base e um expoente. '''

# Verifica se os valores informados são numéricos
    if not isinstance(base, (int, float)) or not isinstance(expoente, (int, float)):
        # Se não forem, lança um ValueError
        raise ValueError("Informe valores numéricos válidos!")

    base = float(base)
    expoente = float(expoente)

# Calcula a potência usando o operador de exponenciação (**)
    calcula_potencia = base ** expoente

    return calcula_potencia


def raiz_quadrada(numero):
    ''' Calcula a raiz quadrada de um número. '''

    # Verifica se o valor informado é numérico
    if not isinstance(numero, (int, float)):
        # Se não for, lança um ValueError
        raise ValueError("Informe um valor numérico válido!")

    numero = float(numero)

    # Verifica se o número é negativo
    if numero < 0:
        # Se for negativo, lança um ValueError
        raise ValueError(
            "Não é possível calcular a raiz quadrada de um número negativo!")

# Calcula a raiz quadrada usando o operador de exponenciação (**)
    calcula_raiz = numero ** 0.5

    return calcula_raiz
