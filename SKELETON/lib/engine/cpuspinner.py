##############################################################################
# cpuspinner.py
##############################################################################
# Class used to keep the game looping.  Generates a tick event each time
# the game loops.
##############################################################################
# 06/12 - Gary Fleming
##############################################################################

from systemevents import *
import pygame
   
class CPUSpinner(SystemEventListener):

   def __init__(self,system_event_manager,fps):
   
      SystemEventListener.__init__(self,system_event_manager)
   
      #reference to the events manager
      self.system_event_manager = system_event_manager
      
      #desired FPS
      self.fps = fps
      
      #boolean to indicate whether we should keep running
      self.running = True
      
      #clock used to maintain FPS
      self.clock = pygame.time.Clock()
      
   #--------------------------------------------------------------------------
      
   def run(self):
      while(self.running):
         self.clock.tick(self.fps)
         event = TickEvent()
         self.system_event_manager.post(event)
         
   #--------------------------------------------------------------------------
   
   def notify(self,event):
      if isinstance(event,QuitEvent):
         self.running = False
      
            
      
