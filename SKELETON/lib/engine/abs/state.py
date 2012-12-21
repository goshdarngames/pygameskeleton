##############################################################################
# state.py
##############################################################################
# A state that the model can be in.  E.g. game state, menu state.
##############################################################################
# 12/12 Flembobs
##############################################################################

class State:
   
   def __init__(self):
      """
      Creates a state with a null reference to the model and an empty list
      of game objects.
      """
      self.model = None
      self.game_objects = []
   
   def register_model(self,model):
      """
      Registers the model with the state.
      """
      self.model = model
      
   def get_game_objects(self):
      """
      Returns a list of all game objects tracked by the state.  Note that it
      is the responsibility of the state to keep these objects ordered
      according to how they should be drawn by the default pygame view.
      """
      return self.game_objects