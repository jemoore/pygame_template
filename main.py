import pygame as pg
import sys
from settings import *
from game import Game

class App:
    def __init__(self) -> None:
        self.screen = pg.display.set_mode(WINDOW_SIZE)
        self.clock = pg.time.Clock()
        self.game = Game()
   
    def update(self) -> None:
        self.game.update()
        self.clock.tick()
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}') 

    def draw(self) -> None:
        self.game.draw()
        pg.display.flip()
        
    def get_time(self) -> None:
        self.time = pg.time.get_ticks() * 0.001
        
    def check_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
                
    def run(self) -> None:
        while True:
            self.check_events()
            self.get_time()
            
            self.update()
            self.draw()

            
if __name__ == '__main__':
    app = App()
    app.run()
