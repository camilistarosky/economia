import math

# Controller de fórmulas financeiras
# Todas as funções esperam i como decimal (ex: 3% -> 0.03) e tempos em períodos (meses, anos) conforme o caso.

# -------------------- JUROS COMPOSTOS --------------------
def juros_compostos(PV=None, FV=None, i=None, n=None):
    """Resolve qualquer variável da fórmula dos juros compostos.
    FV = PV*(1+i)**n
    Retorna dict com PV, FV, i, n (os que puderem ser calculados).
    """
    if PV is not None and i is not None and n is not None:
        FV = PV * (1 + i) ** n
    elif FV is not None and i is not None and n is not None:
        PV = FV / (1 + i) ** n
    elif PV is not None and FV is not None and n is not None:
        i = (FV / PV) ** (1 / n) - 1
    elif PV is not None and FV is not None and i is not None:
        n = math.log(FV / PV) / math.log(1 + i)
    return {"PV": PV, "FV": FV, "i": i, "n": n}


# -------------------- RENDAS (ANUIDADES) --------------------
def renda_postecipada(PMT=None, i=None, n=None, FV=None, PV=None):
    """Renda postecipada (pagamento no final de cada período)
    FV = PMT * ((1+i)**n - 1) / i  (valor futuro ao final do n-ésimo período)
    PV = PMT * (1 - (1+i)**-n) / i  (valor presente no período 0)
    """
    if PMT is not None and i is not None and n is not None:
        FV = PMT * ((1 + i) ** n - 1) / i
        PV = PMT * (1 - (1 + i) ** -n) / i
    elif FV is not None and i is not None and n is not None:
        PMT = FV * i / ((1 + i) ** n - 1)
        PV = PMT * (1 - (1 + i) ** -n) / i
        FV = PMT * ((1 + i) ** n - 1) / i
    elif PV is not None and i is not None and n is not None:
        PMT = PV * i / (1 - (1 + i) ** -n)
        FV = PMT * ((1 + i) ** n - 1) / i
        PV = PMT * (1 - (1 + i) ** -n) / i
    elif PMT is not None and FV is not None and i is not None:
        # resolve n: FV = PMT*((1+i)**n -1)/i  -> (FV*i/PMT)+1 = (1+i)**n
        n = math.log((FV * i / PMT) + 1) / math.log(1 + i)
    elif PMT is not None and PV is not None and i is not None:
        # resolve n: PV = PMT*(1-(1+i)**-n)/i
        n = -math.log(1 - (PV * i / PMT)) / math.log(1 + i)
    else:
        PMT = PMT if 'PMT' in locals() else None
    return {"PMT": PMT, "i": i, "n": n, "FV": FV, "PV": PV}


def renda_antecipada(PMT=None, i=None, n=None, PV=None, FV=None):
    """Renda antecipada (anuidade devida) - primeiro pagamento imediatamente.
    PV = PMT * (1 - (1+i)**-n) / i * (1+i)
    FV = PMT * ((1+i)**n - 1) / i * (1+i)
    """
    if PMT is not None and i is not None and n is not None:
        PV = PMT * (1 - (1 + i) ** -n) / i * (1 + i)
        FV = PMT * ((1 + i) ** n - 1) / i * (1 + i)
    elif PV is not None and i is not None and n is not None:
        PMT = PV * i / ((1 - (1 + i) ** -n) * (1 + i))
        FV = PMT * ((1 + i) ** n - 1) / i * (1 + i)
    elif PMT is not None and PV is not None and i is not None:
        # solve n numerically
        def f_n(x):
            return PMT * (1 - (1 + i) ** -x) / i * (1 + i) - PV
        # bisection
        a = 1e-9; b = 1e3
        for _ in range(200):
            m = (a + b) / 2
            if f_n(a) * f_n(m) <= 0:
                b = m
            else:
                a = m
        n = (a + b) / 2
    return {"PMT": PMT, "i": i, "n": n, "PV": PV, "FV": FV}


# -------------------- DESCONTOS --------------------
def desconto_simples_comercial(FV=None, PV=None, d=None, t=None):
    D = None
    if FV is not None and d is not None and t is not None:
        D = FV * d * t
        PV = FV - D
    elif PV is not None and d is not None and t is not None:
        FV = PV / (1 - d * t)
        D = FV - PV
    elif FV is not None and PV is not None and t is not None:
        d = (FV - PV) / (FV * t)
        D = FV - PV
    elif FV is not None and PV is not None and d is not None:
        t = (FV - PV) / (FV * d)
        D = FV - PV
    if D is None and FV is not None and PV is not None:
        D = FV - PV
    return {"PV": PV, "FV": FV, "d": d, "t": t, "D": D}


def desconto_simples_racional(FV=None, PV=None, i=None, t=None):
    D = None
    if FV is not None and i is not None and t is not None:
        PV = FV / (1 + i * t)
    elif PV is not None and i is not None and t is not None:
        FV = PV * (1 + i * t)
    elif FV is not None and PV is not None and t is not None:
        i = (FV / PV - 1) / t
    elif FV is not None and PV is not None and i is not None:
        t = (FV / PV - 1) / i
    if FV is not None and PV is not None:
        D = FV - PV
    return {"PV": PV, "FV": FV, "i": i, "t": t, "D": D}


def desconto_composto_comercial(FV=None, PV=None, d=None, t=None):
    D = None
    if FV is not None and d is not None and t is not None:
        PV = FV * (1 - d) ** t
    elif PV is not None and d is not None and t is not None:
        FV = PV / ((1 - d) ** t)
    elif FV is not None and PV is not None and t is not None:
        d = 1 - (PV / FV) ** (1 / t)
    elif FV is not None and PV is not None and d is not None:
        t = math.log(PV / FV) / math.log(1 - d)
    if FV is not None and PV is not None:
        D = FV - PV
    return {"PV": PV, "FV": FV, "d": d, "t": t, "D": D}


def desconto_composto_racional(FV=None, PV=None, i=None, t=None):
    D = None
    if FV is not None and i is not None and t is not None:
        PV = FV / (1 + i) ** t
    elif PV is not None and i is not None and t is not None:
        FV = PV * (1 + i) ** t
    elif FV is not None and PV is not None and t is not None:
        i = (FV / PV) ** (1 / t) - 1
    elif FV is not None and PV is not None and i is not None:
        t = math.log(FV / PV) / math.log(1 + i)
    if FV is not None and PV is not None:
        D = FV - PV
    return {"PV": PV, "FV": FV, "i": i, "t": t, "D": D}


# -------------------- AMORTIZAÇÃO (PRICE) --------------------
def amortizacao_price(PV=None, PMT=None, i=None, n=None):
    """Sistema FRANCÊS (PRICE). i em decimal.
    PMT = PV * [i*(1+i)**n] / [(1+i)**n - 1]
    """
    if PV is not None and i is not None and n is not None:
        PMT = PV * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    elif PMT is not None and i is not None and n is not None:
        PV = PMT * ((1 + i) ** n - 1) / (i * (1 + i) ** n)
    elif PV is not None and PMT is not None and i is not None:
        # solve for n
        n = math.log(PMT / (PMT - PV * i)) / math.log(1 + i)
    elif PV is not None and PMT is not None and n is not None:
        # solve for i numerically (bisection)
        def f(rate):
            return PV - PMT * ((1 - (1 + rate) ** -n) / rate)
        a = 1e-12; b = 1.0
        fa = f(a); fb = f(b)
        # expand b if necessary
        while fa * fb > 0:
            b *= 2
            fb = f(b)
        for _ in range(100):
            m = (a + b) / 2
            if f(a) * f(m) <= 0:
                b = m
            else:
                a = m
        i = (a + b) / 2
    return {"PV": PV, "PMT": PMT, "i": i, "n": n}


# -------------------- CONVERSÕES DE TAXAS --------------------
def taxa_nominal_para_efetiva(i_nominal, m):
    return (1 + i_nominal / m) ** m - 1

def taxa_efetiva_para_nominal(i_efetiva, m):
    return m * ((1 + i_efetiva) ** (1 / m) - 1)

def taxa_equivalente(i_origem, p_origem, p_destino):
    return (1 + i_origem) ** (p_destino / p_origem) - 1

def taxa_anual_para_mensal(i_anual):
    return (1 + i_anual) ** (1 / 12) - 1

def taxa_mensal_para_anual(i_mensal):
    return (1 + i_mensal) ** 12 - 1

def taxa_anual_para_trimestral(i_anual):
    return (1 + i_anual) ** (1 / 4) - 1

def taxa_anual_para_semestral(i_anual):
    return (1 + i_anual) ** (1 / 2) - 1

def taxa_anual_para_diaria(i_anual):
    return (1 + i_anual) ** (1 / 252) - 1

def taxa_semestral_para_anual(i_semestral):
    return (1 + i_semestral) ** 2 - 1

def taxa_semestral_para_trimestral(i_semestral):
    return (1 + i_semestral) ** (1 / 2) - 1

def taxa_semestral_para_mensal(i_semestral):
    return (1 + i_semestral) ** (1 / 6) - 1

def taxa_semestral_para_diaria(i_semestral):
    return (1 + i_semestral) ** (1 / 126) - 1

def taxa_trimestral_para_anual(i_trimestral):
    return (1 + i_trimestral) ** 4 - 1

def taxa_trimestral_para_semestral(i_trimestral):
    return (1 + i_trimestral) ** 2 - 1

def taxa_trimestral_para_mensal(i_trimestral):
    return (1 + i_trimestral) ** (1 / 3) - 1

def taxa_trimestral_para_diaria(i_trimestral):
    return (1 + i_trimestral) ** (1 / 63) - 1

def taxa_mensal_para_semestral(i_mensal):
    return (1 + i_mensal) ** 6 - 1

def taxa_mensal_para_trimestral(i_mensal):
    return (1 + i_mensal) ** 3 - 1

def taxa_mensal_para_diaria(i_mensal):
    return (1 + i_mensal) ** (1 / 21) - 1

def taxa_diaria_para_anual(i_diaria):
    return (1 + i_diaria) ** 252 - 1

def taxa_diaria_para_semestral(i_diaria):
    return (1 + i_diaria) ** 126 - 1

def taxa_diaria_para_trimestral(i_diaria):
    return (1 + i_diaria) ** 63 - 1

def taxa_diaria_para_mensal(i_diaria):
    return (1 + i_diaria) ** 21 - 1


# -------------------- OUTRAS --------------------
def estimativa_valor_imovel(PMT, i):
    return PMT / i

def titulo_divida(FV=None, PV=None):
    D = None
    if FV is not None and PV is not None:
        D = FV - PV
    return {"Desconto": D, "FV": FV, "PV": PV}

def fibonacci_series(x, termos=10):
    F = [0, 1]
    for _ in range(2, termos):
        F.append(F[-1] + F[-2])
    S = sum(F[k] / (x ** k) for k in range(termos))
    return {"Sequência": F, "Soma": S}

def digito_verificador_rg(numero):
    numero = str(numero).zfill(9)
    soma = sum((10 - i) * int(numero[i]) for i in range(9))
    resto = soma % 11
    return resto

# ===========================================================
# === VARIAÇÃO SUCESSIVA (repetida ou lista) =================
# ===========================================================

def variacao_repetida(taxa_decimal, k, tipo="aumento"):
    """
    Calcula o equivalente quando a mesma taxa se repete k vezes.
    - taxa_decimal: ex 0.29 para 29%
    - k: número de repetições (int)
    - tipo: "aumento" ou "desconto"
    Retorna dict com:
      - 'decimal' : valor decimal do aumento/desconto equivalente (ex: 1.146689 -> 114.6689% aumento; 
                    para desconto retorna valor POSITIVO do desconto equivalente, ex: 0.19 => 19%)
      - 'percent' : em %
      - 'tipo'    : "aumento" ou "desconto"
    OBS: Para desconto retornamos o desconto equivalente em decimal positivo (ex: 0.19).
    """
    if k < 0:
        raise ValueError("k deve ser inteiro não-negativo")
    if tipo not in ("aumento", "desconto"):
        raise ValueError("tipo deve ser 'aumento' ou 'desconto'")

    r = float(taxa_decimal)
    k = int(k)

    if tipo == "aumento":
        fator_total = (1 + r) ** k
        decimal_eq = fator_total - 1              # >0 para aumento
    else:  # desconto
        fator_total = (1 - r) ** k
        decimal_eq = 1 - fator_total              # desconto equivalente (positivo)

    return {"decimal": decimal_eq, "percent": decimal_eq * 100, "tipo": tipo, "fator_total": fator_total}


def variacao_sucessiva_list(taxas_decimal):
    """
    Calcula o equivalente para uma lista de taxas (podem ser positivas para aumentos
    ou negativas para descontos). Ex: [0.10, -0.05, 0.08].
    Retorna decimal (positivo para aumento líquido, negativo se queda líquida),
    e percent (decimal*100).
    Obs: aqui aceitamos sinal nas taxas (ex: -0.10 para desconto de 10%).
    """
    fator = 1.0
    for t in taxas_decimal:
        fator *= (1 + float(t))
    decimal_eq = fator - 1
    return {"decimal": decimal_eq, "percent": decimal_eq * 100, "fator_total": fator}
