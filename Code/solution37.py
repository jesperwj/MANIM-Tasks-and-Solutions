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
        answers.shift(RIGHT+0.4*DOWN)
        VGroup(question, answers).move_to(ORIGIN)
        all_text =VGroup(question, answers)
        
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
        self.wait(2)
        self.play(FadeOut(question, answers, box))
        self.wait(1)
        

        # Solution part -----------------------------------------------------------------
        size_font = DEFAULT_FONT_SIZE*0.85

        # Define a horizontal shear matrix
        shear_amount = 0.5  # Adjust this to control the amount of shear
        picture_transform_matrix = [[1, shear_amount], [0, 1]]

        solution = VGroup(
            MathTex(r"\text{It is important to make the distinction between}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{the general linear transformation } \mathcal{A} \text{ and the}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{specific transformation A from one basis to another.}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff = 0.4).to_corner(UL).shift(0.2*DOWN)

        mona_lisa = ImageMobject("assets\solution37\standard_Mona_Lisa.jpg").scale(0.5).move_to(ORIGIN + 4*LEFT + 2*DOWN)

        mona_lisa_copy = ImageMobject("assets\solution37\\transformed_Mona_Lisa.png").scale(0.5).move_to(ORIGIN + 4*RIGHT + 1.75*DOWN)

        arrow_1 = Arrow(buff=2, start= LEFT + 2*DOWN, end= RIGHT + 2*DOWN)


        pre_transform_coordinate_system = NumberPlane(
            x_range=[-2.5, 2.5, 0.5],   # Adjust the range to your liking
            y_range=[-2, 2, 0.5],   # Adjust the range to your liking
            background_line_style={"stroke_color": BLUE, "stroke_opacity": 0.5}
        ).move_to(mona_lisa)

        post_transform_coordinate_system = NumberPlane(
            x_range=[-2.5, 2.5, 0.5],   # Adjust the range to your liking
            y_range=[-2, 2, 0.5],   # Adjust the range to your liking
            background_line_style={"stroke_color": BLUE, "stroke_opacity": 0.5}
        ).move_to(mona_lisa.get_center() + 8*RIGHT)

        # Define basis vectors for i-hat and j-hat
        i_hat = Vector([1, 0], color=YELLOW).shift(pre_transform_coordinate_system.get_center())
        j_hat = Vector([0, 1], color=GREEN).shift(pre_transform_coordinate_system.get_center())

        # Label the vectors
        i_hat_label = MathTex("\\hat{i}").next_to(i_hat, RIGHT)
        j_hat_label = MathTex("\\hat{j}").next_to(j_hat, UP)

        # Define basis vectors for transformed i-hat and j-hat
        i_hat_transform = Vector([1, 0], color=YELLOW).apply_matrix(picture_transform_matrix).shift(post_transform_coordinate_system.get_center())
        j_hat_transform = Vector([0, 1], color=GREEN).apply_matrix(picture_transform_matrix).shift(post_transform_coordinate_system.get_center())

        # Label the transformed vectors
        i_hat_label_transform = MathTex("A\\hat{i}").next_to(i_hat_transform, RIGHT)
        j_hat_label_transform = MathTex("A\\hat{j}").next_to(j_hat_transform, UP)

        pre_transform_change_example = [[0, 1], [1, 1]]

        post_transform_change_example = [[1, 2], [0, 0.5]]

        # Define basis vectors for arbitrary i-hat and j-hat
        i_hat_arb = Vector([1, 0], color=YELLOW).apply_matrix(pre_transform_change_example).shift(pre_transform_coordinate_system.get_center())
        j_hat_arb = Vector([0, 1], color=GREEN).apply_matrix(pre_transform_change_example).shift(pre_transform_coordinate_system.get_center())

        # Define basis vectors for arbitrary transformed i-hat and j-hat
        i_hat_transform_arb = Vector([1, 0], color=YELLOW).apply_matrix(post_transform_change_example).shift(post_transform_coordinate_system.get_center())
        j_hat_transform_arb = Vector([0, 1], color=GREEN).apply_matrix(post_transform_change_example).shift(post_transform_coordinate_system.get_center())

        # Change of basis vs linear transform difference explanation

        change_of_basis_exp = VGroup(
            MathTex(r"\text{We see here that the Mona Lisa has recieved a shear;}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{this change is the linear transform } \mathcal{A} \text{.}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{But the matrix A represents only the change between }", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{the two basis systems, and not the underlying transform. }", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{In fact, we can (almost) arbitrarily change the two basis systems,}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{as long as the new A captures the mapping accurately.}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{Notice how changing the basis for the systems did not change}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{the underlying linear transform } \mathcal{A} \text{.}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff = 0.4).to_corner(UL).shift(0.2*DOWN)

        change_of_basis_exp[4].set_opacity(0)
        change_of_basis_exp[5].set_opacity(0)

        change_of_basis_exp[6].set_opacity(0)
        change_of_basis_exp[7].set_opacity(0)

        # Animation

        self.play(Create(solution[0]))
        self.wait(1.5)
        self.play(Create(solution[1]))
        self.wait(1.5)
        self.play(Create(solution[2]))
        self.wait(3)

        self.play(FadeIn(mona_lisa))
        self.wait(1.5)
        self.play(Create(arrow_1))
        self.wait(1.5)
        self.play(FadeIn(mona_lisa_copy))
        self.wait(1.5)

        self.play(FadeIn(pre_transform_coordinate_system))
        self.wait(1.5)
        self.play(FadeIn(post_transform_coordinate_system))
        self.wait(1.5)

        self.play(FadeIn(i_hat), FadeIn(j_hat), FadeIn(i_hat_label), FadeIn(j_hat_label))
        self.wait(1.5)
        self.play(FadeIn(i_hat_transform), FadeIn(j_hat_transform), FadeIn(i_hat_label_transform), FadeIn(j_hat_label_transform))
        self.wait(1.5)

        self.play(FadeOut(solution))
        self.wait(1.5)
        self.play(Create(change_of_basis_exp[0]))
        self.wait(1.5)
        self.play(Create(change_of_basis_exp[1]))
        self.wait(1.5)
        self.play(Create(change_of_basis_exp[2]))
        self.wait(1.5)
        self.play(Create(change_of_basis_exp[3]))
        self.wait(1.5)
        self.play(FadeOut(change_of_basis_exp[0]), FadeOut(change_of_basis_exp[1]), change_of_basis_exp.animate.shift(UP * 2))
        self.wait(1.5)
        change_of_basis_exp[4].set_opacity(1)
        self.play(Create(change_of_basis_exp[4]))
        self.wait(1.5)
        change_of_basis_exp[5].set_opacity(1)
        self.play(Create(change_of_basis_exp[5]))
        self.wait(3)

        #self.play(i_hat.animate.apply_matrix(pre_transform_change_example), j_hat.animate.apply_matrix(pre_transform_change_example))
        self.play(Transform(i_hat, i_hat_arb), i_hat_label.animate.next_to(i_hat_arb, UP))
        self.play(Transform(j_hat, j_hat_arb), j_hat_label.animate.next_to(j_hat_arb, UP))

        self.play(Transform(i_hat_transform, i_hat_transform_arb), i_hat_label_transform.animate.next_to(i_hat_transform_arb, RIGHT))
        self.play(Transform(j_hat_transform, j_hat_transform_arb), j_hat_label_transform.animate.next_to(j_hat_transform_arb, UP))
        self.wait(1.5)

        self.play(FadeOut(change_of_basis_exp[2]), FadeOut(change_of_basis_exp[3]), change_of_basis_exp.animate.shift(UP * 1.75))
        self.wait(1.5)
        change_of_basis_exp[6].set_opacity(1)
        self.play(Create(change_of_basis_exp[6]))
        self.wait(1.5)
        change_of_basis_exp[7].set_opacity(1)
        self.play(Create(change_of_basis_exp[7]))
        self.wait(3)

        self.wait(5)

        # Prev solution below. 
        """
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
        
        """