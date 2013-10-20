from bottle import route, run, template, static_file
import play
import frets
import thread

root = '/home/prakhar/dev/se13/Unbreakables/public/'

@route('/')
def index():
	return static_file('index.html', root=root, mimetype='text/html')

@route('/madfrets')
def index():
	thread.start_new_thread(frets.init())
	return "Initiated Capture"

@route('/css/<filename:re:.*\.css>')
def send_image(filename):
    return static_file(filename, root=root + '/css/', mimetype='text/css')

@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root=root + '/images/', mimetype='image/jpg')

run(host='localhost', port=12000)