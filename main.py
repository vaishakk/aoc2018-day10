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
	# ToDo
	return positions

def move_one_step(positions, velocities):
	# ToDo
	return positions, velocities

def display_positions(positions):
	pass