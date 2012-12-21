##############################################################################
# skeleton.py
##############################################################################
# Main game script.  Creates the model, views and conntrollers.
##############################################################################
# 12/12 - Flembobs
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
      
      #create system events manager
      self.system_event_manager = SystemEventManager()
      
      #create controllers
      self.cpu_spinner = CPUSpinner(self.system_event_manager,FPS)
      self.pygame_events_manager = \
                              PygameEventsManager(self.system_event_manager)
      
      #create model
      self.model = Model(self.system_event_manager)
      self.model.change_state(GameState(SCREEN_SIZE))
      
      #create views
      self.pygame_view = PygameView(self.system_event_manager,GAME_NAME, \
                                                   SCREEN_SIZE, BG_COLOR)
      
      
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
