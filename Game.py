import pygame
from random import choice
from solve import *
from time import time

end=0
pygame.init()
canvas=pygame.display.set_mode((450,450))
canvas.fill((255,255,255))

def write(a,x,y):
	font=pygame.font.Font("freesansbold.ttf",30)
	text=font.render(str(a),True,(0,0,0),(255,255,255))
	text_area=text.get_rect()	
	text_area.center=(x,y)
	return text,text_area


def menu():
	font=pygame.font.Font("freesansbold.ttf",40)
	text=font.render("Choose Difficulty:",True,(0,0,0),(255,255,255))
	text_area=text.get_rect()
	text_area.center=(225,50)	
	canvas.blit(text,text_area)

	text,text_area=write("Novice",225,150)
	canvas.blit(text,text_area)

	text,text_area=write("Average",225,200)
	canvas.blit(text,text_area)

	text,text_area=write("Expert",225,250)
	canvas.blit(text,text_area)

	text,text_area=write("Master",225,300)
	canvas.blit(text,text_area)

	text,text_area=write("Legend",225,350)
	canvas.blit(text,text_area)

	text,text_area=write("God",225,400)
	canvas.blit(text,text_area)


run_menu=True
file_name=[]
while run_menu:
	menu()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run_menu=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			m_x,m_y=pygame.mouse.get_pos()
	
			if m_x < 300 and m_x >150:
				if m_y>125 and m_y<175:
					file_name=["s01a.txt","s01b.txt","s01c.txt","s02a.txt","s02b.txt","s02c.txt","s03a.txt","s03b.txt","s03c.txt"]
				if m_y>175 and m_y<225:
					file_name=["s04a.txt","s04b.txt","s04c.txt","s05a.txt","s05b.txt","s05c.txt","s06a.txt","s06b.txt","s06c.txt"]
				if m_y>225 and m_y<275:
					file_name=["s07a.txt","s07b.txt","s07c.txt","s08a.txt","s08b.txt","s08c.txt","s09a.txt","s09b.txt","s09c.txt"]
				if m_y>275 and m_y<325:
					file_name=["s10a.txt","s10b.txt","s10c.txt","s11a.txt","s11b.txt","s11c.txt","s12a.txt","s12b.txt","s12c.txt"]
				if m_y>325 and m_y<375:
					file_name=["s13a.txt","s13b.txt","s13c.txt","s14a.txt","s14b.txt","s14c.txt","s15a.txt","s15b.txt","s15c.txt"]
				if m_y>375 and m_y<425:
					file_name=["s16.txt"]
	pygame.display.update()
	if file_name!=[]:
		run_menu=False

board=[[0 for i in range(9)] for j in range(9)]
solved=[]
given=[]	
file_to_open=choice(file_name)
file_path="C:\\Users\\abc\\Desktop\\sudoku project\\puzzles\\"+file_to_open
solution_file_name=file_to_open[:-4]+"_s.txt"
solution_path="C:\\Users\abc\\Desktop\\sudoku project\\solutions\\"+solution_file_name
f1=open(file_path,'r')
line=f1.readline()
count=0
while line!="\n":
	if count==9:break
	
	a=line[:-2]
	row=[]
	row_s=a.split()
	for i in range(9):	
		row.append(int(row_s[i]))
	given.append(row)
	line=f1.readline()
	count+=1
	
f1.close()
f1=open(solution_path,'r')
line=f1.readline()
count=0
while line!="\n":
	if count==9:break
	
	a=line
	row=[]
	row_s=a.split()
	for i in range(9):	
		row.append(int(row_s[i]))
	solved.append(row)
	line=f1.readline()
	count+=1
f1.close()

start_x,start_y=0,0

text,text_rect=0,0
pygame.init()
mouse_x,mouse_y=0,0
run=True
thick=1
color=(150,150,150)
is_clicked=False
screen=pygame.display.set_mode((450,550))
screen.fill((255,255,255))

def check_win():
	global run
	if board==solved:
		return True

def default_number(x,a,b):
	global text,text_rect
	font=pygame.font.Font("freesansbold.ttf",35)
	text=font.render(str(x),True,(0,0,0),(255,255,255))
	text_rect=text.get_rect()
	text_rect.center=(a,b)
	board[b//50][a//50]=x
	given[b//50][a//50]=x	
	screen.blit(text,text_rect)


def number(x,a,b):
	global text,text_rect
	font=pygame.font.Font("freesansbold.ttf",35)
	text=font.render(str(x),True,color,(255,255,255))
	text_rect=text.get_rect()
	text_rect.center=(a,b)


def check(x):
	global color
	horizontal=board[start_y//50]
	horizontal[start_x//50]=0
	vertical=[]
	for i in range(9):
		vertical.append(board[i][start_x//50])
	vertical[start_y//50]=0
	box=[]
	box_x,box_y=0,0
	for i in range(0,9,3):
		if (start_x//50)-i<3:
			box_x=i
			break
	for i in range(0,9,3):
		if (start_y//50)-i<3:
			box_y=i
			break
	for i in range(3):
		box.append(board[box_y][box_x+i])
		box.append(board[box_y+1][box_x+i])
		box.append(board[box_y+2][box_x+i])
	if (x in horizontal) or (x in vertical) or (x in box):
		color=(255,0,0)	
	else:
		color=(150,150,150)	

def solve_button():
	global screen
	font=pygame.font.Font("freesansbold.ttf",35)
	text=font.render("SOLVE",True,(0,0,0),(255,255,255))
	text_rect=text.get_rect()
	text_rect.center=(75,500)
	screen.blit(text,text_rect)
start=time()
def time_elapsed():
	global screen
	end=time()
	seconds=end-start
	minutes=int(seconds)/60
	seconds=int(seconds)%60
	if minutes<10:
		minutes="0"+str(minutes)
	if seconds<10:
		seconds="0"+str(seconds)
	run_time=str(minutes)+":"+str(seconds)
	font=pygame.font.Font("freesansbold.ttf",35)
	text=font.render(str(run_time),True,(0,0,0),(255,255,255))
	text_rect=text.get_rect()
	text_rect.center=(375,500)
	screen.blit(text,text_rect)

	
while run:
	solve_button()
	for i in range(9):
			for j in range(9):
				if given[i][j]!=0:
					default_number(given[i][j],(j*50)+25,(i*50)+25)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			if is_clicked:
				pygame.draw.rect(screen,(255,255,255),(start_x,start_y,50,50),2)
				pygame.draw.rect(screen,(255,255,255),(start_x,start_y-50,50,50),2)
				pygame.draw.rect(screen,(255,255,255),(start_x-50,start_y,50,50),2)
				pygame.draw.rect(screen,(255,255,255),(start_x+50,start_y,50,50),2)
				pygame.draw.rect(screen,(255,255,255),(start_x,start_y+50,50,50),2)
					
			start_x,start_y=0,0
			for i in range(0,450,50):
				if mouse_x-i < 50:
					start_x=i
					break
			for i in range(0,450,50):
				if mouse_y-i < 50:
					start_y=i
					break  
					
			pygame.draw.line(screen,(0,0,0),(start_x,start_y),(start_x,start_y+50),3)
			pygame.draw.line(screen,(0,0,0),(start_x,start_y),(start_x+50,start_y),3)
			pygame.draw.line(screen,(0,0,0),(start_x+50,start_y),(start_x+50,start_y+50),3)
			pygame.draw.line(screen,(0,0,0),(start_x,start_y+50),(start_x+50,start_y+50),3)
			is_clicked=True
			if mouse_x<100 and mouse_y>450:
				solve(given)
		keys=pygame.key.get_pressed()
		if not given[start_y/50][start_x/50]:
			
			color=(150,150,150)
			if keys[pygame.K_1]:
				check(1)
				number(1,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=1
				
			if keys[pygame.K_2]:
				check(2)
				number(2,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=2		
		
			if keys[pygame.K_3]:
				check(3)
				number(3,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=3
				
			if keys[pygame.K_4]:
				check(4)
				number(4,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=4

			if keys[pygame.K_5]:
				check(5)
				number(5,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=5

			if keys[pygame.K_6]:
				check(6)
				number(6,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=6

			if keys[pygame.K_7]:
				check(7)
				number(7,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=7

			if keys[pygame.K_8]:
				check(8)
				number(8,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=8	

			if keys[pygame.K_9]:
				check(9)
				number(9,start_x+25,start_y+25)
				board[start_y/50][start_x/50]=9

			if text!=0:
				screen.blit(text,text_rect)
			if keys[pygame.K_0]:
				board[start_y/50][start_x/50]=0
				pygame.draw.rect(screen,(255,255,255),(start_x+5,start_y+5,40,40))
				text=0
	if text:
		screen.blit(text,text_rect)
	
	for i in range(10):
		if i%3==0:
			thick=4
		else:
			thick =1
		if i==0 : thick=1
		pygame.draw.line(screen,(0,0,0),(i*50,0),(i*50,450),thick)
	
		pygame.draw.line(screen,(0,0,0),(0,i*50),(450,i*50),thick)
		pygame.display.update()
	if not check_win():
		time_elapsed()