from manim import *
import numpy as np
import math

class Solution31(Scene):
    def construct(self):

        # Color scheme set up
        first_color = LIGHT_GRAY
        second_color = LIGHT_BROWN
        third_color = BLUE
        forth_color = GREEN

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

        limit_x1 = [-1.2, 6.5]
        axes3 = Axes(
            x_range=[limit_x1[0], limit_x1[1], 1],
            y_range=[limit_y[0], limit_y[1], 1],
            axis_config={"color": first_color, "include_numbers": True},
            y_length = 5,
            x_length = 10

        )
        
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
        def Yf(t):
            if 0 <= t <= 3:
                return 0
            elif 3 < t <= 4:
                return (t-3)*(4-t)
            else:
                return 0
            
        def H_reversed(t):
            if t <= 3:
                return 0
            elif 3 < t <= 5:
                return (t-3)
            else:
                return 0      
             
        def make_signal_on_axes(function,axes_name,color,limit_x):
            num_points = 1000
            t_values = np.linspace(limit_x[0], limit_x[1], num=num_points)

            # Generate points for each function
            signal_values = np.array([function(t) for t in t_values])
            graph = VMobject()
            points = [axes_name.c2p(t_values[i], signal_values[i]) for i in range(num_points)]
            graph.set_points_as_corners(points)
            graph.set_color(color)

            return graph

        graph_u = make_signal_on_axes(U,axes2,third_color,limit_x)
        graph_h = make_signal_on_axes(H,axes1,second_color,limit_x)

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
        
        self.play(FadeIn(question),
                  FadeIn(axes1),
                  FadeIn(axes2),
                  FadeIn(graph_h),
                  FadeIn(graph_u),
                  FadeIn(label1),
                  FadeIn(label2)
        )

        self.wait(3)
        self.play(question[5][1].animate.scale(1.2),
                  question[5][1].animate.set_color(forth_color))
        self.play(question[5][1].animate.scale(0.8))
        self.play(question[5][1].animate.scale(1.2))
        self.play(question[5][1].animate.scale(0.8))
        self.play(question[5][1].animate.scale(1.2))       
        self.wait(1)

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
            MathTex(r"\text{of the input signal } u(t) \text{ and the impulse response } h(t)\text{:} }", 
                    color=first_color, font_size=size_font),
            MathTex(r"y_f(t) = u * h(t) = \int_{-\infty}^{\infty} u(\tau) \cdot h(t - \tau) \, d\tau", 
                    color=WHITE, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).to_edge(UP).shift(DOWN)
        forced_response[2].shift(2*RIGHT+0.5*DOWN)

        # Setting up the text
        forced_response[2][0][6].set_color(third_color)
        forced_response[2][0][8].set_color(second_color)
        forced_response[2][0][17:21].set_color(third_color)
        forced_response[2][0][22:28].set_color(second_color)

        five1 = MathTex(r"5", color=WHITE, font_size=size_font).move_to(forced_response[2][0][3])
        t_five = MathTex(r"5",color=WHITE, font_size=size_font).move_to(forced_response[2][0][10])
        five2 = MathTex(r"5", color=second_color, font_size=size_font).move_to(forced_response[2][0][24])
        
        # Animation
        self.play(Create(forced_response[0]))
        self.wait(1)
        self.play(Create(forced_response[1]))
        self.wait(2.5)
        self.play(Create(forced_response[2]))
        self.wait(2.5)
        self.play(Transform(forced_response[2][0][3], five1))
        self.play(Transform(forced_response[2][0][10], t_five))
        self.play(Transform(forced_response[2][0][24], five2))
        self.wait(2)
        self.play(FadeOut(forced_response[0:2]))
        
        # Equations
        size_font = size_font*1.1
        equations = VGroup(
            MathTex(r"y_f(5) ", 
                    color=WHITE, font_size=size_font),
            MathTex(r"=\int_{-\infty}^{\infty} u(\tau) \cdot h(5 - \tau) \, d\tau", 
                    color=first_color, font_size=size_font),
            MathTex(r"=\int_{3}^{4} (\tau -3) \cdot (4 - \tau) \, d\tau", 
                    color=first_color, font_size=size_font)
        ).arrange(RIGHT).to_corner(UR)
        equations[1][0][5:9].set_color(third_color)
        equations[1][0][10:16].set_color(second_color)

        equations2 = VGroup(
            equations[2],
            MathTex(r"=\int_{0}^{1} \tau \cdot (1 - \tau) \, d\tau",
                    color=first_color, font_size=size_font),
            MathTex(r"=\left[ \frac{\tau^2}{2} - \frac{\tau^3}{3} \right]_{0}^{1} ",
                    color=first_color, font_size=size_font),
            MathTex(r"=\frac{1}{6} ",
                    color=first_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)

        self.play(ReplacementTransform(forced_response[2],VGroup(equations[0],equations[1])))
        self.wait(2)

        # Showing convolution on a graphs
        # First seperately

        axes1.scale(1.2).to_corner(DL)
        axes2.scale(1.2).to_corner(DR)

        graph_u = make_signal_on_axes(U, axes1, third_color,limit_x)
        graph_h = make_signal_on_axes(H, axes2, second_color,limit_x)
        graph_h_reversed = make_signal_on_axes(H_reversed,axes2,second_color,limit_x)

        label1 = axes1.get_axis_labels(x_label="t", y_label="u(t)").set_color(third_color)
        label2 = axes2.get_axis_labels(x_label="t", y_label="h(t)").set_color(second_color)
        label3 = axes2.get_axis_labels(x_label="t", y_label="h(5-t)").set_color(second_color)
        
        # Animations
        self.play(FadeIn(axes1), FadeIn(label1))
        self.wait(0.5)
        self.play(
            ChangeSpeed(
                Create(graph_u),
                speedinfo={0: 0.3},
                rate_func=linear,
            )
        )
        self.wait(1)
        self.play(FadeIn(axes2), FadeIn(label2))
        self.wait(0.5)
        self.play(
            ChangeSpeed(
                Create(graph_h),
                speedinfo={0: 0.3},
                 rate_func=linear,
           )
        )
        # Showing h(5-t)
        self.wait(1)
        self.play(ReplacementTransform(graph_h,graph_h_reversed),
                  ReplacementTransform(label2, label3))
        self.wait(2.5)

        # New axes
        axes3.scale(0.9).to_corner(DL)
        graph_u1 = make_signal_on_axes(U, axes3, third_color,limit_x1)
        graph_yf = make_signal_on_axes(Yf, axes3, forth_color,limit_x1)
        graph_h_reversed1 = make_signal_on_axes(H_reversed,axes3,second_color,limit_x1)

        x_label =MathTex(r"t", color = first_color).next_to(axes3).shift(2*DOWN)
        u_label =MathTex(r"u(t)", color = third_color).scale(0.8).next_to(axes3,UP).shift(DOWN+2*LEFT)     
        h2_label =MathTex(r"h(5-t)", color = second_color).scale(0.8).next_to(u_label,RIGHT).shift(0.5*RIGHT)
        yf_label =MathTex(r"u(t)\cdot h(5-\tau)", color = forth_color).scale(0.8).next_to(h2_label,RIGHT).shift(0.5*RIGHT)
               
        # Animation
        
        self.play(ReplacementTransform(VGroup(axes1,axes2),axes3),
                  ReplacementTransform(graph_u,graph_u1),
                  ReplacementTransform(graph_h_reversed,graph_h_reversed1),
                  FadeOut(label1,label2,label3),
                  FadeIn(x_label),
                  FadeIn(u_label),
                  FadeIn(h2_label))
        self.wait(1)
        self.play(
            ChangeSpeed(
                Create(graph_yf),
                speedinfo={0: 0.3},
                 rate_func=linear,
           )
        )
        self.play(FadeIn(yf_label))
        self.wait(3.5)

        # Equation solution animation
        self.play(Create(equations[2]))
        self.wait(2)
        self.play(Create(equations2[1]))
        self.wait(2)
        self.play(Create(equations2[2]))
        self.wait(2)
        self.play(Create(equations2[3]))
        self.wait(1)
        self.play(equations2[3].animate.set_color(WHITE))  
        self.wait(3)
        
        

        
        