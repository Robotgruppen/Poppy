from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40)

for x in range(150,600):
  if pwm.setPWM(1,0,x):
    print x
