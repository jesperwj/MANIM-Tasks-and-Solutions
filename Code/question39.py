from manim import *
import numpy as np
import math

class Question39(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        size_font =  DEFAULT_FONT_SIZE*0.75
        
        question = VGroup( MathTex(r"\text{A } n \times n \text{ square matrix needs to have } n \text{ different eigenvalues}", 
                    color=first_color, font_size=size_font),
                    MathTex(r"\text{to be diagonizable.}",
                    color=first_color, font_size=size_font)
                    ).arrange(DOWN, center=False, aligned_edge=LEFT)
        answers = VGroup(
            MathTex(r"\text{A: true}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{B: false}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{C: it depends}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{D: I don't know}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        all_text =VGroup(question, answers)
        all_text.arrange(DOWN, center=False, aligned_edge=LEFT)
        answers.shift(RIGHT+0.1*DOWN)
        all_text.move_to(ORIGIN)

        box = Rectangle(
            height=all_text.get_height()+1, 
            width=all_text.get_width()+1, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)
        
        #Animation
        self.play(Create(box))
        self.play(Create(question[0]))
        self.wait(2)
        self.play(Create(question[1]))
        self.wait(3)
        self.play(Create(answers[0]))
        self.wait(1)
        self.play(Create(answers[1]))
        self.wait(1)
        self.play(Create(answers[2]))
        self.wait(1)
        self.play(Create(answers[3]))
        self.wait(3)
        self.play(FadeOut(question, answers, box))