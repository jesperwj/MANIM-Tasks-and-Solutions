from manim import *
import numpy as np
import math

class Solution28(Scene):
    def construct(self):
        
        soloution_text = VGroup(
            MathTex(r"\text{The LTI system with impulse response}",color=LIGHT_GRAY),
            MathTex(r"h(t) = \begin{cases} 1 & \text{for } t \geq 0 \\ 0 & \text{otherwise} \end{cases} ", color = BLUE),
            MathTex(r"\text{ is not a BIBO stable system.}",color=LIGHT_GRAY),
            Tex(r"An easy way to find this out is to check \\ if the response is absultely integrable.",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(1.8*UP).scale(0.90)      
        
        equation_text = VGroup(
            MathTex(r"\int_0^\infty 1 dt", color = BLUE),
            MathTex(r"= [t]^{\infty}_{0}", color = BLUE),
            MathTex(r"= \infty - 0", color = BLUE),
            MathTex(r"= +\infty", color = BLUE),
        ).arrange(DOWN).move_to(3*DOWN + LEFT).scale(0.90)
        
        equation_text[1].next_to(equation_text[0], RIGHT)
        equation_text[2].next_to(equation_text[0], RIGHT)
        equation_text[3].next_to(equation_text[0], RIGHT)
        
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
        self.wait(2)