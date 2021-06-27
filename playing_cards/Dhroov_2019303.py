
import pygame,sys,random,os,time
from pygame.locals import *

image1 = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\2C.png') 

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\new\\Desktop\\playing_cards - Copy\\music.mp3')
pygame.mixer.music.play(-1)
#DISPLAYSURF = pygame.display.set_mode((1000,650), 0, 32)
DISPLAYSURF =pygame.display.set_mode((1366,768),pygame.RESIZABLE)
pygame.display.set_caption('RUMMY')
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW=(255,255,0)
clock=pygame.time.Clock()
done=False
card_dict = {}
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\AC.png').convert()
card_dict["1_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\2C.png').convert()
card_dict["2_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\3C.png').convert()
card_dict["3_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\4C.png').convert()
card_dict["4_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\5C.png').convert()
card_dict["5_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\6C.png').convert()
card_dict["6_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\7C.png').convert()
card_dict["7_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\8C.png').convert()
card_dict["8_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\9C.png').convert()
card_dict["9_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\10C.png').convert()
card_dict["10_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\JC.png').convert()
card_dict["jack_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\QC.png').convert()
card_dict["queen_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\KC.png').convert()
card_dict["king_clubs"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\AS.png').convert()
card_dict["1_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\2S.png').convert()
card_dict["2_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\3S.png').convert()
card_dict["3_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\4S.png').convert()
card_dict["4_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\5S.png').convert()
card_dict["5_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\6S.png').convert()
card_dict["6_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\7S.png').convert()
card_dict["7_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\8S.png').convert()
card_dict["8_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\9S.png').convert()
card_dict["9_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\10S.png').convert()
card_dict["10_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\JS.png').convert()
card_dict["jack_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\QS.png').convert()
card_dict["queen_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\KS.png').convert()
card_dict["king_spades"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\AH.png').convert()
card_dict["1_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\2H.png').convert()
card_dict["2_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\3H.png').convert()
card_dict["3_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\4H.png').convert()
card_dict["4_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\5H.png').convert()
card_dict["5_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\6H.png').convert()
card_dict["6_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\7H.png').convert()
card_dict["7_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\8H.png').convert()
card_dict["8_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\9H.png').convert()
card_dict["9_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\10H.png').convert()
card_dict["10_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\JH.png').convert()
card_dict["jack_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\QH.png').convert()
card_dict["queen_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\KH.png').convert()
card_dict["king_hearts"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\AD.png').convert()
card_dict["1_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\2D.png').convert()
card_dict["2_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\3D.png').convert()
card_dict["3_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\4D.png').convert()
card_dict["4_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\5D.png').convert()
card_dict["5_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\6D.png').convert()
card_dict["6_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\7D.png').convert()
card_dict["7_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\8D.png').convert()
card_dict["8_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\9D.png').convert()
card_dict["9_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\10D.png').convert()
card_dict["10_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\JD.png').convert()
card_dict["jack_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\QD.png').convert()
card_dict["queen_diamonds"] = img
img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\KD.png').convert()
card_dict["king_diamonds"] = img
joker = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\joker.jpg').convert()
joker=pygame.transform.scale(joker,(71,96))
card_dict["joker"] = joker
declare=pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\declare.jpg').convert()
declare=pygame.transform.scale(declare,(80,80))
rect_list6=[[pygame.Rect(1100, 280, 80, 80),1100,280]]
game_over=pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\game_over.png').convert()
game_over=pygame.transform.scale(game_over,(300,150))

suit_store={"1_clubs":["C",1],"2_clubs":["C",2],"3_clubs":["C",3],"4_clubs":["C",4],"5_clubs":["C",5],"6_clubs":["C",6],
   "7_clubs":["C",7],"8_clubs":["C",8],"9_clubs":["C",9],"10_clubs":["C",10],"jack_clubs":["C",11],"queen_clubs":["C",12],
   "king_clubs":["C",13],"1_spades":["S",1],"2_spades":["S",2],"3_spades":["S",3],"4_spades":["S",4],
   "5_spades":["S",5],"6_spades":["S",6],"7_spades":["S",7],"8_spades":["S",8],"9_spades":["S",9],"10_spades":["S",10],
   "jack_spades":["S",11],"queen_spades":["S",12],"king_spades":["S",13],"1_hearts":["H",1],"2_hearts":["H",2],
   "3_hearts":["H",3],"4_hearts":["H",4],"5_hearts":["H",5],"6_hearts":["H",6],"7_hearts":["H",7],"8_hearts":["H",8],
   "9_hearts":["H",9],"10_hearts":["H",10],"jack_hearts":["H",11],"queen_hearts":["H",12],"king_hearts":["H",13],
   "1_diamonds":["D",1],"2_diamonds":["D",2],"3_diamonds":["D",3],"4_diamonds":["D",4],"5_diamonds":["D",5],
   "6_diamonds":["D",6],"7_diamonds":["D",7],"8_diamonds":["D",8],"9_diamonds":["D",9],"10_diamonds":["D",10],
   "jack_diamonds":["D",11],"queen_diamonds":["D",12],"king_diamonds":["D",13],"joker":["JJ",0]}

card_list1= ["1_clubs","2_clubs","3_clubs","4_clubs","5_clubs","6_clubs",
   "7_clubs","8_clubs","9_clubs","10_clubs","jack_clubs","queen_clubs",
   "king_clubs","1_spades","2_spades","3_spades","4_spades",
   "5_spades","6_spades","7_spades","8_spades","9_spades","10_spades",
   "jack_spades","queen_spades","king_spades","1_hearts","2_hearts",
   "3_hearts","4_hearts","5_hearts","6_hearts","7_hearts","8_hearts",
   "9_hearts","10_hearts","jack_hearts","queen_hearts","king_hearts",
   "1_diamonds","2_diamonds","3_diamonds","4_diamonds","5_diamonds",
   "6_diamonds","7_diamonds","8_diamonds","9_diamonds","10_diamonds",
   "jack_diamonds","queen_diamonds","king_diamonds"]
card_list2= ["1_clubs","2_clubs","3_clubs","4_clubs","5_clubs","6_clubs",
   "7_clubs","8_clubs","9_clubs","10_clubs","jack_clubs","queen_clubs",
   "king_clubs","1_spades","2_spades","3_spades","4_spades",
   "5_spades","6_spades","7_spades","8_spades","9_spades","10_spades",
   "jack_spades","queen_spades","king_spades","1_hearts","2_hearts",
   "3_hearts","4_hearts","5_hearts","6_hearts","7_hearts","8_hearts",
   "9_hearts","10_hearts","jack_hearts","queen_hearts","king_hearts",
   "1_diamonds","2_diamonds","3_diamonds","4_diamonds","5_diamonds",
   "6_diamonds","7_diamonds","8_diamonds","9_diamonds","10_diamonds",
   "jack_diamonds","queen_diamonds","king_diamonds"]
   
user=[] #user cards
user.append("joker")
comp=[] 
view_pile=[]
def shuffle():
	global user,comp,card_list1,card_list2,view_pile
	for i in range(12):
		c=random.choice(card_list1)
		user.append(c)
		card_list1.remove(c)
		
	for i in range(13):
		c=random.choice(card_list2)
		comp.append(c)
		card_list2.remove(c)
	for i in range(1):
		c=random.choice(card_list2)
		view_pile.append(c)
		card_list2.remove(c)
shuffle()
DISPLAYSURF.fill(BLUE)
x=10
y=100
z=10
w=430
x_coords1=[]
x_coords2=[]
x_coords3=[]
rect_comp=[]
rect_user=[]
rect_view=[]
def rect_list():
	x=10
	y=100
	z=10
	w=430
	global rect_comp,rect_user,rect_view,view_pile,comp,user
	for i in range(13):
		rect_comp.append([pygame.Rect(x, y, 71, 96),x,y,card_dict[comp[i]],comp[i]])
		x=x+75
	for i in range(13):
		rect_user.append([pygame.Rect(z, w, 71, 96),z,w,card_dict[user[i]],user[i]])
		z=z+75
	for i in range(1):
		rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[view_pile[i]],view_pile[i]])
rect_list()

img = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\Green_back.jpg').convert()
img=pygame.transform.scale(img,(71,96))
#name=input()
def textt(message):
		fontObj = pygame.font.Font('freesansbold.ttf', 32)
		textSurfaceObj = fontObj.render(message, True, GREEN)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (430, 240)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def textt2(message):
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	textSurfaceObj = fontObj.render(message, True, YELLOW)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (140, 560)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def textt3(message):
	xxx=350
	xxx=xxx+20
	fontObj = pygame.font.Font('freesansbold.ttf', 28)
	textSurfaceObj = fontObj.render(message, True, GREEN)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (1150, 470)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def textt4(message):
	xxx=350
	xxx=xxx+20
	fontObj = pygame.font.Font('freesansbold.ttf', 18)
	textSurfaceObj = fontObj.render(message, True, YELLOW)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (1170, 510)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def textt5(message):
	xxx=350
	xxx=xxx+20
	fontObj = pygame.font.Font('freesansbold.ttf', 18)
	textSurfaceObj = fontObj.render(message, True, YELLOW)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (1185, 550)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def textt6(message):
	xxx=350
	xxx=xxx+20
	fontObj = pygame.font.Font('freesansbold.ttf', 18)
	textSurfaceObj = fontObj.render(message, True, YELLOW)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (1163, 590)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
def textt7(message):
	xxx=350
	xxx=xxx+20
	fontObj = pygame.font.Font('freesansbold.ttf', 18)
	textSurfaceObj = fontObj.render(message, True, YELLOW)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (1130, 630)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)

point = pygame.image.load('C:\\Users\\new\\Desktop\\playing_cards\\point.jpg').convert()
point=pygame.transform.scale(point,(350,150))

def show_card():
	summ=0
	x=10
	y=100
	z=10
	w=430
	global rect_comp,rect_user,rect_view,view_pile,comp,user,countt
	DISPLAYSURF.fill(BLACK)
	DISPLAYSURF.blit(point,(1000,45))
	for i in range(13):
		#DISPLAYSURF.blit(card_dict[comp[i]],(x,y))
		DISPLAYSURF.blit(img,(x,y))
		x=x+75

	for i in range(13):
		DISPLAYSURF.blit(card_dict[user[i]],(z,w))
		z=z+75

	for i in range(1):

		pygame.draw.rect(DISPLAYSURF, RED, (500,270, 71, 96)) ##(X,y,width,height)
		DISPLAYSURF.blit(card_dict[view_pile[-1]],(500,270))###see
	for zz in comp:
		summ+=suit_store[zz][1]
	# if(summ>=80):
		# textt2("Your points = 80")
	# else:
	textt2("Your points = " + str(summ))
	textt3("SOME INSTRUCTIONS:")
	textt4("1. First select the card you want to take ")
	textt5("2. Then select the card you want to remove ")
	textt6("3. Wait for computer's turn to get over")
	textt7("4. Declare if you think it's valid")
	DISPLAYSURF.blit(img, (400, 270))
	DISPLAYSURF.blit(declare, (1100, 280))
	pygame.display.update()

show_card()
def show_card1():
	summ=0
	x=10
	y=100
	z=10
	w=430
	global rect_comp,rect_user,rect_view,view_pile,comp,user,countt
	DISPLAYSURF.fill(BLACK)
	DISPLAYSURF.blit(point,(1000,45))
	textt("You made a wrong move")
	for i in range(13):
		DISPLAYSURF.blit(img,(x,y))
		#DISPLAYSURF.blit(card_dict[comp[i]],(x,y))
		x=x+75

	for i in range(13):
		DISPLAYSURF.blit(card_dict[user[i]],(z,w))
		z=z+75

	for i in range(1):

		pygame.draw.rect(DISPLAYSURF, RED, (500,270, 71, 96)) ##(X,y,width,height)
		DISPLAYSURF.blit(card_dict[view_pile[-1]],(500,270))###see
	for zz in comp:
		summ+=suit_store[zz][1]
	# if(summ>=80):
		# textt2("Your points = 80" )
	# else:
	textt2("Your points = " + str(summ))
	textt3("SOME INSTRUCTIONS:")
	textt4("1. First select the card you want to take ")
	textt5("2. Then select the card you want to remove ")
	textt6("3. Wait for computer's turn to get over")
	textt7("4. Declare if you think it's valid")
	DISPLAYSURF.blit(img, (400, 270))
	DISPLAYSURF.blit(card_dict[rect_list5[-1][4]], (300, 270))
	DISPLAYSURF.blit(declare, (1100, 280))#########change
	pygame.display.update()


def textt1(message):
		fontObj = pygame.font.Font('freesansbold.ttf', 32)
		textSurfaceObj = fontObj.render(message, True, GREEN)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (500, 240)
		DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def check_user():
	index2,index3,index4,index5,index6,index7,index8,index9=0,0,0,0,0,0,0,0
	c1=0
	c2=0
	c3=0
	liste=[]
	list3=[]
	print(user)
	for zz in user:
		liste.append(suit_store[zz])
	liste.sort(key = lambda liste: liste[1])
	list3=liste[:]
	for i in liste:
		ccc=0
		for j in list3:
			if(i[1] == j[1]) :
				ccc=ccc+1
				if(ccc==1):
					index10=list3.index(j)
				if(ccc==2):
					index11=list3.index(j)
					break
		if(ccc==2):
			if(list3[index10-1][0]==list3[index10][0]):
				list3.remove(list3[index11])
			else:
				list3.remove(list3[index10])
	for j in range(len(list3)-3):
		if(list3[j+1][1]-list3[j][1]==1) and (list3[j+2][1]-list3[j+1][1]==1) and (list3[j+3][1]-list3[j+2][1]==1) and list3[j][0]==list3[j+1][0]==list3[j+2][0]==list3[j+3][0]:
			c1=1
			index2,index3,index4,index5=j,j+1,j+2,j+3
	for k in range(len(liste)-2):
		if(k!=index2 and k!=index3 and k!=index4 and k!=index5 and liste[k][1]==liste[k+1][1]==liste[k+2][1] and c1==1 ):
			return True 
	for m in range(len(list3)-2):
		if(m!=index2 and m!=index3 and m!=index4 and m!=index5 and list3[m+1][1]-list3[m][1]==1 and (list3[m+2][1]-list3[m+1][1]==1) and list3[m][0]==list3[m+1][0]==list3[m+2][0] and  c1==1):
			return True 
	if "joker" in user:
		for n in range(len(liste)-1):
			if(n!=index2 and n!=index3 and n!=index4 and n!=index5 and liste[n][1]==liste[n+1][1] and c1==1 ):
				return True
	if "joker" in user:
		for i in range(len(list3)-1):
			if((m!=index2 and m!=index3 and m!=index4 and m!=index5 and list3[m+1][1]-list3[m][1]==1) and list3[m+1]==list3[m] and c1==1):
				return True 
	for o in range(len(list3)-2):
		if(list3[o+1][1]-list3[o][1]==1) and (list3[o+2][1]-list3[o+1][1]==1) and list3[o][0]==list3[o+1][0]==list3[o+2][0]:
			c3=1
			index6,index7,index8=o,o+1,o+2	
	for p in range(len(list3)-3):
		if(p!=index6 and p!=index7 and p!=index8 and list3[p+1][1]-list3[p][1]==1) and (list3[p+2][1]-list3[p+1][1]==1) and (list3[p+3][1]-list3[p+2][1]==1) and  list3[p][0]==list3[p+1][0]==list3[p+2][0]==list3[p+3][0] and c3==1:
			return True 
	if "joker" in user:
		for q in range(len(list3)-2):
			if q!=index6 and q!=index7 and q!=index8 and  list3[q+1][1]-list3[q][1]==1 and (list3[q+2][1]-list3[q+1][1]==1) and list3[q][0]==list3[q+1][0]==list3[q+2][0]==list3[q+3][0]  and c3==1:
				return True			
	return False
			
		
def check_comp():
	index2,index3,index4,index5,index6,index7,index8,index9=0,0,0,0,0,0,0,0
	c1=0
	c2=0
	c3=0
	liste=[]
	list3=[]
	for zz in comp:
		liste.append(suit_store[zz])
	liste.sort(key = lambda liste: liste[1])
	list3=liste[:]
	for i in liste:
		ccc=0
		for j in list3:
			if(i[1] == j[1]) :
				ccc=ccc+1
				if(ccc==1):
					index10=list3.index(j)
				if(ccc==2):
					index11=list3.index(j)
					break
		if(ccc==2):
			if(list3[index10-1][0]==list3[index10][0]):
				list3.remove(list3[index11])
			else:
				list3.remove(list3[index10])

	for j in range(len(list3)-3):
		if(list3[j+1][1]-list3[j][1]==1) and (list3[j+2][1]-list3[j+1][1]==1) and (list3[j+3][1]-list3[j+2][1]==1) and list3[j][0]==list3[j+1][0]==list3[j+2][0]==list3[j+3][0]:
			c1=1
			index2,index3,index4,index5=j,j+1,j+2,j+3
	for k in range(len(liste)-2):
		if(k!=index2 and k!=index3 and k!=index4 and k!=index5 and liste[k][1]==liste[k+1][1]==liste[k+2][1] and c1==1 ):
			return True 
	for m in range(len(list3)-2):
		if((m!=index2 and m!=index3 and m!=index4 and m!=index5 and list3[m+1][1]-list3[m][1]==1) and (list3[m+2][1]-list3[m+1][1]==1) and list3[m][0]==list3[m+1][0]==list3[m+2][0] and  c1==1):
			return True 
	if "joker" in comp:
		for n in range(len(liste)-1):
			if(n!=index2 and n!=index3 and n!=index4 and n!=index5 and liste[n][1]==liste[n+1][1] and c1==1 ):
				return True
	if "joker" in comp:
		for i in range(len(list3)-1):
			if((m!=index2 and m!=index3 and m!=index4 and m!=index5 and list3[m+1][1]-list3[m][1]==1) and list3[m+1]==list3[m] and c1==1):
				return True 
	for o in range(len(list3)-2):
		if(list3[o+1][1]-list3[o][1]==1) and (list3[o+2][1]-list3[o+1][1]==1) and list3[o][0]==list3[o+1][0]==list3[o+2][0]:
			c3=1
			index6,index7,index8=o,o+1,o+2	
	for p in range(len(list3)-3):
		if(p!=index6 and p!=index7 and p!=index8 and list3[p+1][1]-list3[p][1]==1) and (list3[p+2][1]-list3[p+1][1]==1) and (list3[p+3][1]-list3[p+2][1]==1) and  list3[p][0]==list3[p+1][0]==list3[p+2][0]==list3[p+3][0] and c3==1:
			return True 
	if "joker" in comp:
		for q in range(len(list3)-2):
			if q!=index6 and q!=index7 and q!=index8 and  list3[q+1][1]-list3[q][1]==1 and (list3[q+2][1]-list3[q+1][1]==1) and list3[q][0]==list3[q+1][0]==list3[q+2][0]==list3[q+3][0]  and c3==1:
				return True			
	return False
new_var1=0
new_var2=0
new_var3=0
new_var4=0
new_var5=0
new_var6=0
new_var7=0
new_var8=0

def comp_move():
	index13,index14,index15=0,0,0
	index17,index18=0,0
	pp=0
	qq=0
	mm=0
	ss=2
	nn=2
	list155=[-1,-2,-3,-4,-5,-6,-8,-9,-10,-11,-12]
	global stocked_pile,view_pile,rect_view,rect_comp,rect_list4,comp,new_var1,new_var2
	list6=[]
	list8=[]
	rr=random.choice(list155)
	index13,index14,index15,index16=0,0,0,0
	last_card=random.choice(stocked_pile)
	stocked_pile.remove(last_card)
	for zz in comp:
		list6.append([zz,suit_store[zz]])
	list6.sort(key = lambda list6: list6[1][1])
	list8=list6[:]
	for i in list6:
		ccc=0
		for j in list8:
			if(i[1][1] == j[1][1]) :
				ccc=ccc+1
				if(ccc==1):
					index10=list8.index(j)
				if(ccc==2):
					index11=list8.index(j)
					break
		if(ccc==2):
			if(list8[index10-1][0]==list8[index10][0]):
				list8.remove(list8[index11])
			else:
				list8.remove(list8[index10])
		
	for o in range(11):
		if(list6[o][1][1]==list6[o+1][1][1]==list6[o+2][1][1] and new_var1!=1 and nn==1 ):      ########as is quickly formed, thus first condition
			index13,index14,index15=o,o+1,o+2
			new_var1=1
			if(suit_store[last_card][1]==list6[o][1][1]):
				if(o==0):
					del comp[-1]
					view_pile.append(comp[-1])
					rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[comp[-1]],comp[-1]])
					show_card()
				else:
					del comp[o-1]
					view_pile.append(o-1)
					rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[comp[o-1]],comp[o-1]])
					show_card()
				comp.append(last_card)
				show_card()
				pp=1
	for o in range(12):
		if(list6[o][1][1]==list6[o+1][1][1] and new_var1!=1 and ss==1):      ########as is quickly formed, thus first condition
			index17,index18=o,o+1
			new_var2=1
			if(suit_store[last_card][1]==list6[o][1][1]):
				if(o==0):
					del comp[-1]
					view_pile.append(comp[-1])
					rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[comp[-1]],comp[-1]])
					show_card()
				else:
					del comp[o-1]
					view_pile.append(o-1)
					rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[comp[o-1]],comp[o-1]])
					show_card()
				comp.append(last_card)
				show_card()
				mm=1
	for r in range(len(list8)-2):
		if r!=index13 and r!=index14 and r!=index15 and r!=index13-1 and r!=index15+1  and list8[r+1][1][1]-list8[r][1][1]==1 and list8[r+2][1][1]-list8[r+1][1][1]==1 and pp==0 and new_var2!=1:
			if(suit_store[last_card][1]-suit_store[comp[r]][1]==1):
				del comp[-3]
				view_pile.append(comp[-3])
				rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[comp[-3]],comp[-3]])
				comp.append(last_card)
				show_card()
				qq=1
			index6,index7=r,r+1
	if(pp==0 and qq==0 and mm==0):
		
		del view_pile[-1]
		view_pile.append(comp[-1])
		rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[comp[-1]],comp[-1]])
		del comp[rr]
		comp.append(last_card)
		show_card()
		rr=rr-2
	
stocked_pile=card_list2 + card_list1
rect_list4=[]
for i in stocked_pile:
	rect_list4.append([pygame.Rect(400, 270, 71, 96),400,270,card_dict[i],i])
rect_list5=[]
left_pile=[]
flag=0
tt=0
user_done=1
var1=0
var2=0
var3=0
var4=0
var5=0
user_turn=1
comp_turn=0
countt=1
while not done : 
	for event in pygame.event.get():
		if event.type == QUIT:
			done=True
			#pygame.quit()
			#sys.exit()
	if(user_turn==1 and comp_turn==0):

		x1, y1 = pygame.mouse.get_pos()
		xyz=pygame.mouse.get_pressed()[0]
		if xyz:
			pos_store1=(x1,y1)
			if(rect_view[0][0].collidepoint(pos_store1) ):
				if(var3==1):
					show_card1()
				else:
					pic_store1=rect_view[0][3]
					main_pos1=(rect_view[0][1],rect_view[0][2])
					print ("Match - ")
					tt=tt+1
			if(rect_list4[0][0].collidepoint(pos_store1) or var1==1 or var2==1 or var3==1):
				x3, y3 = pygame.mouse.get_pos()

				if(rect_list4[0][0].collidepoint(pos_store1)):
					if(var3==1):
						show_card1()
					else:
						new_card=random.choice(stocked_pile)
						stocked_pile.remove(new_card)
						DISPLAYSURF.blit(card_dict[new_card],(300,270))
						rect_list5.append([pygame.Rect(300, 270, 71, 96),300,270,card_dict[new_card],new_card])
				if(pygame.mouse.get_pressed()[0] ):
					var3=1
					pos_store8=(x3,y3)
					if(rect_list5[0][0].collidepoint((x3,y3)) and var2!=1):
						var1=1
				x5,y5=pygame.mouse.get_pos()
				if(pygame.mouse.get_pressed()[0] and var1>=1):
					pos_store6=(x5,y5)
					if(rect_list5[0][0].collidepoint(pos_store6)):
						var2=var2+1
				if(pygame.mouse.get_pressed()[0] and var2>=1):
					pos_store7=(x3,y3)
					var4=0
					for i in range(13):
						if(rect_user[i][0].collidepoint(pos_store7)and var4==0):
							main_pos3=(rect_user[i][1],rect_user[i][2])
							view_pile.append(rect_user[i][4])
							rect_view.append([pygame.Rect(500, 270, 71, 96),500,270,card_dict[rect_user[i][4]],rect_user[i][4]])
							user.remove(rect_user[i][4])
							user.insert(i,new_card)
							rect_user[i][3],rect_user[i][4]=card_dict[new_card],new_card
							show_card()
							pygame.display.update
							var1=0
							var2=0
							var3=0
							var4=var4+1
							var5=1
							comp_turn=1
							user_turn=0
		x6,y6=pygame.mouse.get_pos()
		if(pygame.mouse.get_pressed()[0] ):
			pos_store9=(x6,y6)
			if( var5==1):
				if(rect_list5[0][0].collidepoint(pos_store9)):
					var4=0
		time.sleep(0.2)
		if(flag==1 ):
			x2, y2 = pygame.mouse.get_pos()
			if(pygame.mouse.get_pressed()[0]):
				pos_store5=(x2,y2)
				for i in range(13):
					if(rect_user[i][0].collidepoint(pos_store5)):
						main_pos2=(rect_user[i][1],rect_user[i][2])
						print ("Match - ")
						index1=i
						view_pile.append(rect_user[i][4])
						view_pile.remove(rect_view[-1][4])############
						user.insert(i,rect_view[-1][4])
						user.remove(rect_user[i][4])
						var5,var6=rect_view[-1][3],rect_view[-1][4]
						rect_view[-1][3],rect_view[-1][4]=rect_user[index1][3],rect_user[index1][4]
						rect_user[index1][3],rect_user[index1][4]=var5,var6
						show_card()
						comp_turn=1
						user_turn=0						
						pygame.display.update()
						break
				flag=0
				user_done=1
				tt=0
			time.sleep(0.2)
		if(tt==1):
			flag+=1
			tt=0
		x7,y7=pygame.mouse.get_pos()
		if(pygame.mouse.get_pressed()[0] ):
			pos_store10=(x7,y7)
			if(rect_list6[0][0].collidepoint(pos_store10)):
				if(check_user()):
					show_card()
					DISPLAYSURF.blit(game_over,(300,270))
					textt("You won.....Game exits in 10 seconds")########add points
					pygame.display.update()
					done=True
				else:
					show_card()
					textt1("Invalid Declare...Computer won ...Game exits in 10 seconds")########add points
					pygame.display.update()					
					done=True
					
						
	if(comp_turn==1 and user_turn==0):
		time.sleep(2)
		if(check_comp()):
			textt("computer won....computer cards ")
			for i in range(13):
				DISPLAYSURF.blit(card_dict[comp[i]],(x,y))
				x=x+75
			done=True
		elif(check_comp != True ):
			comp_move()
			textt("Computer just made a move.....Your turn now")
		user_turn=1
		comp_turn=0
	pygame.display.update()
time.sleep(10)
pygame.quit()
sys.exit()

##music credits to death note-Anime
##pic credits to google