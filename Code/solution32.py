from manim import *
import numpy as np
import math

class Solution32(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY
        third_color = BLUE
        fourth_color = RED
        size_font =  DEFAULT_FONT_SIZE*0.75

        box = Rectangle(
            height=3.6, 
            width=10, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)
        self.play(Create(box))

        question = VGroup(
            MathTex(r"\text{Can a delayed LTI system be BIBO stable?}", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{(i.e. system whose impulse response contains a delay)}", 
                    color=first_color, font_size=size_font)
        ).arrange(DOWN)

        answers = VGroup(
            MathTex(r"\text{A: yes}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{B: no}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{C: it depends}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        VGroup(question[1], answers).arrange(DOWN, center=False, aligned_edge=LEFT)
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
            MathTex(r"\text{As soon as the impulse response of the system is absolutely integrable}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{the corresponding LTI system is BIBO stable.}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{Adding delays does not modify the BIBO nature of the system.}", 
                    color=first_color, font_size=size_font)
        ).arrange(DOWN).move_to(ORIGIN)

        
        # Animating solution
        self.play(Create(solution[0]))
        self.wait(1)
        self.play(Create(solution[1]))
        self.wait(2)
        self.play(Create(solution[2]))
        self.wait(2)
        self.play(solution.animate.to_edge(UP))
        self.wait(1)
        
        #For the graph
        limit_x = [0,3]
        limit_y = [0, 2]
        # Defining axes
        axes = Axes(
            x_range=[limit_x[0], limit_x[1], 1],
            y_range=[limit_y[0], limit_y[1], 1],
            axis_config={"color": second_color},
            y_length = 3.5,
            x_length = 6
        ).to_edge(DOWN)
        axes1 = axes.copy()
        axes1.to_corner(DL).scale(0.8).shift(0.5*RIGHT)
        axes2 = axes.copy()
        axes2.to_corner(DR).scale(0.8).shift(0.5*LEFT)
        labels = axes.get_axis_labels(x_label="t", y_label="h(t)").scale(0.9)

        # Parameters
        delay = 1
        alpha = -2

        # Creating the signals
        def H(t):
            if 0 <= t:
                return math.exp(alpha*(t))
            else:
                return 0
        def H_delay(t):
            if delay <= t:
                return math.exp(alpha*(t-delay))
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
        signal_delay = make_signal_on_axes(H_delay, axes2, fourth_color, limit_x)
        tau = MathTex(r"\tau", font_size = size_font*1.2, color = fourth_color).next_to(axes2, DOWN).shift(1.5*LEFT)
        t1 = MathTex(r"t", font_size = size_font, color = second_color).next_to(axes1, DOWN).shift(2.5*RIGHT)
        t2 = MathTex(r"t", font_size = size_font, color = second_color).next_to(axes2, DOWN).shift(2.5*RIGHT)
        
        equation = VGroup(
            MathTex(r"\int_{-\infty}^{+\infty}",
                    r"|",
                    r"f(t)",
                    r"|",
                    r"\,dt",
                    r"< \infty", 
                    color=second_color, font_size=size_font),
            MathTex(r"\Rightarrow}", 
                    color=first_color, font_size=size_font),
            MathTex(r"\int_{-\infty}^{+\infty}"
                    ,r"|",
                    r"f(t-\tau)",
                    r"|",
                    r"\,dt",
                    r"< \infty", 
                    color=second_color, font_size=size_font)
        ).arrange(RIGHT, buff = 1).next_to(VGroup(axes1,axes2), UP).shift(0.2*UP)
        equation[0][2].set_color(third_color)
        equation[2][2].set_color(fourth_color)
        
        #Animation of the function
        self.play(FadeIn(axes1), FadeIn(axes2),FadeIn(t1),FadeIn(t2))
        self.wait(0.5)
        self.play(
            FadeIn(equation[0][2]),
            ChangeSpeed(
                Create(signal),
                speedinfo={0: 0.8},
                rate_func=linear,
            )
        )
        self.wait(1)
        self.play(
            FadeIn(equation[2][2]),
            ChangeSpeed(
                Create(signal_delay),
                speedinfo={0: 0.8},
                rate_func=linear,
            )
        )
        self.play(FadeIn(tau))
        self.wait(3)
        self.play(Create(equation[0][0]), Create(equation[0][1]))
        self.play(Create(equation[0][3]), Create(equation[0][4]))
        self.wait(0.5)
        self.play(Create(equation[0][5]))
        self.wait(0.2)
        self.play(FadeIn(equation[1]))
        self.wait(0.2)
        self.play(Create(equation[2][0]), Create(equation[2][1]))
        self.play(Create(equation[2][3]), Create(equation[2][4]))
        self.wait(0.5)
        self.play(Create(equation[2][5]))
        self.wait(1)
        self.play(FadeOut(axes1,t1,t2,axes2, equation, signal,signal_delay,solution,tau))
        

        