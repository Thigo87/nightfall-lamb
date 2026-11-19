import pygame

pygame.init()

# Tamanho da janela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("jogo base")

relogio = pygame.time.Clock()

# Cores
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
PRETO = (20, 20, 20)
BRANCO = (255, 255, 255)

# Jogador
jogador = pygame.Rect(100, 250, 50, 50)
jogador_pos = pygame.Vector2(100, 250)
velocidade_jogador = 300

# Bloco verde
bloco_verde = pygame.Rect(50, 500, 50, 50)
bloco_verde_visivel = True

# Bloco vermelho
bloco_vermelho = pygame.Rect(700, 350, 50, 50)
bloco_vermelho_visivel = True

# Bloco amarelo
bloco_amarelo = pygame.Rect(500, 50, 50, 50)
bloco_amarelo_visivel = True

rodando = True

while rodando:

    dt = relogio.tick(60) / 1000

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if teclas[pygame.K_RIGHT]:
        dx += 1
    if teclas[pygame.K_LEFT]:
        dx -= 1
    if teclas[pygame.K_UP]:
        dy -= 1
    if teclas[pygame.K_DOWN]:
        dy += 1

    # Normalização diagonal
    movimento = pygame.Vector2(dx, dy)

    if movimento.length() > 0:
        movimento = movimento.normalize()

    jogador_pos += movimento * velocidade_jogador * dt

    # Atualiza o retângulo do jogador
    jogador.topleft = (round(jogador_pos.x), round(jogador_pos.y))

    # Impede de sair da tela
    tela_rect = tela.get_rect()
    if not tela_rect.contains(jogador):
        jogador.clamp_ip(tela_rect)
        jogador_pos.update(jogador.x, jogador.y)

    # Colisão: some o bloco tocado
    if bloco_verde_visivel and jogador.colliderect(bloco_verde):
        bloco_verde_visivel = False
    if bloco_vermelho_visivel and jogador.colliderect(bloco_vermelho):
        bloco_vermelho_visivel = False
    if bloco_amarelo_visivel and jogador.colliderect(bloco_amarelo):
        bloco_amarelo_visivel = False

    # Desenha o cenário
    tela.fill(PRETO)

    pygame.draw.rect(tela, AZUL, jogador)

    if bloco_verde_visivel:
        pygame.draw.rect(tela, VERDE, bloco_verde)
    if bloco_vermelho_visivel:
        pygame.draw.rect(tela, VERMELHO, bloco_vermelho)
    if bloco_amarelo_visivel:
        pygame.draw.rect(tela, AMARELO, bloco_amarelo)

    pygame.display.flip()

pygame.quit()