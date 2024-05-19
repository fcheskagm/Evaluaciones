class Conversiones:
    def __init__(self):        
        self.decimal = 0
        self.binario = ""
        self.terciario = ""
        self.cuaternario = ""
        self.octal = ""
        self.hexadecimal = ""
        self.lista = ["Decimal","Binario","Terciario","Cuaternario","Octal","Hexadecimal"]

    def get_decimal(self):
        return self.decimal
    def set_decimal(self, decimal=0):
        self.decimal = int(decimal)

    def get_binario(self):
        return self.binario
    def set_binario(self, binario=""):
        self.binario = binario

    def get_terciario(self):
        return self.terciario
    def set_terciario(self, terciario=""):
        self.terciario = terciario

    def get_cuaternario(self):
        return self.cuaternario
    def set_cuaternario(self, cuaternario=""):
        self.cuaternario = cuaternario

    def get_octal(self):
        return self.octal
    def set_octal(self, octal=""):
        self.octal = octal

    def get_hexadecimal(self):
        return self.hexadecimal
    def set_hexadecimal(self, hexadecimal=""):
        self.hexadecimal = hexadecimal
            
    def todas_conversiones(self,value1,value2):
        if value1 == "Binario" and value2 == "Decimal":
            resultado_decimal = int(self.binario, 2)
            self.decimal = resultado_decimal

        elif value1 == "Decimal" and value2 == "Binario":
            if self.decimal == 0:
                self.binario = "0"
            resultado_binario = ""
            self.decimal = int(self.decimal)
            while self.decimal > 0:
                residuo = self.decimal % 2
                resultado_binario = str(residuo) + resultado_binario
                self.decimal //= 2
            self.binario = resultado_binario

        elif value1 == "Decimal" and value2 == "Terciario":
            res_terciario = ""
            while self.decimal > 0:
                resto = self.decimal % 3
                res_terciario = str(resto) + res_terciario
                self.decimal //= 3
            self.terciario = res_terciario
        
        elif value1 == "Terciario" and value2 == "Decimal":
            res_decimal = 0
            for i, digito in enumerate(reversed(self.terciario)):
                res_decimal += int(digito) * (3 ** i)
            self.decimal = res_decimal

        elif value1 == "Decimal" and value2 == "Cuaternario":
            res_cuaternario = ""
            while self.decimal > 0:
                resto = self.decimal % 4
                res_cuaternario = str(resto) + res_cuaternario
                self.decimal //= 4
            self.cuaternario = res_cuaternario

        elif value1 == "Cuaternario" and value2 == "Decimal":
            res_decimal = 0
            for i, digito in enumerate(reversed(self.cuaternario)):
                res_decimal += int(digito) * (4 ** i)
            self.decimal = res_decimal

        elif value1 == "Decimal" and value2 == "Octal":
            res_octal = ""
            while self.decimal > 0:
                residuo = self.decimal % 8
                res_octal = str(residuo) + res_octal
                self.decimal //= 8
            self.octal = res_octal

        elif value1 == "Octal" and value2 == "Decimal":
            base = 1
            res_decimal = 0
            for digito in reversed(self.octal):
                res_decimal += int(digito) * base
                base *= 8
            self.decimal = res_decimal
        
        elif value1 == "Decimal" and value2 == "Hexadecimal":
            res_hexadecimal = ""
            while self.decimal > 0:
                residuo = self.decimal % 16
                if residuo < 10:
                    res_hexadecimal = str(residuo) + res_hexadecimal
                else:
                    res_hexadecimal = chr(ord('A') + residuo - 10) + res_hexadecimal
                self.decimal //= 16
            self.hexadecimal = res_hexadecimal

        elif value1 == "Hexadecimal" and value2 == "Decimal":
            res_decimal = 0
            base = 1
            for digito in reversed(self.hexadecimal):
                if digito.isdigit():
                    res_decimal += int(digito) * base
                else:
                    res_decimal += (ord(digito.upper()) - ord('A') + 10) * base
                base *= 16
            self.decimal = res_decimal

        elif value1 == "Hexadecimal" and value2 == "Binario":
            self.todas_conversiones("Hexadecimal","Decimal")
            self.todas_conversiones("Decimal", "Binario")

        elif value1 == "Binario" and value2 == "Hexadecimal":
            self.todas_conversiones("Binario","Decimal")
            self.todas_conversiones("Decimal", "Hexadecimal")    

        elif value1 == "Binario" and value2 == "Terciario":
            self.todas_conversiones("Binario", "Decimal")
            self.todas_conversiones("Decimal", "Terciario")

        elif value1 == "Terciario" and value2 == "Binario":
            self.todas_conversiones("Terciario", "Decimal")
            self.todas_conversiones("Decimal", "Binario")

        elif value1 == "Binario" and value2 == "Cuaternario":
            self.todas_conversiones("Binario", "Decimal")
            self.todas_conversiones("Decimal", "Cuaternario")

        elif value1 == "Cuaternario" and value2 == "Binario":
            self.todas_conversiones("Cuaternario", "Decimal")
            self.todas_conversiones("Decimal", "Binario")

        elif value1 == "Binario" and value2 == "Octal":
            self.todas_conversiones("Binario", "Decimal")
            self.todas_conversiones("Decimal", "Octal")    

        elif value1 == "Octal" and value2 == "Binario":
            self.todas_conversiones("Octal", "Decimal")
            self.todas_conversiones("Decimal", "Binario")    

        elif value1 == "Cuaternario" and value2 == "Terciario":
            self.todas_conversiones("Cuaternario", "Decimal")
            self.todas_conversiones("Decimal", "Terciario")

        elif value1 == "Terciario" and value2 == "Cuaternario":
            self.todas_conversiones("Terciario", "Decimal")
            self.todas_conversiones("Decimal", "Cuaternario")

        elif value1 == "Octal" and value2 == "Terciario":
            self.todas_conversiones("Octal", "Decimal")
            self.todas_conversiones("Decimal", "Terciario")

        elif value1 == "Terciario" and value2 == "Octal":
            self.todas_conversiones("Terciario", "Decimal")
            self.todas_conversiones("Decimal", "Octal")

        elif value1 == "Hexadecimal" and value2 == "Terciario":
            self.todas_conversiones("Hexadecimal","Decimal")
            self.todas_conversiones("Decimal", "Terciario")

        elif value1 == "Terciario" and value2 == "Hexadecimal":
            self.todas_conversiones("Terciario", "Decimal")
            self.todas_conversiones("Decimal", "Hexadecimal")

        elif value1 == "Cuaternario" and value2 == "Octal":
            self.todas_conversiones("Cuaternario", "Decimal")
            self.todas_conversiones("Decimal", "Octal")

        elif value1 == "Octal" and value2 == "Cuaternario":
            self.todas_conversiones("Octal", "Decimal")
            self.todas_conversiones("Decimal", "Cuaternario")

        elif value1 == "Hexadecimal" and value2 == "Cuaternario":
            self.todas_conversiones("Hexadecimal","Decimal")
            self.todas_conversiones("Decimal", "Cuaternario")

        elif value1 == "Cuaternario" and value2 == "Hexadecimal":
            self.todas_conversiones("Cuaternario", "Decimal")
            self.todas_conversiones("Decimal", "Hexadecimal")

        elif value1 == "Hexadecimal" and value2 == "Octal":
            self.todas_conversiones("Hexadecimal","Decimal")
            self.todas_conversiones("Decimal", "Octal")

        elif value1 == "Octal" and value2 == "Hexadecimal":
            self.todas_conversiones("Octal", "Decimal")
            self.todas_conversiones("Decimal", "Hexadecimal")

        elif value1 == value2:
            None 
                    