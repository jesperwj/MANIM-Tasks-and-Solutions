from manim import *
import numpy as np
import math

class Solution14(Scene):
    def construct(self):
        # Defining axes
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 1.2, 0.2],
            axis_config={"color": LIGHT_GRAY, "include_numbers": True},
            y_length = 6,
            x_length = 10
        ).move_to(0.7*LEFT+0.3*DOWN).scale(0.85)
        labels = axes.get_axis_labels(x_label="t", y_label="y(t)").scale(0.9)

        # Parameters and functions
        alpha = -1
        beta = -2
        omega = 5
        
        overdamped = lambda x: math.exp(alpha*x)
        underdamped = lambda x: math.exp(beta*x) * math.cos(omega*x)
        
        # Creating signals on axes
        underdamped_signal = axes.plot(underdamped, color=PURPLE)
        underdamped_label = VGroup(
            MathTex(r"\text{From observing the response,}",color=LIGHT_GRAY),
            MathTex(r"\text{one can see that the}",color=LIGHT_GRAY),
             MathTex(r"\text{response is underdamped.}",color=LIGHT_GRAY),
        ).arrange(DOWN, center=False, aligned_edge = LEFT).move_to(1.8*RIGHT+1.5*UP).scale(0.90)
        
        # Animating combined signal first
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Create(underdamped_signal))
        self.play(FadeIn(underdamped_label[0]), runtime = 0.5)
        self.play(FadeIn(underdamped_label[1]), runtime = 0.5)
        self.play(FadeIn(underdamped_label[2]), runtime = 0.5)
        self.wait(3)
        self.play(FadeOut(underdamped_label))
        
        underdamped_label_2 = VGroup(
            MathTex(r"\text{This is clear from the oscilations,}",color=LIGHT_GRAY),
            MathTex(r"\text{which only happen for underdamped systems}",color=LIGHT_GRAY),
        ).arrange(DOWN, center=False, aligned_edge = LEFT).move_to(1.8*RIGHT+1.5*UP).scale(0.90)
        
        self.wait(0.5)
        self.play(FadeIn(underdamped_label_2[0]), runtime = 0.5)
        self.play(FadeIn(underdamped_label_2[1]), runtime = 0.5)
        self.wait(3)
        self.play(FadeOut(underdamped_label_2))