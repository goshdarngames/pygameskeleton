##############################################################################
# gameobject.py
##############################################################################
# Interface for game objects which are tracked by the model and can be 
# drawn to screen.
##############################################################################
# 12/12 Flembobs
##############################################################################

class GameObject:
   
   def render(self, surface):
      raise NotImplementedError