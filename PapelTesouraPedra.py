# Mini-game do Papel, Tesoura ou Pedra

from random import choice

player_vitorias = 0
cpu_vitorias = 0


def opcao_player():
    print("MINI-GAME")
    esc_player = input("Escolha entre papel / tesoura/ pedra: ")
    esc_player.lower()
    if esc_player == "papel":
        return esc_player
    elif esc_player == "tesoura":
        return esc_player
    elif esc_player == "pedra":
        return esc_player
    else:
        print("Digite uma opção inválida. Tente novamente!")
        print("-"*30)
        opcao_player()


def opcao_cpu():
    esc_cpu = choice(["papel", "tesoura", "pedra"])
    return esc_cpu


while True:

    print("-"*30)
    esc_player = opcao_player()
    esc_cpu = opcao_cpu()
    print("-"*30)

    if (esc_player == "papel") and (esc_cpu == "pedra") \
        or (esc_player == "tesoura") and (esc_cpu == "papel") \
            or (esc_player == "pedra") and (esc_cpu == "tesoura"):
        # O jogador ganha
        print(f"Você escolheu {esc_player} e a CPU escolheu {esc_cpu}"
              ": Você ganhou!")
        player_vitorias += 1

    elif esc_player == esc_cpu:
        # Empate
        print(f"Você escolheu {esc_player} e a CPU escolheu {esc_cpu}"
              ": Deu empate!")

    else:
        # O jogador perdeu
        print(f"Você escolheu {esc_player} e a CPU escolheu {esc_cpu}"
              ": Você perdeu!")
        cpu_vitorias += 1

    print("-"*30)
    print(f"Vitórias do jogador: {player_vitorias}")
    print(f"Vitórias da CPU: {cpu_vitorias}")
    print("-"*30)

    esc_player = input("Você quer jogar novamente? ")
    if esc_player in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif esc_player in ["NÃO", "não", "Não", "n", "N"]:
        break
    else:
        break
