from manim import *
import numpy as np
import math

class Question9(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 2.5, 1],
            axis_config={"color": LIGHT_GRAY},
            y_length = 5,
            x_length = 5
        )
        axes1 = axes.copy()
        axes1.move_to(0.5*UP+ 2.5*LEFT).scale(0.40)
        axes2 = axes.copy()
        axes2.move_to(0.5*UP+ 2.5*RIGHT).scale(0.40)
        axes3 = axes.copy()
        axes3.move_to(2.5*DOWN + 2.5*LEFT).scale(0.40)
        axes4 = axes.copy()
        axes4.move_to(2.5*DOWN + 2.5*RIGHT).scale(0.40)
        
        label1 = axes1.get_axis_labels(x_label="t", y_label="u_1").set_color(YELLOW).scale(0.9)
        label2 = axes2.get_axis_labels(x_label="t", y_label="y_1").set_color(YELLOW).scale(0.9)
        label3 = axes3.get_axis_labels(x_label="t", y_label="u_2 = 2 \cdot u_1").set_color(PURPLE).scale(0.9)
        label4 = axes4.get_axis_labels(x_label="t", y_label="y_2 = 1.5\cdot y_1").set_color(PURPLE).scale(0.9)

        # Parameters
        x = [0, 0, 1, 2, 2, 3]
        u1 = [0, 1, 1, 1, 0, 0]
        u2 = [0, 2, 2, 2, 0, 0]
        y1 = [0, 0, 1, 0, 0, 0]
        y2 = [0, 0, 1.5, 0, 0, 0]

        # Creating signals on axes
        def get_lines(x, y, axes, color):
            adjusted_signal = [axes.c2p(x[i], y[i]) for i in range(len(x))]
            lines = [Line(start=adjusted_signal[i], end=adjusted_signal[i + 1], color=color) for i in range(len(adjusted_signal) - 1)]
            return lines

        # Getting lines of the signal: 0 1 2 3 
        input1 =  get_lines(x, u1, axes1, color = YELLOW)
        output1 =  get_lines(x, y1, axes2, color = YELLOW)
        input2 =  get_lines(x, u2, axes3, color = PURPLE)
        output2 =  get_lines(x, y2, axes4, color = PURPLE)


        # Text of the question
        
        # Deductions
        question = VGroup(
            MathTex(r"\text{Based on system responses }y_1\text{ and } y_2\text{ on inputs } u_1 \text{ and }u_2 \text{ respectively,}}",color=LIGHT_GRAY),
            MathTex(r"\text{ starting from null initial conditions, is this dynamical system an LTI one?}",color=LIGHT_GRAY)
        ).arrange(DOWN, center=False, aligned_edge = LEFT).move_to(3*UP).scale(0.8)
        
        self.play(Write(question[0]))
        self.wait(1)
        self.play(Write(question[1]))
        self.wait(1)

        # Animating the creation of axes and lines
        self.play(
            Create(axes1), 
            Write(label1), 
            Create(axes2), 
            Write(label2))
        self.wait(1)
        for i in range(0, 5):
            self.play(
                FadeIn(input1[i]), 
                FadeIn(output1[i]), 
                runtime = 0.1)
        self.wait(0.5)

        self.play(
            Create(axes3),
            Write(label3), 
            Create(axes4),
            Write(label4))
        self.wait(1)
        for i in range(0, 5):
            self.play(
                Create(input2[i]), 
                Create(output2[i]),
                runtime = 0.1)
        self.wait(5)

