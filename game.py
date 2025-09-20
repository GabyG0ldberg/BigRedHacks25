# code for the display and running the game
import pygame

# pygame setup
pygame.init()
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((int(screen_width* 0.75), int((screen_width*.75)* 3 / 4)))
clock = pygame.time.Clock()
pygame.display.set_caption("FASTEST FASHION")
running = True
dt = 0
#elements to track where we are in the game
closet = True
endScreen = False
#Mid screen height
midheight = screen_height//2
midwidth = screen_width//2
topVisible = False
botVisible = False
corTop = False
corBot = False

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
day1_bad = pygame.image.load("images/day1_bad.png").convert()
day2_bad = pygame.image.load("images/day2_bad.png").convert()
day3_bad = pygame.image.load("images/day3_bad.png").convert()
day4_bad= pygame.image.load("images/day4_bad.png").convert()
day1_good = pygame.image.load("images/day1_good.png").convert()
day2_good = pygame.image.load("images/day2_good.png").convert()
day3_good = pygame.image.load("images/day3_good.png").convert()
day4_good = pygame.image.load("images/day4_good.png").convert()
#gif = pygame.image.load("images/spongebob-squarepants-to-do-list.gif").convert()
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
day2_top3 = pygame.image.load("images/clothing/top-5.png").convert_alpha() # People are feeling festive today
day2_top4 = pygame.image.load("images/clothing/top-10.png").convert_alpha() 
day2_bot1 = pygame.image.load("images/clothing/bottom-5.png").convert_alpha() 
day2_bot2 = pygame.image.load("images/clothing/bottom-6.png").convert_alpha()
day2_bot3 = pygame.image.load("images/clothing/bottom-7.png").convert_alpha()
day2_bot4 = pygame.image.load("images/clothing/bottom-10.png").convert_alpha()
day3_top1 = pygame.image.load("images/clothing/top-6.png").convert_alpha()
day3_top2 = pygame.image.load("images/clothing/top-11.png").convert_alpha()
day3_top3 = pygame.image.load("images/clothing/top-12.png").convert_alpha() 
day3_top4 = pygame.image.load("images/clothing/top-13.png").convert_alpha() # Everyone's loving frog pretty punk zoo core 
day3_bot1 = pygame.image.load("images/clothing/bottom-8.png").convert_alpha() # Everyone's loving frog pretty punk zoo core  
day3_bot2 = pygame.image.load("images/clothing/bottom-12.png").convert_alpha()
day3_bot3 = pygame.image.load("images/clothing/bottom-14.png").convert_alpha()
day3_bot4 = pygame.image.load("images/clothing/bottom-15.png").convert_alpha()
day4_top1 = pygame.image.load("images/clothing/top-9.png").convert_alpha()
day4_top2 = pygame.image.load("images/clothing/top-14.png").convert_alpha()
day4_top3 = pygame.image.load("images/clothing/top-15.png").convert_alpha() # Feral whisker anarchy grunge
day4_top4 = pygame.image.load("images/clothing/top-16.png").convert_alpha()
day4_bot1 = pygame.image.load("images/clothing/bottom-13.png").convert_alpha()
day4_bot2 = pygame.image.load("images/clothing/bottom-11.png").convert_alpha()
day4_bot3 = pygame.image.load("images/clothing/bottom-9.png").convert_alpha()
day4_bot4 = pygame.image.load("images/clothing/bottom-16.png").convert_alpha() # Feral whisker anarchy grunge

class Background:
    def __init__(self, file,fileav):
        self.setBackground(file, fileav)
        self.day = 1
    def setBackground(self, filebg, fileav):
        self.background = filebg #image
        self.background = pygame.transform.scale(self.background,(int(screen_width* 0.75), int((screen_width*.75)* 3 / 4)))
        self.avatar = fileav
        self.avatar = pygame.transform.scale(self.avatar, (screen.get_width()*.9, screen.get_height()*1.05))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.avatar, (-1 * screen_width/15, screen_height/25))

#Block class that basically just takes an image and constructs it so you can set the position of the image
class Block(pygame.sprite.Sprite):
    def __init__(self, imagefile, size=(400, 400), pos=None):
        super().__init__()
        self.visible = False
        self.imagefile = imagefile

        try:
            self.image = pygame.transform.scale(imagefile, size)
        except pygame.error as e:
            print(f"Could not load image {imagefile}: {e}")
            self.image = pygame.Surface(size)
            self.image.fill((255, 0, 0))  # Red fallback

        self.rect = self.image.get_rect()

        if pos is None:
            self.rect = (midwidth, midheight)
        else: 
            self.rect.topleft = pos

        # Shrink the clickable area (bounding box)
        shrink_by = 0.7  # Use 70% of the original size
        self.hitbox = self.rect.inflate(-self.rect.width * (1 - shrink_by),
                                        -self.rect.height * (1 - shrink_by))
    
    def draw(self, surface):
        if self.visible:
            surface.blit(self.image, self.rect)
    
    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)



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
day1_shirt1 = Block(day1_top1, pos=(midwidth/1.07, midheight*0.3))
day1_shirt2 = Block(day1_top2, pos=(midwidth/1.07, midheight*0.3))
day1_shirt3 = Block(day1_top3, pos=(midwidth/1.07, midheight*0.3))
day1_shirt4 = Block(day1_top4, pos=(midwidth/1.07, midheight*0.3))

day2_shirt1 = Block(day2_top1, pos=(midwidth/1.07, midheight*0.3))
day2_shirt2 = Block(day2_top2, pos=(midwidth/1.07, midheight*0.3))
day2_shirt3 = Block(day2_top3, pos=(midwidth/1.07, midheight*0.3))
day2_shirt4 = Block(day2_top4, pos=(midwidth/1.07, midheight*0.3))

day3_shirt1 = Block(day3_top1, pos=(midwidth/1.07, midheight*0.3))
day3_shirt2 = Block(day3_top2, pos=(midwidth/1.07, midheight*0.3))
day3_shirt3 = Block(day3_top3, pos=(midwidth/1.07, midheight*0.3))
day3_shirt4 = Block(day3_top4, pos=(midwidth/1.07, midheight*0.3))

day4_shirt1 = Block(day4_top1, pos=(midwidth/1.07, midheight*0.3))
day4_shirt2 = Block(day4_top2, pos=(midwidth/1.07, midheight*0.3))
day4_shirt3 = Block(day4_top3, pos=(midwidth/1.07, midheight*0.3))
day4_shirt4 = Block(day4_top4, pos=(midwidth/1.07, midheight*0.3))

day1_pants1 = Block(day1_bot1, pos=(midwidth/1.07, midheight*0.45))
day1_pants2 = Block(day1_bot2, pos=(midwidth/1.07, midheight*0.45))
day1_pants3 = Block(day1_bot3, pos=(midwidth/1.07, midheight*0.45))
day1_pants4 = Block(day1_bot4, pos=(midwidth/1.07, midheight*0.45))
day2_pants1 = Block(day2_bot1, pos=(midwidth/1.07, midheight*0.45))
day2_pants2 = Block(day2_bot2, pos=(midwidth/1.07, midheight*0.45))
day2_pants3 = Block(day2_bot3, pos=(midwidth/1.07, midheight*0.45))
day2_pants4 = Block(day2_bot4, pos=(midwidth/1.07, midheight*0.45))

day3_pants1 = Block(day3_bot1, pos=(midwidth/1.07, midheight*0.45))
day3_pants2 = Block(day3_bot2, pos=(midwidth/1.07, midheight*0.45))
day3_pants3 = Block(day3_bot3, pos=(midwidth/1.07, midheight*0.45))
day3_pants4 = Block(day3_bot4, pos=(midwidth/1.07, midheight*0.45))

day4_pants1 = Block(day4_bot1, pos=(midwidth/1.07, midheight*0.45))
day4_pants2 = Block(day4_bot2, pos=(midwidth/1.07, midheight*0.45))
day4_pants3 = Block(day4_bot3, pos=(midwidth/1.07, midheight*0.45))
day4_pants4 = Block(day4_bot4, pos=(midwidth/1.07, midheight*0.45))

day1_shirts.add(day1_shirt1)
day1_shirts.add(day1_shirt2)
day1_shirts.add(day1_shirt3)
day1_shirts.add(day1_shirt4)

day2_shirts.add(day2_shirt1)
day2_shirts.add(day2_shirt2)
day2_shirts.add(day2_shirt3)
day2_shirts.add(day2_shirt4)

day3_shirts.add(day3_shirt1)
day3_shirts.add(day3_shirt2)
day3_shirts.add(day3_shirt3)
day3_shirts.add(day3_shirt4)

day4_shirts.add(day4_shirt1)
day4_shirts.add(day4_shirt2)
day4_shirts.add(day4_shirt3)
day4_shirts.add(day4_shirt4)

day1_pants.add(day1_pants1)
day1_pants.add(day1_pants2)
day1_pants.add(day1_pants3)
day1_pants.add(day1_pants4)

day2_pants.add(day2_pants1)
day2_pants.add(day2_pants2)
day2_pants.add(day2_pants3)
day2_pants.add(day2_pants4)

day3_pants.add(day3_pants1)
day3_pants.add(day3_pants2)
day3_pants.add(day3_pants3)
day3_pants.add(day3_pants4)

day4_pants.add(day4_pants1)
day4_pants.add(day4_pants2)
day4_pants.add(day4_pants3)
day4_pants.add(day4_pants4)

dayspants = [day1_pants,day2_pants,day3_pants,day4_pants]
daystops = [day1_shirts,day2_shirts,day3_shirts,day4_shirts]

#Makes a list of all blocks. blocks is an array
global current_group_shirts
global current_group_pants 

current_group_shirts = day1_shirts.sprites()
current_group_pants = day1_pants.sprites()

level_up_outfits = [
    (None, day1_pants3),             # any shirt, specific pants
    (day2_shirt3, None),             # turtleneck shirt, any pants
    (day3_shirt4, day3_pants1),      # specific shirt and pants
    (day4_shirt3, day4_pants4)
]

#Function so when you click on the arrow, it changes to the next block in the group
current_index_top = 0
current_index_bottom = 0
'''
current_group_shirts = day1_shirts.sprites()
current_group_pants = day1_pants.sprites()
current_group_shirts[current_index].visible = True
current_group_pants[current_index].visible = True
'''

class Day:
    def __init__(self):
        self.day = 1
        pass
    
    def change_group(self, day_num):
            global current_group_pants, current_group_shirts
            current_group_pants = dayspants[day_num-1].sprites()
            current_group_shirts = daystops[day_num-1].sprites()
            current_group_shirts[current_index_top].visible = True
            current_group_pants[current_index_bottom].visible = True

    def pick_group(self):
        match self.day: 
            case 1:
                self.change_group(1)
            case 2:
                self.change_group(2)
            case 3:
                self.change_group(3)
            case 4: 
                self.change_group(4)

day = Day()
day.pick_group()

def show_next_block_top(group):
    global current_index_top
    # Hide current block
    group[current_index_top].visible = False
    # Increment index and wrap around
    current_index_top = (current_index_top + 1) % len(group)
    # Show next block
    group[current_index_top].visible = True

def show_next_block_bottom(group):
    global current_index_bottom
    # Hide current block
    group[current_index_bottom].visible = False
    # Increment index and wrap around
    current_index_bottom = (current_index_bottom + 1) % len(group)
    # Show next block
    group[current_index_bottom].visible = True

def show_prev_block_top(group):
    global current_index_top
    # Hide current block
    group[current_index_top].visible = False
    # Increment index and wrap around
    current_index_top = (current_index_top - 1) % len(group)
    # Show next block
    group[current_index_top].visible = True
def show_prev_block_bottom(group):
    global current_index_bottom
    # Hide current block
    group[current_index_bottom].visible = False
    # Increment index and wrap around
    current_index_bottom = (current_index_bottom - 1) % len(group)
    # Show next block
    group[current_index_bottom].visible = True

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


class Text_Box:
    def __init__(self, pos, caption, box_size=(400, 150)):
        
        self.font = pygame.font.Font(None, 28)  # Smaller font size
        self.text_content = caption
        self.text_color = (255, 255, 255)  # White text
        self.text_background_color = (255, 209, 220)  # Pink box
        if endScreen:
            self.text_background_color = (37, 15, 48)  # Dark box

        # Render the text surface
        self.text_surface = self.font.render(
            self.text_content, True, self.text_color
        )
        self.text_rect = self.text_surface.get_rect()

        # Set up the box rectangle (bigger than text)
        self.box_rect = pygame.Rect(0, 0, *box_size)
        self.box_rect.center = pos

        # Center the text inside the box
        self.text_rect.center = self.box_rect.center

        self.text_surface = self.font.render(self.text_content, True, self.text_color)

        self.alpha = 255
        self.fading = False
        self.visible = True

        # Flag to control visibility
        self.show_text_box = True

    def draw(self, screen):
        if not self.visible:
            return
        # Draw the background box using a new surface so it supports alpha
        box_surface = pygame.Surface(self.box_rect.size, pygame.SRCALPHA)
        box_surface.fill((*self.text_background_color, self.alpha))
        
        # Draw the optional border (static white)
        pygame.draw.rect(screen, (255, 255, 255), self.box_rect, 2, border_radius=12)
        
        # Blit the faded box surface
        screen.blit(box_surface, self.box_rect.topleft)

        # Make a copy of the text surface to apply fade
        text_surface = self.text_surface.copy()
        text_surface.set_alpha(self.alpha)

        screen.blit(text_surface, self.text_rect)

    def start_fade(self):
        self.fading = True

    def update(self):
        if self.fading:
            self.alpha -= 5  # adjust fade speed here
            if self.alpha <= 0:
                self.alpha = 0
                self.fading = False
                self.visible = False
                self.rest()

    def reset(self):
        self.alpha = 255
        self.visible = True
        self.fading = False
    
    def dismiss(self):
        self.show_text_box = False
    
    def is_clicked(self, mouse_pos):
        return self.box_rect.collidepoint(mouse_pos)

#Creates elements
bodyTop = pygame.transform.scale(current_group_shirts[current_index_top].imagefile, (screen.get_width()*.9, screen.get_height()*1.05))
bodyBot = pygame.transform.scale(current_group_pants[current_index_bottom].imagefile, (screen.get_width()*.9, screen.get_height()*1.05))
#text_box = Text_Box((midwidth*0.8,midheight*1.6), "OOh la la, looks like red is in!" , (500,100))
text_refresh = Text_Box( (midwidth,midheight), "REFRESH" , (200,100) )
text_box = Text_Box((midwidth*0.8,midheight*1.6), "OOh la la, looks like festive clothes are in!" , (500,100))
text_box3 = Text_Box((midwidth*0.8,midheight*1.6), "Everyone's loving pretty punk core recently." , (500,100))
text_box4 = Text_Box((midwidth*0.8,midheight*1.6), "Feral Whisker Anarchy Grunge. It's the only way." , (500,100))
text_box2 = Text_Box((midwidth,midheight), "this shirt is OLD!" , (200,100))
show_box2 = False
box = Transparent_Box((midwidth, midheight*0.45), (300,400), (128, 128, 128))
button1 = Button(screen.get_height() - buttonHeight - (screen.get_width()/90),camera, closet )
arrowTopRight = Arrow(arrow, buttonWidth-50, buttonHeight-50, 1, pos=(midwidth*1.34, midheight*0.65))
arrowTopLeft = Arrow(arrow, buttonWidth-50, buttonHeight-50, 0, pos=(midwidth*0.95, midheight*0.65))
arrowBotRight = Arrow(arrow, buttonWidth-50, buttonHeight-50, 1, pos=(midwidth*1.34, midheight * 0.95))
arrowBotLeft = Arrow(arrow, buttonWidth-50, buttonHeight-50, 0, pos=(midwidth*0.95, midheight * 0.95))
bg = Background(day1, av1)
bg.draw(screen)
text_box.draw(screen)
last_outfit_count = 0

def outfit_matches(shirt, pants):
    for good_shirt, good_pants in level_up_outfits:
        if (good_shirt is None or good_shirt == shirt) and \
        (good_pants is None or good_pants == pants):
            return True
    return False

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
                    if closet: 
                        arrow = pygame.image.load("images/arrow-button.png").convert()
                        closet = not closet
                        bg.day +=1
                        day.day +=1
                        outfit = [current_group_shirts[current_index_top], current_group_pants[current_index_bottom]]
                        match bg.day:
                            case 2:
                                bg.setBackground(day1_good, av1)
                            case 3:
                                if corTop and corBot and topVisible and botVisible :
                                    bg.setBackground(day2_good,av2)
                                else:
                                    bg.setBackground(day2_bad, av2)
                                    bg.day-=1
                                    day.day -=1
                            case 4:
                                if corTop and corBot and topVisible and botVisible :
                                    bg.setBackground(day3_good,av3)
                                else:
                                    bg.setBackground(day3_bad, av3)
                                    bg.day-=1
                                    day.day -=1
                            case _:
                                bg.setBackground(day4_bad, av4)
                                last_outfit_count+=1
                                if(last_outfit_count==7): 
                                    endScreen = True
                                    text_refresh = Text_Box( (midwidth,midheight), "REFRESH" , (200,100) )
                                    
                        button1.updateImage() #changes the image depending on where we are
                        day.pick_group()
                    else:
                        arrow = pygame.image.load("images/arrow-button.png").convert()
                        closet = not closet
                        button1.updateImage()
                        topVisible = False
                        botVisible = False
                        corTop = False
                        corBot = False
                        match bg.day:
                            case 1:
                                bg.setBackground(day1, av1)
                            case 2:
                                bg.setBackground(day2, av2)
                            case 3:
                                bg.setBackground(day3, av3)
                            case _:
                                bg.setBackground(day4, av4)
                        
                if text_box.is_clicked(event.pos):
                    text_box.dismiss()
                    text_box.draw(screen)
                if text_box2.is_clicked(event.pos):
                    text_box2.dismiss()
                    text_box2.draw(screen)
                if text_refresh.is_clicked(event.pos):
                    text_refresh.start_fade()
                if arrowTopRight.is_clicked(event.pos):
                    show_next_block_top(current_group_shirts)
                if arrowTopLeft.is_clicked(event.pos):
                    show_prev_block_top(current_group_shirts)
                if arrowBotLeft.is_clicked(event.pos):
                    show_prev_block_bottom(current_group_pants)
                if arrowBotRight.is_clicked(event.pos):
                    show_next_block_bottom(current_group_pants)
                if current_group_pants[current_index_bottom].is_clicked(event.pos):
                    bodyBot = pygame.transform.scale(current_group_pants[current_index_bottom].imagefile, (screen.get_width()*.9, screen.get_height()*1.05))
                    botVisible = True
                    match (bg.day, current_index_bottom):
                        case (3, 0):
                            corBot = True
                        case(1,_):
                            corBot = True
                        case(2, _): 
                            corBot = True
                        case (_,_):
                            corBot = False
                if current_group_shirts[current_index_top].is_clicked(event.pos):
                    bodyTop = pygame.transform.scale(current_group_shirts[current_index_top].imagefile,(screen.get_width()*.9, screen.get_height()*1.05))
                    topVisible = True
                    corTop = True
                    match (bg.day, current_index_top):
                        case (3, 3):
                            corTop = True
                        case(1,_):
                            corTop = True
                        case(2,2): 
                            corTop = True
                        case (_,_):
                            corTop = False
               
    if(endScreen):
        screen.fill(pygame.Color(37, 15, 48))
        text_refresh.draw(screen)
        text_refresh.update()
        # Draw (if still visible)
        text_refresh.draw(screen)
    # fill the screen with a color to wipe away anything from last frame
    elif closet:
        #screen.fill(pygame.Color(255, 217, 228))
         #put the background to the variable background2
        #day1_pants.draw(screen)
        bg.draw(screen)
        if botVisible:
            screen.blit(bodyBot,(-1 * screen_width/15, screen_height/25))
        if topVisible:
            screen.blit(bodyTop,(-1 * screen_width/15, screen_height/25))
        box.draw(screen)
        arrowTopRight.draw()
        arrowTopLeft.draw()
        arrowBotRight.draw()
        arrowBotLeft.draw()
        for block in current_group_pants:
            block.draw(screen)
        for block in current_group_shirts:
            block.draw(screen)
        if bg.day == 2:
            text_box.draw(screen)
        elif bg.day == 3:
            text_box3.draw(screen)
        elif bg.day == 4:
            text_box4.draw(screen)
    else:
        screen.fill(pygame.Color(222, 242, 255))
        bg.draw(screen)
        if botVisible:
            screen.blit(bodyBot,(-1 * screen_width/15, screen_height/25))
        if topVisible:
            screen.blit(bodyTop, (-1 * screen_width/15, screen_height/25))
            
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

