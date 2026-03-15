def converter_para_centavos(valor):
    reais, centavos = valor.split(",")
    return int(reais) * 100 + int(centavos)

def mostrar_valor(valor_centavos):
    reais = valor_centavos // 100
    centavos = valor_centavos % 100
    return f"{reais},{centavos:02d}"