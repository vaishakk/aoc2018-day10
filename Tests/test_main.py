import pytest
import main

def test_scrape_input():
	positions, velocities = main.scrape_input()
	assert positions[0][0] == 9

def test_offset_positions_to_zero():
	positions = main.offset_positions_to_zero([(-2, 3), (-1, -1)])
	assert positions[0][0] == 0

def test_move_one_step():
	positions = main.move_one_step([(-2, 3), (-1, -1)], [(1, 1), (3, 2)])
	assert positions[1][0] == 2

