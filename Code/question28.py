from manim import *
import numpy as np
import math

class Question28(Scene):
    def construct(self):
        
        task_text = VGroup(
            MathTex(r"\text{Is the continous time LTI system characterized}",color=LIGHT_GRAY),
            MathTex(r"\text{by the following impulse response BIBO stable? }",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(1.5*UP).scale(0.90)      
        
        equation_text = VGroup(
            MathTex(r"h(t) = \begin{cases} 1 & \text{for } t \geq 0 \\ 0 & \text{otherwise} \end{cases} ", color = BLUE),
        ).arrange(DOWN).move_to(DOWN).scale(0.90)
        
        self.play(Write(task_text), run_time=3)
        self.wait(1)
        
        self.play(Write(equation_text))
        self.wait(2)