#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import random
# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 50  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
def servoDance():
  for x in range(1,4):
    if x ==1:
      flag = random.randint(0,1)
      if flag:
        pwm.setPWM(x,0,random.randint(150,300))
      else:
        pwm.setPWM(x,0,random.randint(450,600))
    elif x==2:
      pwm.setPWM(x,0,random.randint(100,450))
    else:
      pwm.setPWM(x,0,random.randint(servoMin+50,servoMax-50))
    
  for x in range(8,11):
    pwm.setPWM(x,0,random.randint(servoMin+50,servoMax-50))
  time.sleep(1)
  pwm.setAllPWM(0,servoMax/2)
  time.sleep(1)

for i in range(1,10):
  servoDance()
