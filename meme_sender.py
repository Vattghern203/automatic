import pyautogui as pa
import pyperclip as pc
import time as t

pa.PAUSE = 1 # Pause between commands

pa.press("win") # opening win search
pa.write("gmail") # searching for gmail
pa.press("enter") # opening it

t.sleep(10) # time for gmail loading

pa.click(x=110, y=309) # clicks on "write a new email"
pc.copy("EMAIL GOES HERE") # the destinatary goes here

t.sleep(10) # sleep time until the email window opens
pa.hotkey("ctrl", "v") # paste the destinatary to the email window
pa.press("tab") # switch to the email subject
pa.write("Meme Sender V.001") # paste the subject here
pa.press("tab") # switch to email itself

txt = '''
    Vou enviar um meme kkkk
'''
# your email goes here

pc.copy(txt) # its copied to the clipboard

pa.hotkey("ctrl", "v") # its pasted to the email 

pa.click(x=1304, y=1027) # clicks on the anex button

pa.click(x=128, y=328) # open the image library at explorer

pa.click(x=851, y=552, clicks=2) # double clicks on the meme folder

pa.click(x=690, y=260) # clicks on the designated meme

pa.click(x=698, y=669) # ckiks on the send button

t.sleep(35) # waits for the upload

pa.hotkey("ctrl", "enter") # and finally, sends the email