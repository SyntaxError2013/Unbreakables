import requests

# send(	file_name - Name of file to be sent from /music
# 	url [OPTIONAL] - URL to send the file to
# 	)
# returns:
#	ERROR_UPLOAD 100
#	ERROR_ALREADY_EXISTS 101
#	ERROR_NO_FILE_SENT 102
#	ERROR_MOVE_UPLOADED_FILE_FAILED 103
#	ERROR_NO_RESPONSE 160
#	SUCCESS 150

ERROR_NO_RESPONSE = 160
def send(file_name, user = "Anonymous", url = "http://localhost:8080/share"):
	files = { 'linkin_park' : open('music/' + file_name + '.wav', 'rb')}
	data = {'email': user}
	r = requests.post(url, files=files, data=data)
	if not r.text == '':
		return int(r.text)
	else:
		return ERROR_NO_RESPONSE