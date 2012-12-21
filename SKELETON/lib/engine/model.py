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

   def __init__(self,system_event_manager):
      SystemEventListener.__init__(self,system_event_manager)
      self.system_event_manager = system_event_manager
   
   #--------------------------------------------------------------------------
   
   def change_state(self,new_state):
      self.state = new_state
      self.state.register_model(self)
      
   #--------------------------------------------------------------------------
      
   def notify(self,event):
      if self.state is not None:
         self.state.notify(event)
         
         if isinstance(event,TickEvent):
            self.system_event_manager.post(
                                 ModelUpdated(self.state.get_game_objects()))   