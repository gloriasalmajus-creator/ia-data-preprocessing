# ==============================================================================
# PROJETO: PIPELINE DE TRATAMENTO DE DADOS PARA ENGENHARIA DE IA
# Objetivo: Simular a limpeza e padronização de dados brutos antes de alimentar um modelo de IA.
# ==============================================================================

def limpar_dados_usuario(nome_sujo, idade_suja, email_sujo):
    print("--- Iniciando o processo de limpeza dos dados brutos ---")
    
    # 1. Padronização de Texto (Removendo espaços extras e padronizando caixa alta)
    nome_limpo = nome_sujo.strip().title()
    print(f"Nome processado: de '{nome_sujo}' para '{nome_limpo}'")
    
    # 2. Tratamento de Dados Numéricos / Tipagem (Garantindo que idade é um número inteiro válido)
    try:
        idade_limpo = int(idade_suja)
        if idade_limpo < 0 or idade_limpo > 120:
            idade_limpo = "Dado Inconsistente" # Identifica anomalias na base
    except ValueError:
        idade_limpo = "Dado Ausente/Erro"
    print(f"Idade processada: de '{idade_suja}' para '{idade_limpo}'")
    
    # 3. Validação de Estrutura (Checando se o e-mail possui formato básico para a IA)
    email_limpo = email_sujo.strip().lower()
    if "@" in email_limpo and "." in email_limpo:
        validacao_email = "Válido"
    else:
        validacao_email = "Inválido (Necessita Correção)"
    print(f"E-mail analisado: '{email_limpo}' -> Status: {validacao_email}")
    
    print("--- Tratamento concluído com sucesso! Dados prontos para o Dataset da IA. ---\n")
    return nome_limpo, idade_limpo, email_limpo

# --- SIMULAÇÃO DA ENTRADA DE DADOS BRUTOS (EXEMPLO DE TESTE) ---
# Simulando dados reais que chegam bagunçados de um formulário ou banco de dados
nome_bruto = "   gLÓRIA sALMA oLIVEIRA   "
idade_bruta = "20"
email_bruto = " GLORIASALMA.dados@GMAIL.COM "

# Executando a função do pipeline
dados_tratados = limpar_dados_usuario(nome_bruto, idade_bruta, email_bruto)
