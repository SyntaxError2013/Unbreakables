import lib
import cv2
import time
import play

vc = cv2.VideoCapture(0)
ret, frame = vc.read()
prevLowerPos = (0, 0)

# Timer for saving strum timings and saving music
start = time.time()
gap = 0
prevStrum = ""
song = []

while ret:

	# Change color space for better detection
	hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	fingerImages = lib.fingerImages(hsvframe)
	fingerPositions = lib.getPositions(fingerImages)
	# Detect the mode of playback
	mode = lib.getMode(fingerPositions)

	# Show the mode on screen
	cv2.putText(frame, mode , (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, 255)
	cv2.imshow('preview', frame)	
	
	# Find the postion of lower strumming hand
	lowerPos = lib.getLowerBlob(hsvframe)

	# ------- Motion detection for lower hand
	if prevLowerPos != (0,0):

		# Check for up or down strum
		
		if down == 1:
			if gap == 1:
				elapsed = time.time() - start
				song.append([prevStrum, elapsed])
				gap == 0
			play.play(lib.modeToNotes(mode, 'down'))
			if gap == 0:
				start = time.time()
				prevStrum = lib.modeToNotes(mode, 'down')
				gap = 1

		else:
			if up == 1:
				if gap == 1:
					elapsed = time.time() - start
					song.append([prevStrum, elapsed])
					gap == 0
				play.play(lib.modeToNotes(mode, 'up'))
				if gap == 0:
					start = time.time()
					prevStrum = lib.modeToNotes(mode, 'down')
					gap = 1

	ret, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27:	#Ends the session and save the song. Press ESCAPE key
		play.save('muse', song)
		break

cv2.destroyAllWindows()