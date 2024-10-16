from manim import *
import numpy as np
import math
'''
basis we are using not are we using

animation that we have to do 

domain and codomain 
mona lisa thing
image domain and in the codomain that is warping

define:


add i do not know to answers
'''
class Solution37(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = ORANGE
        size_font =  DEFAULT_FONT_SIZE*0.75

        box = Rectangle(
            height=5.8, 
            width=11, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)

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
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        VGroup(question, answers).arrange(DOWN, center=False, aligned_edge=LEFT)
        answers.shift(RIGHT+0.4*DOWN)
        VGroup(question, answers).move_to(ORIGIN)

        
        # Animating the question
        self.play(Create(box))
        self.play(FadeIn(question, answers))
        self.wait(4)

        # Animating the correct answer indication 
        self.play(Indicate(answers[1], color = first_color))
        self.wait(0.5)
        self.play(Indicate(answers[1], color = first_color))
        self.wait(2)
        self.play(FadeOut(question, answers, box))
        self.wait(1)
        

        # Solution part -----------------------------------------------------------------
        size_font = DEFAULT_FONT_SIZE*0.85

        solution = VGroup(
            MathTex(r"\text{A linear transformation can be expressed by a specific matrix A}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{if we choose which basis we are using for describing the domain}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{and the codomain.}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff = 0.4).to_corner(UL).shift(0.2*DOWN)

        solution[0][0][-14:].set_color(third_color)

        equation_1 = MathTex(            
            r"\begin{bmatrix}"
            r" a_{11} & ... & a_{1n} \\"
            r"... & ... & ...\\"
            r" a_{n1} & ... & a_{nn}"
            r"\end{bmatrix}",
             color=second_color, font_size=size_font)
        
        equation = VGroup(
            MathTex(r"\text{A = }", 
                    color=second_color, font_size=size_font),
            equation_1
        ).arrange(RIGHT).shift(0.2*UP)
        equation[0][0][0].set_color(third_color)

        # Marking the columns
        def mark_column(matrix, number,total_number, color):
            column_box = Rectangle(
                width=matrix.get_width() / total_number-0.2,  # Adjust according to the number of columns
                height=matrix.get_height(),
                color=color,
                stroke_width=3).move_to(matrix.get_center())
            column_box.shift(LEFT * (number*matrix.get_width() / total_number))
            return column_box
        
        column1 =mark_column(equation_1,1,3,RED)
        column3 =mark_column(equation_1,-1,3,BLUE)

        solution2 = VGroup(
            MathTex(r"\text{Each of the columns of the matrix shows how the corresponding}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{element of the basis in the domain maps to something in the}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{codomain (written in terms of a specific basis in the codomain).}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff = 0.4).to_corner(DL).shift(0.2*UP)
        VGroup(solution, solution2).shift(0.5*RIGHT)

        # Animation
        
        self.play(Create(solution[0]))
        self.wait(1.5)
        self.play(Create(solution[1]))
        self.wait(1.5)
        self.play(Create(solution[2]))
        self.wait(3)

        self.play(Create(equation[0]))
        self.wait(1)
        self.play(FadeIn(equation[1]))
        self.wait(3)

        self.play(Create(solution2[0]),
                  Create(column1),
                  Create(column3))
        self.wait(2)
        self.play(Create(solution2[1]))
        self.wait(1.5)
        self.play(Create(solution2[2]))
        self.wait(3)

        self.play(FadeOut(solution, solution2, column1, column3, equation))