import math

# ===========================================================
# === JUROS COMPOSTOS =======================================
# Fórmula: FV = PV * (1 + i)**n
# ===========================================================

def juros_compostos(PV=None, FV=None, i=None, n=None):
    """Resolve qualquer variável da fórmula dos juros compostos."""
    if PV and i and n:
        FV = PV * (1 + i) ** n
    elif FV and i and n:
        PV = FV / (1 + i) ** n
    elif PV and FV and n:
        i = (FV / PV) ** (1 / n) - 1
    elif PV and FV and i:
        n = math.log(FV / PV) / math.log(1 + i)
    return {"PV": PV, "FV": FV, "i": i, "n": n}


# ===========================================================
# === RENDAS (ANUIDADES) ====================================
# ===========================================================

def renda_postecipada(PMT=None, i=None, n=None, FV=None, PV=None):
    """
    Renda postecipada (pagamento no final de cada período)
    FV = PMT * ((1 + i)**n - 1) / i
    PV = PMT * (1 - (1 + i)**-n) / i
    """
    # Valor Futuro
    if PMT and i and n:
        FV = PMT * ((1 + i)**n - 1) / i
        PV = FV / (1 + i)**n
    # Valor Presente
    elif FV and i and n:
        PMT = FV * i / ((1 + i)**n - 1)
        PV = FV / (1 + i)**n
    elif PV and i and n:
        PMT = PV * i / (1 - (1 + i)**-n)
        FV = PV * (1 + i)**n
    elif PMT and FV and i:
        n = math.log((FV * i / PMT) + 1) / math.log(1 + i)
    elif PMT and PV and i:
        n = -math.log(1 - (PV * i / PMT)) / math.log(1 + i)
    return {"PMT": PMT, "i": i, "n": n, "FV": FV, "PV": PV}


def renda_antecipada(PMT=None, i=None, n=None, PV=None):
    """
    Renda antecipada (primeiro pagamento imediato)
    PV = PMT * (1 - (1 + i)**-n) / i * (1 + i)
    """
    if PMT and i and n:
        PV = PMT * (1 - (1 + i)**-n) / i * (1 + i)
    elif PV and i and n:
        PMT = PV * i / ((1 - (1 + i)**-n) * (1 + i))
    return {"PMT": PMT, "i": i, "n": n, "PV": PV}


# ===========================================================
# === DESCONTOS =============================================
# ===========================================================

def desconto_simples_comercial(FV=None, PV=None, d=None, t=None):
    """
    Desconto Comercial Simples (por fora)
    D = FV * d * t ; PV = FV - D
    """
    if FV and d and t:
        D = FV * d * t
        PV = FV - D
    elif PV and d and t:
        FV = PV / (1 - d * t)
        D = FV - PV
    elif FV and PV and t:
        d = (FV - PV) / (FV * t)
        D = FV - PV
    elif FV and PV and d:
        t = (FV - PV) / (FV * d)
        D = FV - PV
    return {"PV": PV, "FV": FV, "d": d, "t": t, "D": D}


def desconto_simples_racional(FV=None, PV=None, i=None, t=None):
    """
    Desconto Racional Simples (por dentro)
    PV = FV / (1 + i * t)
    """
    if FV and i and t:
        PV = FV / (1 + i * t)
    elif PV and i and t:
        FV = PV * (1 + i * t)
    elif FV and PV and t:
        i = (FV / PV - 1) / t
    elif FV and PV and i:
        t = (FV / PV - 1) / i
    D = FV - PV
    return {"PV": PV, "FV": FV, "i": i, "t": t, "D": D}


def desconto_composto_comercial(FV=None, PV=None, d=None, t=None):
    """
    Desconto Comercial Composto
    PV = FV * (1 - d)**t
    """
    if FV and d and t:
        PV = FV * (1 - d)**t
    elif PV and d and t:
        FV = PV / ((1 - d)**t)
    elif FV and PV and t:
        d = 1 - (PV / FV)**(1 / t)
    elif FV and PV and d:
        t = math.log(PV / FV) / math.log(1 - d)
    D = FV - PV
    return {"PV": PV, "FV": FV, "d": d, "t": t, "D": D}


def desconto_composto_racional(FV=None, PV=None, i=None, t=None):
    """
    Desconto Racional Composto
    PV = FV / (1 + i)**t
    """
    if FV and i and t:
        PV = FV / (1 + i)**t
    elif PV and i and t:
        FV = PV * (1 + i)**t
    elif FV and PV and t:
        i = (FV / PV)**(1 / t) - 1
    elif FV and PV and i:
        t = math.log(FV / PV) / math.log(1 + i)
    D = FV - PV
    return {"PV": PV, "FV": FV, "i": i, "t": t, "D": D}


# ===========================================================
# === AMORTIZAÇÃO (PRICE) ===================================
# ===========================================================

def amortizacao_price(PV=None, PMT=None, i=None, n=None):
    """
    Sistema Francês (Price)
    PMT = PV * [i*(1 + i)**n] / [(1 + i)**n - 1]
    """
    if PV and i and n:
        PMT = PV * (i * (1 + i)**n) / ((1 + i)**n - 1)
    elif PMT and i and n:
        PV = PMT * ((1 + i)**n - 1) / (i * (1 + i)**n)
    elif PV and PMT and i:
        n = math.log(PMT / (PMT - PV * i)) / math.log(1 + i)
    elif PV and PMT and n:
        i = ((PMT / PV) * ((1 + i)**n - 1)) / ((1 + i)**n)  # aproximação
    return {"PV": PV, "PMT": PMT, "i": i, "n": n}


# ===========================================================
# === CONVERSÕES DE TAXAS ===================================
# ===========================================================

def taxa_nominal_para_efetiva(i_nominal, m):
    """Converte taxa nominal para efetiva (capitalização m vezes ao ano)."""
    return (1 + i_nominal / m)**m - 1

def taxa_efetiva_para_nominal(i_efetiva, m):
    """Converte taxa efetiva para nominal."""
    return m * ((1 + i_efetiva)**(1 / m) - 1)

def taxa_equivalente(i_origem, p_origem, p_destino):
    """Converte taxa de um período para outro."""
    return (1 + i_origem)**(p_destino / p_origem) - 1

def taxa_anual_para_mensal(i_anual):
    """Converte taxa anual para mensal."""
    return (1 + i_anual)**(1/12) - 1

def taxa_mensal_para_anual(i_mensal):
    """Converte taxa mensal para anual."""
    return (1 + i_mensal)**12 - 1


# ===========================================================
# === OUTRAS FÓRMULAS =======================================
# ===========================================================

def estimativa_valor_imovel(PMT, i):
    """Valor presente aproximado de imóvel com renda perpétua."""
    return PMT / i

def titulo_divida(FV=None, PV=None):
    """Desconto simples entre FV e PV."""
    D = FV - PV
    return {"Desconto": D, "FV": FV, "PV": PV}

def fibonacci_series(x, termos=10):
    """Série financeira tipo Fibonacci: S = F0/x0 + F1/x1 + ..."""
    F = [0, 1]
    for _ in range(2, termos):
        F.append(F[-1] + F[-2])
    S = sum(F[k] / (x ** k) for k in range(termos))
    return {"Sequência": F, "Soma": S}
