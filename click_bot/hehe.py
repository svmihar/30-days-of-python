from PIL import ImageGrab, Image
from mss import mss
import pyautogui
import time


def Click_Bot():  # In seconds

    print('time to switch!')
    time.sleep(5)  # Time to switch to https://www.mouseaccuracy.com/game

    while True:
        screen = ImageGrab.grab(bbox=(1,260,1594,1736))
        print('are you ready?')
        x, y = screen.size
        print(screen.size)
        c_break = False
        for i in range(0, x, 5):  # Skip 10 pixels at each iter.
            if c_break:
                break

            for j in range(0, y, 5):
                # print(pic.getpixel((i, j)))
                r, g, b, a = screen.getpixel((i, j))

                if (r in range(230,250)):  # RED
                    print(f'clicking: {i+1},{j+263}')
                    pyautogui.click(i+1, j+263)
                    c_break = True
                    break

if __name__ == "__main__":
    Click_Bot()
""" 
419, 73
1679, 73

419, 1049
1679, 1049

grab(bbox=(419, 73, 1679, 1049))

1680 x 1050
3360 x 2100
 """

