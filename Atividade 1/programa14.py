print("--- SISTEMA DE PORTARIA: INDÚSTRIAS FORTE ---")

while True:
    print("\n[Aproxime seu crachá] Digite o número do crachá (ou 0 para desligar o painel):")
    num_cracha = int(input("Crachá: "))

    if num_cracha == 0:
        print("Desligando painel de acesso...")
        break

    # Loop para garantir que a hora digitada seja válida (entre 0 e 23)
    while True:
        hora_atual = int(input("Digite a hora atual (0 a 23): "))
        if 0 <= hora_atual <= 23:
            break
        print("Hora inválida! Por favor, digite um valor entre 0 e 23.")

    # Verificação do acesso da Administração
    if 1000 <= num_cracha <= 1999:
        if 8 <= hora_atual <= 18:
            print("ACESSO PERMITIDO: Setor Administrativo.")
        else:
            print("ACESSO NEGADO: Fora do horário permitido para o setor.")

    # Verificação do acesso da Produção
    elif 2000 <= num_cracha <= 2999:
        print("ACESSO PERMITIDO: Setor de Produção (Livre).")

    # Identificação de crachá inválido
    else:
        print("ACESSO NEGADO: Crachá inválido ou não cadastrado.")