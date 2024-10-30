from manim import *
import numpy as np
import math


class Solution38(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        fourth_color = ORANGE
        size_font =  DEFAULT_FONT_SIZE*0.75
        
        question = VGroup( 
                MathTex(r"\text{If a } n \times n \text{ square matrix has } n \text{ different eigenvalues}", 
                    color=first_color, font_size=size_font),
                MathTex(r"\text{then it is diagonalizable.}",
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
    
        # Initial concept explanation-------------------------------------------------------
        title = MathTex(r"\text{Eigenvalues and Eigenvectors}", font_size=50, color=WHITE
            ).to_edge(UP)
        

        description0 = VGroup(
            MathTex(r"\text{Let's consider a generic matrix A of size } n \times n, \text{with eigenvalues } \lambda_1,\lambda_2,...\lambda_n. ", 
                    font_size=35, color=WHITE),
            MathTex(r"\cdot \text{ Let } \lambda_i \text{ be a generic eigenvalue of A.}", 
                    font_size=35, color=WHITE),
            VGroup(MathTex(r"v_i", 
                    font_size=38, color=YELLOW),
                    MathTex(r"\text{ - eigenvector corresponding to }", 
                    font_size=35, color=LIGHT_GRAY),
                    MathTex(r"\lambda_i", 
                    font_size=38, color=YELLOW),).arrange(RIGHT),
            MathTex(r"\lambda_i \text{ determines how } v_i \text{ stretches after}", 
                    font_size=35, color=WHITE),
            MathTex(r"\text{applying the transformation A.}", 
                    font_size=35, color=WHITE),
            VGroup(MathTex(r"Av_i", 
                    font_size=38, color=YELLOW),
                    MathTex(r"=", 
                    font_size=38, color=WHITE),
                    MathTex(r"\lambda_iv_i", 
                    font_size=38, color=YELLOW)).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UL).shift(DOWN)
        
        # Position set up
        description0[2::].shift(0.3*DOWN)
        description0[3::].shift(DOWN)
        description0[5::].shift(1.5*RIGHT)

       
        # Limits for number plane
        limit = [3,2]
        number_plane = NumberPlane(
            x_range=[-limit[0], limit[0], 1],  # Set the x-axis range (min, max, step)
            y_range=[-limit[1]-1, limit[1]+1, 1],  # Set the y-axis range (min, max, step)
            axis_config={"stroke_color": WHITE},  # Customize axis color
            background_line_style={
                "stroke_color": BLUE,  # Grid color
                "stroke_width": 1,
                "stroke_opacity":0.5, 
            }
        ).scale(0.7).set_z_index(-1)

        # Skewed grid
        skew_matrix = np.array([[1, 1], [0, 1.5]])  # Skew transformation matrix
        eigenvalues, eigenvectors = np.linalg.eig(skew_matrix)
        [lambda2, lambda1] = eigenvalues
        two, one = eigenvectors[:, 0], eigenvectors[:, 1]

        matrix_example = VGroup(
            MathTex(r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1.5 \end{bmatrix}", 
                    font_size=35, color=LIGHT_GRAY),
            MathTex(r"\lambda_1 = 1.5 ,  \lambda_2 = 1", 
                    font_size=35, color=LIGHT_GRAY),
            MathTex(r"v_1 = \begin{bmatrix} 2 \\ 1 \end{bmatrix} ,  v_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", 
                    font_size=35, color=LIGHT_GRAY)
        ).arrange(DOWN).shift(RIGHT*1.5+UP*0.8).scale(0.7)

        transformed_plane = NumberPlane(
            x_range=[-limit[0], limit[0], 1],  # Set the x-axis range (min, max, step)
            y_range=[-limit[1], limit[1], 1],  # Set the y-axis range (min, max, step)
            axis_config={"color": BLUE,"stroke_color": WHITE},  # Customize axis color
            background_line_style={
                "stroke_color": BLUE,  # Grid color
                "stroke_width": 1,
                "stroke_opacity":0.5, 
            }).scale(0.7).apply_matrix(skew_matrix).set_z_index(-1)
        
        # Move all down
        VGroup(number_plane,transformed_plane).to_corner(DR, buff = 0.3).shift(0.5*UP).shift(LEFT)
        transformed_plane_copy = transformed_plane.copy()
        transformed_plane_copy2 = transformed_plane.copy()   
        number_plane_copy = number_plane.copy()
        number_plane_copy2 = number_plane.copy()

        # Eigenvectors
        eigenvector1 = Arrow(start=number_plane.c2p(0, 0), end=number_plane.c2p(2,1), color=YELLOW, buff=0)
        eigenvector_label1 = MathTex(r"v_i", color=YELLOW).next_to(eigenvector1.get_end(), UP)
        eigenvector2 = Arrow(start=number_plane.c2p(0, 0), end=number_plane.c2p(1, 0), color=ORANGE, buff=0)
        eigenvector_label2 = MathTex(r"v_j", color=ORANGE).next_to(eigenvector2.get_end(), DOWN)
        
        # Copies
        eigenvector1_copy = eigenvector1.copy()
        eigenvector1_copy2 = eigenvector1.copy()
        eigenvector_label1_copy = eigenvector_label1.copy()
        eigenvector_label1_copy2 = eigenvector_label1.copy()

        eigenvector2_copy = eigenvector2.copy()
        eigenvector_label2_copy = eigenvector_label2.copy()
        
        # Spans
        span1 = Line(start=number_plane.c2p(-limit[0], -limit[0]/2),
                    end=number_plane.c2p(limit[0], limit[0]/2),
                    color = YELLOW).set_opacity(0.5).set_z_index(-1)
        span_label1 = MathTex(r"\text{span(}v_i\text{)}}", 
                              font_size=35, color=YELLOW).scale(0.7).next_to(span1.get_end(), RIGHT*1.5+0.3*DOWN)
        
        span2 = Line(start=number_plane.c2p(-limit[0], 0),
                    end=number_plane.c2p(limit[0], 0),
                    color = ORANGE).set_opacity(0.5).set_z_index(-1)
        span_label2 = MathTex(r"\text{span(}v_j\text{)}}", 
                              font_size=35, color=ORANGE).scale(0.7).next_to(span2.get_end(), DOWN*1.2+0.7*RIGHT)

        # Transformed eigenvector
        transformed_eigenvector1 = Arrow(start=transformed_plane.c2p(0, 0), end=number_plane.c2p(2*lambda1, 1*lambda1), color=YELLOW, buff=0)
        transformed_label1 = MathTex(r"Av_i", color=YELLOW).next_to(transformed_eigenvector1.get_end(), UP)
        transformed_label11 = MathTex(r"\lambda_iv_i", color=YELLOW).next_to(transformed_eigenvector1.get_end(), UP)

        transformed_eigenvector2 = Arrow(start=transformed_plane.c2p(0, 0), end=number_plane.c2p(1*lambda2, 0*lambda2), color=ORANGE, buff=0)
        transformed_label2 = MathTex(r"Av_j", color=ORANGE).next_to(transformed_eigenvector2.get_end(), DOWN)
        transformed_label22 = MathTex(r"\lambda_jv_j", color=ORANGE).next_to(transformed_eigenvector2.get_end(), DOWN)

        # Copies
        transformed_eigenvector1_copy = transformed_eigenvector1.copy()
        transformed_eigenvector1_copy2 = transformed_eigenvector1.copy()
        transformed_label1_copy = transformed_label1.copy()
        transformed_label11_copy= transformed_label11.copy()
        transformed_eigenvector2_copy = transformed_eigenvector2
        
        # Animations part one
        self.play(Create(title,run_time=1))
        self.wait(1)
        self.play(Create(description0[0],run_time=1.5))
        self.wait(1)
        self.play(Create(description0[1],run_time=1))
        self.wait(1)
        self.play(Create(description0[2],run_time=1))
        self.wait(1)
        self.play(Create(number_plane,run_time = 0.5))
        self.play(Create(matrix_example))
        self.wait(1)
        self.play(Create(eigenvector1,run_time = 0.5), 
                  Write(eigenvector_label1))
        self.wait(1)
        self.play(Create(span1), Create(span_label1))
        self.wait(1)
        self.play(Create(description0[3],run_time = 1))
        self.wait(0.5)
        self.play(Create(description0[4],run_time = 1))
        self.wait(1)
        self.play(Create(description0[5],run_time = 1))
        self.wait(1)
        self.play(ReplacementTransform(number_plane, transformed_plane),
                  ReplacementTransform(eigenvector1,transformed_eigenvector1),
                  ReplacementTransform(eigenvector_label1,transformed_label1))
        self.play(Indicate(transformed_label1,scale_factor = 1.2))
        self.wait(1)
        self.play( ReplacementTransform(transformed_label1,transformed_label11))
        self.play(Indicate(transformed_label11,scale_factor = 1.2))
        self.wait(1)



        #------------> Part two <----------------
        self.play(FadeOut(description0[3:5]))
        self.play(description0[5].animate.shift(2.2*UP))
        self.play(ReplacementTransform(transformed_plane, number_plane_copy),
                  ReplacementTransform(transformed_eigenvector1,eigenvector1_copy),
                  ReplacementTransform(transformed_label11,eigenvector_label1_copy))
        self.wait(1)

        description1 = VGroup(
            MathTex(r"\text{Let's consider a generic matrix A of size } n \times n, \text{with eigenvalues } \lambda_1,\lambda_2,...\lambda_n. ", 
                    font_size=35, color=WHITE),
            MathTex(r"\text{Let } \lambda_i \text{ be a generic eigenvalue of A.}", 
                    font_size=35, color=WHITE),
            VGroup(MathTex(r"v_i", 
                    font_size=38, color=YELLOW),
                    MathTex(r"\text{ - eigenvector corresponding to }", 
                    font_size=35, color=WHITE),
                    MathTex(r"\lambda_i", 
                    font_size=38, color=YELLOW),).arrange(RIGHT),
            MathTex(r"\cdot \text{ Now consider a different eigenvalue }\lambda_j", 
                    font_size=35, color=WHITE),
            VGroup(MathTex(r"\lambda_j", 
                    font_size=38, color=ORANGE),
                    MathTex(r"\neq", 
                    font_size=35, color=WHITE),
                    MathTex(r"\lambda_i", 
                    font_size=38, color=YELLOW),).arrange(RIGHT),
            VGroup(MathTex(r"v_j", 
                    font_size=38, color=ORANGE),
                    MathTex(r"\text{ - eigenvector corresponding to }", 
                    font_size=35, color=LIGHT_GRAY),
                    MathTex(r"\lambda_j", 
                    font_size=38, color=ORANGE),).arrange(RIGHT),
            VGroup(MathTex(r"Av_j", 
                    font_size=38, color=ORANGE),
                    MathTex(r"=", 
                    font_size=38, color=WHITE),
                    MathTex(r"\lambda_jv_j", 
                    font_size=38, color=ORANGE)).arrange(RIGHT),
        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UL).shift(DOWN)
        
        description1[2::].shift(0.3*DOWN)
        description1[3::].shift(DOWN)
        description1[4].shift(1.75*RIGHT)
        description1[6].shift(1.5*RIGHT)


        # Animations part two
        self.play(Create(description1[3],run_time = 1))
        self.wait(0.5)
        self.play(Create(description1[4],run_time = 1))
        self.wait(1)
        self.play(Create(description1[5],run_time = 1))
        self.wait(1)
        self.play(Create(eigenvector2,run_time = 0.5), 
                  Write(eigenvector_label2))
        self.wait(1)
        self.play(Create(span2), Create(span_label2))
        self.wait(1)
        self.play(Create(description1[6]))

        self.play(ReplacementTransform(number_plane_copy, transformed_plane_copy),
                  ReplacementTransform(eigenvector1_copy,transformed_eigenvector1_copy),
                  ReplacementTransform(eigenvector_label1_copy,transformed_label1_copy),
                  ReplacementTransform(eigenvector2,transformed_eigenvector2),
                  ReplacementTransform(eigenvector_label2,transformed_label2))
        self.wait(1)
        self.play( ReplacementTransform(transformed_label1_copy,transformed_label11_copy))
        self.play(Indicate(transformed_label11_copy,scale_factor = 1.2))
        self.wait(1)
        self.play( ReplacementTransform(transformed_label2,transformed_label22))
        self.play(Indicate(transformed_label22,scale_factor = 1.2, color= ORANGE))
        self.wait(1)


        #--------------> Part three <-------------
        self.play(FadeOut(description0[1:3],description0[5], description1[3::]),
                        FadeOut(matrix_example))
        self.wait(1)
        self.play(ReplacementTransform(transformed_plane_copy, number_plane_copy2),
                  ReplacementTransform(transformed_eigenvector1_copy,eigenvector1_copy2),
                  ReplacementTransform(transformed_label11_copy,eigenvector_label1_copy2),
                  ReplacementTransform(transformed_eigenvector2,eigenvector2_copy),
                  ReplacementTransform(transformed_label22,eigenvector_label2_copy))
        self.wait(1)
        transformed_eigenvector1 = Arrow(start=transformed_plane.c2p(0, 0), 
                                        end=number_plane_copy2.c2p(2*lambda1, 1*lambda1), 
                                        color=YELLOW, buff=0)
        transformed_eigenvector2 = Arrow(start=transformed_plane.c2p(0, 0), 
                                        end=number_plane_copy2.c2p(2*lambda2, 1*lambda2), 
                                        color=ORANGE, buff=0)

        description2 = VGroup(
            MathTex(r"\text{Let's consider a generic matrix A of size } n \times n, \text{with eigenvalues } \lambda_1,\lambda_2,...\lambda_n. ", 
                    font_size=35, color=WHITE),
            MathTex(r"\text{Eigenvectors of two different eigenvalues}", 
                    font_size=35, color=WHITE),
            MathTex(r"\text{must be linearly independent!}", 
                    font_size=35, color=WHITE),
            MathTex(r"\text{One eigenvector cannot be associated to}", 
                    font_size=35, color=WHITE),
            MathTex(r"\text{two different eigenvalues, because it}", 
                    font_size=35, color=WHITE),
            MathTex(r"\text{cannot be stretched in two different ways.}", 
                    font_size=35, color=WHITE),
        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UL).shift(DOWN)

        description2[1:].shift(DOWN)
        description2[3:].shift(DOWN)

        #Animations
        self.play(Create(description2[1],run_time=1.5))
        self.wait(0.3)
        self.play(Create(description2[2],run_time=1))
        self.wait(0.5)
        self.play(FadeOut(eigenvector_label1_copy2, eigenvector_label2_copy))

        self.play(Rotate(VGroup(span2, eigenvector2_copy), 
                         angle=PI*0.14758, run_time=2, 
                         about_point=number_plane_copy2.c2p(0, 0)))
        #Adding cross to indicate it is wrong
        cross = Cross(stroke_color=RED_D, 
                      stroke_width=20).move_to(eigenvector2_copy).scale(0.5).rotate(PI / 10)
        self.play(Create(cross))
        self.wait(0.7)
        self.play(FadeOut(cross))
        self.play(Rotate(VGroup(span2, eigenvector2_copy), 
                         angle=PI, run_time=2, 
                         about_point=number_plane_copy2.c2p(0, 0)))
        #Adding cross to indicate it is wrong
        cross = Cross(stroke_color=RED_D, 
                      stroke_width=20).move_to(eigenvector2_copy).scale(0.5).rotate(PI / 10)
        self.play(Create(cross))
        self.wait(0.7)
        self.play(FadeOut(cross))
        self.play(Rotate(VGroup(span2, eigenvector2_copy), 
                         angle=PI*0.85242, run_time=1.5, 
                         about_point=number_plane_copy2.c2p(0, 0)))
        self.wait(1)


        # After transformation
        self.play(Create(description2[3],run_time=1.5),
                  Rotate(VGroup(span2, eigenvector2_copy), 
                         angle=PI*0.14758, run_time=2, 
                         about_point=number_plane_copy2.c2p(0, 0)))
        self.play(FadeOut(span_label2,eigenvector2_copy,span2))
        self.play(Create(description2[4],run_time=1))
        self.wait(0.3)
        self.play(Create(description2[5],run_time=1),
                  ReplacementTransform(number_plane_copy2, transformed_plane_copy2),
                  ReplacementTransform(eigenvector1_copy2,VGroup(transformed_eigenvector1,transformed_eigenvector2)))
        self.wait(2)
        self.play(FadeOut(title,
                        description0[0],
                        description2[1::],
                        transformed_plane_copy2,
                        VGroup(transformed_eigenvector1,transformed_eigenvector2),
                        span_label1,
                        span1))
        #OLD PART -----------------------------------------------------------------------------------------------
        text_break = VGroup(
            MathTex(r"\text{Let's go back to the original question:}", 
                    color=LIGHT_GRAY, font_size=size_font),
            MathTex(r"\text{If a } n \times n \text{ square matrix has } n \text{ different eigenvalues}", 
                    color=WHITE, font_size=size_font),
           MathTex(r"\text{is it diagonalizable?}", 
                    color=WHITE, font_size=size_font),
        ).arrange(DOWN)
        text_break[1:].shift(0.5*DOWN)

        # Animation
        self.wait(1)
        self.play(Create(text_break[0], run_time = 1))
        self.wait(1)
        self.play(Create(text_break[1], run_time = 1.5))
        self.wait(0.5)
        self.play(Create(text_break[2], run_time = 1))
        self.wait(2)
        self.play(FadeOut(text_break))
       
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
            MathTex(r"\bullet \text{ number of independent}", 
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
            MathTex(r"\text{In total, there are } n \text{ independent eigenvectors.}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{A basis formed by these eigenvectors will diagonalize the matrix.}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN,buff = 0.5).to_edge(UP).shift(0.2*DOWN)
        
        VGroup(solution[3:4],
               box_geometric,additional_text_geometric,
               box_algebraic,additional_text_algebraic,
               inequality[0], inequality[2], inequality[4],
               inequality2[0], inequality2[2], inequality2[4]).to_edge(UP)
        VGroup(solution[0], solution[1],
               solution2[0], solution2[1]).to_edge(DOWN)
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
        self.play(Create(box_geometric,run_time = 1))
        self.wait(0.8)
        self.play(Create(additional_text_geometric[1]))
        self.wait(0.5)
        self.play(Create(additional_text_geometric[2]))
        self.wait(0.5)
        self.play(Create(additional_text_geometric[3]))
        self.wait(0.5)
        self.play(Create(additional_text_geometric[4]))
        self.wait(1)

        # Additional explenation on algebraic multiplicity
        self.play(Create(box_algebraic, run_time = 1))
        self.wait(0.8)
        self.play(Create(additional_text_algebraic[1]))
        self.wait(0.5)
        self.play(Create(additional_text_algebraic[2]))
        self.wait(0.5)
        self.play(Create(additional_text_algebraic[3]))
        self.wait(0.5)
        self.play(Create(additional_text_algebraic[4]))
        self.wait(3)

        # Animating text
        self.play(Create(solution[0],run_time = 2))
        self.wait(2)
        self.play(Create(solution[1],run_time = 2))
        self.wait(2)
        self.play(GrowFromCenter(inequality[4]))
        self.play(Indicate(inequality[4], color = WHITE))

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

        #Adding text 
        self.play(Create(solution2[0]))
        self.wait(2)
        self.play(Create(solution2[1]))
        self.wait(6)
        self.play(FadeOut(solution2, inequality[1],inequality[4],inequality[2],
                          additional_text_geometric,
                          box_geometric,
                          solution[3]))

