from manim import *
import numpy as np
import math

class Question35(Scene):
    def construct(self):
        
        task_text = VGroup(
            MathTex(r"\text{How may one interpret the kernel}",color=LIGHT_GRAY),
            MathTex(r"\text{of a } \mathbb{R}^{n \times m} \text{ matrix A? }",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(1.5*UP).scale(0.90)      
        
        equation_text = VGroup(
            MathTex(r"\text{A: As the set of equilibria of the system } \dot{{x}} = A{x} ", color = LIGHT_GRAY),
            MathTex(r"\text{B: As the set of equilibria of the system } \dot{{x}} = A{x} + B{u}", color = LIGHT_GRAY),
            MathTex(r"\text{C: As the set of zeros of the linear map induced by } A ", color = LIGHT_GRAY),
            MathTex(r"\text{D: As the domain of the map induced by } A ", color = LIGHT_GRAY),
            MathTex(r"\text{E: It depends } ", color = LIGHT_GRAY)
        ).arrange(DOWN).move_to(DOWN).scale(0.90).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        self.play(Write(task_text), run_time=3)
        self.wait(1)
        
        for element in equation_text:
            self.play(Write(element), run_time=0.85)
            self.wait(2)
        self.wait(2)