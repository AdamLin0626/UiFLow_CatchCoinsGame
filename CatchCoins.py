from m5stack import *
from m5ui import *
from uiflow import *
import time
import unit


setScreenColor(0x111111)
dual_button0 = unit.get(unit.DUAL_BUTTON, unit.PORTA)


LineY = None
my_1X = None
my_2X = None
my_3X = None
score = None



rectangle0 = M5Rect(8, 70, 2, 90, 0xFFFFFF, 0xFFFFFF)
label0 = M5TextBox(83, 70, "Score:00", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=90)

import random



def btnBlue0_wasPressed():
  global LineY, my_1X, my_2X, my_3X, score
  rectangle0.setPosition(8, 0)
  LineY = -1
  pass
dual_button_0.btnBlue.wasPressed(btnBlue0_wasPressed)
def btnBlue0_wasReleased():
  global LineY, my_1X, my_2X, my_3X, score
  rectangle0.setPosition(8, 70)
  LineY = 0
  pass
dual_button_0.btnBlue.wasReleased(btnBlue0_wasReleased)
def btnRed0_wasPressed():
  global LineY, my_1X, my_2X, my_3X, score
  rectangle0.setPosition(8, 150)
  LineY = 1
  pass
dual_button_0.btnRed.wasPressed(btnRed0_wasPressed)
def btnRed0_wasReleased():
  global LineY, my_1X, my_2X, my_3X, score
  rectangle0.setPosition(8, 70)
  LineY = 0
  pass
dual_button_0.btnRed.wasReleased(btnRed0_wasReleased)

label0.hide()
my_1X = 98
my_2X = 98
my_3X = 98
LineY = 0
score = 0
for count in range(10):
  if random.randint(1, 3) == 1:
    # left
    while not my_1X == 8:
      my_1X = my_1X - 3
      lcd.circle(my_1X, 45, 10, fillcolor=)
      wait_ms(1)
      lcd.clear()
      rectangle0.show()
    if LineY == -1:
      score = score + 1
    my_1X = 98
  elif random.randint(1, 3) == 2:
    # mid
    while not my_2X == 8:
      my_2X = my_2X - 3
      lcd.circle(my_2X, 120, 10, fillcolor=)
      wait_ms(1)
      lcd.clear()
      rectangle0.show()
    if LineY == 0:
      score = score + 1
    my_2X = 98
  elif random.randint(1, 3) == 3:
    # right
    while not my_3X == 8:
      my_3X = my_3X - 3
      lcd.circle(my_3X, 190, 10, fillcolor=)
      wait_ms(1)
      lcd.clear()
      rectangle0.show()
    if LineY == 1:
      score = score + 1
    my_3X = 98
label0.hide()
label0.setText(str((str('Score :') + str(score))))
