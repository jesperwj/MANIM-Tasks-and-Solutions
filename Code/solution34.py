from manim import *
import numpy as np
import math

class Solution34(Scene):
    def construct(self):

        # Color scheme set up
        first_color = WHITE
        second_color = LIGHT_GRAY

        #Poles colors 
        third_color = YELLOW
        fourth_color = BLUE
        fifth_color = RED

        size_font =  DEFAULT_FONT_SIZE*0.75

        box = Rectangle(
            height=3.6, 
            width=10.5, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color)

        question = VGroup(
            MathTex(r"\text{Can a LTI system whose transfer function has some poles}", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{on the imaginary axis, be BIBO stable?}", 
                    color=first_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)

        answers = VGroup(
            MathTex(r"\text{A: yes}", 
                    color=second_color, font_size=size_font*0.9),
            MathTex(r"\text{B: no}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{C: it depends}", 
                    color=second_color, font_size=size_font)
        ).arrange(DOWN, center=False, aligned_edge=LEFT)
        
        VGroup(question[1], answers).arrange(DOWN, center=False, aligned_edge=LEFT)
        answers.shift(RIGHT)
        VGroup(question, answers).move_to(ORIGIN)

        
        # Animation question
        self.play(Create(box))
        self.play(FadeIn(question, answers))
        self.wait(4)

        # Animating the correct answer indication 
        self.play(Indicate(answers[1], color = first_color))
        self.wait(0.5)
        self.play(Indicate(answers[1], color = first_color))
        self.wait(2)
        self.play(FadeOut(question, answers, box))
        self.wait(1)
        
        # Solution part -----------------------------------------------------------------
        size_font = DEFAULT_FONT_SIZE*0.85

        #For the graph
        limit_x1 = [-1.8,2]
        limit_y1 = [-1.8, 2]

        limit_x2 = [0, 4.6]
        limit_y2 = [-2.5, 2.5]

        # Defining axes
        axes1 = Axes(
            x_range=[limit_x1[0], limit_x1[1], 5],
            y_range=[limit_y1[0], limit_y1[1], 5],
            axis_config={"color": second_color},
            y_length = 3.5,
            x_length = 3.5
        )
        axes2 = Axes(
            x_range=[limit_x2[0], limit_x2[1], 1],
            y_range=[limit_y2[0], limit_y2[1], 1],
            axis_config={"color": second_color,"include_ticks": False},
            y_length = 3.5,
            x_length = 4
        ).set_z_index(1)
        labels1 = axes1.get_axis_labels(x_label=r"\text{Re[s]}", y_label=r"\text{Im[s]}").set_color(second_color).scale(0.9)
        labels2 = axes2.get_axis_labels(x_label="t", y_label="h(t)").set_color(second_color).scale(0.9)

        #Titles 
        title1 = MathTex(r"\text{Pole placement in s-domain}", 
                    color=second_color, font_size=size_font*1.1).next_to(axes1, UP).shift(0.7*UP)
        title2 = MathTex(r"\text{Impulse response}", 
                    color=second_color, font_size=size_font*1.1).next_to(axes2, UP).shift(0.7*UP)
        
        # Setting up the right position of the axis
        axes1_with_labels = VGroup(axes1, labels1, title1).scale(0.69)
        axes2_with_labels = VGroup(axes2, labels2, title2).scale(0.69)
        VGroup(axes1_with_labels,axes2_with_labels).arrange(DOWN, buff = 0.5).to_edge(LEFT)
        
        # Drawing poles and their impulse responses
        omega = 5
        alpha = -1
        beta = 0.2

        pole1 = Dot(point = axes1.c2p(0,1), 
                    radius = DEFAULT_DOT_RADIUS*1.5, 
                    color=third_color)
        signal1 = lambda x: math.cos(omega*x)
        impulse_response1 = axes2.plot(signal1, color=third_color).set_z_index(-1)

        # Copies for animation
        pole11 = pole1.copy()
        pole111 = pole1.copy()
        impulse_response11 = impulse_response1.copy()
        impulse_response111 = impulse_response1.copy()

        pole2 = Dot(point = axes1.c2p(-1,1), 
                    radius = DEFAULT_DOT_RADIUS*1.5, 
                    color=fourth_color)
        signal2 = lambda x: math.exp(alpha*x)*math.cos(omega*x)
        impulse_response2 = axes2.plot(signal2, color=fourth_color).set_z_index(-1)

        pole3 = Dot(point = axes1.c2p(1,1), 
                    radius = DEFAULT_DOT_RADIUS*1.5, 
                    color=fifth_color)
        signal3 = lambda x: math.exp(beta*x)*math.cos(omega*x)
        impulse_response3 = axes2.plot(signal3, color=fifth_color).set_z_index(-1)

        # Solution text
        solution = VGroup(
            MathTex(r"\text{If the transfer function has some of the poles}", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{on the imaginary axis, impulse response }h(t)", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{has a non-decaying sinusoidal component:}", 
                    color=second_color, font_size=size_font),
            MathTex(r"h(t) = \theta \cos(\omega t + \phi)", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{for opportune parameters } \theta,\text{ } \omega\text{ and } \phi.", 
                    color=second_color, font_size=size_font),
            MathTex(r"\text{Impulse response is not absolutely integrable.}", 
                    color=first_color, font_size=size_font),
            MathTex(r"\Rightarrow \text{not BIBO stable!}", 
                    color=first_color, font_size=size_font),
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff = 0.4).to_corner(UR)
        solution[3:].shift(DOWN*0.3)
        solution[3].shift(2*RIGHT)
        solution[4:].shift(DOWN*0.1)
        solution[5:].shift(DOWN*0.6)
        solution[6].shift(RIGHT)

        # Animating solution
        self.play(FadeIn(axes1_with_labels), FadeIn(axes2_with_labels))
        self.play(FadeIn(pole1))
        self.wait(0.5)
        self.play(
            ChangeSpeed(
                Create(impulse_response1),
                speedinfo={0: 0.5},
                rate_func=linear,
            )
        )
        self.wait(1)

        # Animating shift between poles
        self.play(ReplacementTransform(pole1, pole2),
                  ReplacementTransform(impulse_response1, impulse_response2))
        self.wait(1)

        self.play(ReplacementTransform(pole2, pole11),
                  ReplacementTransform(impulse_response2, impulse_response11))
        self.wait(1)

        self.play(ReplacementTransform(pole11, pole3),
                  ReplacementTransform(impulse_response11, impulse_response3))
        self.wait(1)

        self.play(ReplacementTransform(pole3, pole111),
                  ReplacementTransform(impulse_response3, impulse_response111))
        self.wait(2)

        # Animating text of the solution text

        self.play(Write(solution[0]))
        self.wait(1)
        self.play(Create(solution[1]))
        self.wait(0.8)
        self.play(Create(solution[2]))
        self.wait(3)
        self.play(Create(solution[3]))
        self.wait(2)
        self.play(Create(solution[4]))
        self.wait(3)
        self.play(Create(solution[5]))
        self.wait(2)
        self.play(Create(solution[6]))
        self.wait(4)

        self.play(FadeOut(axes1_with_labels,
                          axes2_with_labels,
                          pole111,
                          impulse_response111,
                          solution))





