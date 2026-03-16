Este repositório é onde coloco em execução boas práticas de código. O objetivo é treinar a escrita de códigos mais limpos, coesos e menos acoplados.

Cada arquivo/módulo deste projeto foca em refatorar um problema comum aplicando uma ou mais regras específicas de boas práticas. Abaixo está a descrição do que foi explorado em cada um deles.

Não usando FLOAT (FLOAT.py)
Tipos primitivos de ponto flutuante (float, double) sofrem de problemas de precisão, o que pode causar bugs graves, especialmente lidando com dinheiro.
Pratiquei a substituição de float para armazenar valores monetários em inteiros/centavos.

Lei de Demeter (LeiDeDemeter.py)
Problema de acoplamento causado por objetos que sabem demais sobre a estrutura interna de outros objetos.
O código foi refatorado para que os objetos apenas se comuniquem com seus amigos imediatos, delegando comportamentos em vez de expor estruturas internas.

Object Calisthenics - Leis 1 e 2 (ObjectCalRule1&2.py)
Regra 1 Apenas um nível de indentação por método de extração de métodos para melhorar a legibilidade e focar na responsabilidade única.
Regra 2. Uso de Early Return para eliminar fluxos condicionais complexos e aninhados.

Object Calisthenics - Lei 3 (ObjectCalRule3.py)
Regra 3 Envolva todos os primitivos e Strings.	 Criação de Value Objects (Objetos de Valor). Em vez de passar um simples string ou int que não tem significado de domínio, criei classes específicas como Email, CPF e Idade para garantir a validação e encapsular o comportamento logo na origem.

Object Calisthenics - Leis 8 e 9 (ObjectCalRule8&9.py)
Regra 8. Promoção de alta coesão desmontando classes Deus (God classes) em objetos menores e mais focados.
Regra 9. O foco passou a ser em pedir para o objeto fazer algo com seus próprios dados, em vez de arrancar os dados dele para manipulá-los em outro lugar.

YAGNI, KISS e SINE (YAGNI.py)
YAGNI - Remoção de códigos especulativos e funcionalidades feitas para o caso de precisarmos no futuro. Foco no requisito atual.
KISS - Refatoração de soluções exageradamente complexas para abordagens mais simples, diretas e fáceis de entender.
SOLID - Aplicação de princípios como Responsabilidade Única (SRP) e Inversão de Dependência (DIP) para deixar a arquitetura mais flexível.