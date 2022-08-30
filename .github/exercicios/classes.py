class Fracao:
    numerador = 1
    denomiandor = 1


    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def add(self, fracao):
        num = (self.numerador + fracao.denomiandor) + (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def solve(self):
      return self.numerador/self.denominador

    def __str__(self):
      return f"{self.numerador}/{self.denomiandor}"


fracao1 = Fracao(1,2)
fracao2 = Fracao(1,2)
fracao3 = fracao1.add(fracao2)
print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2.solve()}")
print(f"fracao3: {fracao2.solve()}")
print(fracao3.solve())
