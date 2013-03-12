##############################################################################
# cpuspinner.py
##############################################################################
# Class used to keep the game looping.  Generates a tick event each time
# the game loops.
##############################################################################
# 06/12 - Flembobs
##############################################################################

from systemevents import *
import pygame
   
class CPUSpinner(SystemEventListener):

   def __init__(self,fps):
   
      SystemEventListener.__init__(self)
      
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
         SystemEventManager.post(event)
         
   #--------------------------------------------------------------------------
   
   def notify(self,event):
      if isinstance(event,QuitEvent):
         self.running = False