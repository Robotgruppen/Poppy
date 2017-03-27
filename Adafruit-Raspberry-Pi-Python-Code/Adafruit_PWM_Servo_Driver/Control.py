from Adafruit_PWM_Servo_Driver import PWM
import msvcrt
pwm=PWM(0x40)
speed=4
aq=300
sw=300
de=300
fr=300
gt=300
hy=300
def move():
  pwm.setPWM(1,0,aq)
  pwm.setPWM(2,0,sw)
  pwm.setPWM(3,0,de)
  pwm.setPWM(8,0,fr)
  pwm.setPWM(9,0,gt)
  pwm.setPWM(10,0,hy)
move()
while True:
  i = msvcrt.getch()
  if i == 'a':
    if aq > 150:
	  aq-=speed
  if i == 's':
    if sw > 150:
	  sw-=speed
  if i == 'd':
    if de > 150:
	  de-=speed
  if i == 'f':
    if fr > 150:
	  fr-=speed
  if i == 'g':
    if gt > 150:
	  gt-=speed
  if i == 'h':
    if hy > 150:
	  hy-=speed
  if i == 'q':
    if aq < 600:
	  aq+=speed
  if i == 'w':
    if sw < 600:
	  sw+=speed
  if i == 'e':
    if de < 600:
	  de+=speed
  if i == 'r':
    if fr < 600:
	  fr+=speed
  if i == 't':
    if gt < 600:
	  gt+=speed
  if i == 'y':
    if hy < 600:
	  hy+=speed
  move()
  if i == 'p'
    break
