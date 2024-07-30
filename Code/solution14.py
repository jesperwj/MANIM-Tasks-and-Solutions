from manim import *
import numpy as np
import math

class Solution14(Scene):
    def construct(self):
        # Defining axes
        axes = Axes(
            x_range=[0, 3, 5],
            y_range=[0, 1.2, 5],
            axis_config={"color": LIGHT_GRAY},
            y_length = 6,
            x_length = 10
        ).move_to(1.5*LEFT+0.1*DOWN).scale(0.8)
        labels = axes.get_axis_labels(x_label="t", y_label="y(t)").scale(0.9)

        # Parameters and functions
        alpha = -2
        beta = -2
        omega = 5
        
        overdamped = lambda x: math.exp(alpha*x)
        underdamped = lambda x: math.exp(beta*x) * math.cos(omega*x)
        
        # Creating signals on axes
        overdamped_signal = axes.plot(overdamped, color=PURPLE)
        underdamped_signal = axes.plot(underdamped, color=PURPLE)
        underdamped_label = VGroup(
            MathTex(r"\text{By observing the shape of the response,}",color=LIGHT_GRAY),
            MathTex(r"\text{we can conclude that it is underdamped.}",color=LIGHT_GRAY)
        ).arrange(DOWN).move_to(1.8*RIGHT+1.5*UP).scale(0.90)
        
        # Animating combined signal first
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Create(underdamped_signal))
        self.play(FadeIn(underdamped_label[0]), runtime = 0.5)
        self.play(FadeIn(underdamped_label[1]), runtime = 0.5)
        self.wait(3)
        self.play(FadeOut(underdamped_label))
        
        underdamped_label_2 = VGroup(
            MathTex(r"\text{This is clear from the oscilations,}",color=LIGHT_GRAY),
            MathTex(r"\text{which only appear in underdamped systems.}",color=LIGHT_GRAY),
        ).arrange(DOWN).move_to(1.8*RIGHT+1.5*UP).scale(0.90)
        
        self.wait(0.5)
        self.play(FadeIn(underdamped_label_2[0]), runtime = 0.5)
        self.play(FadeIn(underdamped_label_2[1]), runtime = 0.5)
        self.wait(3)
        self.play(underdamped_label_2.animate.shift(UP))
    

        # Part two: Slide between overdamped and underdamped response

        # Create slider bar and knob
        slider_bar = Line(start=[-2.5, 0, 0], end=[2.5, 0, 0], color=LIGHT_GRAY).next_to(underdamped_label_2,DOWN).shift(DOWN)
        slider_knob = Dot(color=PURPLE, radius = DEFAULT_DOT_RADIUS*2).move_to(slider_bar.get_left())
        slider_label1 = MathTex(r"\text{underdamped}", color=PURPLE).move_to(slider_bar.get_left()+DOWN).scale(0.9)
        slider_label2 = MathTex(r"\text{overdamped}", color=LIGHT_GRAY).move_to(slider_bar.get_right()+DOWN).scale(0.9)
        
        self.play(
            Create(slider_bar), 
            Create(slider_knob), 
            Write(slider_label1),
            Write(slider_label2))
        self.wait(2)

        # Added because Replacement Transform wasnt working correctly
        overdamped_signal1 = axes.plot(overdamped, color=PURPLE)
        underdamped_signal1 = axes.plot(underdamped, color=PURPLE)

        self.play(
            ReplacementTransform(underdamped_signal, overdamped_signal),
            slider_knob.animate.move_to(slider_bar.get_right()),
            slider_label1.animate.set_color(LIGHT_GRAY),
            slider_label2.animate.set_color(PURPLE))
        self.wait(2)
        self.play(
            ReplacementTransform(overdamped_signal, underdamped_signal1),
            slider_knob.animate.move_to(slider_bar.get_left()),
            slider_label1.animate.set_color(PURPLE),
            slider_label2.animate.set_color(LIGHT_GRAY))
        self.wait(2)
        self.play(
            ReplacementTransform(underdamped_signal1, overdamped_signal1),
            slider_knob.animate.move_to(slider_bar.get_right()),
            slider_label1.animate.set_color(LIGHT_GRAY),
            slider_label2.animate.set_color(PURPLE))
        self.wait(4)

        self.play(FadeOut(underdamped_label_2, 
                          slider_bar, 
                          slider_knob, 
                          slider_label1, 
                          slider_label2, 
                          axes, 
                          overdamped_signal1,
                          labels))

