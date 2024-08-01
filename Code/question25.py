from manim import *
import numpy as np
import math

class Question25(Scene):
    def construct(self):

        # To change the whole color scheme easier
        first_color = LIGHT_GRAY
        second_color = BLUE

        # Create the question and answer choices as a VGroup
        question = VGroup(
            MathTex(r"\text{If one says that the matrix A has a trivial kernel,}", color = first_color),
            MathTex(r"\text{what does this mean?}",color=first_color),
            MathTex(r"\text{a) Ker(A)=0}", color=first_color),
            MathTex(r"\text{b) Ker(A)=\{0\}}", color=first_color),
            MathTex(r"\text{c) it depends}", color=first_color)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).shift(1.5*UP)
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
