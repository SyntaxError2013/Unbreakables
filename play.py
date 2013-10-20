import subprocess
import decimal
import thread

#Usage
# play(notes  - The string containing notes (eg: "A0 B3 E1 C4")
# 	delay_period [OPTIONAL] - Delay between notes' playback
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)

# save(file_name - The file to save to. Do not include an extension
# 	notes  - Array of a 2 element arrays (eg: [["A3 G2", 0.00], ["C3 D1", 0.07]])
# 		The strums play at the time specified in the second argument for each row.
# 	delay_period [OPTIONAL] - Delay between notes' playback (within a particular strum)
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)

def _gen_string(notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	notes_array = notes.split(" ")
	final = ""
	for i in notes_array:
		final += "pl " + i + " "
	if not delay_period == 0:
		two_places = decimal.Decimal ('10') ** -2
		j = 0
		final += "delay "
		while j < len(notes_array):			
			final += str(decimal.Decimal(delay_period * j).quantize(two_places)) + " "
			j += 1	

	j = 0
	if not fade == [0, 0, 0]:
		final += "remix - fade "
		while j < len(fade):
			final += str(fade[j]) + " "
			j += 1
		final += "norm -1"

	return final

def _gen_times(base, size, delay_period = 0.05):
	times = ""
	j = 0
	k = 0
	two_places = decimal.Decimal ('10') ** -2
	while j < size:
		times += str(decimal.Decimal(base + delay_period * j).quantize(two_places)) + " "
		j += 1

	k = delay_period * (j-1) + base
	return k, times


def _play(notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	subprocess.call("play -n synth " + _gen_string(notes, delay_period, fade), shell = True)
	return

def _save(file_name, notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	final = "sox -n music/" + file_name + ".wav synth "
	note_s = ""
	for row in notes:
		final += _gen_string(row[0], 0, [0, 0, 0])
	
	j = 0
	if not fade == [0, 0, 0]:
		final += "delay "
		
		base = 0
		times = " "
		for row in notes:
			base, times = _gen_times(base + row[1], len(row[0].split(" ")), delay_period)
			final += times

	j = 0
	if not fade == [0, 0, 0]:
		final += "remix - fade "
		while j < len(fade):
			final += str(fade[j]) + " "
			j += 1

		final += "norm -1"
	subprocess.call(final, shell = True)

def play(notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	thread.start_new_thread(_play, (notes, delay_period, fade))

def save(file_name, notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	thread.start_new_thread(_save, (file_name, notes, delay_period, fade))

