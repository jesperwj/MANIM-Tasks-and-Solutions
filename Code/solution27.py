from manim import *
import numpy as np
import math

class Solution27(Scene):
    def construct(self):
        
        soloution_text = VGroup(
            MathTex(r"\text{The LTI system with impulse response}",color=LIGHT_GRAY),
            MathTex(r"h(t) = \begin{cases} e^{-2t} & \text{for } t \geq 0 \\ 0 & \text{otherwise} \end{cases} ", color = BLUE),
            MathTex(r"\text{ is a BIBO stable system.}",color=LIGHT_GRAY),
            Tex(r"An easy way to find this out is to check \\ if the response is absultely integrable.",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(1.8*UP).scale(0.90)      
        
        equation_text = VGroup(
            MathTex(r"\int_0^\infty e^{-2t} dt", color = BLUE),
            MathTex(r"= [\frac{1}{2}e^{-2t}]^{\infty}_{0}", color = BLUE),
            MathTex(r"= -\frac{1}{2}e^{-2\cdot\infty} + \frac{1}{2}e^{-2\cdot0}", color = BLUE),
            MathTex(r"= 0 + \frac{1}{2}", color = BLUE),
            MathTex(r"=\frac{1}{2}", color = BLUE),
        ).arrange(DOWN).move_to(3*DOWN + LEFT).scale(0.90)
        
        equation_text[1].next_to(equation_text[0], RIGHT)
        equation_text[2].next_to(equation_text[0], RIGHT)
        equation_text[3].next_to(equation_text[0], RIGHT)
        equation_text[4].next_to(equation_text[0], RIGHT)
        
        self.play(Write(soloution_text[0:3]), run_time=2)
        self.wait(1)
        
        self.play(Write(soloution_text[3:4]), run_time=2)
        self.wait(1)
        
        self.play(Write(equation_text[0]))
        self.wait(2)
        
        self.play(Write(equation_text[1]))
        self.wait(2)
        
        self.play(ReplacementTransform(equation_text[1], equation_text[2]))
        self.wait(0.5)
        
        self.play(ReplacementTransform(equation_text[2], equation_text[3]))
        self.wait(0.5)
        
        self.play(ReplacementTransform(equation_text[3], equation_text[4]))
        self.wait(2)
        
        