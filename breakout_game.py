import pygame
from ball import ball
from player import player
from random import choices , choice
import os

###PYGAME_SETUP
pygame.init()
WIDTH, HEIGHT = 1280,720 #largura e altura
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
###FONTS
panel_font = pygame.font.SysFont('cascadiamonoregular', 15)
###ASSETS
base_dir = os.path.dirname(os.path.abspath(__file__))
###VARS
fases_info = {
    "fase_1" : {
        "fase_name" : "FASE 1",
        "background" : None,    #fase 1 has no background on purpouse
        "base_time" : 360,
        "normal brick count" : 48,
        "unbreakable brick count" : 0,
        "power up count" : 2,
        "tough brick count" : 0, #provisory
        "positions" : [(4, 20), (132, 20), (260, 20), (388, 20), (516, 20), (644, 20), (772, 20), (900, 20), (1028, 20), (1156, 20),\
                       (4, 58), (132, 58), (260, 58), (388, 58), (516, 58), (644, 58), (772, 58), (900, 58), (1028, 58), (1156, 58),\
                       (4, 96), (132, 96), (260, 96), (388, 96), (516, 96), (644, 96), (772, 96), (900, 96), (1028, 96), (1156, 96), \
                       (4, 134), (132, 134), (260, 134), (388, 134), (516, 134), (644, 134), (772, 134), (900, 134), (1028, 134), (1156, 134),\
                       (4, 172), (132, 172), (260, 172), (388, 172), (516, 172), (644, 172), (772, 172), (900, 172), (1028, 172), (1156, 172)]
    },
    "fase_2" : {
        "fase_name" : "CHAT_GPT_FASE",
        "background" : None,    #remender to add background
        "base_time" : 400,
        "normal brick count" : 45,
        "unbreakable brick count" : 5,
        "power up count" : 5,
        "tough brick count" : 0, #provisory
        "positions" : [(4, 20), (132, 20), (260, 20), (388, 20), (516, 20), (644, 20), (772, 20), (900, 20), (1028, 20), (1156, 20),
                       (68, 50), (196, 50), (324, 50), (452, 50), (580, 50), (708, 50), (836, 50), (964, 50), (1092, 50), (1220, 50),
                       (4, 90), (132, 90), (260, 90), (388, 90), (516, 90), (644, 90), (772, 90), (900, 90), (1028, 90), (1156, 90),
                       (68, 130), (196, 130), (324, 130), (452, 130), (580, 130), (708, 130), (836, 130), (964, 130), (1092, 130), (1220, 130),
                       (4, 170), (132, 170), (260, 170), (388, 170), (516, 170), (644, 170), (772, 170), (900, 170), (1028, 170), (1156, 170),
                       (600, 210), (640, 210), (680, 210), (720, 210), (760, 210)]  # Unbreakable bricks in the center
    }, # chat_gpt_pos ---> messed ---> lenght of 55 positions for a total of 68 blocks --->manualy fixed
    "fase_3": {
        "fase_name": "CLAUDE FASE",
        "base_time": 420,
        "normal brick count": 56,
        "unbreakable brick count": 4,
        "power up count": 3,
        "tough brick count" : 0, #provisory
        "positions": [
            # Top curved pattern
            (260, 40), (388, 40), (516, 40), (644, 40), (772, 40), (900, 40),
            (132, 78), (260, 78), (388, 78), (516, 78), (644, 78), (772, 78), (900, 78), (1028, 78),
            (132, 116), (260, 116), (388, 116), (516, 116), (644, 116), (772, 116), (900, 116), (1028, 116),
            
            # Middle section with unbreakable bricks
            (4, 154), (132, 154), (260, 154), (388, 154), (516, 154), (644, 154), (772, 154), (900, 154), (1028, 154), (1156, 154),
            ("unbreakable", 388, 192), ("unbreakable", 516, 192), ("unbreakable", 644, 192), ("unbreakable", 772, 192),
            
            # Bottom V pattern
            (4, 230), (132, 230), (260, 230), (388, 230), (900, 230), (1028, 230), (1156, 230),
            (132, 268), (260, 268), (388, 268), (900, 268), (1028, 268),
            (260, 306), (388, 306), (900, 306), (1028, 306),
            (388, 344), (900, 344)
        ]
},#pos don't match the standart since the unbreakable flag is given, BUT...I was planning to make a similar change\
 #for fixing the position of the unbreakable blocks every time you play, since they are part of the core of phase\
 #structuring 
 "fase_4" : {
        "fase_name" : "Gemini Phase",
        "background" : "space_background.png",  # Example background, replace as needed
        "base_time" : 480, # Increased time for a potentially harder phase
        "normal brick count" : 30,
        "unbreakable brick count" : 10,
        "power up count" : 5, # More power-ups!
        "tough brick count" : 8,
        "positions" : [
            (60, 60), (180, 60), (300, 60), (420, 60), (540, 60), (660, 60), (780, 60), (900, 60), (1020, 60), (1140, 60),
            (60, 120), (180, 120), (300, 120), (420, 120), (540, 120), (660, 120), (780, 120), (900, 120), (1020, 120), (1140, 120),
            (60, 180), (180, 180), (300, 180), (540, 180), (780, 180), (900, 180),
            (60, 240), (300, 240), (540, 240), (780, 240), (1140, 240),
            (180, 300), (420, 300), (660, 300), (900, 300),
            (60, 360), (300, 360), (540, 360), (780, 360), (1140, 360),
            (180, 420), (420, 420), (660, 420), (900, 420)
        ],
        "unbreakable_positions": [ # Separate positions for unbreakable bricks
            (240, 120), (720, 120), (480, 180), (960, 180), (120, 240), (600, 240), (1080, 240), (480, 300), (720, 300), (600, 360)
        ],
        "tough_positions": [ # Positions for tough bricks
            (360, 60), (840, 60), (360, 120), (840, 120), (360, 180), (840, 180), (360, 240), (840, 240)
        ],
        "powerup_positions": [ # Separate positions for power-ups
            (120, 180), (600, 180), (360, 300), (840, 300), (600, 420)
        ]
    },  #gemini code  ##I will be following the same structure
    "fase_5" : {
        "fase_name" : "Copilot",
        "background" : "space",    # Adding a space background for a cool effect
        "base_time" : 300,
        "normal brick count" : 40,
        "unbreakable brick count" : 4,
        "power up count" : 3,
        "tough brick count" : 1,
        "positions" : [(4, 20), (132, 20), (260, 20), (388, 20), (516, 20), (644, 20), (772, 20), (900, 20), (1028, 20), (1156, 20),\
                       (4, 58), (132, 58), (260, 58), (388, 58), (516, 58), (644, 58), (772, 58), (900, 58), (1028, 58), (1156, 58),\
                       (4, 96), (132, 96), (516, 96), (644, 96), (1028, 96), (1156, 96),\
                       (4, 134), (132, 134), (516, 134), (644, 134), (1028, 134), (1156, 134),\
                       (4, 172), (132, 172), (388, 172), (772, 172), (1028, 172), (1156, 172),\
                       (4, 210), (132, 210), (260, 210), (388, 210), (516, 210), (644, 210), (772, 210), (900, 210), (1028, 210), (1156, 210),\
                       (4, 248), (132, 248), (260, 248), (388, 248), (516, 248), (644, 248), (772, 248), (900, 248), (1028, 248), (1156, 248)]
    
}
}

ball_radius = 15
player_size = 150
player_half_size = player_size/2
player1 = player(screen, 'cyan' , player_size, 10 , 585,1,"rect","horizontal",posit_y = 600)
ball_st = ball(screen,'white',ball_radius,fixed_start_speed = True,limit_speed=5,min_speed=3)
ball_st_rect = ball_st.rect ##for collision detection
life = 3
need_build = 1
points = 0
courrent_fase = 1
touch_token = 0
unbreak_toker = 0
fase_start_time = 0
color_list = ["red","orange","yellow","green","blue","purple","pink","white",(35,39,120),(100,12,255)]#make secret black block

###FUNCTIONS
def load_image_from_subfolder(image_name, subfolder="game_thumb"): #fix the error alert
    # Build the full path to the image based on the base_dir
    image_path = os.path.join(base_dir, "assets", subfolder, image_name)
    if os.path.exists(image_path):
        return pygame.image.load(image_path)
    else:
        raise FileNotFoundError(f"Image not found: {image_path}")
    
def leaving_procedure(): #add after running = False , DO whatever needed #I think pygame already handle all I need, but just in case...
    pass

def set_timer(actual_time_input):
    time_in_min = convert_sec_to_min(actual_time_input)
    return time_in_min

def timer(fase_time):
    global fase_start_time
    actual_time = (pygame.time.get_ticks() - fase_start_time)//1000
    try:
        return fase_time - actual_time
    except:
        return 0


def score(): #unsure if this will be used
    pass

def game_over(input): #input ix flexable for each situation
    global ending_screen
    global result
    global phase
    match input:
        case 0:  #No more lifes
            phase = False
            ending_screen = True
            result = "LOSE"
        case "WON":  #win trigered by end fase
            phase = False
            ending_screen = True
            result = input
        case (0,0):  #No time left
            phase = False
            ending_screen = True
            result = "LOSE"

    
    

def end_fase(list_of_blocks,all_blocks):
    global need_build
    global courrent_fase
    if list_of_blocks[0] + list_of_blocks[1] + list_of_blocks[2] == 0:
        clean_blocks(all_blocks) 
        courrent_fase += 1
        need_build = 1
        print("ae")

        #reset timers
            
def final_screen():
    result_font = pygame.font.SysFont('cascadiamonoregular', 40)
    result_text = result_font.render(f"YOU {result}", True, "white")
    screen.blit(result_text,(screen.get_width()//2,screen.get_height()//2))
    points_text = result_font.render(f"POINTS: {points}", True, "white")
    screen.blit(points_text,(screen.get_width()//2,screen.get_height()//2 + 50))

            

def build(fase_info_input):
    blocks = []
    print(fase_info_input)
    possible_pos = fase_info_input["positions"].copy()
    pwerup_num = fase_info_input["power up count"]
    ubrk_num = fase_info_input["unbreakable brick count"]
    norm_num = fase_info_input["normal brick count"]
    if pwerup_num != 0:
        for i in range(pwerup_num):
            pos_i = choice(possible_pos)
            bonus_brick = power_up_brick(pos_i,size_x = 120,size_y = 30)
            pygame.draw.rect(screen, bonus_brick.color, bonus_brick.rect)
            possible_pos.remove(pos_i)
            blocks.append(bonus_brick)
    if ubrk_num != 0:
        for i in range(ubrk_num):
            pos_i = choice(possible_pos)
            unbreakable_brick = Unbreakable_brick(pos_i)
            pygame.draw.rect(screen, unbreakable_brick.color, unbreakable_brick.rect)
            possible_pos.remove(pos_i)
            blocks.append(unbreakable_brick)
    if norm_num != 0:
        for i in range(norm_num):
            pos_i = choice(possible_pos)
            normal_brick = Normal_brick(pos_i)
            pygame.draw.rect(screen, normal_brick.color, normal_brick.rect)
            possible_pos.remove(pos_i)
            blocks.append(normal_brick)
    return blocks

def restricted_build(source_input):  #BUILD with rectricted positions
    try:
        unbreakeble_list = source_input["unbreakable_positions"]
    except:
        pass
    try:
        power_up_list = source_input["power_up_positions"]
    except:
        pass
    try:
        normal_list = source_input["tough_positions"]
    except:
        pass
    #return build({"positions":unbreakeble_list,"power up count":len(power_up_list),"unbreakable brick count":len(unbreakeble_list),"normal brick count":len(normal_list)})


def restart_pos(): #returns ball and players to start position after lose life or pass phase
    ball_st.atualize(0.02,(WIDTH, HEIGHT),init_pos = (player1.player_pos.x,player1.player_pos.y-20),restart=True) #starts ball in player position
    pygame.time.delay(1000)#think of a better way
    ball_st.atualize(0.02,(WIDTH, HEIGHT),ball_should_not_stop = [True,3,5])#return the_timer #check timer in loop till 2 seconds lock ball atulize with if between normal atualize and restart=True
    
def collision(): #umnecessary for now, maybe for bosses?
    pass

def positions_maker(): #for later use --> use lambda when multiple call
    pass

def clean_blocks(_list_blocks_to_clean):
    for i in _list_blocks_to_clean:
        _list_blocks_to_clean.remove(i)
        del i
    #when finishing a fase or losing all remaining objects must be deleted

def convert_sec_to_min(sec):
    min = sec // 60
    sec = sec % 60
    return min,sec

def show_stats(scrn,life,points,time = 0,power_up = []): #time = 0 for tesing
    points_color = (255, 255 - points//1000, 255 - points//1000)
    if points_color[1] < 0:
        points_color = (255, 0, 0)
    points_text = panel_font.render(f"POINTS: {points}", True, points_color)
    life_text = panel_font.render(f"LIFE: {life}", True, (255, 255, 255))
    time_text = panel_font.render(f"TIME: {time[0]}:{time[1]}", True, (255, 255, 255))
    for p in power_up:
        atv_pwr_up_text = panel_font.render(f"{p}", True, (255, 255, 255))
        scrn.blit(atv_pwr_up_text, (30*power_up.index(p), 1))
    scrn.blit(time_text, (600, 1))
    scrn.blit(points_text, (10, 1))
    scrn.blit(life_text, (1200, 1))
    #show life, score, time

def variable_cleaner():
    pass

###BRICKS
class brick():
    def __init__(self,pos ,size_x = 120,size_y = 30):
        self.destroy = False
        self.pos = pos
        self.size_x = size_x
        self.size_y = size_y
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size_x,self.size_y)

    def atualize(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def __del__(self):
        pass

class Normal_brick(brick):
    def __init__(self,pos,size_x = 120,size_y = 30):
        super().__init__(pos,size_x,size_y)
        self.type = "normal"
        self.color = (77,150,99) #making it simple for now
        self.points = 100
        

    def collided(self):
        self.destroy = True
        return self.points

class power_up_brick(brick):
    def __init__(self,pos,size_x = 120,size_y = 30):
        super().__init__(pos)
        self.type = "power up"
        power_list = [multiball, speed_up, slow_down, extend, shrink, shooter, shield, ultimate, invencible, score_up, life_up]
        self.drop = choices(power_list,weights = [10,10,10,10,10,10,10,1,5,10,4]) #thinkng about makeing the colors match the power ups, the bad point is making the game more predictable
        self.color = choice(color_list)
        self.points = 200
        
    def collided(self):
        self.destroy = True
        return self.points
        #return drop #make return a tuple, if [1] is not none them apply power up

class Unbreakable_brick(brick):
    def __init__(self,pos,size_x = 120,size_y = 30):
        super().__init__(pos)
        self.type = "unbreakable"
        self.color = "grey"
        self.points = 1000

    def collided(self, Hyperball = False): #to do hyperball
        if Hyperball == True:
            self.destroy = True
            return self.points
        return 0


class tough_brick(brick):
    def __init__(self,pos,size_x = 120,size_y = 30,life = 3):
        super().__init__(pos)
        self.color = (200,150,170)
        self.type = "tough"
        self.life = life
        self.points = 500

    def collided(self):
        #make the colos lose brightnes upon hit
        self.life -= 1
        if self.life == 0:
            self.destroy = True
            return self.points
        self.color -= (20,20,20)   #don't make it negative -> code fix in future updt
        return 0


###POWER UPS
class power_up():
    def __init__(self,center_pos):        
        pass

    def atualize(self):
        pass

class multiball(power_up):
    pass

class speed_up(power_up):
    pass

class slow_down(power_up):  #player
    pass

class extend(power_up):
    pass

class shrink(power_up):
    pass

class shooter(power_up):
    pass

class shield(power_up):  #ball can't fall
    pass

class ultimate(power_up): #breaks all blocks
    pass

class invencible(power_up):
    pass

class score_up(power_up):   #base points given increase by phase
    pass    

class life_up(power_up):

    def effect(self):
        global life
        life += 1


class inviseble(power_up):  #the ball!  #Debuff  #make one for player #add evil laugh sound
    pass

class ball_magnet(power_up): #later add #-->atract the ball to player center if near enough
    pass

class key(power_up): #later use
    pass
    

class Engenheiros_do_mapii(): ###for future use #menu and modes will be needed #engenheiro_of_mapiis
    def __init__(self):
        pass

#make iter ------> unsure
#case iter reach max --> game beaten --> leaderboard
#create txt file for leaderboard
#points will be time based, completing stages will give extra points, finishing\
# a fase with more then one ball will give extra points
#possible add another win condition later, remember when making end_fase()
#create skin after game beaten (RGB skin)
##//
ending_screen = False
running = True
phase = True
while running:
    while phase:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                phase = False
                running = False

        screen.fill("black")

        if need_build == 1:
            fase_start_time = pygame.time.get_ticks()
            source = fases_info[f"fase_{courrent_fase}"]
            if source["fase_name"] == "end":
                game_over( "WON")
                continue
            try:
                blocks_list = build(source)
            except:
                restricted_build(source)  ##that way making fixed positions is way easier
            blocks_in_fase = [source["normal brick count"],source["power up count"],source["tough brick count"]]
            need_build = 0
        #reminder --> brick size 120

        tempo_agora = timer(source["base_time"])

        if touch_token > 0:
            touch_token -= 1
        if unbreak_toker > 0:
            unbreak_toker -= 1



        if pygame.Rect.colliderect(ball_st.rect, player1.rect) and touch_token == 0:
            ball_st.ball_vel_y *= -1 
            ball_st.ball_vel_x -= (last_player_pos-player1.player_pos.x)*0.5
            touch_token = 15

        
        ##atualizations
        player1.atualize(0.01, (WIDTH, HEIGHT) , 1 , ball_st.player_pos.y , ball_st.player_pos.x)
        ball_st.atualize(0.02, (WIDTH, HEIGHT))
        show_stats(screen,life,points,time = convert_sec_to_min(tempo_agora))
        ##collision + atualization
        for i in blocks_list:
            if pygame.Rect.colliderect(ball_st.rect,i.rect):
                if i.type != "unbreakable" or unbreak_toker == 0:
                    points += i.collided()
                if i.type == "unbreakable"and unbreak_toker == 0:
                    unbreak_toker = 15
                ball_st.ball_vel_y *= -1
                if i.destroy == True:
                    blocks_list.remove(i)
                    match i.type:
                        case "normal":
                            blocks_in_fase[0] -= 1
                        case "power up":
                            blocks_in_fase[1] -= 1
                        case "tough":
                            blocks_in_fase[2] -= 1
            try: 
                i.atualize()
            except:
                                #remember to delete the objects  in further changes
                del i
                #collision sucess

        end_fase(blocks_in_fase,blocks_list)

        ##loop VAR
        try:
            if pygame.time.get_ticks() - last_ticks < 40: ###RESTART mess with the logic #-->restart update Priority
                pass
            else:
                last_ticks = pygame.time.get_ticks()
                last_player_pos = player1.player_pos.x
        except:
            last_ticks = pygame.time.get_ticks()
            last_player_pos = player1.player_pos.x

        if ball_st.player_pos.y > 680: #check if ball falled
            if life < 1:
                game_over(life)
            else:
                time_of_restart = restart_pos()
                life -= 1
        game_over(convert_sec_to_min(tempo_agora))

        pygame.display.flip()
        clock.tick(60)

    while interlude:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                interlude = False
                running = False

        screen.fill("black")
        #interlude_screen()
        pygame.display.flip()
        clock.tick(60)

    while ending_screen:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                ending_screen = False
                running = False

        screen.fill("black")
        final_screen()
        pygame.display.flip()
        clock.tick(60)
        


        


    #########TO DO LIST START
    #add life simble at panel
    #check possible multi block collision glicth
    #add player horizontal speedto the ball
    #add power ups
    #add score system
    #add life system
    #add timer
    #unbreakeble blocks would do better being fixed in the fase, plan to change the input and build
    #add life to end_fase pontuaction system points += 1000*life
    #plan to envelop fase_loop, menu_loop, end_fase_loop and leaderboard_loop in running
    ########To DO LIST END
        

pygame.quit()