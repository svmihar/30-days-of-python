# bot clicker 
using pyautogui, pillow, mss     

inspiration came from [here](https://www.reddit.com/r/Python/comments/c1zx5f/created_a_click_bot_after_reading_automate_boring/)     


## disclaimer

works on mac, fixed the rescaling. 

## screen recording
![](https://i.imgur.com/pvJeOtp.gif)

should've been faster 😅

## using mss for screenshot
because depends on a screenshot method, `PIL ImageGrab` is too slow for capturing realtime data. So I decided to use mss for better(Faster) red pixel recognition    

iterating it 100 times each method has the average of :    
```python
USING IMAGEPIL GRAB: 0.5623156237602234ms
USING MSS : 0.3196454620361328ms
```