import cv2
import sys
import numpy as np
import math

def distance(pointA, pointB):
	distance = math.sqrt(math.pow((pointA[0]-pointB[0]), 2) + math.pow((pointA[1]-pointB[1]), 2))
	return distance

def filterFingers(img):
	# Filters the four fingers
	# Crops the first quadrant

	# Returns an array of four filtered fingers images
	return fingerArray

def getPositions(imgArray):
	# Returns the positions of filtered blobs from given imgs
	return positions

def getMode(positionArray):
	# Finds mode using by filtering four color strips and finding positions

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