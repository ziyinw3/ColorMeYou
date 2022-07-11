# stage 1

import pygame

from src.constants import PLAYER_WIDTH, PLAYER_HEIGHT, MAGENTA, CYAN, BLACK, GREEN, YELLOW, BLUE, SCREEN_WIDTH, \
    SCREEN_HEIGHT
from src.entities.camera import Camera
from src.entities.cartridge import Cartridge, all_cartridges
from src.entities.cartridge_set import CartridgeSet
from src.entities.paper import Paper
from src.entities.platform import Platform
from src.entities.platform_set import PlatformSet
from src.entities.player import Player
from src.entities.win_scene import WinScene
from src.gui.toggler import Toggler
# load in three colored backgrounds
# keep track of state stuff
from src.scenes.scene import Scene

P1 = Platform(BLACK, 0, 540, 300, 300, True)
P2 = Platform(CYAN, 400, 440, 200, 40, True)
P3 = Platform(MAGENTA, 700, 340, 200, 40, False)
P4 = Platform(YELLOW, 1000, 240, 200, 40, False)
P5 = Platform(GREEN, 1300, 140, 200, 40, True)
P6 = Platform(BLUE, 1500, 200, 40, 400, True)
P7 = Platform(BLACK, 1800, 100, 600, 700, True)

test_plat = Platform(BLUE, 300, 200, 40, 500, True)


class Stage(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.platforms = [P1, P2, P3, P4, P5, P6, P7, test_plat]
        self.player = Player(100, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.toggler = Toggler()
        self.platform_set = PlatformSet()
        self.cyan_cartridge = Cartridge(0, 400, 340, 92, 84)
        self.magenta_cartridge = Cartridge(1, 600, 240, 92, 84)
        self.yellow_cartridge = Cartridge(2, 800, 140, 92, 84)
        self.egg_cartridge = Cartridge(3, 400, 140, 96, 95)
        self.all_cartridges = all_cartridges
        self.cartridge_set = CartridgeSet(self.all_cartridges)
        self.paper = Paper(1100, 100, 80, 96, True)

        self.camera = Camera(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, screen)
        self.moving_entities = []
        for platform in self.platforms:
            self.moving_entities.append(platform)
        for cartridge in self.all_cartridges:
            self.moving_entities.append(cartridge)
        self.moving_entities.append(self.paper)

    def update(self):
        super().update()
        # update player
        self.player.update_position()
        self.player.walk_counter()
        self.player.detect_collision(self.platforms)
        # update platforms
        self.toggler.toggle_platforms(self.platform_set.drawn_platforms)
        self.platform_set.update_platforms(self.camera, self.platforms)
        # update objectives
        for cartridge in self.all_cartridges:
            cartridge.detect_collision(self.player)
        self.cartridge_set.update_collected()

        # update paper
        self.cartridge_set.check_win()
        self.paper.stand_counter()
        self.camera.box_target_camera(self.player)
        print(self.paper.rect, self.player.rect)

    def draw(self):
        super().draw()
        self.toggler.draw(self.screen)
        for platform in self.platform_set.drawn_platforms:
            platform.draw(self.screen)

        for cartridge in self.all_cartridges:
            cartridge.draw(self.screen)

        self.paper.draw(self.screen)

        # self.camera.custom_draw(self.player, self.moving_entities)

        self.player.draw(self.screen)

    def process_event(self, event: pygame.event.Event):
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                self.player.states[0] = True
            if event.key == pygame.K_f:
                self.player.states[1] = True
            if event.key == pygame.K_e:
                self.player.states[2] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.player.states[0] = False
            if event.key == pygame.K_f:
                self.player.states[1] = False
            if event.key == pygame.K_e:
                self.player.states[2] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.toggler.toggle_clockwise()
            if event.button == 5:
                self.toggler.toggle_counterclockwise()
        if self.cartridge_set.no_egg_win:
            self.paper.navigate(self.player, self.screen, WinScene)
