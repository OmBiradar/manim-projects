from manim import *

class Test(Scene):
    def construct(self):
        
        # defining the object
        sq = Square(
            side_length = 3, 
            stroke_color = GREEN, 
            fill_color = BLUE, 
            fill_opacity=0.5
        )

        # Play the scene

        self.play(Create(sq), run_time = 3)
        self.wait() # Default wait time of 1s