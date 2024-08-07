from manim import *
import numpy as np
import math

class Solution33(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        fourth_color = RED
        size_font =  DEFAULT_FONT_SIZE*0.75

        box = Rectangle(
            height=3, 
            width=8.5, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)
        self.play(Create(box))

        question = MathTex(r"\text{Can a non-causal LTI system be BIBO stable?}", 
                    color=first_color, font_size=size_font)
        answers = VGroup(
            MathTex(r"\text{A: yes}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{B: no}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{C: it depends}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        VGroup(question, answers).arrange(DOWN, center=False, aligned_edge=LEFT)
        answers.shift(RIGHT)
        VGroup(question, answers).move_to(ORIGIN)

        #Animation question
        self.play(FadeIn(question))
        self.wait(0.5)
        self.play(FadeIn(answers[0]))
        self.wait(0.5)
        self.play(FadeIn(answers[1]))
        self.wait(0.5)
        self.play(FadeIn(answers[2]))
        self.wait(2)
        self.play(Indicate(answers[0], color = first_color))
        self.wait(0.5)
        self.play(Indicate(answers[0], color = first_color))
        self.wait(2)
        self.play(FadeOut(question, answers, box))
        self.wait(0.5)

        # Solution part -----------------------------------------------------------------
        size_font = DEFAULT_FONT_SIZE*0.85
        solution = VGroup(
            MathTex(r"\text{As soon as the impulse response of the system is absolutely}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{integrable the corresponding LTI system is BIBO stable.}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{The fact that there is some non-causal phenomenon does not}", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{necessarily imply a specific BIBO nature of the system.}", 
                    color=first_color, font_size=size_font)
        ).arrange(DOWN).move_to(ORIGIN)

        
        # Animating solution
        self.play(Create(solution[0]))
        self.wait(0.5)
        self.play(Create(solution[1]))
        self.wait(3)
        self.play(Create(solution[2]))
        self.wait(0.5)
        self.play(Create(solution[3]))
        self.wait(3)
        self.play(Uncreate(solution))
        self.wait(1)

        solution1 = VGroup(
            MathTex(r"\text{Example of a function that is non-causal and}", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{absolutely integrable in the same time:}", 
                    color=first_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge = LEFT).to_edge(UP).shift(0.8*DOWN)
        
        #For the graph
        limit_x = [-3,3]
        limit_y = [0, 2]
        # Defining axes
        axes = Axes(
            x_range=[limit_x[0], limit_x[1], 1],
            y_range=[limit_y[0], limit_y[1], 1],
            axis_config={"color": second_color,"include_numbers": True},
            y_length = 3.5,
            x_length = 6
        ).to_edge(DOWN)
        axes1 = axes.copy()
        axes1.to_corner(DL).scale(0.8).shift(0.5*RIGHT+0.5*UP)
        labels = axes.get_axis_labels(x_label="t", y_label="h(t)").scale(0.9)

        # Creating the signals
        def H(t):
            if abs(t) < 1/2:
                return 1
            else:
                return 0
            
        def make_signal_on_axes(function,axes_name,color, limit_x):
            num_points = 1000
            t_values = np.linspace(limit_x[0], limit_x[1], num=num_points)

            # Generate points for each function
            signal_values = np.array([function(t) for t in t_values])
            graph = VMobject()
            points = [axes_name.c2p(t_values[i], signal_values[i]) for i in range(num_points)]
            graph.set_points_as_corners(points)
            graph.set_color(color)

            return graph
        
        signal = make_signal_on_axes(H, axes1, third_color, limit_x)
        t1 = MathTex(r"t", font_size = size_font, color = second_color).next_to(axes1, DOWN).shift(2.5*RIGHT)
        
        equation = VGroup(
            MathTex(r"h(t)",
                    r" = \begin{cases} 1 & \text{for } -\frac{1}{2} \leq t \leq \frac{1}{2} \\ 0 & \text{otherwise} \end{cases} ", 
                    color=second_color, font_size=size_font),
            MathTex(r" \text{and } \int_{-\infty}^{+\infty}",
                    r"|",
                    r"h(t)",
                    r"|",
                    r"\,dt",
                    r"< \infty", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN).next_to(axes1, RIGHT)
        equation[0][0].set_color(third_color)
        equation[1][2].set_color(third_color)
        
        #Animation of the function
        self.play(Create(solution1[0]))
        self.wait(0.5)
        self.play(Create(solution1[1]))
        self.wait(2)
        self.play(FadeIn(equation[0]))
        self.wait(1)
        self.play(FadeIn(axes1),FadeIn(t1))
        self.wait(0.5)
        self.play(
            ChangeSpeed(
                Create(signal),
                speedinfo={0: 0.5},
                rate_func=linear,
            )
        )
        self.wait(1)
        self.wait(2)
        self.play(Create(equation[1]))
        self.wait(4)

        self.play(FadeOut(axes1,t1, equation, signal,solution1))
        

        