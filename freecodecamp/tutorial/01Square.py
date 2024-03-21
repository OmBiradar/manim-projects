# To run type 'manim 01Square.py Scene1 -pqm'
#       'pqm' stands for play quality medium


from manim import *

class Scene1(Scene):
    def construct(self):
        
        # Defining the objects

        sq = Square(
            side_length = 3,
            stroke_color = GREEN,
            fill_color = BLUE,
            fill_opacity = 0.5
        )

        # Play the scene

        self.play(Create(sq), run_time = 3) # Creates the square in 3 seconds
        self.wait() # Waits for by default 1 s