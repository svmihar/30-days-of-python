import pyautogui
from PIL import Image, ImageGrab
from hehe import capture_screenshot
from time import time
from numpy import average as avg


AVG_END1 = []
AVG_END2 = []


def main():
    start = time()
    img2 = ImageGrab.grab(bbox=(1, 314, 1594, 1736))
    img2.save('image/baru.png', 'PNG')
    end1 = time() - start
    print(end1)

    start = time()
    img3 = capture_screenshot()
    img3 = img3.crop((1, 314, 1594, 1736))
    img3 = img3.save('image/hehe.png', 'PNG')
    end2 = time() - start
    print(end2)
    return end1, end2


if __name__ == "__main__":
    for _ in range(100): 
        x, y = main()
        AVG_END1.append(x)
        AVG_END2.append(y)

    print('finished')
    print(f"""
    USING IMAGEPIL GRAB: {avg(AVG_END1)}
    USING MSS : {avg(AVG_END2)}
    """)