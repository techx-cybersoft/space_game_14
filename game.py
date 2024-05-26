import pygame, sys, copy, random, lib_game

# Khởi tạo game
pygame.init()
#Tạo cửa sổ 
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Game demo")

# Load background
bg_game = pygame.image.load("./graphics/background_space.jpg")
bg_game = pygame.transform.scale(bg_game, (SCREEN_WIDTH, SCREEN_HEIGHT))

#Load máy bay
player = pygame.image.load('./graphics/air_craft.png')
player_rect = player.get_rect()

# Tạo ra list các viên đạn
laser = pygame.image.load('./graphics/laser.png')
laser_rect = laser.get_rect()
lst_laser_rect = []

#Tạo ra list chứa các thiên thạch
meteor = pygame.image.load('./graphics/meteor.png')
meteor_rect = meteor.get_rect()
lst_meteor = []
#Yêu cầu load 5 thiên thạch lên màn hình (100, 100) (200, 100) (300, 100) (400, 100) (500, 100)
#Set up thời gian tạo thiên thạch
meteor_time_start = 0

#title (Điểm, mạng, thời gian)
font_game = pygame.font.Font('./graphics/subatomic.ttf', 32)
score = 0
score_title = font_game.render(f'Score: {score}', True, 'Red', 'White')

live = 5
live_title = font_game.render(f"Live: {live}", True, "Red", "White")
live_rect = live_title.get_rect()
live_rect.x = SCREEN_WIDTH - live_rect.width
live_rect.y = 0 

# Tạo vòng lặp game
running = True

while running:
    # load background 
    SCREEN.blit(bg_game, (0,0))
    #Setup thoát game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        lib_game.handle_event_player(event, player_rect, laser_rect, lst_laser_rect)
    #blit máy bay 
    SCREEN.blit(player, (player_rect.x, player_rect.y))
    # Xử lý đạn
    (score, number) = lib_game.handle_laser(SCREEN, laser, lst_laser_rect, lst_meteor, score)

    #Xử lý thiên thạch 
    #Tạo ra thiên thạch sau mỗi khoảng thời gian
    meteor_time_current = pygame.time.get_ticks()
    if meteor_time_current - meteor_time_start >= 1000:
        #Tạo thiên thạch
        new_meteor_rect = copy.deepcopy(meteor_rect)
        new_meteor_rect.y = 0
        new_meteor_rect.x = random.randint(0, SCREEN_WIDTH - new_meteor_rect.width)
        #Đưa thiên thạch
        lst_meteor.append(new_meteor_rect)
        meteor_time_start = meteor_time_current
        
    #Hiển thị thiên thạch
    for meteor_rect_item in lst_meteor: #Duyệt list lấy ra từng thiên thạch rect
        meteor_rect_item.y += 5 #Mỗi lần vòng lặp game chạy thì thay đổi vị trí blit thiên thạch tăng y 10 đơn vị
        SCREEN.blit(meteor, (meteor_rect_item.x, meteor_rect_item.y)) # Lần lượt blit các thiên thạch lên màn hình
        # Xóa các thiên thạch đã quá screen height
        if meteor_rect_item.y >= SCREEN_HEIGHT:
            lst_meteor.remove(meteor_rect_item)
        #Xử lý các thiên thạch khi blit chạm tọa độ máy bay
        print(live)
        if meteor_rect_item.colliderect(player_rect):
            live -= 1
            #Đổi vị trí máy bay sau khi hồi sinh
            # player_rect.x = random.randint(0, SCREEN_WIDTH - player_rect.width)
            lst_meteor.remove(meteor_rect_item)
            if live < 0:
                running = False
    
    print(lst_meteor)
    """x = 0
    for number in range(0, 5):
        new_meteor_rect = copy.deepcopy(meteor_rect)
        x += 100
        new_meteor_rect.x = x
        
        SCREEN.blit(meteor, (new_meteor_rect.x, new_meteor_rect.y))"""
        
    #Hiển thị thông tin trò chơi
    score_title = font_game.render(f'Score: {score}', True, 'Red', 'White')
    SCREEN.blit(score_title, (0,0))
    live_title = font_game.render(f"Live: {live}", True, "Red", "White")
    SCREEN.blit(live_title, (live_rect.x, live_rect.y))
    
    
    #Setup fps 60 (60 khung hình trên 1 giây)
    pygame.time.Clock().tick(90)
    # Cập nhật game liên tục 
    pygame.display.flip()
pygame.quit()
sys.exit()