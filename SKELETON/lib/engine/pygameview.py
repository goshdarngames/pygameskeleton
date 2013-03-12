##############################################################################
# pygameview.py
##############################################################################
# View used to display the game in a pygame window.
##############################################################################
# 06/12 - Flembobs
##############################################################################

import os
import pygame
from systemevents import *

class PygameView(SystemEventListener):
   
   def __init__(self,caption,size,bg_color):
   
      SystemEventListener.__init__(self)
      
      os.environ["SDL_VIDEO_CENTERED"] = "1"
      pygame.display.set_caption(caption)
      self.screen = pygame.display.set_mode(size)
      
      self.bg_color = bg_color
      
   #--------------------------------------------------------------------------
      
   def notify(self, event):
      
      if isinstance(event,ModelUpdated):
         
         self.screen.fill(self.bg_color)
      
         for game_object in event.game_objects:
            game_object.render(self.screen)
            
         pygame.display.flip()