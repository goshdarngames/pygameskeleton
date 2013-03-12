##############################################################################
# events.py
##############################################################################
# Contains superclasses for the event-driven mediator system.
#
# There is an interface for events and listeners.
#
# The EventManager class provides static methods for notifying listeners.
##############################################################################
# 03/13 - Flembobs
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
   
   #keys of this map are objects listening for events
   listeners = WeakKeyDictionary()
      
   #--------------------------------------------------------------------------
   
   @classmethod
   def register_listener(cls,listener):
      cls.listeners[listener] = 1
      
   #--------------------------------------------------------------------------
  
   @classmethod 
   def unregister_listener(cls,listener):
      if listener in cls.listeners.keys():
         del cls.listeners[listener]
         
   #--------------------------------------------------------------------------
   
   @classmethod
   def post(cls,event):
      for listener in cls.listeners.keys():
         listener.notify(event)