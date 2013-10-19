import subprocess
import decimal

#Usage
# play(notes  - The notes containing notes_array
# 	delay_step [OPTIONAL] - Delay between notes_array playback
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)

# save(file_name - The file to save to. Do not include an extension
# 	notes  - The notes containing notes_array
# 	delay_step [OPTIONAL] - Delay between notes_array playback
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)

def _gen_string(notes, delay_step = 0.05, fade = [0, 4, 0.1]):
	# subprocess.call("play -n synth pl G2 pl B2 pl D3 pl G3 pl D4 pl G4 delay 0 .05 .1 .15 .2 .25 remix - fade 0 4 .1 norm -1", shell = True)
	notes_array = notes.split(" ")
	final = "synth "
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
	final += "remix - fade "
	while j < len(fade):
		final += str(fade[j]) + " "
		j += 1

	final += "norm -1"

	return final
	# subprocess.call(final, shell = True)

def play(notes, delay_step = 0.05, fade = [0, 4, 0.1]):
	subprocess.call("play -n " + _gen_string(notes, delay_step, fade), shell = True)

def save(file_name, notes, delay_step = 0.05, fade = [0, 4, 0.1]):
	subprocess.call("sox -n " + file_name + ".wav " + _gen_string(notes, delay_step, fade), shell = True)




