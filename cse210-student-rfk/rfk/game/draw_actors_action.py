from game.action import Action
class DrawActorsAction(Action):

#draws the actor action by getting other methods as parameters


    def __init__(self, output_service ):
        self.output_service = output_service
        

    def execute(self, cast):
        """
        Be sure to clear the screen, draw the actors and then flush the buffer
        """
        self.output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self.output_service.flush_buffer
        
