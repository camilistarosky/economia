#SELEÇÃO

import controller

def main():

    print("Bem-vindo a cálculadora de economia!")
    print("Selecione a matéria desejada:")
    print("1 - Matemática Financeira")
    print("2 - Introdução à Estatística")
    print("3 - Introdução à Macroeconomia")
    
    opcao = input("Digite o número da matéria desejada: ")
    
    match opcao:
        case "1":
            print("")
            print("----------------------------------------")
            print("Você selecionou Matemática Financeira.")
            print("Selecione o tópico desejado:")
            print("1 - Juros Compostos")
            print("2 - Rendas (Anuidades ou Pagamentos Periódicos")
            print("3 - Descontos")
            print("4 - Amortização de Empréstimos")
    
            opcaoMF = input("Digite o número do tópico desejado: ")
            print("")
            print("----------------------------------------")
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
                    print("")
                    print("----------------------------------------")
    
                    match opcaoJC:
                        case "1":
                            print("Você selecionou Montante.")
                            print("Digite os valores:")
                            P = float(input("Capital inicial: "))
                            i = float(input("Taxa por período: ")) / 100
                            n = float(input("Número de períodos: "))
                            resultado = controller.calcular_montante(P, i, n)
                            print(f"O montante é: {resultado:.2f}")
    
                        case "2":
                            print("Você selecionou Capital inicial.")
                            print("Digite os valores:")
                            M = float(input("Montante: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.calcular_capital(M, i, n)
                            print(f"O capital inicial é: {resultado:.2f}")
    
                        case "3":
                            print("Você selecionou Taxa por período.")
                            print("Digite os valores:")
                            M = float(input("Montante: "))
                            P = float(input("Capital inicial: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.calcular_taxa(P, M, n)
                            print(f"A taxa por período é: {resultado:.2f}")
    
                        case "4":
                            print("Você selecionou Número de períodos.")
                            print("Digite os valores:")
                            M = float(input("Montante: "))
                            P = float(input("Capital inicial: "))
                            i = float(input("Taxa por período: "))
                            resultado = controller.calcular_num_periodos(P, M, i)
                            print(f"O número de períodos é: {resultado:.2f}")
    
                        case "*":
                            pass
    
                case "2":
                    print(
                        "Você selecionou Rendas (Anuidades ou Pagamentos Periódicos)."
                    )
                    print("O que você deseja descobrir?")
                    print("1 - Valor presente de uma anuidade")
                    print("2 - Valor futuro de uma anuidade")
                    print("3 - Valor presente de um pagamento único")
                    print("4 - Valor futuro de um pagamento único")
                    print(" * - sair")
                    opcaoRP = input("Digite o número da opção desejada: ")
                    print("----------------------------------------")
    
                    match opcaoRP:
                        case "1":
                            print(
                                "Você selecionou Valor presente de uma anuidade.")
                            print("Digite os valores:")
                            P = float(input("Valor da anuidade: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.valor_presente_anuidade(P, i, n)
                            print(f"O valor presente da anuidade é: {resultado:.2f}")
    
                        case "2":
                            print("Você selecionou Valor futuro de uma anuidade.")
                            print("Digite os valores:")
                            P = float(input("Valor da anuidade: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.valor_futuro_anuidade(P, i, n)
                            print(f"O valor futuro da anuidade é: {resultado:.2f}")
    
                        case "3":
                            print(
                                "Você selecionou Valor presente de um pagamento único."
                            )
                            print("Digite os valores:")
                            P = float(input("Valor do pagamento único: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.valor_presente_pagamento_unico(P, i, n)
                            print(f"O valor presente do pagamento único é: {resultado:.2f}")
    
                        case "4":
                            print(
                                "Você selecionou Valor futuro de um pagamento único."
                            )
                            print("Digite os valores:")
                            P = float(input("Valor do pagamento único: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.valor_futuro_pagamento_unico(P, i, n)
                            print(f"O valor futuro do pagamento único é: {resultado:.2f}")
    
                        case "*":
                            pass
    
                case "3":
                    print("Você selecionou Descontos.")
                    print("O que você deseja descobrir?")
                    print("1 - Valor presente de um desconto")
                    print("2 - Valor futuro de um desconto")
                    print("3 - Valor presente de um desconto racional")
                    print("4 - Valor futuro de um desconto racional")
                    print(" * - sair")
                    opcaoD = input("Digite o número da opção desejada: ")
                    print("----------------------------------------")
    
                    match opcaoD:
                        case "1":
                            print("Você selecionou Valor presente de um desconto.")
                            print("Digite os valores:")
                            P = float(input("Valor do desconto: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.desconto_simples(P, i, n)
                            print(f"O valor presente do desconto é: {resultado:.2f}")
    
                        case "2":
                            print("Você selecionou Valor futuro de um desconto.")
                            print("Digite os valores:")
                            P = float(input("Valor do desconto: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.desconto_composto(P, i, n)
                            print(f"O valor futuro do desconto é: {resultado:.2f}")

                        case "3":
                            print(
                                "Você selecionou Valor presente de um desconto racional."
                            )
                            print("Digite os valores:")
                            P = float(input("Valor do desconto: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.desconto_racional(P, i, n)
                            print(f"O valor presente do desconto racional é: {resultado:.2f}")

                        case "4":
                            print(
                                "Você selecionou Valor futuro de um desconto racional."
                            )
                            print("Digite os valores:")
                            P = float(input("Valor do desconto: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.desconto_racional_futuro(P, i, n)
    
                        case "*":
                            pass
    
                case "4":
                    print("Você selecionou Amortização de Empréstimos.")
                    print("O que você deseja descobrir?")
                    print("1 - Valor da prestação")
                    print("2 - Valor do saldo devedor")
                    print("3 - Valor dos juros da parcela")
                    print(" * - sair")
                    opcaoAE = input("Digite o número da opção desejada: ")
                    match opcaoAE:
                        case "1":
                            print("Você selecionou Valor da prestação.")
                            print("Digite os valores:")
                            P = float(input("Valor do empréstimo: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.calcular_parcela_amortizacao(P, i, n)
                            print(f"O valor da prestação é: {resultado:.2f}")

                        case "2":
                            print("Você selecionou Valor do saldo devedor.")
                            print("Digite os valores:")
                            P = float(input("Valor do empréstimo: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            k = float(input("Número da parcela: "))
                            resultado = controller.calcular_saldo_devedor(P, i, n, k)
                            print(f"O valor do saldo devedor é: {resultado:.2f}")

                        case "3":
                            print("Você selecionou Valor dos juros da parcela.")
                            print("Digite os valores:")
                            P = float(input("Valor do empréstimo: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            k = float(input("Número da parcela: "))
                            resultado = controller.calcular_juros_parcela(P, i, n, k)
                            print(f"O valor dos juros da parcela é: {resultado:.2f}")
    
                        case "*":
                            pass
    
        case "2":
            print("Você selecionou Introdução à Estatística.")
    

if __name__ == "__main__":
    main()