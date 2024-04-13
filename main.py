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


# Ejemplo de uso:
calculadora = CalculadoraMCD()
num1 = 48
num2 = 18
print(f"El MCD de {num1} y {num2} es: {calculadora.calcular_mcd(num1, num2)}")
