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
                            FV = float(input("Valor futuro (FV): "))
                            PV = float(input("Valor presente (PV): "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.juros_compostos(FV=FV, PV=PV, n=n)
                            print(f"A taxa por período é: {resultado['i']:.2f}")
    
                        case "4":
                            print("Você selecionou Número de períodos.")
                            print("Digite os valores:")
                            FV = float(input("Valor futuro (FV): "))
                            PV = float(input("Valor presente (PV): "))
                            i = float(input("Taxa por período: ")) / 100
                            resultado = controller.juros_compostos(FV=FV, PV=PV, i=i)
                            print(f"O número de períodos é: {resultado['n']:.2f}")
    
                        case "*":
                            pass
    
                case "2":
                    print(
                        "Você selecionou Rendas (Anuidades ou Pagamentos Periódicos)."
                    )
                    print("O que você deseja calcular: ")
                    print("1 - Renda postecipada (pagamento no final de cada período)")
                    print("2 - Renda antecipada (primeiro pagamento imediato)")
                    print(" * - sair")
                    opcaoRP = input("Digite o número da opção desejada: ")
                    print("----------------------------------------")

                    match opcaoRP:
                        case "1":  # Renda postecipada
                            print("Você selecionou Renda postecipada.")
                            print("O que você deseja descobrir?")
                            print("1 - Valor futuro (FV)")
                            print("2 - Valor presente (PV)")
                            print("3 - Pagamento (PMT)")
                            print("4 - Número de períodos (n)")
                            print(" * - sair")
                            opcaoPost = input("Digite o número da opção desejada: ")
                            print("")
                            print("----------------------------------------")
    
                            match opcaoPost:
                                case "1":  # Calcular FV (precisa PMT, i, n)
                                    print("Você selecionou Valor futuro (FV).")
                                    print("Digite os valores:")
                                    PMT = float(input("Pagamento (PMT): "))
                                    i = float(input("Taxa por período: ")) / 100
                                    n = float(input("Número de períodos: "))
                                    resultado = controller.renda_postecipada(PMT=PMT, i=i, n=n)
                                    print(f"O Valor futuro (FV) é: {resultado['FV']:.2f}")
                                    print(f"O Valor presente (PV) é: {resultado['PV']:.2f}")  # Calcula ambos, como explicado
    
                                case "2":  # Calcular PV (precisa PMT, i, n)
                                    print("Você selecionou Valor presente (PV).")
                                    print("Digite os valores:")
                                    PMT = float(input("Pagamento (PMT): "))
                                    i = float(input("Taxa por período: ")) / 100
                                    n = float(input("Número de períodos: "))
                                    resultado = controller.renda_postecipada(PMT=PMT, i=i, n=n)
                                    print(f"O Valor presente (PV) é: {resultado['PV']:.2f}")
                                    print(f"O Valor futuro (FV) é: {resultado['FV']:.2f}")  # Calcula ambos
    
                                case "3":  # Calcular PMT (pode ser com FV ou PV, i, n)
                                    print("Você selecionou Pagamento (PMT).")
                                    print("Escolha a base:")
                                    print("1 - Com Valor futuro (FV)")
                                    print("2 - Com Valor presente (PV)")
                                    base = input("Digite 1 ou 2: ")
                                    if base == "1":
                                        FV = float(input("Valor futuro (FV): "))
                                        i = float(input("Taxa por período: ")) / 100
                                        n = float(input("Número de períodos: "))
                                        resultado = controller.renda_postecipada(FV=FV, i=i, n=n)
                                        print(f"O Pagamento (PMT) é: {resultado['PMT']:.2f}")
                                        print(f"O Valor presente (PV) é: {resultado['PV']:.2f}")
                                    elif base == "2":
                                        PV = float(input("Valor presente (PV): "))
                                        i = float(input("Taxa por período: ")) / 100
                                        n = float(input("Número de períodos: "))
                                        resultado = controller.renda_postecipada(PV=PV, i=i, n=n)
                                        print(f"O Pagamento (PMT) é: {resultado['PMT']:.2f}")
                                        print(f"O Valor futuro (FV) é: {resultado['FV']:.2f}")
    
                                case "4":  # Calcular n (pode ser com PMT, FV, i ou PMT, PV, i)
                                    print("Você selecionou Número de períodos (n).")
                                    print("Escolha a base:")
                                    print("1 - Com Valor futuro (FV)")
                                    print("2 - Com Valor presente (PV)")
                                    base = input("Digite 1 ou 2: ")
                                    if base == "1":
                                        PMT = float(input("Pagamento (PMT): "))
                                        FV = float(input("Valor futuro (FV): "))
                                        i = float(input("Taxa por período: ")) / 100
                                        resultado = controller.renda_postecipada(PMT=PMT, FV=FV, i=i)
                                        print(f"O Número de períodos (n) é: {resultado['n']:.2f}")
                                    elif base == "2":
                                        PMT = float(input("Pagamento (PMT): "))
                                        PV = float(input("Valor presente (PV): "))
                                        i = float(input("Taxa por período: ")) / 100
                                        resultado = controller.renda_postecipada(PMT=PMT, PV=PV, i=i)
                                        print(f"O Número de períodos (n) é: {resultado['n']:.2f}")
    
                                case "*":
                                    pass
    
                        case "2":  # Renda antecipada
                            print("Você selecionou Renda antecipada.")
                            print("O que você deseja descobrir?")
                            print("1 - Valor presente (PV)")
                            print("2 - Pagamento (PMT)")
                            print(" * - sair")
                            opcaoAnt = input("Digite o número da opção desejada: ")
                            print("")
                            print("----------------------------------------")
    
                            match opcaoAnt:
                                case "1":  # Calcular PV (precisa PMT, i, n)
                                    print("Você selecionou Valor presente (PV).")
                                    print("Digite os valores:")
                                    PMT = float(input("Pagamento (PMT): "))
                                    i = float(input("Taxa por período: ")) / 100
                                    n = float(input("Número de períodos: "))
                                    resultado = controller.renda_antecipada(PMT=PMT, i=i, n=n)
                                    print(f"O Valor presente (PV) é: {resultado['PV']:.2f}")
    
                                case "2":  # Calcular PMT (precisa PV, i, n)
                                    print("Você selecionou Pagamento (PMT).")
                                    print("Digite os valores:")
                                    PV = float(input("Valor presente (PV): "))
                                    i = float(input("Taxa por período: ")) / 100
                                    n = float(input("Número de períodos: "))
                                    resultado = controller.renda_antecipada(PV=PV, i=i, n=n)
                                    print(f"O Pagamento (PMT) é: {resultado['PMT']:.2f}")
    
                                case "*":
                                    pass
    
                        case "*":
                            pass

                case "3": # FALTA AJUSTAR
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
                    print("1 - PMT")
                    print("2 - Valor presente (PV)")
                    print("3 - número de períodos (n)")
                    print("4 - taxa de juros (i)")
                    print(" * - sair")
                    opcaoAE = input("Digite o número da opção desejada: ")
                    match opcaoAE:
                        case "1":
                            print("Você selecionou PMT.")
                            print("Digite os valores:")
                            PV = float(input("Valor presente (PV): "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.amortizacao_price(PV=PV, i=i, n=n)
                            print(f"O valor da prestação é: {resultado:.2f}")

                        case "2":
                            print("Você selecionou Valor presente (PV).")
                            print("Digite os valores:")
                            FV = float(input("PMT: "))
                            i = float(input("Taxa por período: "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.amortizacao_price(FV=FV, i=i, n=n)
                            print(f"O Valor presente (PV) é: {resultado:.2f}")

                        case "3":
                            print("Você selecionou número de períodos.")
                            print("Digite os valores:")
                            PMT = float(input("Valor PMT: "))
                            PV = float(input("Valor presente (PV): "))
                            i = float(input("taxa de juros: "))
                            resultado = controller.amortizacao_price(PMT=PMT, PV=PV, i=i)
                            print(f"O número de parcelas é: {resultado:.2f}")

                        case "4":
                            print("Você selecionou a taxa de juros")
                            print("Digite os valores:")
                            PMT = float(input("Valor PMT: "))
                            PV = float(input("Valor presente (PV): "))
                            n = float(input("Número de períodos: "))
                            resultado = controller.amortizacao_price(PMT=PMT, PV=PV, n=n)
                            print(f"A taxa de juros é: {resultado:.2f}")
                        
                        case "*":
                            pass
                case "5":
                    print("Você selecionou Conversões e Equivalências de Taxas.")
                    print("O que você deseja descobrir?")
                    print("1 - Taxa nominal para efetiva")
                    print("2 - Taxa efetiva para nominal")
                    print("3 - Equivalência de taxas")
                    print("TAXAS ANUAIS"------------)
                    print("4 - Taxa anual para mensal")
                    print("5 - Taxa anual para trimestral")
                    print("6 - Tava anual para semestral")
                    print("7 - Tava anual para diária")
                    print("TAXAS SEMESTRAIS----------")
                    print("8 - Taxa semestral para anual")
                    print("9 - Taxa semestral para trimestre")
                    print("10- Taxa semestral para mensal")
                    print("11 - Taxa semestral para diária")
                    print("TAXAS TRIMESTRAIS----------")
                    print("12 - Taxa trimestral para anual")
                    print("13 - Taxa trimestral para semestral")
                    print("14 - Taxa trimestral para mensal")
                    print("15 - Taxa trimenstral para diária")
                    print("TAXAS MENSAIS--------------")
                    print("16 - Taxa mensal para anual")
                    print("17 - Taxa mensal para semestral")
                    print("18 - Taxa mensal para trimestral")
                    print("19 - Taxa mensal para diária")
                    print("TAXA DIÁRIAS---------------")
                    print("20 - Taxa diária para anual")
                    print("21 - Taxa diária para semestral")
                    print("22 - Taxa diária para trimenstral")
                    print("23 - Taxa diária para mensal")
                    print(" * - sair")
                    opcaoCT = input("Digite o número da opção desejada:")

                    match opcaoCT:
                        case "1":
                            print("Você selecionou Taxa nominal para efetiva.")
                            print("Digite os valores:")
                            i_nominal = float(input("Taxa nominal: "))
                            m = float(input("Número de períodos: "))
                            resultado = controller.taxa_nominal_para_efetiva(i_nominal, m)
                            print(f"A taxa efetiva é: {resultado:.2f}")

                        case "2":    
                            print("Você selecionou Taxa efetiva para nominal.")
                            print("Digite os valores:")
                            i_efetiva = float(input("Taxa efetiva: "))
                            m = float(input("Número de períodos: "))
                            resultado = controller.taxa_efetiva_para_nominal(i_efetiva, m)
                            print(f"A taxa nominal é: {resultado:.2f}")

                        case "3":
                            print("Você selecionou Equivalência de taxas.")
                            print("Digite os valores:")
                            i_origem = float(input("Taxa de origem: "))
                            p_origem = float(input("Período de origem: "))
                            p_destino = float(input("Período de destino: "))
                            resultado = controller.taxa_equivalente(i_origem, p_origem, p_destino)
                            print(f"A taxa equivalente é: {resultado:.2f}")

                        # TAXAS ANUAIS
                        case "4":
                            print("Você selecionou Taxa anual para mensal.")
                            i_anual = float(input("Taxa anual: "))
                            resultado = controller.taxa_anual_para_mensal(i_anual)
                            print(f"A taxa mensal é: {resultado:.6f}")

                        case "5":
                            print("Você selecionou Taxa anual para trimestral.")
                            i_anual = float(input("Taxa anual: "))
                            resultado = controller.taxa_anual_para_trimestral(i_anual)
                            print(f"A taxa trimestral é: {resultado:.6f}")

                        case "6":
                            print("Você selecionou Taxa anual para semestral.")
                            i_anual = float(input("Taxa anual: "))
                            resultado = controller.taxa_anual_para_semestral(i_anual)
                            print(f"A taxa semestral é: {resultado:.6f}")

                        case "7":
                            print("Você selecionou Taxa anual para diária.")
                            i_anual = float(input("Taxa anual: "))
                            resultado = controller.taxa_anual_para_diaria(i_anual)
                            print(f"A taxa diária é: {resultado:.6f}")

                        # TAXAS SEMESTRAIS
                        case "8":
                            print("Você selecionou Taxa semestral para anual.")
                            i_semestral = float(input("Taxa semestral: "))
                            resultado = controller.taxa_semestral_para_anual(i_semestral)
                            print(f"A taxa anual é: {resultado:.6f}")

                        case "9":
                            print("Você selecionou Taxa semestral para trimestral.")
                            i_semestral = float(input("Taxa semestral: "))
                            resultado = controller.taxa_semestral_para_trimestral(i_semestral)
                            print(f"A taxa trimestral é: {resultado:.6f}")

                        case "10":
                            print("Você selecionou Taxa semestral para mensal.")
                            i_semestral = float(input("Taxa semestral: "))
                            resultado = controller.taxa_semestral_para_mensal(i_semestral)
                            print(f"A taxa mensal é: {resultado:.6f}")

                        case "11":
                            print("Você selecionou Taxa semestral para diária.")
                            i_semestral = float(input("Taxa semestral: "))
                            resultado = controller.taxa_semestral_para_diaria(i_semestral)
                            print(f"A taxa diária é: {resultado:.6f}")

                        # TAXAS TRIMESTRAIS
                        case "12":
                            print("Você selecionou Taxa trimestral para anual.")
                            i_trimestral = float(input("Taxa trimestral: "))
                            resultado = controller.taxa_trimestral_para_anual(i_trimestral)
                            print(f"A taxa anual é: {resultado:.6f}")

                        case "13":
                            print("Você selecionou Taxa trimestral para semestral.")
                            i_trimestral = float(input("Taxa trimestral: "))
                            resultado = controller.taxa_trimestral_para_semestral(i_trimestral)
                            print(f"A taxa semestral é: {resultado:.6f}")

                        case "14":
                            print("Você selecionou Taxa trimestral para mensal.")
                            i_trimestral = float(input("Taxa trimestral: "))
                            resultado = controller.taxa_trimestral_para_mensal(i_trimestral)
                            print(f"A taxa mensal é: {resultado:.6f}")

                        case "15":
                            print("Você selecionou Taxa trimestral para diária.")
                            i_trimestral = float(input("Taxa trimestral: "))
                            resultado = controller.taxa_trimestral_para_diaria(i_trimestral)
                            print(f"A taxa diária é: {resultado:.6f}")

                        # TAXAS MENSAIS
                        case "16":
                            print("Você selecionou Taxa mensal para anual.")
                            i_mensal = float(input("Taxa mensal: "))
                            resultado = controller.taxa_mensal_para_anual(i_mensal)
                            print(f"A taxa anual é: {resultado:.6f}")

                        case "17":
                            print("Você selecionou Taxa mensal para semestral.")
                            i_mensal = float(input("Taxa mensal: "))
                            resultado = controller.taxa_mensal_para_semestral(i_mensal)
                            print(f"A taxa semestral é: {resultado:.6f}")

                        case "18":
                            print("Você selecionou Taxa mensal para trimestral.")
                            i_mensal = float(input("Taxa mensal: "))
                            resultado = controller.taxa_mensal_para_trimestral(i_mensal)
                            print(f"A taxa trimestral é: {resultado:.6f}")

                        case "19":
                            print("Você selecionou Taxa mensal para diária.")
                            i_mensal = float(input("Taxa mensal: "))
                            resultado = controller.taxa_mensal_para_diaria(i_mensal)
                            print(f"A taxa diária é: {resultado:.6f}")

                        # TAXAS DIÁRIAS
                        case "20":
                            print("Você selecionou Taxa diária para anual.")
                            i_diaria = float(input("Taxa diária: "))
                            resultado = controller.taxa_diaria_para_anual(i_diaria)
                            print(f"A taxa anual é: {resultado:.6f}")

                        case "21":
                            print("Você selecionou Taxa diária para semestral.")
                            i_diaria = float(input("Taxa diária: "))
                            resultado = controller.taxa_diaria_para_semestral(i_diaria)
                            print(f"A taxa semestral é: {resultado:.6f}")

                        case "22":
                            print("Você selecionou Taxa diária para trimestral.")
                            i_diaria = float(input("Taxa diária: "))
                            resultado = controller.taxa_diaria_para_trimestral(i_diaria)
                            print(f"A taxa trimestral é: {resultado:.6f}")

                        case "23":
                            print("Você selecionou Taxa diária para mensal.")
                            i_diaria = float(input("Taxa diária: "))
                            resultado = controller.taxa_diaria_para_mensal(i_diaria)
                            print(f"A taxa mensal é: {resultado:.6f}")

                        case "*":
                            pass
                    
                case "6": 
                    print("Você selecionou Série de Fibonacci Financeira")
                    print("Digite os valores:")
                    x = float(input("Valor de x: "))
                    termos = int(input("Número de termos: "))
                    resultado = controller.fibonacci_series(x, termos)
                    print(f"A sequência de Fibonacci é: {resultado['Sequência']}")
                    print(f"A soma da série financeira é: {resultado['Soma']:.2f}")
                    pass

                case "7":
                    print("Você selecionou Estimativa de Valor de Imóvel")
                    print("Digite os valores:")
                    PMT = float(input("Pagamento (PMT): "))
                    i = float(input("Taxa por período: "))
                    resultado = controller.estimativa_valor_imovel(PMT, i)
                    print(f"O valor estimado do imóvel é: {resultado:.2f}")
                    pass

                case "8":
                    print("Você selecionou Título de Dívida e Cálculo de Desconto")
                    print("Digite os valores:")
                    FV = float(input("Valor futuro (FV): "))
                    PV = float(input("Valor presente (PV): "))
                    resultado = controller.titulo_divida(FV, PV)
                    print(f"O desconto é: {resultado['Desconto']:.2f}")
                    pass

if __name__ == "__main__":
    main()