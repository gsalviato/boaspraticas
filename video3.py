#VIOLANDO REGRAS 
class Catraca:
    
    def tentar_entrar(self, idade: int, tem_ingresso: bool):
        # Nível 1 de indentação
        if tem_ingresso:
            # Nível 2 de indentação
            if idade >= 18:
                print("Acesso Liberado! Boa festa.")
            else: # Uso do ELSE 
                print("Acesso Negado: Você é menor de idade.")
        else: # Uso do ELSE 
            print("Acesso Negado: Você não tem ingresso.")
# Aplicando as regras 
class Catraca:
    
    def tentar_entrar(self, idade: int, tem_ingresso: bool):
        
        if not tem_ingresso:
            print("Acesso Negado: Você não tem ingresso.")
            return # Sai da função aqui     

        if idade < 18:
            print("Acesso Negado: Você é menor de idade.")
            return # Sai da função aqui

        print("Acesso Liberado! Boa festa.")