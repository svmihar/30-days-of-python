import pyautogui
from PIL import Image, ImageGrab



img = Image.open('image/baru.png')

print(img.size)

# 22, 118
# 814, 119

# 20, 915
# 813, 915

img2 = ImageGrab.grab(bbox=(1,263,1594,1736))
img2.save('image/baru.png', 'PNG')