# Projeto-RPG-1F

Alunos: Yuri Gustavo Zaions e Gustavo Dos Santos Kell
Turma: 1F

O trabalho tem como objetivo desenvolver um jogo de RPG simples em Python, utilizando listas, matrizes e funções, conforme os requisitos.
O programa foi projetado para rodar diretamente no terminal.

O código foi dividido em funções bem definidas para manter a organização e facilitar o entendimento.
As principais partes do projeto são:

Mapa : Representado por uma lista de listas, onde cada posição contém um ponto ".". O jogador se move dentro desse espaço.

Personagem : O jogador possui atributos como vida, ataque, defesa e inventário.

Movimentação: O jogador pode se mover para cima, baixo, esquerda e direita utilizando as teclas w, s, a, d.

Batalha: Ao se mover, existe a chance de encontrar inimigos (como goblins). A batalha é resolvida por cálculos de ataque e defesa, reduzindo a vida dos participantes.

Inventário: Ao vencer inimigos, o jogador pode coletar itens, como “Poções de Cura”.

Loop principal: Mantém o jogo em execução até o jogador decidir sair ou até sua vida chegar a zero.

Funções Implementadas:

criar_mapa(tamanho: Gera a matriz que representa o mundo do jogo.

mostrar_mapa(mapa, pos_jogador): Exibe o mapa no terminal, indicando a posição do jogador com a letra P.

criar_personagem(nome): Cria um dicionário com os atributos iniciais do jogador.

mover(pos, direcao, tamanho): Controla os movimentos do personagem no mapa.

batalha(jogador, inimigo): Implementa o sistema de combate, subtraindo pontos de vida com base em ataque e defesa.

jogar(): Função principal que organiza o fluxo do jogo, chamando as outras funções.

Recebi ajuda da inteligência Artificial na parte da movimentação do jogador e em alguma partes do inimigo
