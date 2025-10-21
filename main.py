#SELEÇÃO

from typing import Match
from math import log


print("Bem-vindo a cálculadora da economia!")
print("Selecione a matéria desejada:")
print("1 - Matemática Financeira")
print("2 - Introdução à Estatística")
print("3 - Introdução à Macroeconomia")

opcao = input("Digite o número da matéria desejada: ")

match opcao:
    case "1":
       print("Você selecionou Matemática Financeira.")
       print("Selecione o tópico desejado:")
       print("1 - Juros Compostos")
       print("2 - Rendas (Anuidades ou Pagamentos Periódicos")
       print("3 - Descontos")
       print("4 - Amortização de Empréstimos")

       opcaoMF = input("Digite o número do tópico desejado: ")
       match opcaoMF:
            case "1":
                print("Você selecionou Juros Compostos.")
                print("O que você deseja descobrir?")
                print("1 - Montante")
                print("2 - Capital inicial")
                print("3 - Taxa por período")
                print("4 - Número de períodos")
                print(" * - sair")
                opcaoJC = input("Digite o número da opção desejada: ")

                match opcaoJC:
                    case "1":
                        print("Você selecionou Montante.")
                        print("Digite os valores:")
                        P = float(input("Capital inicial: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P * (1 + i) ** n
                        print("O montante é: ", resultado)
                        
                      
                    case "2":
                        print("Você selecionou Capital inicial.")
                        print("Digite os valores:")
                        M = float(input("Montante: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = M / (1 + i) ** n
                        print("O capital inicial é: ", resultado)
                        
                      
                    case "3":
                        print("Você selecionou Taxa por período.")
                        print("Digite os valores:")
                        M = float(input("Montante: "))
                        P = float(input("Capital inicial: "))
                        n = float(input("Número de períodos: "))
                        resultado = (M / P) ** (1 / n) - 1
                        print("A taxa por período é: ", resultado)
                        

                    case "4":
                        print("Você selecionou Número de períodos.")
                        print("Digite os valores:")
                        M = float(input("Montante: "))
                        P = float(input("Capital inicial: "))
                        i = float(input("Taxa por período: "))
                        resultado = log(M / P) / log(1 + i)
                        print("O número de períodos é: ", resultado)
                        
                    case "*":
                        pass

            case "2":
                print("Você selecionou Rendas (Anuidades ou Pagamentos Periódicos).")
                print("O que você deseja descobrir?")
                print("1 - Valor presente de uma anuidade")
                print("2 - Valor futuro de uma anuidade")
                print("3 - Valor presente de um pagamento único")
                print("4 - Valor futuro de um pagamento único")
                print(" * - sair")
                opcaoRP = input("Digite o número da opção desejada: ")
              
                match opcaoRP:
                    case "1":
                        print("Você selecionou Valor presente de uma anuidade.")
                        print("Digite os valores:")
                        P = float(input("Valor da anuidade: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P * ((1 - (1 + i) ** -n) / i)
                        print("O valor presente da anuidade é: ", resultado)
                        

                    case "2":
                        print("Você selecionou Valor futuro de uma anuidade.")
                        print("Digite os valores:")
                        P = float(input("Valor da anuidade: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P * ((1 - (1 + i) ** n) / i)
                        print("O valor futuro da anuidade é: ", resultado)
                        

                    case "3":
                        print("Você selecionou Valor presente de um pagamento único.")
                        print("Digite os valores:")
                        P = float(input("Valor do pagamento único: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P / (1 + i) ** n
                        print("O valor presente do pagamento único é: ", resultado)
                        

                    case "4":
                        print("Você selecionou Valor futuro de um pagamento único.")
                        print("Digite os valores:")
                        P = float(input("Valor do pagamento único: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P * (1 + i) ** n
                        print("O valor futuro do pagamento único é: ", resultado)
                        
                      
                    case "*": 
                        pass

            case "3":
                print("Você selecionou Descontos.")
                print("O que você deseja descobrir?")
                print("1 - Valor presente de um desconto")
                print("2 - Valor futuro de um desconto")
                print(" * - sair")
                opcaoD = input("Digite o número da opção desejada: ")
                match opcaoD:
                    case "1":
                        print("Você selecionou Valor presente de um desconto.")
                        print("Digite os valores:")
                        P = float(input("Valor do desconto: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P / (1 - i) ** n
                        print("O valor presente do desconto é: ", resultado)
                        

                    case "2":
                        print("Você selecionou Valor futuro de um desconto.")
                        print("Digite os valores:")
                        P = float(input("Valor do desconto: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P * (1 - i) ** n
                        print("O valor futuro do desconto é: ", resultado)
                        

                    case "*":
                        pass
                    

            case "4":
                print("Você selecionou Amortização de Empréstimos.")
                print("O que você deseja descobrir?")
                print("1 - Valor da prestação")
                print("2 - Valor do saldo devedor")
                print(" * - sair")
                opcaoAE = input("Digite o número da opção desejada: ")
                match opcaoAE:
                    case "1":
                        print("Você selecionou Valor da prestação.")
                        print("Digite os valores:")
                        P = float(input("Valor do empréstimo: "))
                        i = float(input("Taxa por período: "))
                        n = float(input("Número de períodos: "))
                        resultado = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
                        print("O valor da prestação é: ", resultado)

                    case "*":
                        pass
                    
                      

    case "2":
        print("Você selecionou Introdução à Estatística.")