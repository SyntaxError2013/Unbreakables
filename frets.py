import lib
import cv2

vc = cv2.VideoCapture(0)
ret, frame = vc.read()
prevLowerPos = (0, 0)

while ret:
	cv2.imshow('preview', frame)

	fingerImages = lib.fingerImages(frame)
	fingerPositions = lib.getPositions(fingerImages)
	mode = lib.getMode(fingerPositions)

	lowerPos = lib.getLowerBlob(frame)
	if prevLowerPos != (0,0):
		# Check for up or down strum
		if down == 1:
			lib.strum(mode, 'down')
		else:
			if up == 1:
				lib.strum(mode, 'up')

	key = cv2.waitKey(20)
	ret, frame = vc.read()
	if key == 27:
		break

cv2.destroyAllWindows()