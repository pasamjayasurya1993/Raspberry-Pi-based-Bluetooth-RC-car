import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

IN1=17
IN2=18
IN3=22
IN4=23

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

def forward():
    GPIO.output(IN1,1)
    GPIO.output(IN2,0)
    GPIO.output(IN3,1)
    GPIO.output(IN4,0)

def backward():
    GPIO.output(IN1,0)
    GPIO.output(IN2,1)
    GPIO.output(IN3,0)
    GPIO.output(IN4,1)

def left():
    GPIO.output(IN1,0)
    GPIO.output(IN2,1)
    GPIO.output(IN3,1)
    GPIO.output(IN4,0)

def right():
    GPIO.output(IN1,1)
    GPIO.output(IN2,0)
    GPIO.output(IN3,0)
    GPIO.output(IN4,1)

def stop():
    GPIO.output(IN1,0)
    GPIO.output(IN2,0)
    GPIO.output(IN3,0)
    GPIO.output(IN4,0)
