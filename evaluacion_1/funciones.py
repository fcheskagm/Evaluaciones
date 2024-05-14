class Conversiones:
    def __init__(self, valor):
        
        if isinstance(valor, int):
            self.decimal = valor
            self.binario = ""
        elif isinstance(valor, str):
            self.decimal = 0
            self.binario = valor
            
    def decimal_binario(self):
        if self.binario == "":
            if self.decimal == 0:
                return "0"

            resultado_binario = ""
            self.decimal = int(self.decimal)
            while self.decimal > 0:
                residuo = self.decimal % 2
                resultado_binario = str(residuo) + resultado_binario
                self.decimal //= 2
            return resultado_binario
        
        elif self.decimal == 0:
            resultado_decimal = int(self.binario, 2)
            return resultado_decimal

    def decimal_terciario(self):
        
        if self.decimal == 0:
            terciario = ""
            while decimal > 0:
                resto = decimal % 3
                terciario = str(resto) + terciario
                decimal //= 3

            return terciario
        else:
            decimal = 0
            for i, digito in enumerate(reversed(terciario)):
                decimal += int(digito) * (3 ** i)

            return decimal

    def decimal_cuaternario(self):
        
        if self.decimal == 0:
            cuaternario = ""
            while decimal > 0:
                resto = decimal % 4
                cuaternario = str(resto) + cuaternario
                decimal //= 4

            return cuaternario
        else:
            decimal = 0
            for i, digito in enumerate(reversed(cuaternario)):
                decimal += int(digito) * (4 ** i)

            return decimal

    def decimal_octal(self):
        
        if self.decimal == 0:
            octal = ""
            while decimal > 0:
                residuo = decimal % 8
                octal = str(residuo) + octal
                decimal //= 8

            return octal
        else:
            base = 1
            for digito in reversed(octal):
                decimal += int(digito) * base
                base *= 8

            return decimal
        
    def decimal_hexadecimal(self):

        if self.decimal == 0:
            hexadecimal = ""
            while decimal > 0:
                residuo = decimal % 16
                if residuo < 10:
                    hexadecimal = str(residuo) + hexadecimal
                else:
                    hexadecimal = chr(ord('A') + residuo - 10) + hexadecimal
                decimal //= 16

            return hexadecimal
        else:
            decimal = 0
            base = 1
            for digito in reversed(hexadecimal):
                if digito.isdigit():
                    decimal += int(digito) * base
                else:
                    decimal += (ord(digito.upper()) - ord('A') + 10) * base
                base *= 16

            return decimal




n = Conversiones("10100")
binario = n.decimal_binario()
print(binario)
