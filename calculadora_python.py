
Calculadora utilizando Classe e Médotos


# Criando  Classe Caluculadora 
class Calculadora:
    # Recebe 2 parâmetros 
    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    # Método de soma
    def add(self):
        return self.first + self.second
    
    # Método de Subtração
    def subtract(self):
        return self.first - self.second
    
    # Método de Multiplicação
    def multiply(self):
        return self.first * self.second
    
    # Método de Divisão
    def divide(self):
        return self.first / self.second


# Criação do menu de escolha do tipo de operação
print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Variáveis 
escolha = input("\nDigite sua opção (1/2/3/4): ")

var1 = int(input("\nDigite o primeiro número: "))
var2 = int(input("\nDigite o segundo número: "))

# Criando o objeto Calculadore e passando as duas variáveis 
calc = Calculadora(var1,var2)



# IFs para a verificação da escolha de operação 

# Operação de Soma
if escolha == '1':
    print("O resultado da Soma é : " ,calc.add())
    
# Operação de Subtração
elif escolha == '2':
    print("O resultado da Subtração é : ", calc.subtract())
    
# Operação de Multiplicação    
elif escolha == '3':
    print("O resultado da Multiplicação é : ", calc.multiply())
    
# Operação de Divisão       
elif escolha == '4':
    if(var2 == 0):
        print('!!!erro divisão por zero!!!')
        var3 = int(input("\nDigite o segundo número diferente de zero: "))
        calc2 = Calculadora(var1,var3)
        print("\nO resultado da Divisão é : ", calc2.divide())
    else:      
        print("O resultado da Divisão é : " ,calc.divide())
else:
    print("\nOpção Inválida!")