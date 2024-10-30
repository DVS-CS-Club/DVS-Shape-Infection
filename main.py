
# Importing libraries
import pygame as pyg
import player, level

# Setting up the window
pyg.init()
screenw, screenh = 720, 480
running = True
screen = pyg.display.set_mode((screenw,screenh))
pyg.display.set_caption("DVS Shape Infection")
pyg.display.set_icon(pyg.image.load("img/logo.png").convert())
fps = 60

main_player = player.Player(screenw//2-10, screenh//2-10)
main_level = level.Level([pyg.Rect(0,0,screenw,10), pyg.Rect(0,0,10,screenh), pyg.Rect(screenw-10,0,10,screenh), pyg.Rect(0,screenh-10,screenw,10)], pyg.Vector2(screenw//2-10, screenh//2-10))

# Main loop
while running:
    pyg.time.Clock().tick(fps) # Starting the clock
    # Event detection
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
    
    screen.fill("black") # Filling the screen (Because Life, Is Roblox -DJ Khalid)
    
    main_level.update(screen, -main_player.vel_x*2, -main_player.vel_y*2) # Updating the level
    
    main_player.update(screen) # Updating the player
    
    pyg.display.update() # Updating the screen