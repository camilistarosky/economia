import controller

def read_float(prompt):
        v = input(prompt)
        return float(v.replace(',','.'))


def main():
        print("Bem-vindo a calculadora de economia!")
        print("Selecione a matéria desejada:")
        print("1 - Matemática Financeira")
        print("0 - Sair")

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
                        print("3 - Taxa por período (i)")
                        print("4 - Número de períodos (n)")
                        opcaoJC = input("Digite o número da opção desejada: ")

                        match opcaoJC:
                            case "1":
                                PV = read_float("Valor presente (PV): ")
                                i = read_float("Taxa por período (em %): ")/100
                                n = read_float("Número de períodos: ")
                                r = controller.juros_compostos(PV=PV, i=i, n=n)
                                print(f"FV = {r['FV']:.2f}")

                            case "2":
                                FV = read_float("Valor futuro (FV): ")
                                i = read_float("Taxa por período (em %): ")/100
                                n = read_float("Número de períodos: ")
                                r = controller.juros_compostos(FV=FV, i=i, n=n)
                                print(f"PV = {r['PV']:.2f}")

                            case "3":
                                FV = read_float("Valor futuro (FV): ")
                                PV = read_float("Valor presente (PV): ")
                                n = read_float("Número de períodos: ")
                                r = controller.juros_compostos(FV=FV, PV=PV, n=n)
                                if r['i'] is not None:
                                    print(f"i = {r['i']*100:.6f} %")
                                else:
                                    print("Erro: não foi possível calcular i")

                            case "4":
                                FV = read_float("Valor futuro (FV): ")
                                PV = read_float("Valor presente (PV): ")
                                i = read_float("Taxa por período (em %): ")/100
                                r = controller.juros_compostos(FV=FV, PV=PV, i=i)
                                print(f"n = {r['n']:.6f}")

                    case "2":
                        print("Rendas (Anuidades)")
                        print("1 - Renda postecipada (fim do período)")
                        print("2 - Renda antecipada (início do período)")
                        sub = input("Escolha: ")
                        if sub == "1":
                            print("1 - Calcular FV")
                            print("2 - Calcular PV")
                            print("3 - Calcular PMT")
                            print("4 - Calcular n")
                            op = input("Escolha: ")
                            if op == "1":
                                PMT = read_float("PMT: ")
                                i = read_float("Taxa por período (em %): ")/100
                                n = read_float("n: ")
                                r = controller.renda_postecipada(PMT=PMT, i=i, n=n)
                                print(f"FV = {r['FV']:.2f}")
                            elif op == "2":
                                PMT = read_float("PMT: ")
                                i = read_float("Taxa por período (em %): ")/100
                                n = read_float("n: ")
                                r = controller.renda_postecipada(PMT=PMT, i=i, n=n)
                                print(f"PV = {r['PV']:.2f}")
                            elif op == "3":
                                base = input("Base 1-FV ou 2-PV: ")
                                if base == "1":
                                    FV = read_float("FV: ")
                                    i = read_float("Taxa por período (em %): ")/100
                                    n = read_float("n: ")
                                    r = controller.renda_postecipada(FV=FV, i=i, n=n)
                                    print(f"PMT = {r['PMT']:.2f}")
                                else:
                                    PV = read_float("PV: ")
                                    i = read_float("Taxa por período (em %): ")/100
                                    n = read_float("n: ")
                                    r = controller.renda_postecipada(PV=PV, i=i, n=n)
                                    print(f"PMT = {r['PMT']:.2f}")
                            elif op == "4":
                                base = input("Base 1-FV ou 2-PV: ")
                                if base == "1":
                                    PMT = read_float("PMT: ")
                                    FV = read_float("FV: ")
                                    i = read_float("Taxa por período (em %): ")/100
                                    r = controller.renda_postecipada(PMT=PMT, FV=FV, i=i)
                                    print(f"n = {r['n']:.6f}")
                                else:
                                    PMT = read_float("PMT: ")
                                    PV = read_float("PV: ")
                                    i = read_float("Taxa por período (em %): ")/100
                                    r = controller.renda_postecipada(PMT=PMT, PV=PV, i=i)
                                    print(f"n = {r['n']:.6f}")
                        else:
                            print("1 - Calcular PV")
                            print("2 - Calcular PMT")
                            op = input("Escolha: ")
                            if op == "1":
                                PMT = read_float("PMT: ")
                                i = read_float("Taxa por período (em %): ")/100
                                n = read_float("n: ")
                                r = controller.renda_antecipada(PMT=PMT, i=i, n=n)
                                print(f"PV = {r['PV']:.2f}")
                            else:
                                PV = read_float("PV: ")
                                i = read_float("Taxa por período (em %): ")/100
                                n = read_float("n: ")
                                r = controller.renda_antecipada(PV=PV, i=i, n=n)
                                print(f"PMT = {r['PMT']:.2f}")

                    case "3":
                        print("Descontos")
                        print("1 - Comercial simples")
                        print("2 - Racional simples")
                        print("3 - Comercial composto")
                        print("4 - Racional composto")
                        op = input("Escolha: ")
                        if op == "1":
                            sub = input("1-PV 2-FV 3-d 4-t: ")
                            if sub == "1":
                                FV = read_float("FV: ")
                                d = read_float("d (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_simples_comercial(FV=FV, d=d, t=t)
                                print(f"PV = {r['PV']:.2f}")
                            elif sub == "2":
                                PV = read_float("PV: ")
                                d = read_float("d (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_simples_comercial(PV=PV, d=d, t=t)
                                print(f"FV = {r['FV']:.2f}")
                            elif sub == "3":
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                t = read_float("t: ")
                                r = controller.desconto_simples_comercial(FV=FV, PV=PV, t=t)
                                if r['d'] is not None:
                                    print(f"d = {r['d']*100:.6f} %")
                                else:
                                    print("Erro: não foi possível calcular d")
                            else:
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                d = read_float("d (em %): ")/100
                                r = controller.desconto_simples_comercial(FV=FV, PV=PV, d=d)
                                print(f"t = {r['t']:.6f}")
                        elif op == "2":
                            sub = input("1-PV 2-FV 3-i 4-t: ")
                            if sub == "1":
                                FV = read_float("FV: ")
                                i = read_float("i (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_simples_racional(FV=FV, i=i, t=t)
                                print(f"PV = {r['PV']:.2f}")
                            elif sub == "2":
                                PV = read_float("PV: ")
                                i = read_float("i (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_simples_racional(PV=PV, i=i, t=t)
                                print(f"FV = {r['FV']:.2f}")
                            elif sub == "3":
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                t = read_float("t: ")
                                r = controller.desconto_simples_racional(FV=FV, PV=PV, t=t)
                                if r['i'] is not None:
                                    print(f"i = {r['i']*100:.6f} %")
                                else:
                                    print("Erro: não foi possível calcular i")
                            else:
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                i = read_float("i (em %): ")/100
                                r = controller.desconto_simples_racional(FV=FV, PV=PV, i=i)
                                print(f"t = {r['t']:.6f}")
                        elif op == "3":
                            sub = input("1-PV 2-FV 3-d 4-t: ")
                            if sub == "1":
                                FV = read_float("FV: ")
                                d = read_float("d (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_composto_comercial(FV=FV, d=d, t=t)
                                print(f"PV = {r['PV']:.2f}")
                            elif sub == "2":
                                PV = read_float("PV: ")
                                d = read_float("d (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_composto_comercial(PV=PV, d=d, t=t)
                                print(f"FV = {r['FV']:.2f}")
                            elif sub == "3":
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                t = read_float("t: ")
                                r = controller.desconto_composto_comercial(FV=FV, PV=PV, t=t)
                                if r['d'] is not None:
                                    print(f"d = {r['d']*100:.6f} %")
                                else:
                                    print("Erro: não foi possível calcular d")
                            else:
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                d = read_float("d (em %): ")/100
                                r = controller.desconto_composto_comercial(FV=FV, PV=PV, d=d)
                                print(f"t = {r['t']:.6f}")
                        else:
                            sub = input("1-PV 2-FV 3-i 4-t: ")
                            if sub == "1":
                                FV = read_float("FV: ")
                                i = read_float("i (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_composto_racional(FV=FV, i=i, t=t)
                                print(f"PV = {r['PV']:.2f}")
                            elif sub == "2":
                                PV = read_float("PV: ")
                                i = read_float("i (em %): ")/100
                                t = read_float("t: ")
                                r = controller.desconto_composto_racional(PV=PV, i=i, t=t)
                                print(f"FV = {r['FV']:.2f}")
                            elif sub == "3":
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                t = read_float("t: ")
                                r = controller.desconto_composto_racional(FV=FV, PV=PV, t=t)
                                if r['i'] is not None:
                                    print(f"i = {r['i']*100:.6f} %")
                                else:
                                    print("Erro: não foi possível calcular i")
                            else:
                                FV = read_float("FV: ")
                                PV = read_float("PV: ")
                                i = read_float("i (em %): ")/100
                                r = controller.desconto_composto_racional(FV=FV, PV=PV, i=i)
                                print(f"t = {r['t']:.6f}")

                    case "4":
                        print("Amortização (PRICE)")
                        print("1 - PMT")
                        print("2 - PV")
                        print("3 - n")
                        print("4 - i")
                        op = input("Escolha: ")
                        if op == "1":
                            PV = read_float("PV: ")
                            i = read_float("Taxa por período (em %): ")/100
                            n = read_float("n: ")
                            r = controller.amortizacao_price(PV=PV, i=i, n=n)
                            print(f"PMT = {r['PMT']:.2f}")
                        elif op == "2":
                            PMT = read_float("PMT: ")
                            i = read_float("Taxa por período (em %): ")/100
                            n = read_float("n: ")
                            r = controller.amortizacao_price(PMT=PMT, i=i, n=n)
                            print(f"PV = {r['PV']:.2f}")
                        elif op == "3":
                            PMT = read_float("PMT: ")
                            PV = read_float("PV: ")
                            i = read_float("Taxa por período (em %): ")/100
                            r = controller.amortizacao_price(PV=PV, PMT=PMT, i=i)
                            print(f"n = {r['n']:.6f}")
                        else:
                            PMT = read_float("PMT: ")
                            PV = read_float("PV: ")
                            n = read_float("n: ")
                            r = controller.amortizacao_price(PV=PV, PMT=PMT, n=n)
                            if r['i'] is not None:
                                print(f"i = {r['i']*100:.6f} %")
                            else:
                                print("Erro: não foi possível calcular i")

                    case "5":
                        print("Conversões e Equivalências de Taxas")
                        print("1 - Taxa nominal para efetiva")
                        print("2 - Taxa efetiva para nominal")
                        print("3 - Equivalência de taxas")
                        op = input("Escolha: ")
                        if op == "1":
                            i_nom = read_float("Taxa nominal (em %): ")/100
                            m = int(read_float("m (capitalizações por ano): "))
                            print(f"i_ef = {controller.taxa_nominal_para_efetiva(i_nom, m)*100:.6f} %")
                        elif op == "2":
                            i_ef = read_float("Taxa efetiva (em %): ")/100
                            m = int(read_float("m (vezes/ano): "))
                            print(f"i_nom = {controller.taxa_efetiva_para_nominal(i_ef, m)*100:.6f} %")
                        else:
                            i_o = read_float("Taxa de origem (em %): ")/100
                            p_o = read_float("Período de origem (em meses): ")
                            p_d = read_float("Período de destino (em meses): ")
                            print(f"i_eq = {controller.taxa_equivalente(i_o, p_o, p_d)*100:.6f} %")

                    case "6":
                        x = read_float("Valor de x: ")
                        termos = int(read_float("Número de termos: "))
                        r = controller.fibonacci_series(x, termos)
                        print(f"Soma = {r['Soma']:.6f}")

                    case "7":
                        PMT = read_float("PMT: ")
                        i = read_float("Taxa por período (em %): ")/100
                        print(f"Estimativa PV = {controller.estimativa_valor_imovel(PMT, i):.2f}")

                    case "8":
                        FV = read_float("FV: ")
                        PV = read_float("PV: ")
                        print(f"Desconto = {controller.titulo_divida(FV, PV)['Desconto']:.2f}")

if __name__ == '__main__':
        main()
