from manim import *
import numpy as np
import math

class Solution24(Scene):
    def construct(self):
        
        variables = VGroup(MathTex("y"), MathTex("u")).arrange_submobjects().shift(UP)
        
        soloution_text = VGroup(
            MathTex(r"\text{The origin of some generic system is not necessarily an equilibria.}",color=LIGHT_GRAY),
            MathTex(r"\text{This is easier to see intuitively by looking at a counter example.}",color=LIGHT_GRAY),
            MathTex(r"\text{For this example it is clear that, } \dot{{y}} \text{ is non-zero in the origin.}",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(1.5*UP).scale(0.90)
        
        equation_text_org = VGroup(
            MathTex(r"\dot{{y}} = f({y},{u})")
        ).arrange(DOWN).move_to(0.5*DOWN).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        equation_text_counter = VGroup(
            MathTex(r"\dot{{y}} = ({y}+1)^2")
        ).arrange(DOWN).move_to(0.5*DOWN).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        equation_origin = VGroup(
            MathTex(r"\dot{{y}} = (0+1)^2 = 1")
        ).arrange(DOWN).move_to(0.5*DOWN+0.1*RIGHT).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        self.play(Write(soloution_text[0]))
        self.wait(1)
        
        self.play(Write(equation_text_org))
        self.wait(1)
        
        self.play(Write(soloution_text[1]))
        self.wait(1)
        
        self.play(TransformMatchingTex(equation_text_org, equation_text_counter))
        self.wait(2)
        
        self.play(Write(soloution_text[2]))
        self.wait(0.5)
        
        self.play(TransformMatchingTex(equation_text_counter, equation_origin))
        self.wait(2)