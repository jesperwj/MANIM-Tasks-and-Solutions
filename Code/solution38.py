from manim import *
import numpy as np
import math

'''
Comments
take a generic A n*n 
has n eigs from 1 to n
focus on generic lambda i 
then boxes

end
we need to make clear that two different eigs can be associated to same space
to eg vectors have to be linearly independant

animation that stresses this

cant same eigen vector in the beginning

whenever we have one vector it cannot be 
eig vector for two eig values
cannot be stretched in two different ways
we can stress this in the beginning

eigenvectros of different eigs are lin independant 
then the solution
'''

class Solution38(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        fourth_color = ORANGE
        size_font =  DEFAULT_FONT_SIZE*0.75
        
        question = VGroup( MathTex(r"\text{If a } n \times n \text{ square matrix has } n \text{ different eigenvalues}", 
                    color=first_color, font_size=size_font),
                    MathTex(r"\text{then it is diagonizable.}",
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
        self.play(Indicate(answers[0], color = first_color))
        self.wait(0.5)
        self.play(Indicate(answers[0], color = first_color))
        self.wait(1)
        self.play(FadeOut(question, answers, box))
        self.wait(1)

        
                
        # Solution part -----------------------------------------------------------------
        size_font = DEFAULT_FONT_SIZE*0.8
    
        geometric = VGroup(
            MathTex(r"\text{geometric multiplicity}", 
                    color=fourth_color, font_size=size_font),
            MathTex(r"\text{of eigenvalue } \lambda_i", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN)

        algebraic = VGroup(
            MathTex(r"\text{algebraic multiplicity}", 
                    color=third_color, font_size=size_font),
            MathTex(r"\text{of eigenvalue } \lambda_i", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN)

        inequality = VGroup(
            MathTex(r"1 \le", color=first_color, font_size=size_font),
            geometric,
            MathTex(r"\le", color=first_color, font_size=size_font),
            algebraic,
            MathTex(r"= 1", color=first_color, font_size=size_font)
        ).arrange(RIGHT,buff=0.8)
        inequality[2].shift(0.07*RIGHT)

        inequality2 = VGroup(
            MathTex(r"1 =", color=first_color, font_size=size_font),
            geometric,
            MathTex(r"=", color=first_color, font_size=size_font*1.1),
            algebraic,
            MathTex(r"= 1", color=first_color, font_size=size_font)
        ).arrange(RIGHT,buff=0.8)
        inequality2[2].shift(0.07*RIGHT)

        solution = VGroup(
            MathTex(r"\text{In the case when a matrix has all different eigenvalues (from }\lambda_1 \text{ to }\lambda_n\text{),}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{each of the algebraic multiplicities is 1.}", 
                    color=second_color, font_size=size_font),
            inequality,
            MathTex(r"\forall i \in \{1, \ldots, n\}" ,
                    color=GRAY_C, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff = 0.5).to_edge(UP).shift(0.2*DOWN)
        
        inequality.move_to(ORIGIN)
        solution[3].shift(1.2*UP)
        inequality2.move_to(ORIGIN)
        solution[4:].shift(2*DOWN)

        # Additional explanation
        additional_text_geometric = VGroup(
            geometric,
            MathTex(r"\bullet \text{ number of independant}", 
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\text{eigenvectors corresponding }", 
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\text{to eigenvalue }\lambda_i" ,
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\bullet \text{ dimension of the eigenspace}", 
                    color=second_color, font_size=size_font*0.9)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        additional_text_geometric[1].shift(0.35*LEFT)
        additional_text_geometric[-1].shift(0.35*LEFT)
        additional_text_geometric[1:].shift(0.5*DOWN)
        box_geometric = Rectangle(
            height=additional_text_geometric.get_height()+0.45, 
            width=additional_text_geometric.get_width()+0.45, 
            fill_color=fourth_color, 
            fill_opacity=0.1, 
            stroke_color=fourth_color).move_to(additional_text_geometric)
        
        additional_text_algebraic = VGroup(
            algebraic,
            MathTex(r"\bullet \text{ number of times }\lambda_i", 
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\text{appears as a root of the}", 
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\text{characteristic polynomial }" ,
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\text{ of the matrix}", 
                    color=second_color, font_size=size_font*0.9)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        additional_text_algebraic[1].shift(0.3*LEFT)
        additional_text_algebraic[1:].shift(0.5*DOWN)
        

        box_algebraic = Rectangle(
            height=additional_text_algebraic.get_height()+0.45, 
            width=additional_text_algebraic.get_width()+0.45, 
            fill_color=third_color, 
            fill_opacity=0.1, 
            stroke_color=third_color).move_to(additional_text_algebraic)

        solution2 = VGroup(
            MathTex(r"\text{In total, there are } n \text{ independant eigenvectors.}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{A basis formed by these eigenvectors will diagonalize the matrix.}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN,buff = 0.5).to_edge(UP).shift(0.2*DOWN)
        
        # Animation
        self.play(Create(solution[3]))
        self.wait(1)
        self.play(Create(inequality[0]))
        self.wait(0.5)
        self.play(Create(inequality[1][0]))
        self.wait(0.5)
        self.play(Create(inequality[1][1]))
        self.wait(1)
        self.play(Create(inequality[2]))
        self.wait(0.5)
        self.play(Create(inequality[3][0]))
        self.wait(0.5)
        self.play(Create(inequality[3][1]))
        self.wait(3)

        # Additional explenation on geometric multiplicity
        self.play(Create(box_geometric))
        self.wait(0.8)
        self.play(Create(additional_text_geometric[1]))
        self.wait(0.8)
        self.play(Create(additional_text_geometric[2]))
        self.wait(0.8)
        self.play(Create(additional_text_geometric[3]))
        self.wait(0.8)
        self.play(Create(additional_text_geometric[4]))
        self.wait(1)

        # Additional explenation on algebraic multiplicity
        self.play(Create(box_algebraic))
        self.wait(0.8)
        self.play(Create(additional_text_algebraic[1]))
        self.wait(0.8)
        self.play(Create(additional_text_algebraic[2]))
        self.wait(0.8)
        self.play(Create(additional_text_algebraic[3]))
        self.wait(0.8)
        self.play(Create(additional_text_algebraic[4]))
        self.wait(3)

        # Animating text
        self.play(Create(solution[0]))
        self.wait(2)
        self.play(Create(solution[1]))
        self.wait(2)
        self.play(GrowFromCenter(inequality[4]))

        self.wait(2)
        self.play(FadeOut(VGroup(inequality[3], box_algebraic,additional_text_algebraic)))
        self.play(FadeOut(inequality[4][0][-2]))
        self.play(inequality[4][0][-1].animate.shift(2.7*LEFT),
                  VGroup(inequality[0:3],box_geometric,additional_text_geometric[1:]).animate.shift(2.7*RIGHT))
        self.wait(1)
        self.play(FadeOut(inequality[0]))
        inequality[4][0][-2].shift(2.7*LEFT)
        self.play( Transform(inequality[2],inequality[4][0][-2]))
        self.wait(2)
        self.play(Uncreate(solution[0:2]))
        self.wait(1.5)
        self.play(Create(solution2[0]))
        self.wait(2)
        self.play(Create(solution2[1]))
        self.wait(6)
        self.play(FadeOut(solution2, inequality[1],inequality[4],inequality[2],
                          additional_text_geometric,
                          box_geometric,
                          solution[3]))

