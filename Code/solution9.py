from manim import *
import numpy as np
import math

class Solution9(Scene):
    def construct(self):

        # Defining axes
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 2.5, 1],
            axis_config={"color": LIGHT_GRAY},
            y_length = 4,
            x_length = 5
        )
        axes1 = axes.copy()
        axes1.move_to(0.5*DOWN+ 3*LEFT).scale(0.9)
        axes2 = axes.copy()
        axes2.move_to(0.5*DOWN+ 3*RIGHT).scale(0.9)
        
        label1 = axes1.get_axis_labels(x_label="t", y_label="u").set_color(LIGHT_GRAY).scale(0.9)
        label2 = axes2.get_axis_labels(x_label="t", y_label="y").set_color(LIGHT_GRAY).scale(0.9)

        # Parameters
        x = [0, 0, 1, 2, 2, 3]
        u1 = [0, 1, 1, 1, 0, 0]
        u2 = [0, 2, 2, 2, 0, 0]
        y1 = [0, 0, 1, 0, 0, 0]
        y2 = [0, 0, 1.5, 0, 0, 0]
        y3 = [0, 0, 2, 0, 0, 0]

        # Creating signals on axes
        def get_lines(x, y, axes, color):
            adjusted_signal = [axes.c2p(x[i], y[i]) for i in range(len(x))]
            lines = [Line(start=adjusted_signal[i], end=adjusted_signal[i + 1], color=color) for i in range(len(adjusted_signal) - 1)]
            return lines

        # Getting lines of the signal: 0 1 2 3 
        input1 =  get_lines(x, u1, axes1, color = YELLOW)
        output1 =  get_lines(x, y1, axes2, color = YELLOW)
        input2 =  get_lines(x, u2, axes1, color = GREEN)
        output2 =  get_lines(x, y2, axes2, color = PURPLE)
        output_lti = get_lines(x, y3, axes2, color = GREEN)

        marker1 = MathTex("u1", color = YELLOW).next_to(input1[4])
        marker2 = MathTex("y1", color = YELLOW).next_to(output1[4])
        marker3 = MathTex("u2", color = YELLOW).next_to(input2[4])
        marker4 = MathTex("y2", color = YELLOW).next_to(output2[4])
        marker5 = MathTex("y", color = YELLOW).next_to(output_lti[4])


        # Solution
        solution = VGroup(
            MathTex(r"\text{For any LTI system, superposition principle has to be satisfied.}",color=LIGHT_GRAY),
            MathTex(r"\text{In this case, it is not.}",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(3*UP).scale(0.8)
        
        self.play(Write(solution[0]))
        self.wait(1)
        self.play(Write(solution[1]))
        self.wait(1)       

        self.play(FadeOut(solution))

        solution2 = VGroup(
            MathTex(r"\text{By the superposition principle, if an input } u_1 \text{ produces an output } y_1\text{,}",color=LIGHT_GRAY),
            MathTex(r"\text{the response on } u_2 =u_1 + u_1 = 2\cdot u_1\text{ must be }  y_1 + y_1 = 2 \cdot y_1.",color=LIGHT_GRAY),
             MathTex(r"\text{However, the produced output is } y_2 = 1.5 \cdot y_1.",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(3*UP).scale(0.8)
        # Animating the creation of axes and lines
        self.play(
            Create(axes1), 
            Write(label1), 
            Create(axes2), 
            Write(label2))
        self.wait(1)
        self.play(Write(solution2[0]))
        self.wait(1)
        for i in range(0, 5):
            self.play(
                Create(input1[i]), 
                Create(output1[i]), 
                runtime = 0.1)
        self.wait(0.5)

        self.play(Write(solution2[1]))
        self.wait(1)
        for i in range(0, 5):
            self.play(
                Create(input2[i]), 
                Create(output_lti[i]),
                runtime = 0.1)
        self.wait(5)

        self.play(Write(solution2[2]))
        self.wait(1)
        for i in range(0, 5):
            self.play(
                Create(output2[i]),
                runtime = 0.1)
        self.wait(5)



