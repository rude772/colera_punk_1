"""
Cólera Punk 1 - por: Tiago77 - 03/05/2020
Jogo de plataforma com temática de gangues e culturas de rua, inspirado nos coletivos e gangues de Punks do Brasil
"""

import pygame
import os

screen_width = 1600
screen_heigth = 900


class Player(pygame.sprite.Sprite):

    # Configurações de teste do Player. Será desenhado para testar movimentação
    player_width = 25
    player_height = 60
    player_color = (255, 255, 255)

    # Inicialização do Player
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((self.player_width, self.player_height))
        self.surf.fill(self.player_color)
        self.rect = self.surf.get_rect()

        # Posição inicial do Player
        self.rect.bottom = screen_heigth
        self.rect.left = self.player_width * 5

        # Configurações iniciais de vetores de velocidade
        self.change_x = 0
        self.change_y = 0

    # Configurações de movimentos do Player
    def update(self):

        # Definições de parâmetros para gravidade
        self.gravity()
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    # Calcular o efeito da gravidade
    def gravity(self):
        g = self.player_height * 0.27  # Define o valor de gravidade
        self.change_y += g if self.change_y != 0 else 0

        # Checa se o player está no chão
        if self.rect.y >= screen_heigth - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_heigth - self.rect.height

    # Funções para movimentação horizontal
    def go_left(self):
        self.change_x = -10

    def go_right(self):
        self.change_x = 10

    def stop(self):
        self.change_x = 0

    # Função para pular
    def jump(self):
        jump_height = -self.player_height  # Define a altura do pulo
        if self.rect.bottom >= screen_heigth:
            self.change_y = jump_height


class Game:
    running = True
    player = Player()
    clock = pygame.time.Clock()

    def __init__(self):
        pygame.init()  # Iniciar o pygame

        # Configura a tela
        self.tile = pygame.display.set_caption("Cólera Punk 1!")
        self.screen = pygame.display.set_mode((screen_width, screen_heigth))

    # Cria o loop do game
    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                # Define as condições de encerramento do jogo
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.type == pygame.QUIT:
                    self.running = False
                # Define as condições de movimentação do jogador
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.go_right()
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.player.change_x < 0:
                        self.player.stop()
                    if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                        self.player.stop()

            # Atualiza o jogador
            self.player.update()

            # Cria o background
            self.screen.fill((0, 0, 0))

            # Cria o jogador
            self.screen.blit(self.player.surf, self.player.rect)

            # Tela e elementos são renderizados
            pygame.display.flip()

            # Mantém o framerate estável:
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.game_loop()
