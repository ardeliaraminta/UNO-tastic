  
import random 
from tkinter import *

# colours is stored, cardnum = numbers/ type of uno cards (skip, reverse, +2,  wild, +4)
# 1-9 = numbers, special cards =  (10 = skip, 11 = reverse, 12 = +2 , 13 = wild, 14 = +4 wildcard)

class Card:
    def __init__(self, color,cardnum):                                                               
        self.color = color #stores color of the card
        self.cardnum = cardnum #stores the card based on their functionality and numbers
        self.img = PhotoImage(file=str(cardnum)+" "+str(color)+".png") #stores the image of the cards 
        self.but= Button(area_toplay,image=self.img, command = self.useCard, cursor = "heart") #create a button using image of the card

    def useCard(self):
        if self.cardnum == discard.cards[0].cardnum or self.color == discard.cards[0].color or self.color == 4: #if the card can be played of the same number of diffrent color or same colour different number or wildcard/+4 
            playCard(self) #play that card
            endClear()

class Deck:

# to make a deck and empty deck if the card is available == 1, create a full deck and if available == 0, make an empty deck 
# 4 colours ( red, yellow, green, blue) except wildcards and make 2 copies of each cards 
# create deck
    def __init__(self, available): #create 115 cards in deck 
        self.cards = [] #create an empty deck 
        self.available = available 
        if self.available == 1: #if available 1, make a full deck. if available = 0, make an empty deck 
            for i in range(4): #for everycard except wildcard
                self.cards.append(Card(i,0)) #make 1 zero card 
                for twice in range(2): #make duplicate of card of the cards below 
                    for special_cards in range(0,13): #number cards 0-9, skip, reverse and +2 
                        self.cards.append(Card(i, special_cards))
            for w in range(4): # make 4 wildcards and 4 +4 wildcards 
                for wildcard in range(13,15): #13 - wildcard, 14- +4 wildcard 
                    self.cards.append(Card(4,wildcard))
                random.shuffle(self.cards) #shuffle the deck 

 # removes and returns the value of the cards in position of the deck, if the card is empty, refresh the pile using the discard pile    
    def arrange(self, position): 
        try:
            return self.cards.pop(position)
        except IndexError: #if the draw pile is empty 
            RefreshDraw() #refresh the draw pile using the discard pile 
            return self.cards.position(position)
    
    def add_front_deck(self, card): #add card in front of the deck
        self.cards = [card] + self.cards 

#Fuctions used with buttons 

def endButton(): # activate when End Turn button is clicked 
	global counterturn 
	endClear() #clear the screen for next turn 
	counterturn = (counterturn + direction)%len(playernames)  # advance to the next turnk
	showNext() 

 # when the Next Turn is clicked
def nextButton():
	nextbut.pack_forget() # remove the Next Turn button
	nextTurn() # create a setup the next turn for the next player


def leftArrow(): # when left arrow is clicked
	global pagenum
	pagenum -= 1 #change the cards in playerhands on the left page by one 
	refreshCards()  # create the new page display up


def rightArrow(): # when right arrow is clicked
	global pagenum
	pagenum += 1  #change the cards in playerhands on the right page by one if there are more than 5 cards in hand 
	refreshCards() # create the new page display up


# when the color picker button is clicked
# remove the color choices on the screen
def redClick():
	discard.cards[0].color = 0 #red
	clearChoice() 

def yellowClick(): 
	discard.cards[0].color = 1 #yellow
	clearChoice()

def greenClick(): 
	discard.cards[0].color = 2 #green 
	clearChoice()

def blueClick():
	discard.cards[0].color = 3 ## blue
	clearChoice()

# clear the color choices from the screen
def clearChoice(): 
	colorinstructions.pack_forget() 
	for x in unocolours: 
		x.pack_forget()
	showNext() 

# Main Game Functions

# setup for the launch of the game that allow the selection numbers of players to proceed
def Setup():
	spacer_label1.pack(side = TOP)  
	welcome_label.pack()
	number_label.pack() #this will ask how many players  
	spacer_label2.pack()
	playerselection.pack() # listbox to select how many players playing
	choices = ["2", "3", "4"] # choices for number of users
	for i in range(len(choices)): 
		playerselection.insert(i, choices[i])
	spacer_label3.pack()
	numberokaybutton.pack()  #display okay button

#after clicking okay to a selected amount of players
def Confirm(): 
	global listofentries, numberofplayers  #make these two variables global
	spacer_label2.pack_forget()
	spacer_label3.pack_forget()
	numberofplayers = [playerselection.get(i) for i in playerselection.curselection()] # the number of players = the number from the listbox
	numberofplayers = int(numberofplayers[0]) #convert from string to int
	listofentries = [] #make a list for the different text entry boxes
	numberokaybutton.pack_forget() #delete all number of users pieces
	playerselection.pack_forget()
	number_label.pack_forget() 
	name_label.pack(side=TOP) #ask names of users
	for i in range(numberofplayers): #create one text entry for each user
		listofentries.append(0)
		listofentries[i] = Entry(area_toplay)
		listofentries[i].pack()
	confirm_names_button.pack() #enter button
#confirm numbers of players 

def EnterName(): # if the input names are confirmed
	for i in range(numberofplayers): # repeat for as many players there are
		playernames.append(listofentries[i].get()) # add to the list playernames each entered name
		listofentries[i].pack_forget()  # delete text entry
	confirm_names_button.pack_forget()  # delete other aspects
	name_label.pack_forget() 
	welcome_label.pack_forget() # remove everything from the screen
	spacer_label3.pack_forget()
	Begin()

 # starts the game
def Begin():
	sevenCards()
	createDiscard()
	nextTurn()

window = Tk() 
# create a hand of 7 cards for each player in the game
def sevenCards():
	for i in range(len(playernames)):  # make an empty deck for each player in the game
		playerhands.append(Deck(0)) 

 # each player will get 7 cards in their hands
	for i in range(7):
		for x in playerhands:
			x.add_front_deck(drawpile.arrange(0))

 # makes the discard pile at the beginning of the game
def createDiscard():
	while True: #start the game by creating discard pile 
		discard.add_front_deck(drawpile.arrange(0)) #continuous loop of adding the cards
		if discard.cards[0].cardnum <= 9: #until the 1-9 number cards is on top the process continues 
			break
#draw card 
def drawCard(): 
	playerhands[counterturn].cards.append(drawpile.arrange(0)) # adds card to end of player's hand
	drawbut.pack_forget() # remove draw button so they can't draw more than one card in a turn
	refreshCards() # refresh the cards in hand so they can access the new card they have just drawn
	endbut.pack() # show the Next Turn button

# it will run when a card that can be played is clicked on
# if the player now has no cards in their hand run win()
def playCard(card):
	global direction, counterturn
	cardindex = playerhands[counterturn].cards.index(card) 
	endClear() 
	discard.add_front_deck(playerhands[counterturn].arrange(cardindex)) 
	if len(playerhands[counterturn].cards) == 0:
		win() 

# this is the function of special cards that defne the loop of the game

	if card.cardnum == 10: # skip
		counterturn = (counterturn+(2*direction))%len(playernames)
		showNext() 
	elif card.cardnum == 11: # reverse
		direction = direction * (-1) # reverse the direction of the turns
		counterturn = (counterturn + direction)%len(playernames)
		showNext()
	elif card.cardnum == 12: # + 2
		for i in range(2):
			playerhands[(counterturn+direction)%len(playernames)].cards.append(drawpile.arrange(0)) # next player draws 2 cards
		counterturn = (counterturn+(2*direction))%len(playernames) # skip that player
		showNext()
	elif card.cardnum == 13: # wildcard
		counterturn = (counterturn + direction)%len(playernames)
		colorPicker() # allow player to pick the color of their wildcard
	elif card.cardnum == 14: # + 4
		for i in range(4):
			playerhands[(counterturn+direction)%len(playernames)].cards.append(drawpile.arrange(0))
		counterturn = (counterturn+(2*direction))%len(playernames) 
		colorPicker() # gets player to pick the color of their wild draw4 card
	else: # number cards
		counterturn = (counterturn + direction)%len(playernames)
		showNext()

#transition of players' turns and so the next player can start their turn
def showNext():
	nextbut.config(text = playernames[counterturn] + ", please click to take your turn.") 
	nextbut.pack(side = TOP) 

# runs when next button is clicked
def nextTurn(): 
	refreshInformation() 
	refreshBoard()

def colorPicker():
	colorinstructions.pack(side=TOP) 
	for x in unocolours: 
		x.pack(side=TOP)

# clears the screen at the end of a player's turn
def endClear(): 
	global pagenum
	pagenum = 0 #
	drawbut.pack_forget() 
	endbut.pack_forget()
	topcard.pack_forget()
	discardlabel.pack_forget()
	leftbut.pack_forget()
	rightbut.pack_forget()
	wildlabel.pack_forget()
	for x in playerhands[counterturn].cards:
		x.but.pack_forget()

 # refreshes the board
def refreshBoard(): 
	refreshCards() # shows their first page of cards
	refreshDiscard() # updates top of discard pile
	drawbut.pack() # adds the draw button 
# refreshes the player's cards in hand

# Refreshes the information at the top of the in-game screen when the next player goes
def refreshInformation(): 
	for i in range(len(playernames)): 
		infolist[i].pack_forget() #clear the information of the current player
		# Changes the text of each of the information labels
		if i == counterturn: # if it is the player's turn
			infolist[i].config(text = playernames[i] + " , now it's your turn!")
		else: #  if it isn't the player's turn then show how many cards left in hand
			infolist[i].config(text = playernames[i] + " Player cards in hand:" + str(len(playerhands[i].cards)))
	infolist[4].pack_forget() # remove the draw pile label
	infolist[4].config(text = "Cards left in draw pile: " + str(len(drawpile.cards))) # refresh the draw pile display
	for i in range(len(playernames)): # add the number of cards in the the other playerhand
		infolist[i].pack(fill = Y, side=LEFT) # add each player's information
	infolist[4].pack(fill = Y) # add draw pile display back

def refreshCards(): 
	for x in playerhands[counterturn].cards:  #remove every card in the player's hand from the screen
		x.but.pack_forget()
	leftbut.pack_forget() # remove the left arrow
	rightbut.pack_forget() # remove the right arrow
	if pagenum > 0: #if not in the first page
		leftbut.pack(side=LEFT) # add left arrow so the player can scroll left of page
	for x in playerhands[counterturn].cards[pagenum:pagenum+5]:
		x.but.pack(side=LEFT) # Show 5 cards (or fewer) in the player's hand depending on which page you are on
	if pagenum < len(playerhands[counterturn].cards)-5:
		rightbut.pack(side=LEFT)  

def refreshDiscard(): # update the discard
	discardlabel.pack(side = TOP) # add a label to show that this is the top card of the discard pile 
	if discard.cards[0].cardnum == 13 or discard.cards[0].cardnum == 14: # if the front of the card is wildcard or +4 wildcard 
		wildlabel.config(text = "This wild card is \n" + colorlist[discard.cards[0].color], fg = colorlist[discard.cards[0].color])
		wildlabel.pack() #add colour text to indicate the wildcard chosen 
	topcard.config(image = discard.cards[0].img) # update the image of the discard pile 
	topcard.pack(side=RIGHT) # put the topcard right in 

def refreshDraw():
	discardlength = len(discard.cards) #if the drawpile ran out, every card will reshuffle from the discard pile but not the top card 
	for i in range(discardlength-1):
		drawpile.add_front_deck(discard.arrange(-1)) # move every cards except the top front card of deck, starting with the bottom card, of the discard pile to the draw pile
	random.shuffle(drawpile.cards) # shuffle the new draw pile

# remove everything on the main in-game screen
def win():
	information.pack_forget() 
	leftbox.pack_forget()
	area_toplay.pack_forget()
	rightbox.pack_forget()
	butbox.pack_forget()
	discardbox.pack_forget()
	winbox.pack()
	winbox.pack_propagate(0) 
	winlabel.config(text = playernames[counterturn] + " wins!", fg = "white", bg = "pale violet red") #show the winner 
	winlabel.pack(fill=BOTH) 


# Setting up the main frames in the game
#propagate - stop the window from sinking
information = Frame(window, width = 1000, height = 50) # show information  at the top
information.pack_propagate(0) 
information.pack()
leftbox = Frame(window, width = 64, height = 300, bg = "burlywood4") # box for left arrow
leftbox.pack_propagate(0)
leftbox.pack(side=LEFT)
area_toplay = Frame(window, width = 650, height = 300, bg = "burlywood4") # create area of the game to play with the cards
area_toplay.pack_propagate(0)
area_toplay.pack(side=LEFT)
rightbox = Frame(window, width = 64, height = 300, bg = "burlywood4") # box for right arrow
rightbox.pack_propagate(0)
rightbox.pack(side=LEFT)
butbox = Frame(window, width = 130, height = 300, bg =  "burlywood4") #box for button 
butbox.pack_propagate(0)
butbox.pack(side=LEFT)
discardbox = Frame(window, width = 125, height = 300, bg =  "burlywood4") # box for top of discard pile
discardbox.pack_propagate(0)
discardbox.pack(side=LEFT) 
winbox = Frame(window, width = 1000, height = 350) # box when a player wins. Gets packed at the end

# Creating labels & buttons
topcard = Label(discardbox) # displays image of top of discard pile
discardlabel = Label(discardbox, text = "Game Discard Pile ", bg = "black", fg = "burlywood2", width = 18, height = 3) # Shows that this card is the discard pile
winlabel = Label(winbox, font=("Courier", 60))
drawbut = Button(butbox, text = "Draw Card", command = drawCard, width = 10, height = 2 )
endbut = Button(butbox, text = "End Turn", command = endButton)
nextbut = Button(area_toplay, text = "Next Player, please click this button to begin your turn.", width = 30, height = 3, command = nextButton)
leftimage = PhotoImage(file="leftarrow1.png")
leftbut = Button(leftbox, image = leftimage, command = leftArrow)
rightimage = PhotoImage(file="rightarrow1.png")
rightbut = Button(rightbox, image = rightimage, command = rightArrow)

# Creating variables & objects
playernames = [] # 
playerhands = [] # this list will be used to call on each player hands  
drawpile = Deck(1) # create a full deck 
discard = Deck(0) # create an initial empty discard pile
direction = 1 # direction flow of the game but can be reversed with a special card : reverse card
counterturn = 0 # corresponds to the index of the player whose turn it is
pagenum = 0 #determines which page of hards in the player's hand gets displayed
infolist = [Label(information, bg = "antique white"), Label(information, bg = "lightblue"), Label(information, bg = "thistle"),Label(information, bg = "LightPink2"),Label(information)] 
unocolours = [Button(butbox, bg='red', height = 2, width = 10, command = redClick), Button(butbox,  bg='orange', height = 2, width = 10, command = yellowClick),Button(butbox,  bg='green',  height = 2, width = 10, command = greenClick),Button(butbox, bg='blue',  height = 2, width = 10, command = blueClick)]
colorinstructions = Label(area_toplay, text = "Choose a color you would like your wild card to be.", bg = "burlywood4", fg = "black", font=("Helvetica", 12, "bold italic"))
wildlabel = Label(discardbox, bg = "burlywood3")  # displays the color of wild card
colorlist = ["red","yellow","green","blue"]  # used to convert color from numbers to strings
playerselection = Listbox(area_toplay, selectmode = BROWSE, width =5, height=8) #this is the listbox for selecting the number of players
confirm_names_button = Button(area_toplay, text = "Enter", command = EnterName) #this is the button to confirm the names inputted
name_label = Label(area_toplay, text = 'Enter Player Names')
number_label = Label(area_toplay, text = 'Select Number of Players')
welcome_label = Label(area_toplay, text = "Welcome to UNO!Tastic", fg = "black",
		 bg = "burlywood3",
		 font = "Helvetica 16 bold italic") # welcome label 
numberokaybutton = Button(area_toplay, text = "Okay", command = Confirm) #this is the button to confirm number of players selection
spacer_label1 = Label(area_toplay, bg = "burlywood4")
spacer_label2 = Label(area_toplay, bg = "burlywood4")
spacer_label3 = Label(area_toplay, bg = "burlywood4")


Setup() #begin the setup !!!!!!!

window.title("UNO!tastic ")

window.mainloop()
