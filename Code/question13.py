from manim import *
import numpy as np
import math

class Question13(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 1.2, 0.2],
            axis_config={"color": LIGHT_GRAY, "include_numbers": True},
            y_length = 6,
            x_length = 10
        ).move_to(0.2*LEFT+0.3*DOWN).scale(0.85)
        labels = axes.get_axis_labels(x_label="t", y_label="y(t)").scale(0.95)

        # Parameters and functions
        alpha = -1
        beta = -2
        omega = 5
        
        overdamped = lambda x: math.exp(alpha*x)
        underdamped = lambda x: math.exp(beta*x) * math.cos(omega*x)

        # Creating signals on axes
        combined_signal = axes.plot(overdamped, color=PURPLE)
        combined_label = VGroup(
            MathTex(r"\text{The following plot corresponds to}",color=PURPLE),
            MathTex(r"\text{a response from which type of system?}",color=PURPLE),
            MathTex(r"\text{\: a) underdamped}",color=LIGHT_GRAY),
            MathTex(r"\text{\: b) overdamped}",color=LIGHT_GRAY),
            ).arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.9)
        combined_label.move_to(1.5*UP+2*RIGHT)

        VGroup(combined_label[2], combined_label[3]).shift(RIGHT)

        # Animating impulse response and the question lines
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Write(combined_label[0]))
        self.wait(0.5)
        self.play(Write(combined_label[1]))
        self.wait(0.5)
        self.play(
            Create(combined_signal),
            runtime = 0.5
            )
        self.wait(2)
        self.play(Write(combined_label[2]))
        self.wait(0.5)
        self.play(Write(combined_label[3]))
        self.wait(4)

        self.play(*[FadeOut(mob)for mob in self.mobjects])