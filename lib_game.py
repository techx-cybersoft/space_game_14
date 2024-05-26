import pygame, copy

def handle_event_player(event, player_rect, laser_rect, lst_laser_rect):
    # Xử lý tọa độ chuột 
    if event.type == pygame.MOUSEMOTION: #Hành động rê chuột
        x, y = event.pos # (x, y) Lấy ra tọa độ con trỏ chuột
        # Chỉnh tọa độ máy bay về giữa con chuột
        player_rect.x = x - player_rect.width // 2 
        player_rect.y = y - player_rect.height // 2 
    if event.type == pygame.MOUSEBUTTONDOWN: 
        # Xử lý click chuột bắn lấy tọa độ xuât phát viên đạn = tọa độ của máy bay
        # Tạo mới hoàn toàn viên đạn sau mỗi lần click
        new_laser_rect = copy.deepcopy(laser_rect)
        new_laser_rect.x = player_rect.x + player_rect.width / 2
        new_laser_rect.y = player_rect.y
        # Lưu laser rect vào list
        lst_laser_rect.append(new_laser_rect) #[laser_rect1, laser_rect2, laser_rect3]
    
def handle_laser(SCREEN, laser, lst_laser_rect, lst_meteor, score):
    # Xử lý đạn
    # Thay đổi tọa độ viên đạn sau mỗi khung hình và vẽ lại từng viên đạn sau mỗi lần vòng lặp game (while true chạy)
    for laser_rect_item in lst_laser_rect:
        laser_rect_item.y -= 10
        #blit đạn
        SCREEN.blit(laser, (laser_rect_item.x, laser_rect_item.y))
        if laser_rect_item.y < 0:
            lst_laser_rect.remove(laser_rect_item)
        #Khi blit viên đạn xử lý bắn trúng 
        #Duyệt list thiên thạch xem có thiên thạch nào chạm từng viên đạn hay không
        for meteor_rect in lst_meteor:
            if laser_rect_item.colliderect(meteor_rect):
                #Xử lý bắn trúng => cộng điểm và xóa thiên thạch
                score += 100
                lst_meteor.remove(meteor_rect)
                lst_laser_rect.remove(laser_rect_item)  
    """ Gía trị primitive không bị thay đổi khi sử dụng hàm vì vậy  khi xử lý 
    xong cần lấy những giá trị này ra bên ngoài thì return thành kết quả (Nếu có nhiều
    kết quả thì có thể return tuple sau đó tại chỗ gọi hàm lấy ra xử lý)"""
    return (score, 123)