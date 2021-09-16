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

# Creating some Game Variables
GAME_OVER = True

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
        # Creating some Required Variables for the Player
        self.player = pygame.image.load(GAME_SPRITES["player_walk_1"]).convert_alpha()
        self.player_X  = 100
        self.player_Y = 260
        self.player_Y_move = 0
        self.gravity = 0.8
        self.jump = -15
        self.player_rect = self.player.get_rect(center = (self.player_X, self.player_Y))

        # Creating some Player Animation Variables
        self.player_walk_1 = pygame.image.load(GAME_SPRITES["player_walk_1"]).convert_alpha()
        self.player_walk_2 = pygame.image.load(GAME_SPRITES["player_walk_2"]).convert_alpha()

        self.player_animation_frames = [
            self.player_walk_1,
            self.player_walk_2
        ]
        
        self.frame_index = 1
    
    # Creating the Function to Draw the Player
    def draw_player(self):
        SCREEN.blit(self.player, self.player_rect)
    
        # Adding Gravity to the Player
        self.player_Y_move += self.gravity
        self.player_rect.centery += self.player_Y_move
    
        # Creating the Boundary for the Player
        if self.player_rect.centery >= self.player_Y:
            self.player_rect.centery = self.player_Y
            self.player = pygame.image.load(GAME_SPRITES["player_walk_1"]).convert_alpha()

    # Creating the Function to Add the Animation
    def add_player_animation(self):
        self.new_player = self.player_animation_frames[self.frame_index]
        self.player_rect = self.new_player.get_rect(center = (float(self.player_rect.centerx), float(self.player_rect.centery)))

        return self.new_player, self.player_rect

# Creating the Class for the Snail 
class SNAIL:
    def __init__(self):
        # Some Required Variables for the Snail
        self.snail = pygame.image.load(GAME_SPRITES["snail1"]).convert_alpha()
        self.snail_X = 850
        self.snail_Y = 282
        self.snail_X_move = -7

        # Variables needed for the Animation
        self.snail1 = pygame.image.load(GAME_SPRITES["snail1"]).convert_alpha()
        self.snail2 = pygame.image.load(GAME_SPRITES["snail2"]).convert_alpha()

        self.snail_animation_frames = [
            self.snail1,
            self.snail2
        ]
        
        self.frame_index = 1

    # Creating the Function to Draw the Snail
    def draw_snail(self):
        self.snail_rect = self.snail.get_rect(center = (self.snail_X, self.snail_Y))
        SCREEN.blit(self.snail, self.snail_rect)

        # Moving the Snail
        self.snail_X += self.snail_X_move

        # Creating the Boundary of Re-position for the Snail
        if self.snail_X <= -50:
            self.snail_X = 850
            
    # Creating the Function to Add the Animation for the Snail
    def add_snail_animation(self):
        self.new_snail = self.snail_animation_frames[self.frame_index]
        self.snail_rect = self.new_snail.get_rect(center = (self.snail_X, self.snail_Y))

        return self.new_snail, self.snail_rect

# Creating the Class for the Fly
class FLY:
    def __init__(self):
        # Creating the Required Variables for the Fly
        self.fly = pygame.image.load(GAME_SPRITES["fly1"]).convert_alpha()
        self.fly_X = 2250
        self.fly_Y = 182
        self.fly_X_move = -7

        # Variables needed for the Animation
        self.fly1 = pygame.image.load(GAME_SPRITES["fly1"]).convert_alpha()
        self.fly2 = pygame.image.load(GAME_SPRITES["fly2"]).convert_alpha()

        self.fly_animation_frames = [
            self.fly1,
            self.fly2
        ]
        
        self.frame_index = 1
        
    # Creating the Function to Draw the Fly
    def draw_fly(self):
        self.fly_rect = self.fly.get_rect(center = (self.fly_X, self.fly_Y))
        SCREEN.blit(self.fly, self.fly_rect)

        # Moving the Snail
        self.fly_X += self.fly_X_move

        # Creating the Boundary of Re-position for the Snail
        if self.fly_X <= -1450:
            self.fly_X = 2250
            
    # Creating the Function to Add the Fly Animation
    def add_fly_animation(self):
        self.new_fly = self.fly_animation_frames[self.frame_index]
        self.fly_rect = self.new_fly.get_rect(center = (self.fly_X, self.fly_Y))

        return self.new_fly, self.fly_rect

# Creating the Class for the Main logic of the Game
class MAIN:
    def __init__(self):
        self.background = BACKGROUND()
        self.the_player = PLAYER()
        self.the_snail = SNAIL()
        self.the_fly = FLY()

    # Creating the Function to Draw all the Sprites at once
    def draw_all_sprites(self):
        self.the_player.draw_player()
        self.the_snail.draw_snail()
        self.the_fly.draw_fly()
        self.check_collision()
        
    # Creating the Function to Check for Collision
    def check_collision(self):
        global RUNNING
        if self.the_player.player_rect.colliderect(self.the_snail.snail_rect) or self.the_player.player_rect.colliderect(self.the_fly.fly_rect):
            RUNNING = False


# Assigning the Classes
main_game = MAIN()

# Creating the Userevents for the Animations

## Player Animation
PLAYER_ANIMATION = pygame.USEREVENT
pygame.time.set_timer(PLAYER_ANIMATION, 150)

## Snail Animation 
SNAIL_ANIMATION = pygame.USEREVENT + 1
pygame.time.set_timer(SNAIL_ANIMATION, 150)

## Fly Animation
FLY_ANIMATION = pygame.USEREVENT + 2
pygame.time.set_timer(FLY_ANIMATION, 150)



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
                
        # Using the Player Animation Event to Animate the Player
        elif event.type == PLAYER_ANIMATION and (main_game.the_player.player_rect.centery >= main_game.the_player.player_Y):
            if main_game.the_player.frame_index < 1:
                main_game.the_player.frame_index += 1
            else:
                main_game.the_player.frame_index = 0

            (main_game.the_player.player), (main_game.the_player.player_rect) = main_game.the_player.add_player_animation()
            
        # Using the Snail Animation Event to Animate the Snail
        elif event.type == SNAIL_ANIMATION:
            if main_game.the_snail.frame_index < 1:
                main_game.the_snail.frame_index += 1
            else:
                main_game.the_snail.frame_index = 0

            (main_game.the_snail.snail), (main_game.the_snail.snail_rect) = main_game.the_snail.add_snail_animation()
            
        # Using the Fly Animation Event to Animate the Fly
        elif event.type == FLY_ANIMATION:
            if main_game.the_fly.frame_index < 1:
                main_game.the_fly.frame_index += 1
            else:
                main_game.the_fly.frame_index = 0

            (main_game.the_fly.fly), (main_game.the_fly.fly_rect) = main_game.the_fly.add_fly_animation()
        

    # Adding the Background Image
    main_game.background.draw_background()

    # Calling the Functions to Draw the Spites
    main_game.draw_all_sprites()

    # Updating the Display Continiously
    pygame.display.update()

    # Keeping a Fixed FPS
    CLOCK.tick(60)