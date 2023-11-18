import pygame
import sys
import bluemarble_UI
import ground
import player

pygame.init()

pygame.display.set_mode((bluemarble_UI.WIDTH, bluemarble_UI.HEIGHT))

class PygameWindow:
    def __init__(self):
        pygame.init()
        self.width = bluemarble_UI.WIDTH
        self.height = bluemarble_UI.HEIGHT
        self.screen = pygame.display.set_mode((bluemarble_UI.WIDTH, bluemarble_UI.HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_screen = bluemarble_UI.START_MENU(self.screen)

    def run_game(self):
        ground.Board.make_block()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.current_screen = self.current_screen.handle_events(event)
            self.current_screen.update()
            self.current_screen.draw()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    window = PygameWindow()
    window.run_game()
pygame.quit()