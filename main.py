class CalculadoraMCD:
    def calcular_mcd(self, a, b):
        """
        Calcula el máximo común divisor (MCD) de dos números enteros.

        Argumentos:
        a -- Primer número entero
        b -- Segundo número entero

        Retorna:
        El máximo común divisor de a y b
        """
        while b != 0:
            a, b = b, a % b
        return a

    def calcular_mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo (mcm) de dos números enteros.

        Argumentos:
        a -- Primer número entero
        b -- Segundo número entero

        Retorna:
        El mínimo común múltiplo de a y b
        """
        return abs(a * b) // self.calcular_mcd(a, b)


# Ejemplo de uso:
calculadora = CalculadoraMCD()
num1 = 48
num2 = 18
print(f"El MCD de {num1} y {num2} es: {calculadora.calcular_mcd(num1, num2)}")
print(f"El mcm de {num1} y {num2} es: {calculadora.calcular_mcm(num1, num2)}")
