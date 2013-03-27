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

   def __init__(self,screen_size):
      SystemEventListener.__init__(self)      
      self.screen_size = screen_size
   
   #--------------------------------------------------------------------------
   
   def change_state(self,new_state):
      self.state = new_state
      
   #--------------------------------------------------------------------------
      
   def notify(self,event): 
      pass
                                 
                                 
##############################################################################
# GAME OBJECT
##############################################################################

class GameObject:
   
   def render(self, screen):
      raise NotImplementedError
      
##############################################################################
# STATE
##############################################################################

class State:
   
   def __init__(self,model):
      """
      Creates a state with a null reference to the model and an empty list
      of game objects.
      """
      self.model = model
      self.game_objects = []
      
   def process_tick(self):
      """
      Called by the model when it receives a TICK event.  Note - the state
      handles ticks like this so that the model may generate a Model Updated
      Event when the state has been updated.
      
      Tick Events should not be handled via the Listener interface.
      """
      pass