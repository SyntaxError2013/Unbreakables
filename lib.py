import cv2
import numpy as np
import play

neck_len=500
neck_top=0
neck_bottom=500

strums = [
	['A',  'E4 C#3 A4 E3 A2 E2'],
	['C', 'E4 C3 G3 E3 C2 E2'],
	['D', 'F#4 D3 A4 D3 A2 E2'],
	['E', 'E4 B3 G#3 E3 B2 E2'],
	['G', 'G4 B3 G3 D3 B2 G2']]

"""
#(post_fix_num,note)

strums = [
	'A': [(3,7),(2,4),(3,0),(2,7),(1,0),(1,7)],
	'C': [(3,7),(2,3),(10,2),(2,7),(1,3),(1,7)],
	'D': [(3,9),(2,5),(3,0),(2,5),(1,0),(1,7)],
	'E': [(3,7),(2,2),(2,11),(2,7),(1,2),(1,7)],
	'G': [(3,10),(2,2),(2,10),(2,5),(1,2),(1,10)]]

"""

notes_ar = [['A1','A#1','B1','C1','C#1','D1','D#1','E1','F1','F#1','G1','G#1'],
		['A2','A#2','B2','C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2'],
		['A3','A#3','B3','C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3'],
		['A4','A#4','B4','C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4'],
		['A5','A#5','B5','C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5']]

# HSV color ranges
ranges = [[(160, 179),(106, 255),(0, 255)], # Red
		[(60, 90),(81, 255),(0, 255)],	# Green
		[(100, 119),(136, 255),(0, 255)]] # Blue

def clearNoise(img):
	kernel = np.ones((10, 10), np.uint8)
	clrimg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	clrimg = cv2.erode(morph, kernel, iterations=1)
	kernel = np.ones((20, 20), np.uint8)
	clrimg = cv2.dilate(morph, kernel, iterations=2)
	# Clears noise from image
	return clrimg

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

def filterFingers(img):
		
	height = img.shape[0]
	width = img.shape[1]

	imgcropped = img[0:(height/2), (width/2):(width-1)] # Cropping the ROI

	fingerArray = []

	for x in range(3):
		min = np.array([ranges[x-1][0][0], ranges[x-1][1][0], ranges[x-1][2][0]], np.uint8)
		max = np.array([ranges[x-1][0][1], ranges[x-1][1][1], ranges[x-1][2][1]], np.uint8)
		im = cv2.inRange(imgcropped, min, max)
		im = clearNoise(im)
		fingerArray.append(im)

	# Returns an array of three filtered fingers images
	return fingerArray

def getPositions(imgArray):
	# Returns the topmost points of filtered blobs from given imgs

	positions=[]

	for img in imgArray:

		contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		if len(contours)<1:
			positions.append((0,0))
			continue


		cnt=contours[0]

		topmost = tuple(cnt[cnt[:,:,1].argmin()][0])

		positions.append(topmost)

	return positions

def getMode(positionArray):
	# Finds mode using by filtering three color strips and finding positions

	#Testing with Y coordinate Only

	R=positionArray[0][1]
	G=positionArray[1][1]
	B=positionArray[2][1]

	if R<G<B:
		mode='A'

	elif B<G<R:
		mode='C'

	elif R<B<G: 
		mode='D'

	elif G<B<R:
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

	min = np.array([ranges[2][0][0], ranges[2][1][0], ranges[2][2][0]], np.uint8)
	max = np.array([ranges[2][0][1], ranges[2][1][1], ranges[2][2][1]], np.uint8)
	lowerhand = [cv2.inRange(imgcropped, min, max)]

	pos = getPositions(lowerhand)

	if pos != (0, 0):
		position = pos

	return position

def getPattern(mode,dist):
	pattern=''
	for note in strum[mode]:
		if(note[1]+dist>11):
			pattern=pattern+notes_ar[note[0]+1][(note[1]+dist)%12]+' '
		else
			pattern=pattern+notes_ar[note[0]][(note[1]+dist)%12]+' '

	return pattern

def initNeck(top,bottom):
	#Initialize the neck length
	neck_len=bottom[0]-top[0]
	neck_bottom=bottom[0]
	neck_top=top[0]

def getDistance(positions):
	#Get Distance on the neck
	mean=0

	for pos in positions:
		mean+=pos[0]

	mean=mean/3-neck_top

	if mean > 3*neck_len/4:
		return 3
	elif mean > 2*neck_len/4:
		return 2
	elif mean > neck_len/4:
		return 1
	else:
		return 0
