import random

def criar_tabuleiro(linhas, colunas, num_minas):
    tabuleiro = [[0] * colunas for _ in range(linhas)]

    for _ in range(num_minas):
        linha, coluna = random.randint(0, linhas - 1), random.randint(0, colunas - 1)

        while tabuleiro[linha][coluna] == -1:
            linha, coluna = random.randint(0, linhas - 1), random.randint(0, colunas - 1)

        tabuleiro[linha][coluna] = -1  

       
        for i in range(linha - 1, linha + 2):
            for j in range(coluna - 1, coluna + 2):
                if 0 <= i < linhas and 0 <= j < colunas and tabuleiro[i][j] != -1:
                    tabuleiro[i][j] += 1

    return tabuleiro

def imprimir_tabuleiro(tabuleiro, mostrar_minas=False):
    for linha in tabuleiro:
        for celula in linha:
            if celula == -1 and not mostrar_minas:
                print(" ", end=" ")
            else:
                print(celula, end=" ")
        print()

def revelar_celula(tabuleiro, tabuleiro_exibicao, linha, coluna):
    if 0 <= linha < len(tabuleiro) and 0 <= coluna < len(tabuleiro[0]) and tabuleiro_exibicao[linha][coluna] == -1:
        tabuleiro_exibicao[linha][coluna] = tabuleiro[linha][coluna]

        if tabuleiro[linha][coluna] == 0:
            
            for i in range(linha - 1, linha + 2):
                for j in range(coluna - 1, coluna + 2):
                    revelar_celula(tabuleiro, tabuleiro_exibicao, i, j)

def jogar():
    linhas = 5
    colunas = 5
    num_minas = 5

    tabuleiro = criar_tabuleiro(linhas, colunas, num_minas)
    tabuleiro_exibicao = [[-1] * colunas for _ in range(linhas)]  

    while True:
        imprimir_tabuleiro(tabuleiro_exibicao)
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))

        if tabuleiro[linha][coluna] == -1:
            print("Você perdeu! Uma mina foi atingida.")
            imprimir_tabuleiro(tabuleiro, mostrar_minas=True)
            break
        else:
            revelar_celula(tabuleiro, tabuleiro_exibicao, linha, coluna)

            
            if all(tabuleiro_exibicao[i][j] != -1 or tabuleiro[i][j] == -1 for i in range(linhas) for j in range(colunas)):
                print("Parabéns! Você ganhou!")
                imprimir_tabuleiro(tabuleiro, mostrar_minas=True)
                break

if __name__ == "__main__":
    jogar()
