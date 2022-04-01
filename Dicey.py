import time
import thumby
import random

# Begin Sprites/Bitmaps
# Manual Button: width: 8, height: 7
manMap = bytearray([2,42,6,0,65,34,20,8])
manSprite = thumby.Sprite(8, 7, manMap, key=0)
manSprite.x = 64
manSprite.y = 1

# Info Button: width: 8, height: 7
infoMap = bytearray([8,20,34,65,0,0,58,0])
infoSprite = thumby.Sprite(8, 7, infoMap, key=0)
infoSprite.x = 0
infoSprite.y = 1

# Arrow: width: 4, height: 7
arrowMap = bytearray([65,34,20,8])
arrowSprite = thumby.Sprite(4, 7, arrowMap, key=0)
# End Sprites/Bitmaps


# Begin Variables Init
ver = "Ver. 0.2.1"
state = 0
modState = 1
maxHistory = 10

dice = 1
incNum = 1
sides = 6
resultInt = 0
history = []
histBegin = 0
# End Variables Init


# Begin Functions
def printResults():
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
    if resultInt != 0:
        thumby.display.drawText(str(history[0]), 0, 33, 1)
        if len(history) >= 2:
            thumby.display.drawText(str(history[1]), 0, 24, 1)
        if len(history) >= 3:
            thumby.display.drawText(str(history[2]), 0, 15, 1)
            
def cleanHistory():
    if len(history) == maxHistory:
        history.pop(9)
        
def printHistory():
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
    if resultInt != 0 and histBegin < len(history):
        thumby.display.drawText(str(history[histBegin]), 0, 33, 1)
        if len(history) > histBegin + 1:
            thumby.display.drawText(str(history[histBegin + 1]), 0, 24, 1)
        if len(history) > histBegin + 2:
            thumby.display.drawText(str(history[histBegin +2]), 0, 15, 1)

    
# End Functions


# Splash Screen

###

# End Splash Screen


###########
# Main Loop
while(True):

    ##############
    # Title Screen
    while(state == 0):
        thumby.display.fill(0)
        thumby.display.drawSprite(infoSprite)
        thumby.display.drawSprite(manSprite)
        thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
        thumby.display.drawText("DICEY", 13, 1, 1)
        thumby.display.drawLine(0, 10, 72, 10, 1)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("Thumby", 17, 13, 1)
        thumby.display.drawText("Dice Roller", 4, 21, 1)
        thumby.display.drawLine(0, 30, 72, 30, 1)
        thumby.display.drawText("press a/b", 10, 32, 1)
        
        if thumby.buttonL.justPressed():
            state = 10
            
        if thumby.buttonR.justPressed():
            state = 20
    
        if thumby.buttonA.justPressed() or thumby.buttonB.justPressed():
            state = 40
    
        thumby.display.update()
     
    #############
    # Info Screen    
    while(state == 10):
        thumby.display.fill(0)
        
        thumby.display.blit(arrowMap, 68, 1, 4, 7, 0, 0, 0)
        thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
        thumby.display.drawText("DICEY", 13, 1, 1)
        thumby.display.drawLine(0, 10, 72, 10, 1)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("By Alexander", 0, 13, 1)
        thumby.display.drawText("Fretz", 30, 21, 1)
        thumby.display.drawLine(0, 30, 72, 30, 1)
        thumby.display.drawText(str(ver), 6, 32, 1)
        
        if thumby.buttonR.justPressed():
            state = 0
        
        thumby.display.update()
    
    #################
    # Manual Screen 1
    while(state == 20):

        thumby.display.fill(0)
        thumby.display.blit(arrowMap, 0, 1, 4, 7, 0, 1, 0)
        thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
        thumby.display.drawText("MANUAL", 10, 1, 1)
        thumby.display.drawLine(0, 10, 72, 10, 1)
        thumby.display.drawSprite(manSprite)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("A: Roll Dice", 0, 13, 1)
        thumby.display.drawText("B: Switch #", 0, 23, 1)
        thumby.display.drawText("Mode", 30, 31, 1)
        
        if thumby.buttonR.justPressed():
            state = 21
            
        if thumby.buttonL.justPressed():
            state = 0
                
        thumby.display.update()
 
    #################
    # Manual Screen 2
    while(state == 21):

        thumby.display.fill(0)
        thumby.display.blit(arrowMap, 0, 1, 4, 7, 0, 1, 0)
        thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
        thumby.display.drawText("MANUAL", 10, 1, 1)
        thumby.display.drawLine(0, 10, 72, 10, 1)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("U/D: # Dice", 0, 15, 1)
        thumby.display.drawText("L/R: # Sides", 0, 26, 1)
        
        if thumby.buttonL.justPressed():
            state = 20
                
        thumby.display.update() 
    
    ####################        
    # Dice Roller Screen
    while(state == 40):
        
        # Blank screen, then draw divider
        thumby.display.fill(0)
        thumby.display.drawLine(0, 8, 72, 8, 1)
        
        # Change State Modifier
        if thumby.buttonB.justPressed():
            modState += 1
        if modState > 4:
            modState = 1
            
        # Display # State Modifier
        if modState == 1:
            thumby.display.drawText("*1", 60, 0, 1)
        if modState == 2:
            thumby.display.drawText("*5", 60, 0, 1)
        if modState == 3:
            thumby.display.drawText("*10", 54, 0, 1) 
        if modState == 4:
            state = 50
#        if modState == 4:
#            thumby.display.drawText("History (A)", 0, 0, 1)
            
            
        # Define Incrementation Value based on State Modifier
        if modState == 2:
            incNum = 5
        elif modState == 3:
            incNum = 10
        else:
            incNum = 1
            
        # Let User Change numDie & Sides
        if thumby.buttonU.justPressed():
            dice += incNum
        if thumby.buttonD.justPressed():
            dice -= incNum
        if thumby.buttonR.justPressed():
            sides += incNum
        if thumby.buttonL.justPressed():
            sides -= incNum
        
        # Enforce Minimum and Maximum numDie & Sides 
        if dice < 1:
            dice = 1
        if dice > 99:
            dice = 99
        if sides < 2:
            sides = 2
        if sides > 100:
            sides = 100
            
        # Print numDie & Sides
        if modState != 4:
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText(str(dice), 0, 0, 1)
            thumby.display.drawText("d", len(str(dice)) * 6, 0, 1)
            thumby.display.drawText(str(sides), len(str(dice)) * 6 + 6, 0, 1)
            
        # Roll the dice on buttonA press unless modState is 4, in which case open history screen
        if thumby.buttonA.justPressed():
            if modState != 4:
                resultInt = 0
                for x in range(dice):
                    random.seed(time.ticks_us())
                    resultInt += random.randint(1, sides)
                result = "{}d{}:{}".format(dice, sides, resultInt)
                history.insert(0, result)
#            else:
#                state = 50
            
        cleanHistory()
        printResults()    
        thumby.display.update()
        
    ################
    # History Screen
    while(state == 50):
        
        # Blank screen, then draw divider
        thumby.display.fill(0)
        thumby.display.drawLine(0, 8, 72, 8, 1)
        thumby.display.drawText("History", 0, 0, 1)
        
        thumby.display.drawText("{}-{}".format(histBegin + 1, histBegin + 3), 55, 0, 1)
        
        if thumby.buttonU.justPressed():
            if histBegin < len(history) - 3:
                histBegin += 1

        if thumby.buttonD.justPressed():
            if histBegin > 0:
                histBegin -= 1
        
        if thumby.buttonB.justPressed():
            modState = 1
            state = 40
        
        printHistory()
        thumby.display.update()
        