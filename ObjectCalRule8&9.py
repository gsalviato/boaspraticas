#VIOLANDO REGRA 8 e 9 
class Carro:
    #Desrespeitando a regra 8, com 3 variaves de instancia
    def __init__(self, marca: str, modelo: str, velocidade_atual: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    # Criando getters e setters. 
    def get_velocidade(self) -> int:
        return self.velocidade_atual

    def set_velocidade(self, nova_velocidade: int):
        self.velocidade_atual = nova_velocidade

#APLICANDO AS REGRAS 8 e 9

#Criando uma classe para agrupar informacoes, respeitando a regra 8
class FichaTecnica:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

class Carro:
    def __init__(self, ficha: FichaTecnica, velocidade_inicial: int):
        self.ficha = ficha
        self.velocidade_atual = velocidade_inicial


    def acelerar(self, incremento: int):
        self.velocidade_atual += incremento

    # Ao inves de getter, um metodo que mostra o painel, respeitando a regra 9
    def mostrar_painel(self):
        print(f"Velocidade: {self.velocidade_atual} km/h")