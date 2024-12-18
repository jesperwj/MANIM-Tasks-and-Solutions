from manim import *
import numpy as np
import math

class Solution40(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        size_font =  DEFAULT_FONT_SIZE*0.75
        
        question = VGroup( MathTex(r"\text{A } n \times n \text{ square matrix needs to have determinant different from zero}", 
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
        
        
        # Animating the question
        self.play(Create(box))
        self.play(FadeIn(question, answers))
        self.wait(4)

        # Animating the correct answer indication 
        self.play(Indicate(answers[1], color = first_color))
        self.wait(0.5)
        self.play(Indicate(answers[1], color = first_color))
        self.wait(1)
        self.play(FadeOut(question, answers, box))
        self.wait(1)
        
        
        # Solution part -----------------------------------------------------------------
        size_font = DEFAULT_FONT_SIZE*0.85

        solution = VGroup(
            MathTex(r"\text{The simple example of a matrix with determinant equal to zero}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{which is diagonizable (being already diagonal) is the zero matrix.}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff = 0.4).to_edge(UP).shift(0.2*DOWN)
        solution[1][0][-14:].set_color(third_color)

        equation_1 = MathTex(            
            r"\begin{bmatrix}"
            r" 0 & 0 & 0\\"
            r"0 & 0 & 0\\"
            r" 0 & 0 & 0"
            r"\end{bmatrix}",
             color=second_color, font_size=size_font)
        
        equation = VGroup(
            MathTex(r"\mathbf{0}_{3 \times 3}=", 
                    color=second_color, font_size=size_font),
            equation_1
        ).arrange(RIGHT).shift(0.2*UP)
        equation[0][0][0:4].set_color(third_color)

        condition = VGroup(
            MathTex(r"\text{For }n = 3 \text{:}", 
                    color=second_color, font_size=size_font),
            equation
        ).arrange(DOWN)
        condition[0].to_edge(LEFT).shift(0.78*RIGHT)
        equation.shift(0.4*DOWN)

        solution2 = MathTex(r"\text{Therefore, as proven by contradiction, the statement is false.}", 
                    color=second_color, font_size=size_font).to_edge(DOWN).shift(0.3*UP)
        
        # Animation
        self.play(Create(solution[0]))
        self.wait(1.5)
        self.play(Create(solution[1]))
        self.wait(3)

        self.play(Create(condition[0]))
        self.wait(1)
        self.play(Create(equation[0]))
        self.play(FadeIn(equation[1]))
        self.wait(3)
        self.play(Create(solution2))
        self.wait(3)
        self.play(FadeOut(solution, condition, solution2))
