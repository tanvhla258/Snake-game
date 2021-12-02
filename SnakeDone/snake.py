import pygame
from time import sleep
from random import randint
pygame.init()
screen=pygame.display.set_mode((600,660))
pygame.display.set_caption("Snake")

GREEN=(0,200,0)
RED=(255,0,0)
BLUE=(0,0,200)
WHITE=(255,255,255)
BLACK=(0,0,0)
SnakesColor=(83, 134, 166)

running=True
snakes=[[5,6],[5,7],[5,8]]
direction = "right"
clock = pygame.time.Clock()
milisecond=0.1
apple=[randint(0,19),randint(2,21)]
tail_x=0
tail_y=0
font1=pygame.font.SysFont('Verdana',25)
font2=pygame.font.SysFont('Verdana',50)
font3=pygame.font.SysFont('Verdana',30)
highscore=0
pausing =False
score=0
Start=False
Quit=False
Death=False
mouse_x=0
mouse_y=0
snake_speed=0.07
OnMusic=True
ranfruit=randint(1,3)
bigapple=[randint(0,19),randint(2,21)]
checkbigfruit=0
point1_txt=font1.render(": 1 point",True,BLACK)
point5_txt=font1.render(": 5 point",True,BLACK)

#Image
Menu_Background=pygame.image.load("BG.PNG")

Background = pygame.image.load("IngameBG2.jpg")
OnMusic_button=pygame.image.load("OnMusic.png")
OffMusic_button=pygame.image.load("OffMusic.png")
Replay_button=pygame.image.load("Replay.png")

Uphead=pygame.image.load("Uphead2.png")
Downhead=pygame.image.load("Downhead2.png")
Lefthead=pygame.image.load("Lefthead2.png")
Righthead=pygame.image.load("Righthead2.png")
Body=pygame.image.load("Body2.png")
title=pygame.image.load("title2.png")
fruit1=pygame.image.load("apple.png")
fruit2=pygame.image.load("coconut.png")
fruit3=pygame.image.load("orange.png")
fruit4=pygame.image.load("pineapple.png")

#Transform
Menu_Background=pygame.transform.scale(Menu_Background,(600,660))

Background=pygame.transform.scale(Background,(601,601))
OnMusic_button=pygame.transform.scale(OnMusic_button,(67,67))
OffMusic_button=pygame.transform.scale(OffMusic_button,(67,67))
Replay_button=pygame.transform.scale(Replay_button,(67,67))

Uphead=pygame.transform.scale(Uphead,(30,30))
Downhead=pygame.transform.scale(Downhead,(30,30))
Righthead=pygame.transform.scale(Righthead,(30,30))
Lefthead=pygame.transform.scale(Lefthead,(30,30))
Body=pygame.transform.scale(Body,(30,30))
title=pygame.transform.scale(title,(600,60))
fruit1=pygame.transform.scale(fruit1,(30,30))
fruit2=pygame.transform.scale(fruit2,(30,30))
fruit3=pygame.transform.scale(fruit3,(30,30))
fruit4=pygame.transform.scale(fruit4,(40,40))



#Sound
Music_Background=pygame.mixer.music.load("MenuMusic.wav")
eat_sound=pygame.mixer.Sound("power.wav")
death_sound=pygame.mixer.Sound("Death.mp3")
pygame.mixer.music.play(-1)


while Start==False:
	screen.blit(Menu_Background,(0,0))
	screen.blit(fruit1,(10,570))
	screen.blit(fruit2,(45,570))
	screen.blit(fruit3,(80,570))
	screen.blit(fruit4,(5,610))
	screen.blit(point1_txt,(120,570))
	screen.blit(point5_txt,(45,620))

	mouse_x,mouse_y=pygame.mouse.get_pos()
	if OnMusic==True:
		screen.blit(OnMusic_button,(440,12))
	else :
		screen.blit(OffMusic_button,(440,12))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type==pygame.MOUSEBUTTONDOWN:	
			if event.button==1:
				if (262<mouse_x<332) and (437<mouse_y<510): #StartButton
					Start=True
					pygame.mixer.pause()	
				if (440<mouse_x<507) and (12<mouse_y<79) :
					if OnMusic==True:
						pygame.mixer.music.pause()
						OnMusic=False
					else :
						pygame.mixer.music.unpause()
						OnMusic=True
				if (530<mouse_x<578) and (18<mouse_y<70):
					pygame.quit()
				print(mouse_x)	
				print(mouse_y)
				
	pygame.display.flip()


while running:
	clock.tick(60)
	mouse_x,mouse_y=pygame.mouse.get_pos()
	screen.blit(Background,(0,60))
	screen.blit(title,(0,0))

	if OnMusic==True:
		screen.blit(OnMusic_button,(520,5))
	else :
		screen.blit(OffMusic_button,(520,5))

	#Draw Grid and Score
	
	score_txt=font1.render("Score: " +str(score),True,WHITE)
	screen.blit(score_txt,(5,25))

	#Draw Snake
	for snake in snakes:
		screen.blit(Body,(snake[0]*30,snake[1]*30))

	if direction=="right":
		screen.blit(Righthead,(snakes[-1][0]*30,snakes[-1][1]*30))
	if direction=="left":
		screen.blit(Lefthead,(snakes[-1][0]*30,snakes[-1][1]*30))
	if direction=="up":
		screen.blit(Uphead,(snakes[-1][0]*30,snakes[-1][1]*30))
	if direction=="down":
		screen.blit(Downhead,(snakes[-1][0]*30,snakes[-1][1]*30))
	
	# Draw Apple
	if ranfruit==1:
		screen.blit(fruit1,(apple[0]*30,apple[1]*30))
	if ranfruit==2:
		screen.blit(fruit2,(apple[0]*30,apple[1]*30))
	if ranfruit==3:
		screen.blit(fruit3,(apple[0]*30,apple[1]*30))

		
	
	# Snake move
	if pausing==False:
		if direction=="right":
			snakes.append([snakes[-1][0]+1,snakes[-1][1]]) 
			snakes.pop(0)
		if direction == "left":
			snakes.append([snakes[-1][0]-1,snakes[-1][1]])
			snakes.pop(0)
		if direction=="up":
			snakes.append([snakes[-1][0],snakes[-1][1]-1])
			snakes.pop(0)
		if direction == "down":
			snakes.append([snakes[-1][0],snakes[-1][1]+1])
			snakes.pop(0)


	# Eat Apple
	if apple[0]==snakes[-1][0] and apple[1]==snakes[-1][1]:
		pygame.mixer.Sound.play(eat_sound)
		tail_x=snakes[0][0]
		tail_y=snakes[0][1]
		snakes.insert(0,[tail_x,tail_y])
		checkAP=False
		apple = [randint(0,19),randint(2,21)]
		ranfruit=randint(1,3)
		while checkAP==False:
			checkAP=True
			for snake in snakes:
				if apple[0]==snake[0] and apple[1]==snake[1]:
					checkAP==False
			if checkAP==False:
				apple = [randint(0,19),randint(0,21)]
		score+=1
		checkbigfruit+=1
		if highscore<score:
			highscore=score


	# Create BigFruit

	if checkbigfruit>=5:
		screen.blit(fruit4,(bigapple[0]*30,bigapple[1]*30))
	#Eat Big Fruit
	if bigapple[0]==snakes[-1][0] and bigapple[1]==snakes[-1][1] and checkbigfruit>=5:
		pygame.mixer.Sound.play(eat_sound)
		tail_x=snakes[0][0]
		tail_y=snakes[0][1]
		snakes.insert(0,[tail_x,tail_y])
		score+=5
		checkbigfruit=0
		bigapple=[randint(0,19),randint(2,20)]
		if highscore<score:
			highscore=score

	#Check Crash Wall or Crash itself
	if snakes[-1][0]<0 or snakes[-1][0]>19 or snakes[-1][1]<2 or snakes[-1][1]>21:	#Wall
		pausing =True
	if len(snakes)>4:	# Eat itself
		for i in range(len(snakes)-1):
			if snakes[-1][0]==snakes[i][0] and snakes[-1][1]==snakes[i][1]:
				pausing=True
				break

	#Die
	if pausing ==True:
		Gameover_txt=font2.render("Game over",True,BLACK)
		Highscore_txt=font2.render("High score: " + str(highscore),True,BLACK)
		screen.blit(Gameover_txt,(150,220))
		screen.blit(Highscore_txt,(150,290))
		screen.blit(Replay_button,(280,370))


	sleep(snake_speed)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type==pygame.MOUSEBUTTONDOWN:
			if (520<mouse_x<520+67) and (5<mouse_y<5+67) :
					if OnMusic==True:
						pygame.mixer.music.pause()
						OnMusic=False
					else :
						pygame.mixer.music.unpause()
						OnMusic=True
			if (280<mouse_x<280+67) and (370<mouse_y<370+67) and pausing ==True:	#reset game
				pausing=False
				snakes=[[5,6],[5,7],[5,8]]
				score=0
				direction="right"
				apple=[randint(0,19),randint(2,21)]
				checkbigfruit=0

		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_UP and direction!="down":
				direction="up"
			if event.key==pygame.K_DOWN and direction!="up":
				direction="down"
			if event.key==pygame.K_LEFT and direction!="right":
				direction="left"
			if event.key==pygame.K_RIGHT and direction!="left":
				direction="right"
			
		
			

	pygame.display.flip()

pygame.quit()