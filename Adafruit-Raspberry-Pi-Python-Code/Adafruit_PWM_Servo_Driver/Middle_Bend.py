from Adafruit_PWM_Servo_Driver import PWM
import time
pwm = PWM(0x40)

pwm.setPWM(2,0,400)
pwm.setPWM(3,0,200)
time.sleep(3)
pwm.setPWM(2,0,300)
pwm.setPWM(3,0,300)
