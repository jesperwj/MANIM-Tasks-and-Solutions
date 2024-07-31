from manim import *
import numpy as np
import math

class Question17(Scene):
    def construct(self):

        # To change the whole color scheme easier
        first_color = LIGHT_GRAY
        second_color = BLUE

        # Create the question and answer choices as a VGroup
        question = VGroup(
            MathTex(r"\text{What are the equilibria of the system: }", color = first_color),
            MathTex(r"\dot{x}=f(x)=x^2-2x-3",color=second_color),
            MathTex(r"\text{a) -1}", color=first_color),
            MathTex(r"\text{b) 3}", color=first_color),
            MathTex(r"\text{c) both -1 and 3}", color=first_color)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).shift(1.5*UP)

        VGroup(question[1:]).shift(RIGHT)
        VGroup(question[2:]).shift(RIGHT)

        # Animating the question
        self.play(Write(question[0]))
        self.wait(0.5)
        self.play(Write(question[1]))
        self.wait(0.5)
        self.play(Write(question[2]))
        self.wait(0.5)
        self.play(Write(question[3]))
        self.wait(0.5)
        self.play(Write(question[4]))
        self.wait(5)
