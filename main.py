import pygame
from pygame import mixer

# Initializing the Pygame
pygame.init()

# Creating some Game Variables
RUNNING = True
CLOCK = pygame.time.Clock()
WIDTH = 800
HEIGHT = 300
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
ICON = pygame.image.load("graphics/icon/icon.png").convert_alpha()
pygame.display.set_icon(ICON)
pygame.display.set_caption("Pixel Runner")

# Adding the Game Sprites Using a Dictionary
GAME_SPRITES = {
    "fly1" : "graphics/fly/fly1.png",
    "fly2" : "graphics/fly/fly2.png",
    "jump" : "graphics/player/jump.png",
    "player_stand" : "graphics/player/player_stand.png",
    "player_walk_1" : "graphics/player/player_walk_1.png",
    "player_walk_2" : "graphics/player/player_walk_2.png",
    "snail1" : "graphics/snail/snail1.png",
    "snail2" : "graphics/snail/snail2.png"
}

# Adding the Background
GAME_SPRITES["bg"] = "graphics/bg.png"
GAME_SPRITES["ground"] = "graphics/ground.png"

# Adding the Game Audio Using a Dictionary
GAME_AUDIO = {
    "jump" : "audio/jump.mp3",
    "music" : "audio/music.wav"
}

# Creating a Class for the Game Background
class BACKGROUND:
    def __init__(self):
        
        # Creating some Background Variables
        self.bg = pygame.image.load(GAME_SPRITES["bg"]).convert_alpha()
        self.bg_X = 0
        self.bg_Y = 0

        # Creating some Ground Variables
        self.ground = pygame.image.load(GAME_SPRITES["ground"]).convert_alpha()
        self.ground_X = 0
        self.ground_Y = 230

    # Creating the Function to Add the Background Image on the Screen
    def draw_background(self):
        SCREEN.blit(self.bg, (self.bg_X, self.bg_Y))
        SCREEN.blit(self.ground, (self.ground_X, self.ground_Y))

        
# Creating the Class for the Main logic of the Game
class MAIN:
    def __init__(self):
        self.background = BACKGROUND()


# Assigning the Classes
main_game = MAIN()



# Creating the Main loop of the Game
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    # Adding the Background Image
    main_game.background.draw_background()

    # Updating the Display Continiously
    pygame.display.update()

    # Keeping a Fixed FPS
    CLOCK.tick(60)