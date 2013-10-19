import cv2
import sys
import numpy as np
import math
import play

strums = [
	['A',  'E4 C#3 A4 E3 A2 E2'],
	['C', 'E4 C3 G3 E3 C2 E2'],
	['D', 'F#4 D3 G#3 D3 A2 E2'],
	['E', 'E4 B3 G#3 E3 B2 E2'],
	['G', 'G4 B3 G3 D3 B2 G2']]

def get_strum(mode, direction):
	if direction == 'up':
		for row in strums:
			if row[0] == mode:
				return row[1]
	else:
		for row in strums:
			if row[0] == mode:
				rev = ""
				_array = row[1].split(" ")
				for row2 in reversed(_array):
					rev += row2 + " "
				return rev[:-1]

def strum(mode, direction):
	play.play(get_strum(mode, direction))

def distance(pointA, pointB):
	distance = math.sqrt(math.pow((pointA[0]-pointB[0]), 2) + math.pow((pointA[1]-pointB[1]), 2))
	return distance

def filterFingers(img):
	ranges = [[(160, 179),(),()], [(38, 75),(),()], [(75, 130),(),()]]
	
	height = img.shape[0]
	width = img.shape[1]

	imgcropped = img[0:(height/2), (width/2):(width-1)] # Cropping the ROI

	min = np.array([ranges[0][0][0], ranges[1][0][0], ranges[2][0][0]], np.uint8)
	max = np.array([ranges[0][0][1], ranges[1][0][1], ranges[2][0][1]], np.uint8)
	red = cv2.inRange(imgcropped, min, max)

	min = np.array([ranges[0][1][0], ranges[1][1][0], ranges[2][1][0]], np.uint8)
	max = np.array([ranges[0][1][1], ranges[1][1][1], ranges[2][1][1]], np.uint8)
	green = cv2.inRange(imgcropped, min, max)

	min = np.array([ranges[0][2][0], ranges[1][2][0], ranges[2][2][0]], np.uint8)
	max = np.array([ranges[0][2][1], ranges[1][2][1], ranges[2][2][1]], np.uint8)
	blue = cv2.inRange(imgcropped, min, max)
	fingerArray = [red, green, blue]
	# Returns an array of three filtered fingers images
	return fingerArray

def getPositions(imgArray):
	# Returns the topmost points of filtered blobs from given imgs

	count=0

	positions=[]

	for img in imgArray:

		image, contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		if len(contours)<1:
			positions[count]=(0,0)
			count+=1
			continue


		cnt=contours[0]

		topmost = tuple(cnt[cnt[:,:,1].argmin()][0])

		positions[count]=topmost

		count+=1

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

def getLowerBlob(img):
	# Filters lower blob and returns position
	position = (0, 0)
	height = img.shape[0]
	width = img.shape[1]

	imgcropped = img[(height/2):(height-1), 0:(width/2)] # Cropping the ROI
	
	ranges = [(160, 179),(),()]

	min = np.array([ranges[0][0], ranges[0][0], ranges[0][0]], np.uint8)
	max = np.array([ranges[0][1], ranges[0][1], ranges[0][1]], np.uint8)
	lowerhand = [cv2.inRange(imgcropped, min, max)]

	pos = getPositions(lowerhand)

	if pos != (0, 0):
		position = pos

	return position

print get_strum('G', 'down')