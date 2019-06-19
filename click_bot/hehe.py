from PIL import Image
import pyautogui
import time


def Click_Bot(duration):  # In seconds

    print('time to switch!')
    time.sleep(5)  # Time to switch to https://www.mouseaccuracy.com/game

    # A Black strip to cover the browser header
    im = Image.new('RGBA', (1680, 300), 'black')
    # A Black Strip to cover taskbar
    # im2 = Image.new('RGBA', (1280, 80), 'black')

    initial = time.time()

    while True:

        c_break = False

        pic = pyautogui.screenshot()

        pic.paste(im, (0, 0))

        x, y = pic.size
        # print(f'x: {x}\n y:{y}')

        for i in range(0, x, 10):  # Skip 10 pixels at each iter.

            if c_break:
                print('called c_break')
                break

            for j in range(200, y-80, 10):

                # print(pic.getpixel((i, j)))
                r, g, b, z = pic.getpixel((i, j))

                if (r in range(245, 254)):  # RED
                    # print(i, j)
                    # print(f'r: {r}')
                    pyautogui.click(i, j)
                    c_break = True
                    break

        if time.time() - initial > duration:
            break


if __name__ == "__main__":
    Click_Bot(30)
