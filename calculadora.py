class Calculadora:
    #variáveis
    __area_paredes: float
    __area_teto: float

    #método onde vai receber a area da parede
    def calcular_area_paredes(self, comodo):
        self.__area_paredes = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_paredes

    #método onde vai receber a area do teto
    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto

    #método onde vai trazer o resultado
    def calcular_litragem_necessaria(self):
       return (self.__area_paredes + self.__area_teto) / 10