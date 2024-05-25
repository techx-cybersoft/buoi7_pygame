import pygame
import sys

#Khởi tạo game
pygame.init()
#Cài đặt cửa sổ game
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640

#set up cửa sổ game
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#setup tên game trên cửa sổ
pygame.display.set_caption("Ecommerce Gym")
# -------------------------------------------------------------Trước khi load surface game (1 lần)---------------
#Các bước hiển thị surface (TEXT)
#b1: Tạo font chữ cho game (kiểu chữ, kích thuớc)
font_game = pygame.font.Font("font.otf", 35)
#B2:Tạo nội dung              (nội dung, độ sắc nét của chữ, màu sắc chữ, màu nền chữ)
title_game1 = font_game.render("New Game", True, "White") # Có thể dùng RGB và hexadecimal cho phần màu
#B3: Định tọa độ ban đầu cho text (surface)
title_game1_x = SCREEN_WIDTH / 2 - title_game1.get_width() /2
title_game1_y = SCREEN_HEIGHT / 2 - title_game1.get_height() / 2
#Khoảng cách dòng
line_height = 20
#Tạo ra các title
title_game2 = font_game.render("Introduce", True, "White")
title_game2_x = title_game1_x
title_game2_y = title_game1_y + title_game1.get_height() + line_height

title_game3 = font_game.render("Setting", True, "White")
title_game3_x = title_game1_x
title_game3_y = title_game2_y + title_game2.get_height() + line_height
#Các bước hiển thị surface (image)
bg_img = pygame.image.load("bg1.jpg")
x_bg_img = 0
y_bg_img = 0

#blit hero img
hero = pygame.image.load("hero.png")
hero = pygame.transform.scale(hero, (100, 100.4167))
x_hero = 0
y_hero = 0
#Lấy ra hình chữ nhật của hình ảnh
hero_rect = hero.get_rect()
# Hình chữ nhật sẽ có tọa độ x, y
hero_rect.x

#Setup Thời gian
clock = pygame.time.Clock() # => ms: number Lấy ra thời điểm 
#Setup âm thanh 
sound_game = pygame.mixer.Sound("music.wav")
sound_game.play(-1) # Tham số (input) là number => 1 lần ..... n: n lần => -1: phát lại mỗi khi hết bài

title_pos = font_game.render("(0,0)", True, "Red", "White")
title_pos_x = 0
title_pos_y = 0


# ----------------------------------------------------------Bắt đầu vòng lặp game (load trên mili giây)-----
#Vòng lặp game
#Game là sự load lại các khung hình trên từng mili giây liên tục
running = True

while running:
    # Thời gian trôi qua
    #number, mặc định là ms
    current_time = pygame.time.get_ticks() // 1000 # Đổi sang giây
    text_curent_time = font_game.render(f"Time: {current_time}", True, "Red", "White")
    #Đếm ngược thời gian
    count_down = 60 - current_time
    text_count_down = font_game.render(f"Count down: {count_down}", True, "Red", "White")
    #Nhận sự kiện từ người dùng
    event = pygame.event.poll()
    
    
    #Xây dựng xử lý thoát game
    if event.type == pygame.QUIT:
        running = False
        
    #Event: Các hành động từ chuột và bàn phím
    #Event phím (bấm nút đè phím)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        hero_rect.x += 10
    if keys[pygame.K_LEFT]:
        hero_rect.x -= 10
    if keys[pygame.K_UP]:
        hero_rect.y -= 10
    if keys[pygame.K_DOWN]:
        hero_rect.y += 10
    #Event về chuột (mouse)
    mouse_button = pygame.mouse.get_pressed()
    
    if mouse_button[0]: #chuột trái được click (có đè)
        #Xử lý nhân vật xuất hiện tại điểm đó
        x,y = pygame.mouse.get_pos() #pos là position => Lấy ra tọa độ của x, y chuột
        hero_rect.x = x
        hero_rect.y = y
        # Surface text tọa độ vị trí
        title_pos_x = x
        title_pos_y = y + hero.get_height()
        #Nội dung của surface text pos sẽ viết lại
        title_pos = font_game.render(f"({title_pos_x}, {title_pos_y})", True, "Red", "White")
    if mouse_button[2]: #chuột phải được click (có đè)
        x, y = pygame.mouse.get_pos() 
        hero_rect.x = x
        hero_rect.y = y 
    
    # -----------------------------Phần đưa lên game hiển thị ---------------------------------
    
    
    #Đưa surface lên game thông qua window.blit()
    WINDOW.blit(bg_img, (x_bg_img, y_bg_img))
    WINDOW.blit(title_game1, (title_game1_x, title_game1_y))
    WINDOW.blit(title_game2, (title_game2_x, title_game2_y))
    WINDOW.blit(title_game3, (title_game3_x, title_game3_y))
    WINDOW.blit(text_curent_time, (0, 50))
    WINDOW.blit(text_count_down, (0, 100))
    WINDOW.blit(title_pos, (title_pos_x, title_pos_y))
    #Vẽ hình chữ nhật lên window
    #               nơi vẽ, màu viền, hình chữ nhật, độ dày viền 
    pygame.draw.rect(WINDOW, "Pink", hero_rect, 2)
    """Đối với các nhân vật có hành động thì tọa độ blit ảnh sẽ lấy dựa trên tọa độ hình chữ nhật đã 
    được xử lý (vẽ lại hình trên tọa độ hình chữ nhật)"""
    WINDOW.blit(hero, (hero_rect.x, hero_rect.y))
    
    
    #Load lại màn hình
    #pygame.display.update()
    pygame.display.flip()
    clock.tick(60) #lệnh setup bao nhiêu khung hình trên 1 giây
pygame.quit()
sys.exit()