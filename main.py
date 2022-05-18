from operator import itemgetter

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

def display_positions(positions):
	max_x = max(positions, key=itemgetter(0))[0]
	max_y = max(positions, key=itemgetter(1))[1]
	for y in range(0, max_y+1):
		cols = filter(lambda p: p[1] == y, positions)
		msg_row = ['.']*(max_x+1)
		for c in cols:
			msg_row[c[0]] = '#'
		print(''.join([str(m) for m in msg_row]))