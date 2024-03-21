# To run type 'manim .py Scene1 -pqm'  # Assuming the animation file is named Scene1.py
# 'pqm' stands for play quality medium

from manim import *

class Scene1(Scene):
    def construct(self):

        # Defining the Objects
        name = Tex("Manim")

        # Play the scene
        self.play(Write(name))
