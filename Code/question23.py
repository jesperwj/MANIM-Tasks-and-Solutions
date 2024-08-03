from manim import *
import numpy as np
import math

class Question23(Scene):
    def construct(self):

        task_text = VGroup(
            MathTex(r"\text{Is the origin (\textbf{u}, \textbf{y}) always an equilibrium}",color=LIGHT_GRAY),
            MathTex(r"\text{for an LTI system of following type? }",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(1.5*UP).scale(0.90)
        
        equation_text = VGroup(
            MathTex(r"\dot{y} = Ay + Bu", substrings_to_isolate = "y, u")
        ).arrange(DOWN).move_to(0*DOWN).scale(0.90)
        
        equation_text[0].set_color_by_tex("y", ORANGE)
        equation_text[0].set_color_by_tex("u", BLUE)
        
        options_text = VGroup(
            MathTex(r"\text{A: True}"),
            MathTex(r"\text{B: False}"),
            MathTex(r"\text{C: It depends}")
        ).arrange(DOWN).move_to(1.5*DOWN + 0.5*LEFT).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        self.play(Write(task_text))
        self.wait(1)
        
        self.play(Write(equation_text))
        self.wait(1)
        
        self.play(Write(options_text))
        self.wait(2)