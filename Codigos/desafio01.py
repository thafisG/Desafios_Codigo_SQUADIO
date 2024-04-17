def aventura_do_explorador():
    quantidade_passos = int(input())

    if quantidade_passos <= 0:
        print("Nenhum passo dado na floresta.")
        return

    for i in range(1, quantidade_passos + 1):
        print("Explorador:", i, "passo" if i == 1 else "passos")

aventura_do_explorador()
