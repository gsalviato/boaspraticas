# VIOLAÇÕES COM YAGNI, KISS E SINE
# Criando parâmetros para 'peso' e 'internacional' desnecessarios. 
# Uso de classes e construtores para resolver um problema de 1 linha de lógica.
# Criando codigo "complexo" para um problema simples.

class CalculadoraDeFrete:
    def __init__(self, tipo_envio="nacional"):
        self.tipo_envio = tipo_envio
        self.taxa_futura_correios = 0.0 

    def calcular(self, valor_carrinho: float, peso: float = 0.0, distancia_km: int = 0):
        if self.tipo_envio == "nacional":
            if valor_carrinho > 100.0:
                valor_frete = 0.0
            else:
                valor_frete = 15.0
            return valor_frete
        elif self.tipo_envio == "internacional":
            pass 
        else:
            raise ValueError("Tipo de envio desconhecido")

#APLICANDO YAGNI, KISS E SINE

def calcular_frete(valor_carrinho: float) -> float:

    # Criando constantes para deixar o codigo simples
    VALOR_FRETE_FIXO = 15.0
    LIMITE_FRETE_GRATIS = 100.0

    if valor_carrinho >= LIMITE_FRETE_GRATIS:
        return 0.0
        
    return VALOR_FRETE_FIXO
