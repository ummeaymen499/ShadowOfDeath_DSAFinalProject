import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    '''Main game class'''
    def __init__(self):
        '''Initialize pygame, set screen, clock, delta time, global trigger and global event
        and start new game'''
        pg.init()   # Initialize pygame
        pg.mouse.set_visible(False) # Hide mouse
        self.screen = pg.display.set_mode(RES) # Set screen
        self.clock = pg.time.Clock() # Set clock
        self.delta_time = 1 # Set delta time
        self.global_trigger = False # Set global trigger
        
        self.global_event = pg.USEREVENT + 0    # Set global event
        pg.time.set_timer(self.global_event, 40)    # Set global event timer
        self.new_game() # Start new game

    def show_start_message(self):
        '''Display start message for 3 seconds'''
        background_image = pg.image.load('D:/DSA Final Project/aymen.png')
        background_image = pg.transform.scale(background_image, RES)
        font = pg.font.SysFont('ALGERIAN', 120)

        message = font.render('Shadow Of Death', True, pg.Color('white'))
        rect = message.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
        self.screen.blit(background_image, (0, 0))
        self.screen.blit(message, rect)
        pg.display.flip()
        pg.time.delay(500)

    
        # Wait for user to press any key
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    waiting = False

    def show_rules(self):
        '''Display game rules'''
        background_image = pg.image.load('D:/DSA Final Project/aymen.png')
        background_image = pg.transform.scale(background_image, RES)
        font = pg.font.SysFont('Arial', 40)

        rules = [
            "In this action-adventure game,players navigate a perilous grid-based on ",
            "environment filled with hostile non-player characters(NPCs).The primary ",
            "objective is to survive by defeating these enemies while managing health ",
            "and navigating obstacles.Players must employ strategic combat tactics and ",
            "utilize a pathfinding system to outmaneuver NPCs that actively seek them  ",
            "out. The game features immersive visuals and sound effects, enhancing the ",
            "experience as players explore, engage in combat, and strive for victory ",
            "over relentless foes.Ultimately,the game challenges players to demonstrate ",
            "skill and resourcefulness in overcoming the dangers of the game world."
        ]

        self.screen.blit(background_image, (0, 0))
        for i, rule in enumerate(rules):
            message = font.render(rule, True, pg.Color('white'))
            rect = message.get_rect(center=(HALF_WIDTH, HALF_HEIGHT - 180 + i * 50))
            self.screen.blit(message, rect)
            pg.display.flip()
            pg.time.delay(50)


        # Wait for user to press any key
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    waiting = False

    def new_game(self):
        '''Start new game
        Create map, player, object renderer, ray casting, object handler, weapon, sound and path finding
        and play music'''
        self.sound = Sound(self)    # Create sound
        pg.mixer.music.play(-1) # Play music
        self.show_start_message()  # Show start message
        self.show_rules()  # Show game rules

        self.map = Map(self)   # Create map
        self.player = Player(self)  # Create player
        self.object_renderer = ObjectRenderer(self) # Create object renderer
        self.raycasting = RayCasting(self)  # Create ray casting
        self.object_handler = ObjectHandler(self)   # Create object handler
        self.weapon = Weapon(self)  # Create weapon
        
        self.pathfinding = PathFinding(self)    # Create path finding
        #pg.mixer.music.play(-1) # Play music

    def update(self):
        '''Update game
        Update player, ray casting, object handler, weapon and display fps
        and set delta time'''
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
