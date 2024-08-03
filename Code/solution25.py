from manim import *
import numpy as np
import math

class Solution25(Scene):
    def construct(self):

        # To change the whole color scheme easier
        first_color = LIGHT_GRAY
        second_color = BLUE

        # Create the question and answer choices as a VGroup
        box = Rectangle(
            height=4.5, 
            width=12, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=first_color)

        question = VGroup(
            MathTex(r"\text{If one says that the matrix A has a trivial kernel,}", color = first_color),
            MathTex(r"\text{what does this mean?}",color=first_color),
            MathTex(r"\text{a) Ker(A)= 0}", color=first_color),
            MathTex(r"\text{b) Ker(A)= \{0\}}", color=first_color),
            MathTex(r"\text{c) it depends}", color=first_color)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).shift(1.5*UP)
        VGroup(question[2:]).shift(RIGHT)

        question_scaled =VGroup(question, box).copy().scale(0.5).to_corner(UL, buff=0.3)
        # Animating the question
        self.play(Create(box))
        self.wait(0.5)
        self.play(Write(question[0]))
        self.wait(0.5)
        self.play(Write(question[1]))
        self.wait(0.5)
        self.play(Write(question[2]))
        self.wait(0.5)
        self.play(Write(question[3]))
        self.wait(0.5)
        self.play(Write(question[4]))
        self.wait(2)
        self.play(question[3].animate.set_color(second_color))
        self.wait(2)
        self.play(Transform(VGroup(question,box), question_scaled))
        self.wait(1)

        # Showing what Kernel is
        kernel_definition = VGroup(
            MathTex(r"\text{Kernel is a subspace of the domain,}", color = first_color),
            MathTex(r"\Rightarrow \text{ it is a set of elements.}",color=first_color),
            MathTex(r"\text{ Ker(A) = \{...\}}",color=second_color)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.8).next_to(question_scaled, RIGHT)
        kernel_definition[2].shift(RIGHT)
        kernel_definition.shift(0.2*UP)

        ellipse_1 = VGroup(
            Ellipse(width=2.0, height=4.0, color=first_color),
            MathTex(r"\text{Domain}", color = first_color,font_size=DEFAULT_FONT_SIZE*0.8)
            ).arrange(UP).shift(1.5*RIGHT+1.5*DOWN)
        
        ellipse_2 = VGroup(
            Ellipse(width=2.0, height=4.0, color=first_color),
            MathTex(r"\text{Codomain}", color = first_color,font_size=DEFAULT_FONT_SIZE*0.8)
            ).arrange(UP).shift(5.5*RIGHT+1.5*DOWN)
        
        arrow = VGroup(
            Arrow(color = first_color),
            MathTex(r"A", color = first_color)
            ).arrange(UP).scale(0.8).next_to(ellipse_1, RIGHT+0.1*UP)
        
        ellipse_3 = VGroup(
            Ellipse(width=1.0, height=2.0, color=second_color),
            MathTex(r"\text{Ker(A)}", color = second_color,font_size=DEFAULT_FONT_SIZE*0.7)
            ).arrange(UP).move_to(ellipse_1)
        
        dot = VGroup(
            Dot(color = second_color),
            MathTex(r"0", color = second_color,font_size=DEFAULT_FONT_SIZE*0.7)
            ).arrange(UP).move_to(ellipse_2)
        
        lines = VGroup(
            Line(start=ellipse_3[0].get_top(), end=dot[0].get_center(), color = second_color),
            Line(start=ellipse_3[0].get_bottom(), end=dot[0].get_center(), color = second_color))
        lines2 = lines.copy()

        self.play(
            Create(ellipse_1),
            Create(ellipse_2))
        self.wait(1)
        self.play(Create(arrow))
        self.wait(0.5)
        self.play(Create(ellipse_3))
        self.wait(0.5)
        self.play(Create(lines), Create(dot))
        self.wait(2)
        self.play(Create(kernel_definition[0]))
        self.wait(0.5)
        self.play(Create(kernel_definition[1]))
        self.wait(0.5)
        self.play(Create(kernel_definition[2]))
        self.wait(2)

        trivial_definition = VGroup(
            MathTex(r"\text{Trivial kernel means that Ker(A) }", color = first_color),
            MathTex(r"\text{contains only one element, which is 0.}",color=first_color),
            MathTex(r"\Rightarrow\text{ Ker(A) = \{0\}}",color=second_color),
            MathTex(r"\text{Writing Ker(A)= 0 indicates that }", color = first_color),
            MathTex(r"\text{kernel is an element of the domain,}",color=first_color),
            MathTex(r"\text{which is improper, because }",color=first_color),
            MathTex(r"\text{it is a subset, not an element.",color=first_color),
        ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.8).next_to(question_scaled, DOWN)
        trivial_definition.shift(0.5*RIGHT)
        trivial_definition[2].shift(RIGHT)
        trivial_definition[3:].shift(DOWN)
        dot2 = VGroup(
            Dot(color = second_color),
            MathTex(r"0", color = second_color,font_size=DEFAULT_FONT_SIZE*0.7)
            ).arrange(UP).move_to(ellipse_3)
        line2 = Line(start=dot2[0].get_center(), end=dot[0].get_center(), color = second_color)
        
        self.play(Create(trivial_definition[0]))
        self.wait(0.8)
        self.play(Create(trivial_definition[1]), Create(dot2))
        self.wait(1)
        self.play(Create(trivial_definition[2]))
        self.wait(2)
        self.play(Create(trivial_definition[3]))
        self.wait(0.3)
        self.play(Create(trivial_definition[4]), ReplacementTransform(lines, line2), FadeOut(ellipse_3))
        self.wait(1)
        self.play(Create(trivial_definition[5]))
        self.wait(0.3)
        self.play(Create(trivial_definition[6]), FadeIn(ellipse_3),ReplacementTransform(line2, lines2) )
        self.wait(2)

        self.play(question[3].animate.set_color(second_color))
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])


