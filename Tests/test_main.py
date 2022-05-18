import pytest
import main

def test_scrape_input():
	positions, velocities = main.scrape_input()
	assert positions[0][0] == 9

def test_offset_positions_to_zero():
	pass

def test_move_one_step():
	pass

