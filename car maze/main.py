###这个小程序打开时好像就会自动切换成中文输入法，需要按shift进行操作，用英文状态下的WASD键进行操作
###方向盘子自动回正
###WASD键以小车的正面朝向为W键的指向方向
###吃完所有星星才可以碰重点的啦
###时间比较紧迫，所以没有写太多个关卡
# level3.txt - 有几个简单障碍物结构
###
import pygame
import config
from game_manager import GameManager
from utils.draw_text import draw_text
##这里可以删了from player import Player

pygame.init()
pygame.font.init()
pygame.mixer.init()##初始化声音
screen=pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_HEIGHT))
clock=pygame.time.Clock()

ico=pygame.image.load("images/maze.png").convert()
pygame.display.set_icon(ico)
pygame.display.set_caption("汽车小迷宫")

##player=Player()
pygame.mixer.music.load("sounds/bgm.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)###参数为-1表示循环播放


game_manager=GameManager(screen,1)

running=True
success_time=-1##$#-1表示当前没有获胜，否则表示获胜的时刻
success_finished=False

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif success_finished and event.type==pygame.KEYDOWN:
            running=False###显示已经通关，按下任意键，程序结束运行

    if success_finished:
        screen.fill("black")
        draw_text(screen,"You Win!",200,config.SCREEN_WIDTH/2,config.SCREEN_HEIGHT/2)
    else:
        if success_time>=0:
            if pygame.time.get_ticks()-success_time>2000:####获胜的场景停留两秒钟
                has_next=game_manager.next_level()
                if not has_next:###如果没有下一关，则游戏结束
                    success_finished=True
                    continue
                success_time=-1###将通关时间清空
        screen.fill("black")
        if game_manager.update():
            success_time=pygame.time.get_ticks()###获取成功通过该关卡时的时刻

    pygame.display.flip()

    clock.tick(config.FPS)

pygame.quit()

