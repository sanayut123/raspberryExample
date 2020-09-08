import time
import RPi.GPIO as GPIO
import pygame

GPIO.setwarnings(False)
in1 = 17 # Physical Pin 11
in2 = 27 # Physical Pin 13
in3 = 22 # Physical Pin 15
in4 = 23 # Physical Pin 18
GPIO.setmode(GPIO.BCM) # Use GPIO numbering instead of physical numbering
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
fw = True
ba = True
tl = True
tr = True
rl = True
rr = True
def forward():
    #ซ้าย
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    #ขวา
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

def back():
        #ซ้าย
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    #ขวา
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
def turnLeft():
        #ซ้าย
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    #ขวา
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

def turnRight():
    #ซ้าย
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    #ขวา
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
def rotateLeft():
     #ซ้าย
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    #ขวา
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
def rotateRight():
    #ซ้าย
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    #ขวา
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
def stopMotor():
    #ซ้าย
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    #ขวา
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

widht = 500
high = 500

fps = 30

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((widht,high))
pygame.display.set_caption("ART Control Car")
clock = pygame.time.Clock()

runing = True
while runing:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    even = pygame.key.get_pressed()
        #print(even)
    if even[pygame.K_UP] and even[pygame.K_LEFT]:
        if rl:
            rotateLeft()
            rl = False
    elif even[pygame.K_UP] and even[pygame.K_RIGHT]:
        if rr:            
            rotateRight()
            rr = False
    elif even[pygame.K_LEFT]:
        if tl:
            tl = False
            turnLeft()  
    elif even[pygame.K_RIGHT]:
        if tr:
            tr = False
            turnRight()
    elif even[pygame.K_UP]:
        if fw:
            fw = False
            forward()
    elif even[pygame.K_DOWN]:
        if ba:
            ba = False
            back()
    else:
        fw = True
        ba = True
        tl = True
        tr = True
        rl = True
        rr = True
        stopMotor()
    #elif event[pygame.K_LEFT]:
     #   pass
            #print("not press")
        
            
 #   screen.fill(black)
 #   pygame.display.flip()
    
    
pygame.quit()





