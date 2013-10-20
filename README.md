Mad Frets
===
*Make you crave music like never before!*

A virtual guitar based on gesture recognition. Works on computer vision using webcams.

###Dependencies
* [Python 2.7.*](http://www.python.org)
* [Numpy](http://www.numpy.org)
* **OpenCV** Python : See setup instructions [here](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html#table-of-content-setup).

###Setting up
* Start the `server.py` script.
* Visit `http://localhost:12000` in your browser.
* To share your tracks, make sure your computer is connected to the internet.

###Using
* Put red, green and blue strips on your first three fingers.
* Use your left hand to make guitar modes (A, E, etc).
* Use your right hand (with a red strip) to strum a chord.
And that's it.

###Working
* The video frames are converted to HSV color space.
* HSV frames are filtered to detect the position of fingers (openCV).
* The positions of fingers determine the mode of playback.
* Strumming is identified by checking the positon of the right hand between frames.

###License
MIT Licensed
Copyright (C) 2013 Unbreakables.




