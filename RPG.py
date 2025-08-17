import random



def criar_mapa(tamanho):
   
    return [["." for _ in range(tamanho)] for _ in range(tamanho)]

def mostrar_mapa(mapa, pos_jogador):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if (i, j) == pos_jogador:
                print("P", end=" ")
            else:
                print(mapa[i][j], end=" ")
        print()
    print()

def criar_personagem(nome):
    
    return {
        "nome": nome,
        "vida": 100,
        "ataque": 15,
        "defesa": 5,
        "inventario": []
    }

def mover(pos, direcao, tamanho):
   
    x, y = pos
    if direcao == "w" and x > 0:
        x -= 1
    elif direcao == "s" and x < tamanho - 1:
        x += 1
    elif direcao == "a" and y > 0:
        y -= 1
    elif direcao == "d" and y < tamanho - 1:
        y += 1
    return (x, y)

def batalha(jogador, inimigo):
   
    print(f"\nUm {inimigo['nome']} apareceu!")
    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        dano_jogador = max(0, jogador["ataque"] - inimigo["defesa"])
        dano_inimigo = max(0, inimigo["ataque"] - jogador["defesa"])
        
        inimigo["vida"] -= dano_jogador
        jogador["vida"] -= dano_inimigo

        print(f"Você causou {dano_jogador} de dano. Vida inimigo: {inimigo['vida']}")
        print(f"O {inimigo['nome']} causou {dano_inimigo} de dano. Sua vida: {jogador['vida']}\n")

    if jogador["vida"] > 0:
        print("Você venceu a batalha!\n")
        jogador["inventario"].append("Poção de Cura")
    else:
        print("Você foi derrotado...\n")


def jogar():
    tamanho = 5
    mapa = criar_mapa(tamanho)
    pos_jogador = (0, 0)
    jogador = criar_personagem("Herói")

    while jogador["vida"] > 0:
        mostrar_mapa(mapa, pos_jogador)
        print(f"Status: Vida={jogador['vida']} | Inventário={jogador['inventario']}")
        comando = input("Mover (w/a/s/d) ou q para sair: ")

        if comando == "q":
            print("Saindo do jogo...")
            break

        pos_jogador = mover(pos_jogador, comando, tamanho)

    
        if random.random() < 0.3:
            inimigo = {"nome": "Goblin", "vida": 40, "ataque": 10, "defesa": 3}
            batalha(jogador, inimigo)

    print("Fim de jogo!")

if __name__ == "__main__":
    jogar()