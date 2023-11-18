import sys
import bluemarble_UI
from ground import *
from player import *
game_Turn = 0

global board
pygame.init()

class PygameWindow:
    def __init__(self):
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_screen = START_MENU(self.screen)

    def run_game(self):
        board = Board.make_block()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #if User.position == 10:#여기서 말하는 User는 현재 플레이하는 유저
                #    if  User.roll_dice_event()== True:
                #        User.move()
                #if User.position == 20:
                #    if Board.blocks[20].price !=0:
                #        User.receive_Tax(,Board.blocks[20])# 현재 플레이하는 user 넣어야함
                #if User.position == 30:
            self.current_screen = self.current_screen.handle_events(events)
            if type(self.current_screen)==bluemarble_UI.GAME_SCREEN:
                self.current_screen.update()
                self.current_screen.draw(board)
            else:
                self.current_screen.update()
                self.current_screen.draw()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    window = PygameWindow()
    window.run_game()
pygame.quit()