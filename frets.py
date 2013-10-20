import lib
import cv2
import time
import play
	
def init():
	#Initialize and configure

	vc = cv2.VideoCapture(0)
	
	configure()
	play()

	cv2.destroyAllWindows()



def configure():

	time.sleep(3)

	ret, frame = vc.read()
	
	if ret:
		hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		fingerImages = lib.filterFingers(hsvframe)
		fingerPositions = lib.getPositions(fingerImages)
		lowerPos = lib.getLowerBlob(hsvframe)
		lib.initNeck(fingerPositions[0],lowerPos)

	time.sleep(1)


def play():
	ret, frame = vc.read()

	# Timer for saving strum timings and saving music
	start = time.time()
	gap = 0
	prevStrum = ""
	song = []

	# Motion detection flags
	prevPos = 0
	direction = 0
	up = 0
	down = 0
	firstframe = 1

	while ret:
		# Change color space for better detection
		hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		fingerImages = lib.filterFingers(hsvframe)
		cv2.imshow('red', fingerImages[0])	
		cv2.imshow('green', fingerImages[1])
		cv2.imshow('blue', fingerImages[2])

		fingerPositions = lib.getPositions(fingerImages)

		# Detect the mode of playback
		mode = lib.getMode(fingerPositions)
		distance = lib.getDistance(fingerPositions)

		# Show the mode on screen
		cv2.putText(frame, mode , (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, 255)
		cv2.imshow('preview', frame)	
		
		# Find the postion of lower strumming hand
		lowerPos = lib.getLowerBlob(hsvframe)

		# Motion detection for lower hand
		if prevPos != 0:
			disp = lowerPos[0][1] - prevPos
			direction = direction + disp
			if direction < -200:
				up = 1
				direction = 0
			if direction > 200:
				down = 1
				direction = 0
		if firstframe == 1:
			firstframe = 0
		prevPos = lowerPos[0][1]
			
		# Perform the playback and append the strum in song
		if down == 1:
			if gap == 1:
				elapsed = time.time() - start
				song.append([prevStrum, elapsed])
				gap == 0
			play.play(lib.get_strum(mode, 'down'))
			if gap == 0:
				start = time.time()
				prevStrum = lib.get_strum(mode, 'down')
				gap = 1
			down = 0

		else:
			if up == 1:
				if gap == 1:
					elapsed = time.time() - start
					song.append([prevStrum, elapsed])
					gap == 0
				play.play(lib.get_strum(mode, 'up'))
				if gap == 0:
					start = time.time()
					prevStrum = lib.get_strum(mode, 'down')
					gap = 1
				up = 0

		ret, frame = vc.read()
		key = cv2.waitKey(20)
		if key == 27:	#Ends the session and save the song. Press ESCAPE key
			play.save('muse', song)
			break