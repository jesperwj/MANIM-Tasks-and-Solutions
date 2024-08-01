from manim import *
import numpy as np
import math

class Solution23(Scene):
    def construct(self):
        
        variables = VGroup(MathTex("y"), MathTex("u")).arrange_submobjects().shift(UP)
        
        soloution_text = VGroup(
            MathTex(r"\text{The origin of an LTI system is always an equilibria.}",color=LIGHT_GRAY),
            MathTex(r"\text{This is easier to see intuitively by looking at the scalar case.}",color=LIGHT_GRAY),
            MathTex(r"\text{In the origin it does not matter what a and b are, }",color=LIGHT_GRAY),
            MathTex(r"\dot{{y}} \text{ is zero for all values of a and b}}",color=LIGHT_GRAY)
            
        ).arrange(DOWN).move_to(1.5*UP).scale(0.90)
        
        equation_text_linAlg = VGroup(
            MathTex(r"\dot{{y}} = A{y} + B{u}")
        ).arrange(DOWN).move_to(0.5*DOWN).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        equation_text_scalar = VGroup(
            MathTex(r"\dot{{y}} = a{y} + b{u}")
        ).arrange(DOWN).move_to(0.5*DOWN).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        equation_origin = VGroup(
            MathTex(r"\dot{{y}} = a\cdot0 + b\cdot0")
        ).arrange(DOWN).move_to(0.5*DOWN).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        equation_origin_zero = VGroup(
            MathTex(r"\dot{{y}} = a\cdot0 + b\cdot0 = 0")
        ).arrange(DOWN).move_to(0.5*DOWN+0.1*RIGHT).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        self.play(Write(soloution_text[0]))
        self.wait(1)
        
        self.play(Write(equation_text_linAlg))
        self.wait(1)
        
        self.play(Write(soloution_text[1]))
        self.wait(1)
        
        self.play(TransformMatchingTex(equation_text_linAlg, equation_text_scalar))
        self.wait(2)
        
        self.play(Write(soloution_text[2]))
        self.wait(0.5)
        
        self.play(Write(soloution_text[3]))
        self.wait(0.5)
        
        self.play(TransformMatchingTex(equation_text_scalar, equation_origin))
        self.wait(1)
        
        self.play(TransformMatchingTex(equation_origin, equation_origin_zero))
        self.wait(2)