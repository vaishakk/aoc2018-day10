from operator import itemgetter
from PIL import Image
import numpy as np

INITIAL_POS = 10630
NUM_MOVES = 20

def scrape_input(input_file='sample-input'):
	positions = []
	velocities = []
	with open(input_file, 'r') as file:
		input = file.read()
	lines  = input.split('\n')
	for line in lines:
		position = line.split('>')[0].split('<')[1].split(',')
		for i, p in enumerate(position):
			position[i] = int(p)
		positions.append(position)
		velocity = line.split('>')[1].split('<')[1].split(',')
		for i, v in enumerate(velocity):
			velocity[i] = int(v)
		velocities.append(velocity)
	return positions, velocities

def offset_positions_to_zero(positions):
	min_x = min(positions, key=itemgetter(0))[0]
	min_y = min(positions, key=itemgetter(1))[1]

	for i, position in enumerate(positions):
		positions[i] = position[0] + -min_x, position[1] + -min_y
	return positions

def move_one_step(positions, velocities):
	for i, position in enumerate(positions):
		positions[i] = position[0] + velocities[i][0], position[1] + velocities[i][1]
	return positions

def move_many_steps(positions, velocities, steps):
	for i, position in enumerate(positions):
		positions[i] = position[0] + steps*velocities[i][0], position[1] + steps*velocities[i][1]
	return positions

def write_image(positions, max_x, max_y, step):
	image = np.zeros([max_x+1, max_y+1])
	for i, p in enumerate(positions):
		image[positions[i][0], positions[i][1]] = 255
	array = np.array(image.transpose(), dtype=np.uint8)
	new_image = Image.fromarray(array)
	new_image.save('pos_{}.png'.format(step))


def display_positions(positions, max_x, max_y):
	step_y = int(max_y/100)
	step_x = int(max_x/100)
	sampled_positions = positions.copy()
	for i, position in enumerate(positions):
		sampled_positions[i] = int(position[0]/step_x), int(position[1]/step_y)
	for y in range(0, 100):
		cols = filter(lambda p: p[1] == y, sampled_positions)
		msg_row = ['.']*100
		for c in cols:
			if c[0] == 100:
				msg_row[99] = '#'
			else:
				msg_row[c[0]] = '#'
		print(''.join([str(m) for m in msg_row]))

positions, velocities = scrape_input('input')
max_x = max(positions, key=itemgetter(0))[0]
max_y = max(positions, key=itemgetter(1))[1]
positions = move_many_steps(positions, velocities, INITIAL_POS)
for i in range(0, NUM_MOVES):
	positions = offset_positions_to_zero(positions)
	max_x = max(positions, key=itemgetter(0))[0]
	max_y = max(positions, key=itemgetter(1))[1]
	write_image(positions, max_x, max_y, i + INITIAL_POS)
	positions = move_one_step(positions, velocities)
