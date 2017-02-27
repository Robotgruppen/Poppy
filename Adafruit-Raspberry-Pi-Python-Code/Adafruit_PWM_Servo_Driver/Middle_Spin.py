from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

pwm.setPWM(1,0,450)
pwm.setPWM(8,0,150)
time.sleep(3)
pwm.setAllPWM(0,300)
#pwm.setPWM(1,0,300)
#pwm.setPWM(8,0,300)
