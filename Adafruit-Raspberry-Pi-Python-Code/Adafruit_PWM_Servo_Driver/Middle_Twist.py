from Adafruit_PWM_Servo_Driver import PWM
import time
pwm = PWM(0x40)

pwm.setPWM(1,0,450)
pwm.setPWM(8,0,150)
pwm.setPWM(2,0,400)
pwm.setPWM(3,0,200)
time.sleep(1)
pwm.setPWM(9,0,200)
time.sleep(3)
pwm.setAllPWM(0,280)
time.sleep(1)
pwm.setAllPWM(0,300)
