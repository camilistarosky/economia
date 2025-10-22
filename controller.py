import math

# --- Juros Compostos ---

def calcular_montante(P, i, n):
  """Calcula o montante em juros compostos."""
  return P * (1 + i) ** n

def calcular_juros_compostos(P, i, n):
  """Calcula os juros compostos (montante - capital)."""
  M = calcular_montante(P, i, n)
  return M - P

def calcular_capital(M, i, n):
  """Calcula o capital inicial dado o montante, taxa e períodos."""
  return M / (1 + i) ** n

def calcular_num_periodos(P, M, i):
  """Calcula o número de períodos dados o capital, montante e taxa."""
  return math.log(M / P) / math.log(1 + i)

def calcular_taxa(P, M, n):
  """Calcula a taxa de juros composta dada o capital, montante e número de períodos."""
  return (M / P) ** (1 / n) - 1

# --- Rendas (Anuidades) ---

def valor_futuro_anuidade(R, i, n):
    """Valor futuro de uma anuidade (pagamentos periódicos)."""
    return R * ((1 + i) ** n - 1) / i

def valor_presente_anuidade(R, i, n):
    """Valor presente de uma anuidade."""
    return R * (1 - (1 + i) ** -n) / i

def valor_presente_pagamento_unico(R, i, n):
    """Valor presente de um pagamento único."""
    return R / (1 + i) ** n

def valor_futuro_pagamento_unico(R, i, n):
    """Valor futuro de um pagamento único."""
    return R * (1 + i) ** n

# --- Descontos ---

def desconto_simples(N, d, t):
    """Calcula o desconto simples e o valor presente."""
    D = N * d * t
    PV = N - D
    return D, PV

def desconto_composto(N, d, t):
    """Calcula o valor presente no desconto composto."""
    PV = N * (1 - d) ** t
    return PV

def desconto_racional(N, i, t):
  """Calcula o valor presente pelo desconto racional (desconto por dentro)."""
  PV = N / (1 + i * t)
  D = N - PV  # valor do desconto
  return D, PV

def desconto_racional_futuro(N, i, t):
  """Calcula o valor futuro pelo desconto racional (desconto por fora)."""
  VF = N * (1 + i * t)
  D = VF - N  # valor do desconto
  return D, VF

# --- Amortização (Sistema Francês) ---

def calcular_parcela_amortizacao(P, i, n):
    """Calcula a parcela fixa mensal de um empréstimo pelo sistema francês."""
    parcela = P * (i * (1 + i) * n) / ((1 + i) * n - 1)
    return parcela

def calcular_saldo_devedor(P, i, n, k):
   """Calcula o saldo devedor de um empréstimo pelo sistema francês."""
   saldo = P * ((1 + i) * n - k) / ((1 + i) * n - 1)
   return saldo

def calcular_juros_parcela(P, i, n, k):
   """Calcula os juros da parcela k de um empréstimo pelo sistema francês."""
   juros = P * i * ((1 + i) * n - k) / ((1 + i) * n - 1)
   return juros

