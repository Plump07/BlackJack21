import random

# Inicialização das cartas e fichas
baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
mao_jogador = []
mao_dealer = []
fichas_jogador = 1000
aposta = 0


# Função para calcular o valor da mão
def valor_mao(mao):
    valor = 0
    conta_as = 0
    for carta in mao:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            valor += 11
            conta_as += 1
        else:
            valor += int(carta)
    while valor > 21 and conta_as > 0:
        valor -= 10
        conta_as -= 1
    return valor


# Função para exibir a mão
def mostrar_mao(mao, nome):
    print(f"Mão de {nome}: {', '.join(mao)} (Valor: {valor_mao(mao)})")


# Função principal do jogo
def principal():
    global fichas_jogador, aposta
    while True:
        print(f"\nVocê tem {fichas_jogador} fichas.")
        aposta = int(input("Digite sua aposta: "))

        if aposta > fichas_jogador:
            print("Você não tem fichas suficientes!")
            continue

        iniciar_nova_rodada()

        while True:
            mostrar_mao(mao_jogador, "Jogador")
            if valor_mao(mao_jogador) > 21:
                print("Você estourou! Dealer vence.")
                fichas_jogador -= aposta
                break

            acao = input("Você quer [C]artas ou [P]arar? ").upper()
            if acao == 'C':
                mao_jogador.append(random.choice(baralho))
            elif acao == 'P':
                while valor_mao(mao_dealer) < 17:
                    mao_dealer.append(random.choice(baralho))
                mostrar_mao(mao_dealer, "Dealer")

                valor_jogador = valor_mao(mao_jogador)
                valor_dealer = valor_mao(mao_dealer)

                if valor_dealer > 21 or valor_jogador > valor_dealer:
                    print("Você venceu!")
                    fichas_jogador += aposta
                elif valor_jogador < valor_dealer:
                    print("Dealer vence!")
                    fichas_jogador -= aposta
                else:
                    print("Empate!")
                break

        if fichas_jogador <= 0:
            print("Você está sem fichas! Fim de jogo.")
            break

        jogar_novamente = input("Você quer jogar novamente? [S/N] ").upper()
        if jogar_novamente != 'S':
            break


def iniciar_nova_rodada():
    global mao_jogador, mao_dealer
    mao_jogador = [random.choice(baralho), random.choice(baralho)]
    mao_dealer = [random.choice(baralho), random.choice(baralho)]
    print("\nIniciando uma nova rodada...")
    mostrar_mao(mao_dealer[:1], "Dealer")


if __name__ == "__main__":
    principal()
