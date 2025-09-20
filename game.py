# code for the display and running the game
import pygame

# pygame setup
pygame.init()
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((int(screen_width* 0.75), int((screen_width*.75)* 3 / 4)))
clock = pygame.time.Clock()
pygame.display.set_caption("HACKATHON GAME")
running = True
dt = 0
#elements to track where we are in the game
closet = True
day = 1

#Mid screen height
midheight = screen_height//2
midwidth = screen_width//2

#initalizing images
arrow = pygame.image.load("images/arrow-button.png").convert_alpha()
closet = pygame.image.load("images/closet.PNG").convert()
camera = pygame.image.load("images/camera.PNG").convert()
day1 = pygame.image.load("images/day1.jpg").convert()
day2 = pygame.image.load("images/day2.jpg").convert()
day3 = pygame.image.load("images/day3.jpg").convert()
day4 = pygame.image.load("images/day4.jpg").convert()
av1 = pygame.image.load("images/av1.PNG").convert_alpha()
av2 = pygame.image.load("images/av2.PNG").convert_alpha()
av3 = pygame.image.load("images/av3.PNG").convert_alpha()
av4 = pygame.image.load("images/av4.PNG").convert_alpha()
#day5 = pygame.image.load("images/day5.jpg").convert()


#TODO: add the rest of the backgrounds and clothes as images

day1_top1 = pygame.image.load("images/clothing/top-1.png").convert_alpha()
day1_top2 = pygame.image.load("images/clothing/top-2.png").convert_alpha()
day1_top3 = pygame.image.load("images/clothing/top-3.png").convert_alpha()
day1_top4 = pygame.image.load("images/clothing/top-7.png").convert_alpha()
day1_bot1 = pygame.image.load("images/clothing/bottom-1.png").convert_alpha()
day1_bot2 = pygame.image.load("images/clothing/bottom-2.png").convert_alpha()
day1_bot3 = pygame.image.load("images/clothing/bottom-3.png").convert_alpha() # Wear something bright today?
day1_bot4 = pygame.image.load("images/clothing/bottom-4.png").convert_alpha()
day2_top1 = pygame.image.load("images/clothing/top-8.png").convert_alpha()
day2_top2 = pygame.image.load("images/clothing/top-4.png").convert_alpha()
day2_top3 = pygame.image.load("images/clothing/top-5.png").convert_alpha()
day2_top4 = pygame.image.load("images/clothing/top-10.png").convert_alpha()
day2_bot1 = pygame.image.load("images/clothing/bottom-5.png").convert_alpha() # People are feeling festive today
day2_bot2 = pygame.image.load("images/clothing/bottom-6.png").convert_alpha()
day2_bot3 = pygame.image.load("images/clothing/bottom-7.png").convert_alpha()
day2_bot4 = pygame.image.load("images/clothing/bottom-10.png").convert_alpha()
day3_top1 = pygame.image.load("images/clothing/top-6.png").convert_alpha()
day3_top2 = pygame.image.load("images/clothing/top-11.png").convert_alpha()
day3_top3 = pygame.image.load("images/clothing/top-12.png").convert_alpha() # Everyone's loving rog pretty punk zoo core 
day3_top4 = pygame.image.load("images/clothing/top-13.png").convert_alpha()
day3_bot1 = pygame.image.load("images/clothing/bottom-8.png").convert_alpha()
day3_bot2 = pygame.image.load("images/clothing/bottom-12.png").convert_alpha()
day3_bot3 = pygame.image.load("images/clothing/bottom-14.png").convert_alpha()
day3_bot4 = pygame.image.load("images/clothing/bottom-15.png").convert_alpha()
day4_top1 = pygame.image.load("images/clothing/top-9.png").convert_alpha()
day4_top2 = pygame.image.load("images/clothing/top-14.png").convert_alpha()
day4_top3 = pygame.image.load("images/clothing/top-15.png").convert_alpha() # Feral house cat whisker anarchy grunge
day4_top4 = pygame.image.load("images/clothing/top-16.png").convert_alpha()
day4_bot1 = pygame.image.load("images/clothing/bottom-13.png").convert_alpha()
day4_bot2 = pygame.image.load("images/clothing/bottom-11.png").convert_alpha()
day4_bot3 = pygame.image.load("images/clothing/bottom-9.png").convert_alpha()
day4_bot4 = pygame.image.load("images/clothing/bottom-16.png").convert_alpha()

class Background:
    def __init__(self, file):
        self.setBackground(file)
        self.day = 1
    #TODO: change the background based on which part of the game we are at
    def setBackground(self, file):
        self.background = file #image
        self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

'''
class Day:
    def __init__(self):
    #set background
        self.num = 1
        
    #set clothes for the day 
    def changeDay(self, dayNum):
        self.num = dayNum
'''    

#Block class that basically just takes an image and constructs it so you can set the position of the image
class Block(pygame.sprite.Sprite):
    def __init__(self, image, size=(128, 128), pos=None):
        super().__init__()
        self.visible = False

        try:
            self.image = pygame.transform.scale(image, size)
        except pygame.error as e:
            print(f"Could not load image {image}: {e}")
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
day1_shirts = pygame.sprite.Group()
day2_shirts = pygame.sprite.Group()
day3_shirts = pygame.sprite.Group()
day4_shirts = pygame.sprite.Group()
day1_pants = pygame.sprite.Group()
day2_pants = pygame.sprite.Group()
day3_pants = pygame.sprite.Group()
day4_pants = pygame.sprite.Group()

all_media_sprites = pygame.sprite.Group()

# Initializing some blocks and adding them to the closet group
#TODO: Add all clothes as blocks
day1_shirt1 = Block(day1_top1, pos=(midwidth*1.1, midheight*0.6))
day1_shirt2 = Block(day1_top2, pos=(midwidth*1.1, midheight*0.6))
day1_shirt3 = Block(day1_top3, pos=(midwidth*1.1, midheight*0.6))
day1_shirt4 = Block(day1_top4, pos=(midwidth*1.1, midheight*0.6))

day2_shirt1 = Block(day2_top1, pos=(midwidth*1.1, midheight*0.6))
day2_shirt2 = Block(day2_top2, pos=(midwidth*1.1, midheight*0.6))
day2_shirt3 = Block(day2_top3, pos=(midwidth*1.1, midheight*0.6))
day2_shirt3 = Block(day2_top4, pos=(midwidth*1.1, midheight*0.6))

day3_shirt1 = Block(day3_top1, pos=(midwidth*1.1, midheight*0.6))
day3_shirt2 = Block(day3_top2, pos=(midwidth*1.1, midheight*0.6))
day3_shirt3 = Block(day3_top3, pos=(midwidth*1.1, midheight*0.6))
day3_shirt4 = Block(day3_top4, pos=(midwidth*1.1, midheight*0.6))

day4_shirt1 = Block(day4_top1, pos=(midwidth*1.1, midheight*0.6))
day4_shirt2 = Block(day4_top2, pos=(midwidth*1.1, midheight*0.6))
day4_shirt3 = Block(day4_top3, pos=(midwidth*1.1, midheight*0.6))
day4_shirt4 = Block(day4_top4, pos=(midwidth*1.1, midheight*0.6))

day1_pants1 = Block(day1_bot1, pos=(midwidth*1.1, midheight*0.9))
day1_pants2 = Block(day1_bot2, pos=(midwidth*1.1, midheight*0.9))
day1_pants3 = Block(day1_bot3, pos=(midwidth*1.1, midheight*0.9))
day1_pants4 = Block(day1_bot4, pos=(midwidth*1.1, midheight*0.9))

day2_pants1 = Block(day2_bot1, pos=(midwidth*1.1, midheight*0.9))
day2_pants2 = Block(day2_bot2, pos=(midwidth*1.1, midheight*0.9))
day2_pants3 = Block(day2_bot3, pos=(midwidth*1.1, midheight*0.9))
day2_pants4 = Block(day2_bot4, pos=(midwidth*1.1, midheight*0.9))

day3_pants1 = Block(day3_bot1, pos=(midwidth*1.1, midheight*0.9))
day3_pants2 = Block(day3_bot2, pos=(midwidth*1.1, midheight*0.9))
day3_pants3 = Block(day3_bot3, pos=(midwidth*1.1, midheight*0.9))
day3_pants4 = Block(day3_bot4, pos=(midwidth*1.1, midheight*0.9))

day4_pants1 = Block(day4_bot1, pos=(midwidth*1.1, midheight*0.9))
day4_pants2 = Block(day4_bot2, pos=(midwidth*1.1, midheight*0.9))
day4_pants3 = Block(day4_bot3, pos=(midwidth*1.1, midheight*0.9))
day4_pants4 = Block(day4_bot4, pos=(midwidth*1.1, midheight*0.9))

day1_shirts.add(day1_shirt1)
day1_shirts.add(day1_shirt2)
day1_shirts.add(day1_shirt3)
day1_shirts.add(day1_shirt4)

day2_shirts.add(day1_shirt1)
day2_shirts.add(day1_shirt2)
day2_shirts.add(day1_shirt3)
day2_shirts.add(day1_shirt4)

day3_shirts.add(day1_shirt1)
day3_shirts.add(day1_shirt2)
day3_shirts.add(day1_shirt3)
day3_shirts.add(day1_shirt4)

day4_shirts.add(day1_shirt1)
day4_shirts.add(day1_shirt2)
day4_shirts.add(day1_shirt3)
day4_shirts.add(day1_shirt4)

day1_pants.add(day1_pants1)
day1_pants.add(day1_pants2)
day1_pants.add(day1_pants3)
day1_pants.add(day1_pants4)

day2_pants.add(day1_pants1)
day2_pants.add(day1_pants2)
day2_pants.add(day1_pants3)
day2_pants.add(day1_pants4)

day3_pants.add(day1_pants1)
day3_pants.add(day1_pants2)
day3_pants.add(day1_pants3)
day3_pants.add(day1_pants4)

day4_pants.add(day1_pants1)
day4_pants.add(day1_pants2)
day4_pants.add(day1_pants3)
day4_pants.add(day1_pants4)

dayspants = [day1_pants,day2_pants,day3_pants,day4_pants]
daystops = [day1_shirts,day2_shirts,day3_shirts,day4_shirts]

#Makes a list of all blocks. blocks is an array
current_group_shirts = day1_shirts.sprites()
current_group_pants = day1_pants.sprites()


#Function so when you click on the arrow, it changes to the next block in the group
current_index = 0
current_group_shirts = day1_shirts.sprites()
current_group_pants = day1_pants.sprites()
current_group_shirts[current_index].visible = True
current_group_pants[current_index].visible = True

class Day:
    def pick_group(day_num):
            global current_group_pants, current_group_shirts
            current_group_pants = dayspants[day].sprites()
            current_group_shirts = daystops[day].sprites()

    match day: 
        case 1:
            pick_group(1)
        case 2:
            pick_group(2)
        case 3:
            pick_group(3)
        case 4: 
            pick_group(4)


def show_next_block(group):
    global current_index
    # Hide current block
    group[current_index].visible = False
    # Increment index and wrap around
    current_index = (current_index + 1) % len(group)
    # Show next block
    group[current_index].visible = True

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
    def __init__(self, image, width,height, right, pos = None):
        self.image = image  # image should be a pygame.Surface here
        self.scaled_image = pygame.transform.scale(self.image, (width, height))
        self.rectangle = self.scaled_image.get_rect()
        self.right = right
        
        
        if pos is None:
            self.rectangle.center = (midwidth, midheight)
        else: 
            self.rectangle.topleft = pos
        if not right:
            self.scaled_image = pygame.transform.flip(self.scaled_image, 1,0)

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
arrowTopRight = Arrow(arrow, buttonWidth-50, buttonHeight-50, 1, pos=(midwidth*1.4, midheight*0.6))
arrowTopLeft = Arrow(arrow, buttonWidth-50, buttonHeight-50, 0, pos=(midwidth*0.95, midheight*0.6))
arrowBotRight = Arrow(arrow, buttonWidth-50, buttonHeight-50, 1, pos=(midwidth*1.4, midheight))
arrowBotLeft = Arrow(arrow, buttonWidth-50, buttonHeight-50, 0, pos=(midwidth*0.95, midheight))
bg = Background(day1)
bg.draw(screen)

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
                        bg.day +=1
                        match bg.day:
                            case 1:
                                bg.setBackground(day1)
                            case 2:
                                bg.setBackground(day2)
                            case 3:
                                bg.setBackground(day3)
                            case 4:
                                bg.setBackground(day4)
                        print(bg.day)
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
         #put the background to the variable background2
        day1_pants.draw(screen)
        bg.draw(screen)
    else:
        screen.fill(pygame.Color(222, 242, 255))

    box.draw(screen)
    button1.draw()
    arrowTopRight.draw()
    arrowTopLeft.draw()
    arrowBotRight.draw()
    arrowBotLeft.draw()
    '''
    for block in current_group_pants:
        block.draw(screen)
    for block in current_group_shirts:
        block.draw(screen)
    '''
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

