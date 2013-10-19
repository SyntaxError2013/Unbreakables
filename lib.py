import cv2
import sys
import numpy as np
import math

def distance(pointA, pointB):
	distance = math.sqrt(math.pow((pointA[0]-pointB[0]), 2) + math.pow((pointA[1]-pointB[1]), 2))
	return distance

def filterFingers(img):
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	ranges = [[(160, 179),(),()], [(38, 75),(),()], [(75, 130),(),()]]
	# Crop the first quadrant
	min = np.array([ranges[0][0][0], ranges[1][0][0], ranges[2][0][0]], np.uint8)
	max = np.array([ranges[0][0][1], ranges[1][0][1], ranges[2][0][1]], np.uint8)
	red = cv2.inRange(hsv, min, max)

	min = np.array([ranges[0][1][0], ranges[1][1][0], ranges[2][1][0]], np.uint8)
	max = np.array([ranges[0][1][1], ranges[1][1][1], ranges[2][1][1]], np.uint8)
	green = cv2.inRange(hsv, min, max)

	min = np.array([ranges[0][2][0], ranges[1][2][0], ranges[2][2][0]], np.uint8)
	max = np.array([ranges[0][2][1], ranges[1][2][1], ranges[2][2][1]], np.uint8)
	blue = cv2.inRange(hsv, min, max)
	fingerArray = [red, green, blue]
	# Returns an array of three filtered fingers images
	return fingerArray

def getPositions(imgArray):
	# Returns the positions of filtered blobs from given imgs

	count=0

	for img in imgArray:

		image, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		if len(contours)<1:
			#Error
			break


		cnt=contours[0]

		topmost = tuple(cnt[cnt[:,:,1].argmin()][0])

		positions[count]=topmost

		count++

	return positions

def getMode(positionArray):
	# Finds mode using by filtering three color strips and finding positions

	#Testing with Y coordinate Only

	R=positionArray[0][1]
	G=positionArray[1][1]
	B=positionArray[2][1]

	if R>G>B:
		mode='A'

	elif B>G>R:
		mode='C'

	elif R>B>G: 
		mode='D'

	elif G>B>R:
		mode='E'

	else:
		mode='G'

	return mode

def strum(mode, direction):
	# Plays the given mode using sox
	return

def getLowerBlob(img):
	# Filters lower blob and returns position
	return position