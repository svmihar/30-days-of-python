from PIL import ImageGrab, Image
from mss import mss
import pyautogui
import time


def Click_Bot():  # In seconds

    print('time to switch!')
    time.sleep(3)  # Time to switch to https://www.mouseaccuracy.com/game

    while True:
        screen = capture_screenshot()
        screen = screen.crop((1,314,1594,1736))
        # screen.save(f'image/{asdf}.jpg')
        x, y = screen.size
        c_break = False
        for i in range(0, x, 5):  # Skip 10 pixels at each iter.
            if c_break:
                break

            for j in range(0, y, 5):
                # print(pic.getpixel((i, j)))
                r, g, b = screen.getpixel((i, j))

                if (r in range(230,250)):  # RED
                    print(f'clicking: {(i+1)/2},{(j+314)/2}')
                    pyautogui.click((i+1)/2, (j+314)/2)
                    c_break = True
                    break

def capture_screenshot():
    # Capture entire screen
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

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

