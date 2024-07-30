from manim import *
import numpy as np
import math

class Question13(Scene):
    def construct(self):

        # To change the whole color scheme easier
        second_color = YELLOW

        # Defining axes
        axes = Axes(
            x_range=[0, 3, 5],
            y_range=[0, 1.2, 5],
            axis_config={"color": LIGHT_GRAY},
            y_length = 6,
            x_length = 10
        ).move_to(1.5*LEFT+0.1*DOWN).scale(0.8)
        labels = axes.get_axis_labels(x_label="t", y_label="y(t)").scale(0.95)

        # Parameters and functions
        alpha = -2
        beta = -2
        omega = 5
        
        overdamped = lambda x: math.exp(alpha*x)
        underdamped = lambda x: math.exp(beta*x) * math.cos(omega*x)

        # Creating signals on axes
        combined_signal = axes.plot(overdamped, color=second_color)
        combined_label = VGroup(
            MathTex(r"\text{Which type of system is represented}",color=second_color),
            MathTex(r"\text{by the response on the graph?}",color=second_color),
            MathTex(r"\text{\: a) underdamped system}",color=LIGHT_GRAY),
            MathTex(r"\text{\: b) overdamped system}",color=LIGHT_GRAY),
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