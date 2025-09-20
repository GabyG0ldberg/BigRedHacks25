# code for the display and running the game
import pygame
import os

# pygame setup
pygame.init()
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((int(screen_width* 0.75), int((screen_width*.75)* 3 / 4)))
clock = pygame.time.Clock()
running = True
dt = 0
#whether or not we are in the closet
closet = True

#Mid screen height
midheight = screen_height//2
midwidth = screen_width//2

#initalizing images
arrow = pygame.image.load("images/arrow-button.png").convert()
closet = pygame.image.load("images/closet.PNG").convert()
camera = pygame.image.load("images/camera.PNG").convert()
day1 = pygame.image.load("images/day1.jpg").convert()
#TODO: add the rest of the backgrounds and clothes as images

# Load and scale background
#TODO: change the background based on which part of the game we are at
background = day1
background = pygame.transform.scale(background, (screen_width, screen_height))

#Block class that basically just takes an image and constructs it so you can set the position of the image
class Block(pygame.sprite.Sprite):
    def __init__(self, image_path, size=(128, 128), pos=None):
        super().__init__()

        self.visible = False

        try:
            original_image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(original_image, size)
        except pygame.error as e:
            print(f"Could not load image {image_path}: {e}")
            self.image = pygame.Surface(size)
            self.image.fill((255, 0, 0))  # Red fallback

        self.rect = self.image.get_rect()

        if pos is None:
            self.rect = (midwidth, midheight)
        else: 
            self.rect.topleft = pos
    
    def draw(self, surface):
        if self.visible:
            surface.blit(self.image, self.rect)

#2 Groups that aren't really used for much but categorization of elements
all_closet_sprites = pygame.sprite.Group()
all_media_sprites = pygame.sprite.Group()

# Initializing some blocks and adding them to the closet group
#TODO: Add all clothes as blocks
block = Block("images/day1.jpg", pos=(midwidth*1.1, midheight*0.6))
block2 = Block("images/mirror-button.jpg", pos=(midwidth*1.1, midheight*0.6))
all_closet_sprites.add(block)
all_closet_sprites.add(block2)

#Makes a list of all blocks. blocks is an array
blocks = all_closet_sprites.sprites()

#Function so when you click on the arrow, it changes to the next block in the group
current_index = 0
blocks[current_index].visible = True
def show_next_block():
    global current_index
    # Hide current block
    blocks[current_index].visible = False
    # Increment index and wrap around
    current_index = (current_index + 1) % len(blocks)
    # Show next block
    blocks[current_index].visible = True

#Shirts
#shirt1 = Block("images/shirt1.jpg", 100, 150)
#shirt2 = Block("images/shirt2.jpg", 200, 150)
#shirt3 = Block("images/shirt3.jpg", 300, 150)
#shirt4 = Block("images/shirt4.jpg", 400, 150)
#shirt5 = Block("images/shirt5.jpg", 500, 150)

#Pants
#pants1 = Block("images/shirt1.jpg", 100, 250)
#pants2 = Block("images/shirt2.jpg", 200, 250)
#pants3 = Block("images/shirt3.jpg", 300, 350)
#pants4 = Block("images/shirt4.jpg", 400, 450)
#pants5 = Block("images/shirt5.jpg", 500, 550)


# buttons
buttonWidth = screen.get_width()/8
buttonHeight = buttonWidth
class Button:
    def __init__(self, top, image1,image2):
        #initalize the button with top y coordinate 'top' and two images for each state (depending if we are in the closet or not)
        self.top = top
        self.rectangle = pygame.Rect(screen.get_width() -buttonWidth - (screen.get_width()/90), self.top, buttonWidth, buttonHeight) #creates a rectangle base for the button
        self.scaled_image = pygame.transform.scale(image1, (self.rectangle.width, self.rectangle.height)) #scales the image to the size of the button
        self.image1 = image1
        self.image2 = image2
    
    def updateImage(self):
        if closet:
            self.scaled_image = pygame.transform.scale(self.image1, (self.rectangle.width, self.rectangle.height))
        else:
            self.scaled_image = pygame.transform.scale(self.image2, (self.rectangle.width, self.rectangle.height))
            
    def draw(self):
        pygame.draw.rect(screen, "green", self.rectangle)
        screen.blit(self.scaled_image, self.rectangle)

        
    def is_clicked(self, mouse_pos):
        return self.rectangle.collidepoint(mouse_pos)

#This is another button implementation that I made for the left and right arrows of choosing clothes
class Arrow: 
    def __init__(self, image, width,height, pos = None):
        self.image = image  # image should be a pygame.Surface here
        self.scaled_image = pygame.transform.scale(self.image, (width, height))
        self.rectangle = self.scaled_image.get_rect()
        
        if pos is None:
            self.rectangle.center = (midwidth, midheight)
        else: 
            self.rectangle.topleft = pos

    def draw(self):
        screen.blit(self.scaled_image, self.rectangle)

    def is_clicked(self, mouse_pos):
        return self.rectangle.collidepoint(mouse_pos)

#Makes a transparent box, transparency is set with the alpha value 0 = transparent 250 = opaque
class Transparent_Box:
    def __init__(self, pos, size, color, alpha=200):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = color
        self.alpha = alpha

    #transparent surface 
        self.surface = pygame.Surface(size, pygame.SRCALPHA)
        self.surface.fill((*self.color, self.alpha)) 

    def draw(self, surface):
        screen.blit(self.surface, self.rect.topleft)


#Creates elements
box = Transparent_Box((midwidth, midheight*0.45), (300,400), (128, 128, 128))
button1 = Button(screen.get_height() - buttonHeight - (screen.get_width()/90),camera, closet )
arrow_button = Arrow(arrow, buttonWidth-50, buttonHeight-50, pos=(midwidth*1.3, midheight*0.6))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #if the closet/camera button is clicked, we change the state of the game to the opposite
                if button1.rectangle.collidepoint(event.pos):
                    print("Button was clicked!")
                    if closet: 
                        arrow = pygame.image.load("images/arrow-button.png").convert()
                        closet = not closet
                        button1.updateImage() #changes the image depending on where we are
                    else:
                        arrow = pygame.image.load("images/arrow-button.png").convert()
                        closet = not closet
                        button1.updateImage()
                if arrow_button.is_clicked(event.pos):
                    show_next_block ()
                

    # fill the screen with a color to wipe away anything from last frame
    if closet:
        #screen.fill(pygame.Color(255, 217, 228))
        screen.blit(background, (0, 0)) #put the background to the variable background
        all_closet_sprites.draw(screen)
    else:
        screen.fill(pygame.Color(222, 242, 255))

    box.draw(screen)
    button1.draw()
    arrow_button.draw()
    for block in blocks:
        block.draw(screen)
    ##pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    '''
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    '''

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

