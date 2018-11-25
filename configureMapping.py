import time

def up():
	time.sleep(5)
	diagnostics.debug("press")
	vJoy[0].setButton(0, True)
	time.sleep(1)
	vJoy[0].setButton(0, False)
	time.sleep(0.05)
	
def down():
	time.sleep(5)
	diagnostics.debug("press")
	vJoy[0].setButton(1, True)
	time.sleep(1)
	vJoy[0].setButton(1, False)
	time.sleep(0.05)
	
def left():
	time.sleep(5)
	diagnostics.debug("press")
	vJoy[0].setButton(2, True)
	time.sleep(1)
	vJoy[0].setButton(2, False)
	time.sleep(0.05)

def right():
	time.sleep(5)
	diagnostics.debug("press")
	vJoy[0].setButton(3, True)
	time.sleep(1)
	vJoy[0].setButton(3, False)
	time.sleep(0.05)
	
def light():
	time.sleep(5)
	diagnostics.debug("press")
	vJoy[0].setButton(4, True)
	time.sleep(1)
	vJoy[0].setButton(4, False)
	time.sleep(0.05)
	
if starting:
	diagnostics.debug("start")
	
if keyboard.getPressed(Key.UpArrow):
	diagnostics.debug("up")
	up()
	
if keyboard.getPressed(Key.DownArrow):
	diagnostics.debug("down")
	down()

if keyboard.getPressed(Key.LeftArrow):
	diagnostics.debug("left")
	left()

if keyboard.getPressed(Key.RightArrow):
	diagnostics.debug("right")
	right()
	
if keyboard.getPressed(Key.L):
	diagnostics.debug("L")
	light()