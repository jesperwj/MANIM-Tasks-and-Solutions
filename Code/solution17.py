from manim import *

class Solution17(Scene):
    def construct(self):

        # To change the whole color scheme easier
        first_color = LIGHT_GRAY
        second_color = BLUE
        dot_color = WHITE

        # Defining axes
        axes = Axes(
            x_range=[-3, 5, 1],
            y_range=[-5, 20, 5],
            axis_config={"color": first_color, "include_numbers": True},
            y_length = 6,
            x_length = 8
        ).move_to(1.5*DOWN).scale(0.7)
        labels = axes.get_axis_labels(x_label="t", y_label=r"\dot{x}").scale(0.9)

        function  = lambda x: x*x-2*x-3
        signal = axes.plot(function, color=second_color)

        dot1 = Dot(point = axes.c2p(-1,0), radius = DEFAULT_DOT_RADIUS*1.5, color=dot_color)
        dot2 = Dot(point = axes.c2p(3,0), radius = DEFAULT_DOT_RADIUS*1.5, color=dot_color)
        # Create the question and answer choices as a VGroup
        solution = VGroup(
            MathTex(r"\text{The equilibria of the system }", color = first_color),
            MathTex(r"\dot{x}=x^2-2x-3",color=second_color),
            MathTex(r"\text{are both -1 and 3.}", color=first_color)
        ).arrange(DOWN).scale(0.8)

        # Animating the question
        self.play(Write(solution[0]))
        self.wait(0.5)
        self.play(Write(solution[1]))
        self.wait(0.5)
        self.play(Write(solution[2]))
        self.wait(3)
        self.play(FadeOut(solution[0],solution[2]))
        
        # Create the question and answer choices as a VGroup
        solution1 = VGroup(
            MathTex(r"\text{Equilibria are all the zeros of the first derivative.}", color = first_color),
            MathTex(r"\dot{x}=x^2-2x-3",color=second_color),
            MathTex(r"\text{thus both 3 and -1 are the equilibria.}", color=first_color)
        ).arrange(DOWN).shift(2.5*UP).scale(0.8)

        # Create the question and answer choices as a VGroup
        solution2 = VGroup(
            MathTex(r"\text{Equilibria are all the zeros of the first derivative.}", color = first_color),
            MathTex(r"\dot{x}=(x+1)(x-3)",color=second_color),
            MathTex(r"\text{thus both 3 and -1 are the equilibria.}", color=first_color)
        ).arrange(DOWN).shift(2.5*UP).scale(0.8)

        # Animating the question
        
        self.play(solution[1].animate.move_to(solution1[1]))
        self.play(Create(axes), Write(labels))
        self.wait
        self.play(Write(solution1[0]))
        self.wait(0.5)
        self.play(Write(signal))
        self.play(ReplacementTransform(solution[1], solution2[1]))
        self.wait(1)
        self.play(Write(solution1[2]), FadeIn(dot1), FadeIn(dot2))
        self.wait(4)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

