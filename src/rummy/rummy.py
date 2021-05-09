import pygame,sys,random,pygame.mouse,time
from pygame.locals import *
pygame.init()
DISPLAYSURF= pygame.display.set_mode((600,600))
pygame.display.set_caption('Rummy:- Saurav Rao')
suits=["C","H","S","D"]
ranks=["A","2","3","4","5","6","7","8","9","T","J","Q","K"]
rankvalue={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13}

def checkbook(sequence):
	for card in sequence:
		if card.rank!=sequence[0].rank:
			return False
	return True

def checkrun(sequence):
		rankvalue["A"]=1
		sortt(sequence)
		for card in sequence:
			if card.suit!=sequence[0].suit:
				return False
		if sequence[0].rank =="A":
			if sequence[1].rank=="Q" or sequence[1].rank=="J" or sequence[1].rank=="K":
				rankvalue[sequence[0].rank]=14
				sortt(sequence)
		for i in range(1,len(sequence)):
			if rankvalue[sequence[i].rank]!=rankvalue[sequence[i-1].rank]+1:
				return False
		return True

def sortt(sequence):
	complete=False
	while complete==False:
		complete =True
		for i in  range(0,len(sequence)-1):
			if rankvalue[sequence[i].rank]>rankvalue[sequence[i+1].rank]:
				temp=sequence[i+1]
				sequence[i+1]=sequence[i]
				sequence[i]=temp
				complete=False
	return sequence


class card:
	def __init__(self,rank,suit):
		self.suit=suit
		self.rank=rank

class deck:
	def __init__(self):
		self.cards=[]
		for suitt in suits:
			for rankk in ranks:
				self.cards.append(card(rankk,suitt))
	def shuffle(self):
		random.shuffle(self.cards)
	
	def drawcard(self):
		drawn_card= self.cards[0]
		self.cards.pop(0)
		return drawn_card

class player:
	def __init__(self,name,deck,game):
		self.stash=[]
		self.name=name 
		self.deckk=deck
		self.game=game
	def givecard(self,card):
		try:
			self.stash.append(card)
			if len(self.stash)>14:
				raise ValueError("CARD LIMIT REACHED")
		except ValueError as err:
			print(err.args)
	def drop(self,cardd):
		if cardd not in self.stash:
			return False
		self.stash.remove(cardd)
		#self.game.addpile(cardd)
		return True
	def close(self):
		ar = [self.stash[:3], self.stash[3:6], self.stash[6:9], self.stash[9:]]
		for s in ar:
			if checkrun(s) == False and checkbook(s) == False:
				return False

		return True

class game:
	def __init__(self,deck):
		self.pile=[]
		self.players=[]
		self.players.append(player("YOU",deck,self))
		self.players.append(player("COMPUTER",cdeck,self))
	
	def displaypile(self):
		if len(self.pile)==0:
			return "EMPTY PILE"
		else:
			return self.pile
	def addpile(self,card):
		self.pile.insert(0,card)
	def drawpile(self):
		if len(self.pile)>0:
			return self.pile.pop(0)
		else:
			return None
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
font = pygame.font.Font('freesansbold.ttf', 32)

cdeck=deck()
cdeck.shuffle()
g=game(cdeck)
g0=g.players[0]
g1=g.players[1]
for i in range(13):
	for elem in g.players:
		card=cdeck.drawcard()
		elem.givecard(card)
first_card = cdeck.drawcard()

g.addpile(first_card)

def show1(g0):
	x=50
	y=400
	for a in g0.stash:
		card1=pygame.image.load(r'..\\assets\\'+a.rank+a.suit+".png")
		DISPLAYSURF.blit(pygame.transform.scale(card1, (70, 100)), (x, y))
		x+=30
def show(x,y):
	white = (255, 255, 255) 
	green = (0, 255, 0) 
	blue = (0, 0, 128) 
	font = pygame.font.Font('freesansbold.ttf', 32)
	text1= font.render('#', True, green, blue)
	DISPLAYSURF.blit(text1,(x,y))

def showpile(a):
	card1=pygame.image.load(r'..\\assets\\'+a.rank+a.suit+".png")
	DISPLAYSURF.blit(pygame.transform.scale(card1, (70, 100)), (200,200))
def showdeck():
	card1=pygame.image.load(r'..\\assets\\red_back.png')
	DISPLAYSURF.blit(pygame.transform.scale(card1, (70, 100)), (100,200))


def show2(g1):
	x=50
	y=50
	for a in g1.stash:
		card1=pygame.image.load(r"..\\assets\\red_back.png")
		DISPLAYSURF.blit(pygame.transform.scale(card1, (70, 100)), (x, y))
		x+=30


def get_object(x,y):
	count=0
	if y>=400 and y<=500 and len(g0.stash)==14:
		i=(x-50)//30
		if 0<=i<len(g0.stash): 
			a=g0.stash[i]
			g0.drop(a)
			g.addpile(a)
			count+=1
	if y>=200 and y<=300 and len(g0.stash)<14:
		if 100<x and x <170 :
			a=cdeck.drawcard()
			g0.stash.insert(0,a)
			count+=1
		elif 200<x and x<270:
			a=g.drawpile()
			if a!=None:
				g0.stash.insert(0,a)
				count+=1
	return count
def computerturn():
	if len(g1.stash)<14:
		if random.randint(0,1)==1 and len(g.pile)>0:
			a=g.drawpile()
			if a!=None:
				g1.stash.insert(0,a)
		else :
			a=cdeck.drawcard()
			g1.stash.insert(0,a)
	
	pygame.display.update()
	if len(g1.stash)==14:
		i=random.randint(0,13)
		a=g1.stash[i]
		g1.drop(a)
		g.addpile(a)

def declare():
	white = (255, 255, 255) 
	green = (0, 255, 0) 
	blue = (0, 0, 128) 
	font = pygame.font.Font('freesansbold.ttf', 50)
	text1= font.render('Declare', True, green, blue)
	DISPLAYSURF.blit(text1,(300,200))

z=0
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	DISPLAYSURF.fill((0,0,0))
	(xa,yb)=pygame.mouse.get_pos()
	(button1, button2, button3)=pygame.mouse.get_pressed()
	if button1==True:
		(x,y)=pygame.mouse.get_pos()
		z+=get_object(x,y)
		if x<400 and x>300 and y>200 and y<250:
			if g0.close()==True:
				DISPLAYSURF.fill((0,0,0))
				text0=font.render("You Won", True, green,(0,0,0))
				DISPLAYSURF.blit(text0,(150,350))
				break
			else:
				text0=font.render("Please Continue", True, green,(0,0,0))
				DISPLAYSURF.blit(text0,(150,350))

	if z==2:
		text0=font.render(g.players[1].name+" to play now", True, green,(0,0,0))
		DISPLAYSURF.blit(text0,(100,10))
		
		show1(g0)
		if len(g.pile)>0:
			showpile(g.pile[0])
		if len(cdeck.cards)>1:
			showdeck()
		pygame.display.update()
		computerturn()
		z=0
	declare()
	if z==0:
		text0=font.render("Draw a card",True,blue,(0,0,0))
		DISPLAYSURF.blit(text0,(100,10))

	if z==1:
		text0=font.render("Discard a card",True,blue,(0,0,0))
		DISPLAYSURF.blit(text0,(100,10))
	sortt(g.players[0].stash)

	show1(g0)
	if len(g.pile)>0:
		showpile(g.pile[0])
	if len(cdeck.cards)>1:
		showdeck()
	show2(g1)
	

	
	pygame.display.update()
