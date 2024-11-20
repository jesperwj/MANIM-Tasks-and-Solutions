from manim import *
import numpy as np
import math
from scipy.integrate import quad
from pydub import AudioSegment

class convolution(Scene):
    def construct(self):
         #___________________________________________________________________________
        # Music setup 

        # Parameters
        music_volume = 0.7
        audio_path = "music/convo.mp3"
        desired_duration = 19 * 1000  # 10 seconds in milliseconds
        fade_out_duration = 2 * 1000  # 2 seconds fade-out

        # Load and trim the audio to the desired duration, then apply fade-out
        audio_segment = AudioSegment.from_file(audio_path)
        trimmed_audio = audio_segment[:desired_duration].fade_out(fade_out_duration)
        trimmed_audio.export("music/trimmed_fadeout_manim_song.mp3", format="mp3")
        self.add_sound("music/trimmed_fadeout_manim_song.mp3", time_offset=0, gain=music_volume)
        
        # Color scheme set up
        first_color = WHITE
        second_color = GRAY_C

        # Poles colors
        third_color = ORANGE
        function2_color = BLUE
        fifth_color = PINK
        function1_color = GREEN

        fill_color = RED

        # Default font
        size_font = DEFAULT_FONT_SIZE * 0.75

        # Set limits
        limit_x1 = [-5, 5]  # Adjust these values as needed
        limit_y1 = [-2, 2]
        selected_ticks = np.arange(limit_x1[0], limit_x1[1] + 0.1, 0.5).tolist()
        # Create axes with extended lengths and tick configuration
        axes1 = Axes(
            x_range=[limit_x1[0], limit_x1[1], 0.25],  
            y_range=[limit_y1[0], limit_y1[1]+1, 1],
            axis_config={"color": second_color,"include_ticks": True},
            x_length=14 ,  
            y_length=2.85,  
            tips=False,  
        ).to_edge(UP, buff= 0)
        axes2 = Axes(
            x_range=[limit_x1[0], limit_x1[1], 0.25],  
            y_range=[limit_y1[0], limit_y1[1], 1],
            axis_config={"color": second_color,"include_ticks": True},
            x_length=14 ,  
            y_length=2.28,  
            tips=False,  
        ).next_to(axes1,DOWN, buff = 0)
        axes3 = Axes(
            x_range=[limit_x1[0], limit_x1[1], 0.25],  
            y_range=[limit_y1[0]-1, limit_y1[1], 1],
            axis_config={"color": second_color,"include_ticks": True},
            x_length=14 ,  
            y_length=2.85,  
            tips=False,  
        ).next_to(axes2,DOWN, buff = 0)
        #axes3 = axes2.copy().next_to(axes2,DOWN, buff = 0)
        label1 = VGroup(
            MathTex(r"u(t)", 
                    color=function1_color, font_size=size_font*0.9),
            MathTex(r"h(-t+\tau)",
                    color=function2_color, font_size=size_font*0.9)
            ).arrange(LEFT, center=False, buff = 6.6)
        labels = VGroup(
            label1,
            MathTex(r"\text{Product:  } u(t) \cdot h(-t+\tau)", 
                    color=fifth_color, font_size=size_font*0.9),
            MathTex(r"\text{Convolution:  }y(t) = \int_{-\infty}^\infty u(\tau) h(t - \tau) \, d\tau", 
                    color=third_color, font_size=size_font*0.9)
        ).arrange(DOWN, center=False, aligned_edge=LEFT,buff=2).to_corner(UL,buff=0.6)
        labels[2].shift(0.2*UP)
        # Signal parameters
        omega = 5
        alpha = -1/2
        beta = 0.2

        # Define the signals
        def signal_0(t, start=0, length=2):
            return math.exp(alpha * t) if t >= 0 else 0

        def signal_1(t, start=0, length=2):
            return math.cos(omega * t) if t >= 0 else 0

        def signal_2(t, start=0, length=2):
            return math.exp(alpha * t) * math.cos(omega * t) if t >= 0 else 0

        def signal_3(t, start=0, length=2):
            return math.exp(beta * t) * math.cos(omega * t) if t >= 0 else 0

        def signal_4(t, start=0, length=2):
            return 1 if start <= t < start + length else 0
        
        def flip_signal(func):
            return lambda t: func(-t)
        
        def convolution_function(t):
            return np.interp(t, x_values, y_values)
        
        def custom_rate_func(self, t):
            if t < 0.5:  # First half: Slow down for tau [0, 2.5]
                return (t / 0.5) ** 0.5 * 2.5 / 5  # Ease-out
            else:  # Second half: Speed up for tau [2.5, 5]
                return 2.5 / 5 + ((t - 0.5) / 0.5) ** 2 * 2.5 / 5  # Ease-in
        # --------------------------> CHOICE OF FUNCTION <-----------------------------
        function1 = signal_1
        function2 = signal_1
        function2_flipped = flip_signal(function2)

        x_values, y_values = calculate_convolution_values(function1, function2, limit_x1)
        function_convolution = convolution_function
        conv_graph = create_graph(function_convolution, axes3, third_color, limit_x1)

        # Create ValueTracker for tau
        time_tracker = ValueTracker(-2)

        # Create Function 1 graph
        function1_graph = create_graph(function1, axes1, GREEN, limit_x1)
        
        # Create Function 2 flipped graph
        function2_graph = VMobject(color=function2_color)
        update_function2_graph(function2_graph, function2_flipped, axes1, limit_x1, tau_value=-2)
        
        # Create product graph
        product_graph = always_redraw(lambda: axes2.plot(
            lambda t: function1(t) * function2_flipped(t - time_tracker.get_value()), 
            x_range=limit_x1, 
            color=fifth_color, 
            use_smoothing=False
        ))


        # Adding to the scene 
        self.add(axes1, axes2, axes3, labels)
        self.add(function2_graph,function1_graph)
        self.add(conv_graph)
        self.add(product_graph)
        
        # Updaters ---------------------------------------------------------
        
        # Slide function2
        function2_graph.add_updater(
            lambda m: update_function2_graph(m, function2_flipped, axes1, limit_x1, time_tracker.get_value())
        )
        # Dynamic shading for the product area
        shaded_area = always_redraw(lambda: axes2.get_area(
            product_graph, x_range=[limit_x1[0], 
                                    time_tracker.get_value()], 
                                    color=third_color, 
                                    opacity=0.5
        )).set_z_index(-1)
        self.add(shaded_area)

        # Update convolution
        def update_graph(graph):
            tau = time_tracker.get_value()  # Get the value of the time tracker
            updated_y_values = np.array([function_convolution(t) for t in x_values[x_values<tau]])
            points = [axes3.c2p(x_values[i], updated_y_values[i]) for i in range(len(x_values[x_values<tau]))]
            graph.set_points_as_corners(points)
        conv_graph.add_updater(update_graph)

        # Animate time_tracker 
        self.play(time_tracker.animate.set_value(5), run_time=15, rate_func=linear)
        self.wait(2)
        
        


# Function to flip a signal
def flip_signal(func):
    return lambda t: func(-t)


# Function to find convolution function
def calculate_integral(func, start, end):
    integral_value, _ = quad(func, start, end)
    return integral_value

def calculate_convolution_values(signal_1, signal_2, limit_x):
    # Generate x values for the convolution graph up to the current value of tau
    x_values = np.linspace(limit_x[0], limit_x[1], 1000)
    y_values = []

    # Calculate convolution for x values
    for t in x_values:
        # Define the convolution integral dynamically
        convolution = lambda x: signal_1(t - x) * signal_2(x)
        integral_value = calculate_integral(convolution, limit_x[0], limit_x[1])  
        y_values.append(integral_value)
    
    return x_values, y_values  # Return both x and y values for proper interpolation

def update_function2_graph(graph, function, axes, limit_x, tau_value):
    t_values = np.linspace(limit_x[0], limit_x[1], 1000)
    function_values = [function(t - tau_value) for t in t_values]
    points = [axes.c2p(t, function_values[i]) for i, t in enumerate(t_values)]
    graph.set_points_as_corners(points)

# Create stationary graph
def create_graph(function, axes_name, color, limit_x):
    num_points = 1000
    t_values = np.linspace(limit_x[0], limit_x[1], num=num_points)
    signal_values = np.array([function(t) for t in t_values])
    graph = VMobject()
    points = [axes_name.c2p(t_values[i], signal_values[i]) for i in range(num_points)]
    graph.set_points_as_corners(points)
    graph.set_color(color)
    return graph

def update_product_graph(graph, function1, function2_flipped, axes, color, limit_x, tau_value):
    t_values = np.linspace(limit_x[0], limit_x[1], 1000)
    product_values = [function1(t) * function2_flipped(t - tau_value) for t in t_values]
    points = [axes.c2p(t, product_values[i]) for i, t in enumerate(t_values)]
    graph.set_points_as_corners(points)
    graph.set_color(color)


