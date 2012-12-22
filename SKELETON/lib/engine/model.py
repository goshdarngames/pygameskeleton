##############################################################################
# model.py
##############################################################################
# State-based model that interpets input and generates events to alert views
# to changes.
##############################################################################
# 06/12 - Flembobs
##############################################################################

import pygame
from systemevents import *

class Model(SystemEventListener):

   def __init__(self,system_event_manager,screen_size):
      SystemEventListener.__init__(self,system_event_manager)
      self.system_event_manager = system_event_manager
      
      self.screen_size = screen_size
   
   #--------------------------------------------------------------------------
   
   def change_state(self,new_state):
      self.state = new_state
      
   #--------------------------------------------------------------------------
      
   def notify(self,event):
      if self.state is not None:
         self.state.notify(event)
         
         if isinstance(event,TickEvent):
            self.system_event_manager.post(
                                 ModelUpdated(self.state.get_game_objects()))   