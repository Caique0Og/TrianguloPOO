# Crie uma classe chamada Retângulo que represente um retângulo.
#  A classe deve possuir atributos para largura e altura, além de métodos para:

# Calcular a área do retângulo.
# Calcular o perímetro do retângulo.
# Redimensionar o retângulo, alterando sua largura e altura.
# Exibir as propriedades (largura e altura) do retângulo.

# Implemente a classe e teste suas funcionalidades instanciando objetos e chamando seus métodos.



class triangulo:
  def __init__(self):
    self.altura = 0
    self.largura = 0

  def area(self):
    return self.altura * self.largura

  def perimetro(self):
    return 2 * (self.altura + self.largura)

  def redimensionamentor(self, novaAltura, novaLargura):
    self.altura = novaAltura
    self.largura = novaLargura

  def exibir(self):
    print("os dimencionamentos atuais são:/n Altura: ", self.altura, "/n Largura: ", self.largura )


triangulo1 = triangulo()