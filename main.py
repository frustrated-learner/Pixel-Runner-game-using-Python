import pygame
from pygame import mixer

# Initializing the Pygame
pygame.init()

# Creating some Game Variables
RUNNING = True
CLOCK = pygame.time.Clock()
WIDTH = 800
HEIGHT = 400
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
        self.ground_Y = 300

    # Creating the Function to Add the Background Image on the Screen
    def draw_background(self):
        SCREEN.blit(self.bg, (self.bg_X, self.bg_Y))
        SCREEN.blit(self.ground, (self.ground_X, self.ground_Y))

# Creating the Class for the Player
class PLAYER:
    def __init__(self):
        self.player = pygame.image.load(GAME_SPRITES["player_walk_1"]).convert_alpha()
        self.player_X  = 100
        self.player_Y = 260
        self.player_Y_move = 0
        self.gravity = 0.8
        self.jump = -15
        
        self.player_rect = self.player.get_rect(center = (self.player_X, self.player_Y))
    
    # Creating the Function to Draw the Player
    def draw_player(self):
        # global self.player
        # global self.player_Y_move
        # global self.gravity
        SCREEN.blit(self.player, self.player_rect)
    
        # Adding Gravity to the Player
        self.player_Y_move += self.gravity
        self.player_rect.centery += self.player_Y_move
    
        # Creating the Boundary for the Player
        if self.player_rect.centery >= 260:
            self.player_rect.centery = 260
            self.player = pygame.image.load(GAME_SPRITES["player_walk_1"]).convert_alpha()
        
# Creating the Class for the Main logic of the Game
class MAIN:
    def __init__(self):
        self.background = BACKGROUND()
        self.the_player = PLAYER()

    # Creating the Function to Draw all the Sprites at once
    def draw_all_sprites(self):
        self.the_player.draw_player()


# Assigning the Classes
main_game = MAIN()



# Creating the Main loop of the Game
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        # Creating the Game Keys
        elif event.type == pygame.KEYDOWN:
            # Creating the Player Jumping Keys
            if event.key == pygame.K_SPACE and main_game.the_player.player_rect.centery >= 260:
                jump_sound = pygame.mixer.Sound(GAME_AUDIO["jump"])
                jump_sound.play()
                main_game.the_player.player = pygame.image.load(GAME_SPRITES["jump"]).convert_alpha()
                main_game.the_player.player_Y_move = 0
                main_game.the_player.player_Y_move += main_game.the_player.jump


    # Adding the Background Image
    main_game.background.draw_background()

    # Calling the Functions to Draw the Spites
    main_game.draw_all_sprites()

    # Updating the Display Continiously
    pygame.display.update()

    # Keeping a Fixed FPS
    CLOCK.tick(60)