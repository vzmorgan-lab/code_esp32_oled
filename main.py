import time
import my_oled

state = 0

while True:
   print(state)
    time.sleep(1)

    state = state + 1

    if state >=4:
        state = 0

    if state == 0
        my_oled_print_text("test", 0, 0)
    
    if state == 1:
        my_oled.print_text("something else", 0, 56)

    if state == 2:
        my_oled.oled.fill(0)
        my_oled.oled.line(0, 63, 127, 0, 1)
        my_oled.oled.show()

    if state == 3:
        my_oled.oled.fill(0)
        my_oled.graphic.fill_rect(64, 32, 64, 32, 1)
        my_oled.oled.show()
