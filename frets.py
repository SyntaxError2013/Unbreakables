import lib
import cv2
import time
import play

vc = cv2.VideoCapture(0)
ret, frame = vc.read()
prevLowerPos = (0, 0)

start = time.time()
gap = 0
prevStrum = ""

song = ""
gaps = []

while ret:
	cv2.imshow('preview', frame)

	hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	fingerImages = lib.fingerImages(hsvframe)
	fingerPositions = lib.getPositions(fingerImages)
	mode = lib.getMode(fingerPositions)

	#Add mode text

	lowerPos = lib.getLowerBlob(hsvframe)
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

	key = cv2.waitKey(20)
	ret, frame = vc.read()
	if key == 27:
		play.save('muse', song)
		break

cv2.destroyAllWindows()