import pygame
from pygame.sprite import Group



from settings import Settings
from game_stats import GameStats
from ship import Ship
#from alien import Alien
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.

    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
    #Make a ship.
    ship = Ship(ai_settings,screen)

    #Mage a bullet Group
    bullets = Group()

    #Make an alien
    #alien = Alien(ai_settings,screen)
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # Main game loop


    while True:

        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings,stats, screen, ship, aliens, bullets)
        #print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
