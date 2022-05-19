import os
from operator import itemgetter
from PIL import Image
import numpy as np

with open('input', 'r') as file:
	ip = file.read()
lines  = ip.split('\n')
positions = []
velocities = []
for line in lines:
	position = line.split('>')[0].split('<')[1].split(',')
	for i, p in enumerate(position):
		position[i] = int(p)
	positions.append(position)
	velocity = line.split('>')[1].split('<')[1].split(',')
	for i, v in enumerate(velocity):
		velocity[i] = int(v)
	velocities.append(velocity)

min_x = min(positions, key=itemgetter(0))[0]
min_y = min(positions, key=itemgetter(1))[1]

for i, position in enumerate(positions):
	positions[i] = position[0] + -min_x, position[1] + -min_y
n = 0
for i, position in enumerate(positions):
		positions[i] = position[0] + 10630*velocities[i][0], position[1] + 10630*velocities[i][1]
while(True):
	min_x = min(positions, key=itemgetter(0))[0]
	min_y = min(positions, key=itemgetter(1))[1]

	for i, position in enumerate(positions):
		positions[i] = position[0] + -min_x, position[1] + -min_y
	max_x = max(positions, key=itemgetter(0))[0]
	max_y = max(positions, key=itemgetter(1))[1]
	print(max_x, max_y)
	#step_x = int(max_x/8000) + 1
	#step_y = int(max_y/8000) + 1
	sampled_positions = positions.copy()
	image = np.zeros([max_x+1, max_y+1])
	for i, p in enumerate(positions):
		#sampled_positions[i] = int(p[0]/step_x), int(p[1]/step_y)
		image[sampled_positions[i][0], sampled_positions[i][1]] = 255
	
	array = np.array(image.transpose(), dtype=np.uint8)
	new_image = Image.fromarray(array)
	new_image.save('new_{}.png'.format(n))
	for i, position in enumerate(positions):
		positions[i] = position[0] + velocities[i][0], position[1] + velocities[i][1]
	#res = input("Press any key.")
	n += 1
	if n == 100:
		break
