import pyautogui as pa
import pyperclip as pc
import time as t

pa.PAUSE = 1

pa.press("win")
pa.write("chrome")
pa.press("enter")

t.sleep(5)
pa.click(x=1096, y=698)

pc.copy("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
pa.hotkey("ctrl", "v")
pa.press("enter")

t.sleep(5)
pa.click(x=464, y=996)


