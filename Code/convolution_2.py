from manim import *
import numpy as np
import math
from scipy.integrate import quad
from pydub import AudioSegment

class Convolution2(Scene):
    def construct(self):
        # =========================== Setup ===================================
        self.setup_audio()
        self.setup_constants()
        axes1, axes2, axes3 = self.create_axes()
        labels = self.create_labels()
        title = self.create_title()

        # =========================== Signals =================================
        function1 = self.signal_cosine
        function2 = self.signal_cosine
        function2_flipped = self.flip_signal(function2)
        
        x_values, y_values = self.calculate_convolution(function1, function2, self.limit_x_conv)
        function_convolution = lambda t: np.interp(t, x_values, y_values)

        # =========================== Graphs ==================================
        time_tracker = ValueTracker(-2)
        function1_graph = self.create_graph(function1, axes1, self.colors["function1"])
        function2_graph = self.create_dynamic_graph(function2_flipped, axes1, time_tracker)
        product_graph = self.create_product_graph(function1, function2_flipped, axes2, time_tracker)
        conv_graph = self.create_convolution_graph(function_convolution, axes3, x_values, time_tracker)

        shaded_area = self.create_shaded_area(axes2, product_graph, time_tracker).set_z_index(-1)

        # =========================== Scene ===================================
        self.add(axes1, axes2, axes3, labels, title)
        self.add(function1_graph, function2_graph, product_graph, conv_graph, shaded_area)
        self.play(time_tracker.animate.set_value(self.limit_x[1]), run_time=15, rate_func=linear)
        self.wait(2)

    # =========================== Helper Methods ============================
    def setup_audio(self):
        audio_path = "music/convo.mp3"
        trimmed_audio_path = "music/trimmed_fadeout_manim_song.mp3"
        duration = 20 * 1000
        fade_out_duration = 2 * 1000
        music_volume = 0.7

        audio_segment = AudioSegment.from_file(audio_path)
        trimmed_audio = audio_segment[:duration].fade_out(fade_out_duration)
        trimmed_audio.export(trimmed_audio_path, format="mp3")
        self.add_sound(trimmed_audio_path, time_offset=0, gain=music_volume)

    def setup_constants(self):
        self.colors = {
            "axes": GRAY_C,
            "function1": GREEN,
            "function2": BLUE,
            "product": PINK,
            "convolution": ORANGE,
            "shaded": ORANGE,
        }
        self.font_size = DEFAULT_FONT_SIZE * 0.68
        self.limit_x = [-5, 5]
        self.limit_y = [-2, 2]

        # Convolution: sometimes gets too big, might want to adjust
        self.limit_x_conv= [-5, 5]
        self.limit_y_conv = [-3, 3]


    def create_axes(self):
        axes_config = {"color": self.colors["axes"], "include_ticks": True}
        axes1 = Axes([self.limit_x[0], self.limit_x[1],0.25], [self.limit_y[0], self.limit_y[1] + 1, 1], 
                     axis_config=axes_config, x_length=14, y_length=2.85, tips = False).to_edge(UP, buff=0)
        axes2 = Axes([self.limit_x[0], self.limit_x[1],0.25], self.limit_y, 
                     axis_config=axes_config, x_length=14, y_length=2.28,tips = False).next_to(axes1, DOWN, buff=0)
        axes3 = Axes([self.limit_x_conv[0], self.limit_x_conv[1],0.25], [self.limit_y_conv[0], self.limit_y_conv[1], 1], 
                     axis_config=axes_config, x_length=14, y_length=2.85,tips = False).next_to(axes2, DOWN, buff=0)
        return axes1, axes2, axes3

    def create_labels(self):
        label1 = VGroup(
            MathTex(r"u(t)", 
                    color=self.colors["function1"], font_size=self.font_size),
            MathTex(r"h(-t+\tau)",
                    color=self.colors["function2"], font_size=self.font_size)
            ).arrange(LEFT, center=False, buff = 6)
        labels = VGroup(
            label1,
            MathTex(r"\text{Product:  } u(t) \cdot h(-t+\tau)", 
                    color=self.colors["product"], font_size=self.font_size),
            MathTex(r"\text{Convolution:  }y(t) = \int_{-\infty}^\infty u(\tau) h(t - \tau) \, d\tau", 
                    color=self.colors["convolution"], font_size=self.font_size)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff=2).to_corner(UL,buff=0.7)
        labels[2].shift(0.2*UP)
        labels.shift(1.75*DOWN)
        return labels
    
    def create_title(self):
        title_text = MathTex(r"\text{Convolution Visualization}", 
                             color=WHITE, font_size=self.font_size*1.2).set_z_index(2)
        underline = Underline(title_text, color=self.colors["axes"]).set_stroke(width=2).set_z_index(2)
        title_box = Rectangle(
            width=title_text.width + 0.4,  
            height=title_text.height + 0.27,
            color=BLACK,  
            fill_color=BLACK,  
            fill_opacity=1  
        ).move_to(title_text.get_center()).set_z_index(1)  
        title = VGroup(title_box,underline,title_text).to_edge(UP, buff = 0)
        self.add(title)
        return title

    # =========================== Signal Functions ===========================
    def signal_cosine(self, t):
        return math.cos(5 * t) if t >= 0 else 0

    def signal_exp_decay(self, t):
        return math.exp(-0.5 * t) if t >= 0 else 0

    def signal_rect(self, t):
        return 1 if 0 <= t <= 1 else 0

    def signal_sine(self, t):
        return math.sin(5 * t) if t >= 0 else 0

    def signal_triangular(self, t):
        return 1 - abs(t) if -1 <= t <= 1 else 0

    # =========================== Utility Methods ============================
    def flip_signal(self, func):
        return lambda t: func(-t)

    def create_graph(self, function, axes, color):
        num_points = 1000
        t_values = np.linspace(self.limit_x[0], self.limit_x[1], num=num_points)
        signal_values = np.array([function(t) for t in t_values])
        graph = VMobject()
        points = [axes.c2p(t_values[i], signal_values[i]) for i in range(num_points)]
        graph.set_points_as_corners(points)
        graph.set_color(color)
        return graph

    def create_dynamic_graph(self, func, axes, tracker):
        graph = VMobject(color=self.colors["function2"])
        graph.add_updater(lambda m: self.update_function2_graph(m, func, axes, tracker.get_value()))
        return graph

    def create_product_graph(self, func1, func2_flipped, axes, tracker):
        return always_redraw(lambda: axes.plot(
            lambda t: func1(t) * func2_flipped(t - tracker.get_value()),
            x_range=self.limit_x,
            color=self.colors["product"],
            use_smoothing=False
        ))

    def create_convolution_graph(self, func, axes, x_values, tracker):
        graph = VMobject(color=self.colors["convolution"])
        graph.add_updater(lambda m: self.update_convolution_graph(m, func, axes, x_values, tracker.get_value()))
        return graph

    def create_shaded_area(self, axes, graph, tracker):
        return always_redraw(lambda: axes.get_area(
            graph, x_range=[self.limit_x[0], 
            tracker.get_value()], 
            color=self.colors["shaded"], 
            opacity=0.5))

    def update_function2_graph(self, graph, func, axes, tau_value):
        t_values = np.linspace(self.limit_x[0], self.limit_x[1], 1000)
        points = [axes.c2p(t, func(t - tau_value)) for t in t_values]
        graph.set_points_as_corners(points)

    def update_convolution_graph(self, graph, func, axes, x_values, tau):
        points = [axes.c2p(x, func(x)) for x in x_values if x < tau]
        if points:  
            graph.set_points_as_corners(points)

    def calculate_convolution(self, func1, func2, limit_x):
        x_values = np.linspace(limit_x[0], limit_x[1], 1000)
        y_values = [quad(lambda x: func1(t - x) * func2(x), limit_x[0], limit_x[1])[0] for t in x_values]
        return x_values, y_values
