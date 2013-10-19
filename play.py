import subprocess
import decimal

#Usage
# play(string  - The string containing notes
# 	delay_step [OPTIONAL] - Delay between notes playback
# 	fade [OPTIONAL] - Fade time at end of playback
# 	)
def gen_string(string, delay_step = 0.05, fade = [0, 4, 0.1]):
	# subprocess.call("play -n synth pl G2 pl B2 pl D3 pl G3 pl D4 pl G4 delay 0 .05 .1 .15 .2 .25 remix - fade 0 4 .1 norm -1", shell = True)
	notes = string.split(" ")
	result = "synth "
	for i in notes:
		result += "pl " + i + " "
	if not delay_step == 0:
		two_places = decimal.Decimal ('10') ** -2
		j = 0
		result += "delay "
		while j < len(notes):			
			result += str(decimal.Decimal(delay_step * j).quantize(two_places)) + " "
			j += 1	

	j = 0
	result += "remix - fade "
	while j < len(fade):
		result += str(fade[j]) + " "
		j += 1

	result += "norm -1"

	return result
	# subprocess.call(result, shell = True)

def play(string, delay_step = 0.05, fade = [0, 4, 0.1]):
	subprocess.call("play -n " + gen_string("G2 B2 D3", delay_step, fade), shell = True)

play("G2 B2 D3")



