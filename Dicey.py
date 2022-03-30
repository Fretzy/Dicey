import time
import thumby
import random

ver = "Ver. 0.1.1"

# BITMAP: width: 8, height: 7
manMap = bytearray([2,42,6,0,65,34,20,8])
manSprite = thumby.Sprite(8, 7, manMap, key=0)
manSprite.x = 64
manSprite.y = 1

# BITMAP: width: 8, height: 7
infoMap = bytearray([8,20,34,65,0,0,58,0])
infoSprite = thumby.Sprite(8, 7, infoMap, key=0)
infoSprite.x = 0
infoSprite.y = 1

# BITMAP: width: 4, height: 7
arrowMap = bytearray([65,34,20,8])
arrowSprite = thumby.Sprite(4, 7, arrowMap, key=0)

state = 0

dice = 1
incNum = 1
sides = 6
result = 0

while(True):

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
            state = 1
            
        if thumby.buttonR.justPressed():
            state = 2
    
        if thumby.buttonA.justPressed() or thumby.buttonB.justPressed():
            state = 3
    
        thumby.display.update()
     
    # Info Screen    
    while(state == 1):
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
    
    # Manual Screen
    while(state == 2):
        thumby.display.fill(0)
        
        thumby.display.blit(arrowMap, 0, 1, 4, 7, 0, 1, 0)
        thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
        thumby.display.drawText("DICEY", 13, 1, 1)
        thumby.display.drawLine(0, 10, 72, 10, 1)
        
    
        if thumby.buttonL.justPressed():
            state = 0
    
        thumby.display.update()
    
    # Dice Roller Screen
    while(state == 3):
        # Fill canvas to black
        thumby.display.fill(0)
        thumby.display.drawLine(0, 8, 72, 8, 1)
        
        if thumby.buttonB.pressed():
            incNum = 5
        else:
            incNum = 1
            
        if thumby.buttonU.justPressed():
            dice += incNum
        if thumby.buttonD.justPressed():
            dice -= incNum
        if thumby.buttonR.justPressed():
            sides += incNum
        if thumby.buttonL.justPressed():
            sides -= incNum
            
        if dice < 1:
            dice = 1
            
        if dice > 99:
            dice = 99
            
        if sides < 2:
            sides = 2
            
        if sides > 100:
            sides = 100
            
        if thumby.buttonA.justPressed():
            result = 0
            for x in range(dice):
                random.seed(time.ticks_us())
                result += random.randint(1, sides)
    
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText(str(dice), 0, 0, 1)
        thumby.display.drawText("d", len(str(dice)) * 6, 0, 1)
        thumby.display.drawText(str(sides), len(str(dice)) * 6 + 6, 0, 1)
        thumby.display.drawText(str(incNum), 66, 0, 1)
        if result != 0:
            #thumby.display.setFont("/lib/font8x8.bin", 8, 8, 1)
            thumby.display.drawText("Result: ", 0, 33, 1)
            thumby.display.drawText(str(result), 41, 33, 1)
        #thumby.display.drawText(str(timer), 0, 20, 1)
        thumby.display.update()
