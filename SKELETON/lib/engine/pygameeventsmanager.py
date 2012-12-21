##############################################################################
# pygameeventsmanager.py
##############################################################################
# Checks pygame for events on each tick and posts corresponding system
# events.
##############################################################################
# 06/12 - Flembobs
##############################################################################

from systemevents import *
import pygame

class PygameEventsManager(SystemEventListener):

   def __init__(self,system_event_manager):
   
      SystemEventListener.__init__(self,system_event_manager)
   
      #save reference to events manager for posting system events
      self.system_event_manager = system_event_manager
      
   #--------------------------------------------------------------------------
      
   def notify(self,event):
   
      if isinstance(event,TickEvent):
      
         #get most recent pygame events
         pygame_events = pygame.event.get()         
         
         #convert pygame events into system events
         for pygame_event in pygame_events:
         
            event_to_post = None
         
            #pygame quit (window closing)
            if pygame_event.type == pygame.QUIT:
               event_to_post = QuitEvent()
               
            #keyboard event
            if pygame_event.type == pygame.KEYDOWN or \
               pygame_event.type == pygame.KEYUP:
               
               event_to_post = KeyboardEvent(pygame_event.type,
                                             pygame_event.key)
               
            #mouse button event
            if pygame_event.type == pygame.MOUSEBUTTONUP or \
               pygame_event.type == pygame.MOUSEBUTTONDOWN:
               
               event_to_post = MouseButtonEvent(pygame_event.type,
                                                pygame_event.button,
                                                pygame_event.pos)
                                                
            #mouse motion event
            if pygame_event.type == pygame.MOUSEMOTION:
               event_to_post = MouseMotionEvent(pygame_event.pos,
                                                pygame_event.rel,
                                                pygame_event.buttons)
            
            #post the event that has been generated
            self.system_event_manager.post(event_to_post)
               