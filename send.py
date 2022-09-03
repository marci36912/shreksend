import time
from pywinauto.keyboard import send_keys 

time.sleep(15)
for line in open('shrek.txt', 'r'):
    time.sleep(3)
    send_keys(line, with_spaces=True)
    time.sleep(2)
    send_keys('{ENTER}', with_spaces=True)