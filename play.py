import subprocess
import decimal

#Usage
# play(notes  - The notes containing notes (string)
# 	delay_step [OPTIONAL] - Delay between notes playback
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)

# save(file_name - The file to save to. Do not include an extension
# 	notes  - The notes containing notes_array
# 	delay_step [OPTIONAL] - Delay between notes_array playback
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)

# save(file_name - The file to save to. Do not include an extension
# 	notes  - Array of a 2 element arrays (eg: [["A3 G2", 0.00], ["C3 D1", 0.07]])
# 		The strum plays at the specified time.
# 	delay_step [OPTIONAL] - Delay between notes_array playback
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)

def _gen_string(notes, delay_step = 0.05, fade = [0, 4, 0.1]):
	# subprocess.call("play -n synth pl G2 pl B2 pl D3 pl G3 pl D4 pl G4 delay 0 .05 .1 .15 .2 .25 remix - fade 0 4 .1 norm -1", shell = True)
	notes_array = notes.split(" ")
	final = ""
	for i in notes_array:
		final += "pl " + i + " "
	if not delay_step == 0:
		two_places = decimal.Decimal ('10') ** -2
		j = 0
		final += "delay "
		while j < len(notes_array):			
			final += str(decimal.Decimal(delay_step * j).quantize(two_places)) + " "
			j += 1	

	j = 0
	if not fade == [0, 0, 0]:
		final += "remix - fade "
		while j < len(fade):
			final += str(fade[j]) + " "
			j += 1
		final += "norm -1"

	return final
	# subprocess.call(final, shell = True)

def _gen_times(base, size, delay_step = 0.05):
	times = ""
	j = 0
	k = 0
	two_places = decimal.Decimal ('10') ** -2
	while j < size:
		times += str(decimal.Decimal(base + delay_step * j).quantize(two_places)) + " "
		j += 1

	k = delay_step * (j-1) + base
	return k, times


def play(notes, delay_step = 0.05, fade = [0, 4, 0.1]):
	subprocess.call("play -n synth " + _gen_string(notes, delay_step, fade), shell = True)

def save(file_name, notes, delay_step = 0.05, fade = [0, 4, 0.1]):
	subprocess.call("sox -n synth " + file_name + ".wav " + _gen_string(notes, delay_step, fade), shell = True)

def save(file_name, notes, delay_step = 0.05, fade = [0, 4, 0.1]):
	final = "sox -n " + file_name + ".wav synth "
	# final = "play -n synth "
	note_s = ""
	for row in notes:
		final += _gen_string(row[0], 0, [0, 0, 0])
	
	j = 0
	if not fade == [0, 0, 0]:
		final += "delay "
		
		base = 0
		times = " "
		for row in notes:
			base, times = _gen_times(base + row[1], len(row[0].split(" ")), delay_step)
			final += times

	j = 0
	if not fade == [0, 0, 0]:
		final += "remix - fade "
		while j < len(fade):
			final += str(fade[j]) + " "
			j += 1

		final += "norm -1"
	subprocess.call(final, shell = True)




