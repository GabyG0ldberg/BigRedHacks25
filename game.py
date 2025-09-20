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

#initalizing images
arrow = pygame.image.load("images/closet.PNG").convert()
mirror = pygame.image.load("images/camera.PNG").convert()

class Block(pygame.sprite.Sprite):
    def __init__(self, image_path, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        
        # Load the image from file
        try:
            self.image = pygame.image.load(image_path)
        except pygame.error as e:
            print(f"Could not load image {image_path}: {e}")
            # Create a fallback colored rectangle
            self.image = pygame.Surface([64, 64])
            self.image.fill((255, 0, 0))  # Red fallback
        
        # Get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

all_closet_sprites = pygame.sprite.Group()
all_media_sprites = pygame.sprite.Group()

# Usage
block = Block("images/mirror-button.jpg", 100, 150)

#Shirts
#shirt1 = Block("images/shirt1.jpg", 100, 150)
#shirt2 = Block("images/shirt2.jpg", 200, 150)
#shirt3 = Block("images/shirt3.jpg", 300, 150)
#shirt4 = Block("images/shirt4.jpg", 400, 150)
#shirt5 = Block("images/shirt5.jpg", 500, 150)

'''
shirts = [shirt1,shirt2,shirt3,shirt4,shirt5]
for item in shirts:
    all_closet_sprites.add(item)
'''

#Pants
#pants1 = Block("images/shirt1.jpg", 100, 250)
#pants2 = Block("images/shirt2.jpg", 200, 250)
#pants3 = Block("images/shirt3.jpg", 300, 350)
#pants4 = Block("images/shirt4.jpg", 400, 450)
#pants5 = Block("images/shirt5.jpg", 500, 550)

'''
pants = [pants1,pants2,pants3,pants4,pants5]
for item in shirts:
    all_closet_sprites.add(item)
'''

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


button1 = Button(screen.get_height() - buttonHeight - (screen.get_width()/90),mirror, arrow )

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
                if button1.is_clicked(event.pos):
                    print("Button was clocked")

    # fill the screen with a color to wipe away anything from last frame
    
    if closet:
        screen.fill(pygame.Color(255, 217, 228))
        #all_closet_sprites.draw(screen)
    else:
        screen.fill(pygame.Color(222, 242, 255))

    button1.draw()
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

