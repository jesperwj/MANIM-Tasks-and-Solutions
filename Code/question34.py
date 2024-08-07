from manim import *
import numpy as np
import math

class Question34(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        size_font =  DEFAULT_FONT_SIZE*0.75

        box = Rectangle(
            height=3.6, 
            width=11, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)
        self.play(Create(box))

        question = VGroup(
            MathTex(r"\text{Can a LTI system whose transfer function has some poles}", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{on the imaginary axis, be BIBO stable?}", 
                    color=first_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)

        answers = VGroup(
            MathTex(r"\text{A: yes}", 
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\text{B: no}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{C: it depends}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        VGroup(question[1], answers).arrange(DOWN, center=False, aligned_edge=LEFT)
        answers.shift(RIGHT)
        VGroup(question, answers).move_to(ORIGIN)

        #Animation

        self.play(Create(question[0]))
        self.wait(0.5)
        self.play(Create(question[1]))
        self.wait(3)

        self.play(Create(answers[0]))
        self.wait(0.5)
        self.play(Create(answers[1]))
        self.wait(0.5)
        self.play(Create(answers[2]))
        self.wait(2)

        self.play(FadeOut(question, answers, box))