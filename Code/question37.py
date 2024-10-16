from manim import *
import numpy as np
import math

class Question37(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        size_font =  DEFAULT_FONT_SIZE*0.75

        box = Rectangle(
            height=5.5, 
            width=11.5, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)
        self.play(Create(box))

        question = VGroup( MathTex(r"\text{Which is more correct to say among these two options?}", 
                    color=first_color, font_size=size_font),
                    MathTex(r"\text{1. a matrix defines a specific linear transformation}",
                    color=first_color, font_size=size_font),
                    MathTex(r"\text{2. a matrix defines a specific linear transformation from}", 
                    color=first_color, font_size=size_font),
                    MathTex(r"\text{ a specific basis into another}", 
                    color=first_color, font_size=size_font),
                    ).arrange(DOWN, center=False, aligned_edge=LEFT)
        question[1:].shift(0.2*DOWN)
        question[2:].shift(0.2*DOWN)
        question[3].shift(0.4*RIGHT)

        answers = VGroup(
            MathTex(r"\text{A: first one}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{B: second one}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{C: they are equivalent}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{D: I don't know}", 
                    color=second_color, font_size=size_font),
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        VGroup(question, answers).arrange(DOWN, center=False, aligned_edge=LEFT)
        answers.shift(RIGHT+0.1*DOWN)
        VGroup(question, answers).move_to(ORIGIN)

        all_text =VGroup(question, answers)
        box = Rectangle(
            height=all_text.get_height()+1, 
            width=all_text.get_width()+1, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)
        
        #Animation

        self.play(Create(question[0]))
        self.wait(2)
        self.play(Create(question[1]))
        self.wait(3)
        self.play(Create(question[2]))
        self.play(Create(question[3]))
        self.wait(3)
        self.play(Create(answers[0]))
        self.wait(1)
        self.play(Create(answers[1]))
        self.wait(1)
        self.play(Create(answers[2]))
        self.wait(1)
        self.play(Create(answers[3]))
        self.wait(2)

        self.play(FadeOut(question, answers, box))