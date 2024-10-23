
# Importing libraries
import pygame as pyg

# Setting up the window
pyg.init()
screenw, screenh = 720, 480
running = True
screen = pyg.display.set_mode((screenw,screenh))
pyg.display.set_caption("DVS Shape Infection")
pyg.display.set_icon(pyg.image.load("img/logo.png").convert())
fps = 60

# Main loop
while running:
	pyg.time.Clock().tick(fps) # Starting the clock
	# Event detection
	for event in pyg.event.get():
		if event.type == pyg.QUIT:
			running = False
	screen.fill("black") # Filling the screen
	
	pyg.display.update() # Updating the screen