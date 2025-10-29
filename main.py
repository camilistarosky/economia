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
            print("1 - Juros Compostos")
            print("2 - Rendas / Anuidades (Simples, Antecipada, com Entrada)")
            print("3 - Descontos (Simples e Compostos, Comercial e Racional)")
            print("4 - Amortização de Empréstimos (Sistema PRICE)")
            print("5 - Conversões e Equivalências de Taxas")
            print("6 - Série de Fibonacci Financeira")
            print("7 - Estimativa de Valor de Imóvel")
            print("8 -  Título de Dívida e Cálculo de Desconto")
            print("9 - Transformações de Taxas Nominal e Efetiva")
    
            opcaoMF = input("Digite o número do tópico desejado: ")
            print("")
            print("----------------------------------------")
            match opcaoMF:
                case "1":
                    print("Você selecionou Juros Compostos.")
                    print("O que você deseja descobrir?")
                    print("1 - Valor futuro (FV)")
                    print("2 - Valor presente (PV)")
                    print("3 - Taxa por período")
                    print("4 - Número de períodos")
                    print(" * - sair")
                    opcaoJC = input("Digite o número da opção desejada: ")
                    print("")
                    print("----------------------------------------")
    
                    match opcaoJC:
                        case "1":
                            print("Você selecionou Valor futuro (FV).")
                            print("Digite os valores:")
                            PV = float(input("Valor presente (PV): "))
                            i = float(input("Taxa por período: ")) / 100
                            n = float(input("Número de períodos: "))
                            resultado = controller.juros_compostos(PV=PV, i=i, n=n)
                            print(f"O Valor futuro (FV) é: {resultado['FV']:.2f}")
    
                        case "2":
                            print("Você selecionou Valor presente (PV).")
                            print("Digite os valores:")
                            FV = float(input("Valor futuro (FV): "))
                            i = float(input("Taxa por período: ")) / 100
                            n = float(input("Número de períodos: "))
                            resultado = controller.juros_compostos(FV=FV, i=i, n=n)
                            print(f"O Valor presente (PV) é: {resultado['PV']:.2f}")
    
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
                            i = float(input("Taxa por período: ")) / 100
                            resultado = controller.calcular_num_periodos(P, M, i)
                            print(f"O número de períodos é: {resultado:.2f}")
    
                        case "*":
                            pass
    
                case "2":
                    print(
                        "Você selecionou Rendas (Anuidades ou Pagamentos Periódicos)."
                    )
                    print("O que voce deseja calcular: ")
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
                case "5":
                    pass
                    
                case "6":
                    pass

                case "7":
                    pass
    

if __name__ == "__main__":
    main()