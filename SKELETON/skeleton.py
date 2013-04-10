##############################################################################
# skeleton.py
##############################################################################
# Main script to launch game.  Creates the model, views and controllers.
##############################################################################
# 03/13 - Flembobs
##############################################################################

import pygame

from lib.engine.systemevents import SystemEventManager

#controllers
from lib.engine.cpuspinner import CPUSpinner
from lib.engine.pygameeventsmanager import PygameEventsManager

#model
from lib.engine.model import Model

#views
from lib.engine.pygameview import PygameView

#initial state
from lib.gamestate import GameState

##############################################################################
# CONSTANTS
##############################################################################

GAME_NAME = "Skeletons, skeletons, skeletons..."
FPS = 60
SCREEN_SIZE = (480,480)
BG_COLOR = (0,0,0)

##############################################################################
# GAME ENGINE CLASS
##############################################################################

class GameEngine:
   
   def __init__(self):
      
      #initialise pygame environment
      pygame.init()
      
      #create controllers
      self.cpu_spinner = CPUSpinner(FPS)
      self.pygame_events_manager = PygameEventsManager()
      
      #init model
      Model.change_state(GameState())
      
      #create views
      self.pygame_view = PygameView(GAME_NAME, SCREEN_SIZE, BG_COLOR)
      
      
   #--------------------------------------------------------------------------
      
   def start(self):
      
      #start the cpu spinner
      self.cpu_spinner.run()
      
   
   
##############################################################################
# MAIN EXECUTION
##############################################################################

gameEngine = GameEngine()
gameEngine.start()
pygame.quit()