from manim import *
import numpy as np
import math

class Solution35(Scene):
    def construct(self):
        
        # To change the whole color scheme easier
        first_color = LIGHT_GRAY
        second_color = BLUE
        
        soloution_text = VGroup(
            MathTex(r"\text{How may one interpret the kernel}",color=first_color),
            MathTex(r"\text{of a } \mathbb{R}^{n \times m} \text{ matrix A? }",color=first_color)
        ).arrange(DOWN).move_to(1.5*UP).scale(0.90)      
        
        answers = VGroup(
            MathTex(r"\text{A: As the set of equilibria of the system } \dot{{x}} = A{x} ", color = first_color),
            MathTex(r"\text{B: As the set of equilibria of the system } \dot{{x}} = A{x} + B{u}", color = first_color),
            MathTex(r"\text{C: As the set of zeros of the linear map induced by } A ", color = first_color),
            MathTex(r"\text{D: As the domain of the map induced by } A ", color = first_color),
            MathTex(r"\text{E: It depends } ", color = first_color)
        ).arrange(DOWN).move_to(DOWN).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        self.play(Write(soloution_text), run_time=3)
        self.wait(1)
        
        for answer in answers:
            self.play(Write(answer), run_time=0.85)
            self.wait(2)
        self.wait(2)
        
        self.play(Indicate(answers[2], color = second_color))
        self.wait(0.5)
        self.play(Indicate(answers[2], color = second_color))
        self.wait(0.5)
        
        self.play(answers[2].animate.set_color(second_color))
        self.wait(2)
        
        self.play(FadeOut(soloution_text))
        self.wait(0.5)
        
        #self.play(answers.animate.shift(UP + 0.25*LEFT))
        #self.wait(0.5)
        
        # --- EXPLANATION SECTION ---

        # Create the question and answer choices as a VGroup
        box = Rectangle(
            height=4.5, 
            width=12, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=first_color).move_to(DOWN + 0.25*RIGHT)

        question_scaled =VGroup(answers, box).copy().scale(0.5).to_corner(UL, buff=0.3)
        # Animating the question
        self.play(Create(box))
        self.wait(0.5)
        self.play(Transform(VGroup(answers,box), question_scaled))
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

        soloution_explanation = VGroup(
            MathTex(r"\text{For the mapping introduced by A}", color = first_color),
            MathTex(r"\text{the kernel Ker(A) is the set in the domain}",color=first_color),
            MathTex(r"\text{which maps to 0 in the codomain.}",color=second_color),
            MathTex(r"\text{Answer A. is therefore imprecise }", color = first_color),
            MathTex(r"\text{as this explanation is valid for } \dot{{x}} = A{x}",color=first_color),
            MathTex(r"\text{but is not valid for \textit{any} matrix A.}",color=first_color),
            MathTex(r"\text{Answer B is also imprecise, but additionally because",color=first_color),
            MathTex(r"\text{if } u \neq 0 \text{ the equilibria do not necessarily} ",color=first_color),
            MathTex(r"\text{coincide with the kernel of A.}",color=first_color),
        ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.6).next_to(question_scaled, DOWN)
     
        soloution_explanation.shift(0.5*RIGHT)
        
        delta = 0.4
        shift_value = 0
            
        soloution_explanation[0:3].shift(shift_value*DOWN)
        
        shift_value += delta
        
        soloution_explanation[3:6].shift(shift_value*DOWN)
        
        shift_value += delta
        
        soloution_explanation[6:9].shift(shift_value*DOWN)
        
        
        self.play(Create(soloution_explanation[0]))
        self.wait(2)
        self.play(Create(soloution_explanation[1]))
        self.wait(2)
        self.play(Create(soloution_explanation[2]))
        self.wait(2)
        self.play(Create(soloution_explanation[3]))
        self.wait(2)
        self.play(Create(soloution_explanation[4]))
        self.wait(2)
        self.play(Create(soloution_explanation[5]))
        self.wait(2)
        self.play(Create(soloution_explanation[6]))
        self.wait(2)
        self.play(Create(soloution_explanation[7]))
        self.wait(2)
        self.play(Create(soloution_explanation[8]))
        self.wait(2)

        self.wait(5)

        self.play(*[FadeOut(mob)for mob in self.mobjects])
        
        