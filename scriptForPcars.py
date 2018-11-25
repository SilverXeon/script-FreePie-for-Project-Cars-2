import time

def openTC():
	#Open
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	for i in range(0, 4):
		vJoy[0].setButton(1, True)
		time.sleep(0.1)
		vJoy[0].setButton(1, False)
		time.sleep(0.15)
	
	vJoy[0].setButton(3, True)
	time.sleep(0.1)
	vJoy[0].setButton(3, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(1, True)
	time.sleep(0.1)
	vJoy[0].setButton(1, False)
	time.sleep(0.15)
	
def openABS():
	#Open
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	for i in range(0, 4):
		vJoy[0].setButton(1, True)
		time.sleep(0.1)
		vJoy[0].setButton(1, False)
		time.sleep(0.15)
	
	vJoy[0].setButton(3, True)
	time.sleep(0.1)
	vJoy[0].setButton(3, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(1, True)
	time.sleep(0.1)
	vJoy[0].setButton(1, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(1, True)
	time.sleep(0.1)
	vJoy[0].setButton(1, False)
	time.sleep(0.15)

def increase():
	#Increase
	vJoy[0].setButton(3, True)
	time.sleep(0.1)
	vJoy[0].setButton(3, False)
	time.sleep(0.15)
	
def decrease():
	#Increase
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
def moveToTC():
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
def moveToABS():
	vJoy[0].setButton(1, True)
	time.sleep(0.1)
	vJoy[0].setButton(1, False)
	time.sleep(0.15)
	
def closeABS():
	
	#Close
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
	for i in range(0, 4):
		vJoy[0].setButton(0, True)
		time.sleep(0.1)
		vJoy[0].setButton(0, False)
		time.sleep(0.15)
		
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
def closeTC():
	
	#Close
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
	for i in range(0, 4):
		vJoy[0].setButton(0, True)
		time.sleep(0.1)
		vJoy[0].setButton(0, False)
		time.sleep(0.15)
		
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
def changeMotor(motorNumber):
	#Open
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	for i in range(0,2):
		vJoy[0].setButton(1, True)
		time.sleep(0.1)
		vJoy[0].setButton(1, False)
		time.sleep(0.15)
	
	#change
	for i in range(0,2):
		vJoy[0].setButton(2, True)
		time.sleep(0.1)
		vJoy[0].setButton(2, False)
		time.sleep(0.15)
		
	for i in range(0, motorNumber):
		vJoy[0].setButton(3, True)
		time.sleep(0.1)
		vJoy[0].setButton(3, False)
		time.sleep(0.15)
		
	#exit
	for i in range(0,2):
		vJoy[0].setButton(0, True)
		time.sleep(0.1)
		vJoy[0].setButton(0, False)
		time.sleep(0.15)
		
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
def changeStrat(stratNumber):
	#Open
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	for i in range(0,5):
		vJoy[0].setButton(1, True)
		time.sleep(0.1)
		vJoy[0].setButton(1, False)
		time.sleep(0.15)
		
	vJoy[0].setButton(3, True)
	time.sleep(0.1)
	vJoy[0].setButton(3, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(1, True)
	time.sleep(0.1)
	vJoy[0].setButton(1, False)
	time.sleep(0.15)
		
	vJoy[0].setButton(3, True)
	time.sleep(0.1)
	vJoy[0].setButton(3, False)
	time.sleep(0.15)
	
	#Goto strat
	
	for i in range(0, stratNumber):
		vJoy[0].setButton(1, True)
		time.sleep(0.1)
		vJoy[0].setButton(1, False)
		time.sleep(0.15)
	
	#change strat
	vJoy[0].setButton(3, True)
	time.sleep(0.1)
	vJoy[0].setButton(3, False)
	time.sleep(0.15)
	
	#exit
	for i in range(0, stratNumber):
		vJoy[0].setButton(0, True)
		time.sleep(0.1)
		vJoy[0].setButton(0, False)
		time.sleep(0.15)
	
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	time.sleep(0.15)
	
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
	
	for i in range(0,5):
		vJoy[0].setButton(0, True)
		time.sleep(0.1)
		vJoy[0].setButton(0, False)
		time.sleep(0.15)
		
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	time.sleep(0.15)
		
def flash():
	vJoy[0].setButton(4, True)
	time.sleep(0.1)
	vJoy[0].setButton(4, False)
	
def up():
	vJoy[0].setButton(0, True)
	time.sleep(0.1)
	vJoy[0].setButton(0, False)
	
def down():
	vJoy[0].setButton(1, True)
	time.sleep(0.1)
	vJoy[0].setButton(1, False)
	
def left():
	vJoy[0].setButton(2, True)
	time.sleep(0.1)
	vJoy[0].setButton(2, False)
	
def right():
	vJoy[0].setButton(3, True)
	time.sleep(0.1)
	vJoy[0].setButton(3, False)
	
def light():
	vJoy[0].setButton(4, True)
	time.sleep(0.1)
	vJoy[0].setButton(4, False)

#---------------------------------Init--------------------------------------------
if starting :
	inOperation = False
	inTc = False
	inABS = False
	stratComplete = True
	lastStratButton = 0
	motorComplete = True
	lastMotorButton = 0
	flasherTime = time.time()
	lastFlash = time.time()
	flashOn = False
	startTime = time.time()
	diagnostics.debug("start")
	
#--------------------------------Flasher------------------------------

#TODO Bouton
if joystick[0].getPressed(0):
	diagnostics.debug("start flasher")
	flasherTime = time.time()
	lastFlash = time.time()
	flash()
	flashOn = True
	

#--------------------------------Mode moteur---------------------------------------------
#TODO Bouton
for i in range(0, 3):
	if joystick[0].getPressed(i) and i != lastMotorButton:
		diagnostics.debug("change to motor "+ str(i))
		inOperation = True
		motorComplete = False
		lastMotorButton = i
		startTime = time.time()
		
#--------------------------------Strat---------------------------------------------
#TODO Bouton
for i in range(0, 12):
	if joystick[0].getPressed(i) and i != lastStratButton:
		diagnostics.debug("change to strat "+ str(i))
		inOperation = True
		stratComplete = False
		lastStratButton = i
		startTime = time.time()

#----------------------------------TC------------------------------------------------
#TODO Bouton
if joystick[0].getPressed(0):
	
	if inOperation and inTc :
		diagnostics.debug("increase TC")
		increase()
		startTime = time.time()
	elif not inOperation :
		diagnostics.debug("open TC")
		inOperation = True
		inTc = True
		openTC()
		increase()
		startTime = time.time()
	elif inOperation and inABS:
		inTc = True
		inABS = False
		moveToTC()
		increase()
		startTime = time.time()
	else:
		diagnostics.debug("ignore TC")

#TODO Bouton
if joystick[0].getPressed(1):
	
	if inOperation and inTc :
		diagnostics.debug("decrease TC")
		decrease()
		startTime = time.time()
	elif not inOperation :
		diagnostics.debug("open TC")
		inOperation = True
		inTc = True
		openTC()
		decrease()
		startTime = time.time()
	elif inOperation and inABS:
		inTc = True
		inABS = False
		moveToTC()
		decrease()
		startTime = time.time()
	else:
		diagnostics.debug("ignore TC")

#----------------------------------ABS------------------------------------------------
#TODO Bouton
if joystick[0].getPressed(2):
	
	if inOperation and inABS :
		diagnostics.debug("increase ABS")
		increase()
		startTime = time.time()
	elif not inOperation :
		diagnostics.debug("open ABS")
		inOperation = True
		inABS = True
		openABS()
		increase()
		startTime = time.time()
	elif inOperation and inTc:
		inTc = False
		inABS = True
		moveToABS()
		increase()
		startTime = time.time()
	else:
		diagnostics.debug("ignore ABS")
		
#TODO Bouton		
if joystick[0].getPressed(3):
	
	if inOperation and inABS :
		diagnostics.debug("decrease ABS")
		decrease()
		startTime = time.time()
	elif not inOperation :
		diagnostics.debug("open ABS")
		inOperation = True
		inABS = True
		openABS()
		decrease()
		startTime = time.time()
	elif inOperation and inTc:
		inTc = False
		inABS = True
		moveToABS()
		decrease()
		startTime = time.time()
	else:
		diagnostics.debug("ignore ABS")


#-------------------Navigation manuelle-----------------------
if keyboard.getPressed(Key.UpArrow) and not inOperation:
	diagnostics.debug("up")
	up()
	
if keyboard.getPressed(Key.DownArrow) and not inOperation:
	diagnostics.debug("down")
	down()

if keyboard.getPressed(Key.LeftArrow) and not inOperation:
	diagnostics.debug("left")
	left()

if keyboard.getPressed(Key.RightArrow) and not inOperation:
	diagnostics.debug("right")
	right()

#TODO Corriger POV
if joystick[0].pov[0] and not inOperation:
	diagnostics.debug("up")
	up()
	
if joystick[0].pov[0] and not inOperation:
	diagnostics.debug("down")
	down()

if joystick[0].pov[0] and not inOperation:
	diagnostics.debug("left")
	left()

if joystick[0].pov[0] and not inOperation:
	diagnostics.debug("right")
	right()
	
if keyboard.getPressed(Key.L):
	diagnostics.debug("light")
	light()

#TODO Bouton
if joystick[0].getPressed(0):
	diagnostics.debug("light")
	light()
#----------------------Close automatique------------------------
if time.time() - startTime > 3 :
	if inOperation:
		inOperation = False
		if inTc :
			inTc = False
			diagnostics.debug("close TC")
			closeTC()
		if inABS :
			inABS = False
			diagnostics.debug("close ABS")
			closeABS()
		if not stratComplete:
			diagnostics.debug("strat "+ str(lastStratButton))
			changeStrat(lastStratButton)
			stratComplete = True
		if not motorComplete:
			diagnostics.debug("motor "+ str(lastMotorButton))
			changeMotor(lastMotorButton)
			motorComplete = True

if time.time() - flasherTime < 3:
	if time.time() - lastFlash > 0.3:
		diagnostics.debug("flasher")
		flash()
		lastFlash = time.time()
		flashOn = not flashOn
else:
	if flashOn:
		diagnostics.debug("stop flasher")
		flash()
		flashOn = False