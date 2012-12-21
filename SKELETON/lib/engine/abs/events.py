##############################################################################
# events.py
##############################################################################
# Contains superclasses for the event-driven mediator system.
##############################################################################
# 06/12 - Gary Fleming
##############################################################################

from weakref import WeakKeyDictionary

##############################################################################
# EVENT SUPERCLASS
##############################################################################

class Event:
   """
   Superclass for all events.
   """
   pass
   
##############################################################################
# LISTENER SUPERCLASS
##############################################################################
   
class Listener:
   """
   Interface for listeners.                                                   
   """
   
   def __init__(self,event_manager):
      event_manager.register_listener(self)
   
   def notify(self,event):
      raise NotImplementedError
      
##############################################################################
# EVENT MANAGER SUPERCLASS
##############################################################################
   
class EventManager:
   """
   Superclass for all event managers.  Keeps a list of listeners and 
   dispatches events to them.
   """
   
   def __init__(self):
      self.listeners = WeakKeyDictionary()
      
   #--------------------------------------------------------------------------
   
   def register_listener(self,listener):
      self.listeners[listener] = 1
      
   #--------------------------------------------------------------------------
   
   def unregister_listener(self,listener):
      if listener in self.listeners.keys():
         del self.listeners[listener]
         
   #--------------------------------------------------------------------------
   
   def post(self,event):
      for listener in self.listeners.keys():
         listener.notify(event)
   
   