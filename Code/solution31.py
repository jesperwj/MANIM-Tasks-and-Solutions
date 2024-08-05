from manim import *
import numpy as np
import math

class Solution31(Scene):
    def construct(self):

        # Color scheme set up
        first_color = LIGHT_GRAY
        second_color = LIGHT_BROWN
        third_color = BLUE

        #For the graph
        limit_x = [-1.2, 5.2]
        limit_y = [-0.2, 2.8]
        # Defining axes
        axes = Axes(
            x_range=[limit_x[0], limit_x[1], 1],
            y_range=[limit_y[0], limit_y[1], 1],
            axis_config={"color": first_color, "include_numbers": True},
            y_length = 3.5,
            x_length = 6

        )
        axes1 = axes.copy().scale(0.8)
        axes1.to_corner(UR)
        axes2 = axes.copy().scale(0.8)
        axes2.to_corner(DR).shift(0.1*UP)
        
        label1 = axes1.get_axis_labels(x_label="t", y_label="h(t)").set_color(second_color).scale(0.9)
        label2 = axes2.get_axis_labels(x_label="t", y_label="u(t)").set_color(third_color).scale(0.9)

        # Functions
        def H(t):
            if 0 <= t <= 2:
                return -t + 2
            else:
                return 0
            
        def U(t):
            if 0 <= t <= 1:
                return t
            elif 1 < t <= 3:
                return 1
            elif 3 < t <= 4:
                return -(t-3) + 1
            else:
                return 0
            
         # High resolution
        num_points = 1000
        t_values = np.linspace(limit_x[0], limit_x[1], num=num_points)

        # Generate points for each function
        h_values = np.array([H(t) for t in t_values])
        u_values = np.array([U(t) for t in t_values])

        # Create lines manually
        graph_h = VMobject()
        graph_u = VMobject()
        
        # Smooth lines for H(t)
        points_h = [axes1.c2p(t_values[i], h_values[i]) for i in range(num_points)]
        graph_h.set_points_as_corners(points_h)
        graph_h.set_color(second_color)
        
        # Smooth lines for U(t)
        points_u = [axes2.c2p(t_values[i], u_values[i]) for i in range(num_points)]
        graph_u.set_points_as_corners(points_u)
        graph_u.set_color(third_color)

        # Animation of the question
        size_font =  DEFAULT_FONT_SIZE*0.75
        
        answers = VGroup(
            MathTex(r"\text{A:  1 }", color=first_color, font_size=size_font),
            MathTex(r"\text{B:  } \frac{1}{6} ", color=first_color, font_size=size_font),
            MathTex(r"\text{C:  6 }", color=first_color, font_size=size_font)
        ).arrange(RIGHT, buff=1.8)

        question = VGroup(
            MathTex(r"\text{Consider a continuous-time LTI system with }", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{the following characteristics: }", 
                    color=first_color, font_size=size_font),
            MathTex(r"h(t) = \begin{cases} -t + 2 & \text{for } 0 \leq t \leq 2 \\ 0 & \text{otherwise} \end{cases} ", 
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"u(t) = \begin{cases} t & \text{for } 0 \leq t \leq 1 \\ 1 & \text{for } 1 < t \leq 3 \\ -(t-3) + 1 & \text{for } 3 < t \leq 4 \\ 0 & \text{otherwise} \end{cases} ", 
                    color=third_color, font_size=size_font*0.9),
            MathTex(r"\text{The forced response of the system at } t = 5 \text{ is: }", color=first_color, font_size=size_font),
            answers
        ).arrange(DOWN, center=False, aligned_edge=LEFT).to_corner(UP + LEFT)

        #Setting up text
        VGroup(question[5:]).shift(RIGHT)
        VGroup(question[2:]).shift(0.3*DOWN)
        VGroup(question[3:]).shift(0.4*DOWN)
        VGroup(question[4:]).shift(0.3*DOWN)
        VGroup(question[2]).shift(RIGHT)
        VGroup(question[3]).shift(RIGHT)
        
        self.play(AddTextWordByWord(question[0]))
        self.play(AddTextWordByWord(question[1]))
        self.wait(0.5)
        self.play(FadeIn(axes1,label1), FadeIn(axes2,label2))
        self.wait(1)
        self.play(AddTextWordByWord(question[2]))
        self.wait(1)
        self.play(
            ChangeSpeed(
                Create(graph_h),
                speedinfo={0: 0.3},
                rate_func=linear,
            )
        )
        self.wait(2)
        self.play(AddTextWordByWord(question[3]))
        self.wait(1)
        self.play(
            ChangeSpeed(
                Create(graph_u),
                speedinfo={0: 0.3},
                rate_func=linear,
            )
        )
        self.wait(3)
        self.play(AddTextWordByWord(question[4]))
        self.wait(1)
        self.play(Create(question[5][0]))
        self.wait(0.5)
        self.play(Create(question[5][1]))
        self.wait(0.5)
        self.play(Create(question[5][2]))
        self.wait(3)
        self.play(question[5][1].animate.set_color(YELLOW))
        self.wait(0.1)
        self.play(question[5][1].animate.set_color(first_color))
        self.wait(0.1)
        self.play(question[5][1].animate.set_color(YELLOW))
        self.wait(2)

        self.play(FadeOut(
            question,
            axes1,
            axes2,
            graph_h,
            graph_u,
            label1,
            label2
        ))
        
        # Solution part

        forced_response = VGroup(
            MathTex(r"\text{For a continuous time system, forced response } y_f(t)\text{ is the convolution }", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{of the impulse response } h(t) \text{ and the input signal } u(t)\text{:} }", 
                    color=first_color, font_size=size_font),
            MathTex(r"y_f(t) = h * u(t) = \int_{-\infty}^{\infty} h(\tau) \cdot u(t - \tau) \, d\tau", 
                    color=WHITE, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).to_edge(UP).shift(DOWN)
        forced_response[2].shift(2*RIGHT+0.5*DOWN)

        # Setting up the text
        forced_response[2][0][6].set_color(second_color)
        forced_response[2][0][8].set_color(third_color)
        forced_response[2][0][17:21].set_color(second_color)
        forced_response[2][0][22:28].set_color(third_color)

        five1 = MathTex(r"5", color=WHITE, font_size=size_font).move_to(forced_response[2][0][3])
        t_five = MathTex(r"5",color=WHITE, font_size=size_font).move_to(forced_response[2][0][10])
        five2 = MathTex(r"5", color=third_color, font_size=size_font).move_to(forced_response[2][0][24])
        
        # Animation
        self.play(Create(forced_response[0]))
        self.wait(0.5)
        self.play(Create(forced_response[1]))
        self.wait(0.5)
        self.play(Create(forced_response[2]))
        self.wait(0.5)
        self.play(Transform(forced_response[2][0][3], five1))
        self.play(Transform(forced_response[2][0][10], t_five))
        self.play(Transform(forced_response[2][0][24], five2))
        self.wait(2)
        self.play(FadeOut(forced_response[0:2]))
        self.play(forced_response[2].animate.shift(2*UP+2*LEFT))
        self.wait(2)

        self.play(FadeIn(axes1,label1), FadeIn(axes2,label2))
        self.wait(1)
        self.play(
            ChangeSpeed(
                AnimationGroup(
                    Create(graph_u),
                    Create(graph_h)),
                speedinfo={0: 0.3},
                rate_func=linear,
            )
        )



        