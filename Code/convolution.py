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
        desired_duration = 15 * 1000  # 10 seconds in milliseconds
        fade_out_duration = 2 * 1000  # 2 seconds fade-out

        # Load and trim the audio to the desired duration, then apply fade-out
        audio_segment = AudioSegment.from_file(audio_path)
        trimmed_audio = audio_segment[:desired_duration].fade_out(fade_out_duration)
        trimmed_audio.export("music/trimmed_fadeout_manim_song.mp3", format="mp3")
        self.add_sound("music/trimmed_fadeout_manim_song.mp3", time_offset=1, gain=music_volume)
        
        # Color scheme set up
        first_color = WHITE
        second_color = GRAY_C

        #Poles colors 
        third_color = YELLOW
        fourth_color = BLUE
        fifth_color = RED

        fill_color = RED 
        
        # Default font
        size_font =  DEFAULT_FONT_SIZE*0.75

        # Set limits
        limit_x1 = [-7, 7]  # Adjust these values as needed
        limit_y1 = [-1.5, 5]

        # Create axes with extended lengths and tick configuration
        axes1 = Axes(
            x_range=[limit_x1[0], limit_x1[1], 1],  # Adjust tick spacing as needed
            y_range=[limit_y1[0], limit_y1[1], 1],
            axis_config={"color": second_color, "include_ticks": True},
            x_length=14,  # Full width minus padding
            y_length=8,  # Full height minus padding
            tips=False,  # Turn off axis tips
        )
        labels1 = axes1.get_axis_labels(x_label=r"\text{t}", y_label=r"\text{y(t)}").set_color(second_color).scale(0.9)
        axes2 = axes1.copy().shift(2*UP)
                             
        title1 = MathTex(r"\text{Pole placement in s-domain}", 
                    color=second_color, font_size=size_font*1.1).next_to(axes1, UP).shift(0.7*UP)
        
        text1 = VGroup(
                    MathTex(r"x(t) = e^{-\frac{t}{2}u(t)}", 
                            color=third_color, font_size=size_font),
                    MathTex(r"h(t) = u(t) - u(t-2)}", 
                        color=fourth_color, font_size=size_font)
                ).arrange(DOWN).to_edge(UP, buff = 1).shift(4*RIGHT)
        
        text2 = VGroup(
                    MathTex(r"x(\tau) = e^{-\frac{\tau}{2}u(\tau)}", 
                            color=third_color, font_size=size_font),
                    MathTex(r"h(\tau) = u(\tau) - u(\tau-2)}", 
                        color=fourth_color, font_size=size_font)
                ).arrange(DOWN).to_edge(UP, buff = 1).shift(4*RIGHT)
        
        text3 = VGroup(
                    MathTex(r"x(\tau) = e^{-\frac{\tau}{2}u(\tau)}", 
                            color=third_color, font_size=size_font),
                    MathTex(r"h(-\tau) = u(-\tau) - u(-\tau-2)}", 
                        color=fourth_color, font_size=size_font)
                ).arrange(DOWN).to_edge(UP, buff = 1).shift(4*RIGHT)
        
        text4 = VGroup(
                    MathTex(r"x(\tau) = e^{-\frac{\tau}{2}u(\tau)}", 
                            color=third_color, font_size=size_font),
                    MathTex(r"h(t-\tau) = u(t-\tau) - u(t-\tau-2)}", 
                        color=fourth_color, font_size=size_font)
                ).arrange(DOWN).to_edge(UP, buff = 0.3).shift(4*RIGHT)
        
        instructions = VGroup(
            MathTex(r"y(t) = \int_{-\infty}^{\infty} x(\tau) \, u(t - \tau) \, d\tau", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{Step 1: } t \rightarrow \tau", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{Step 2: } h(\tau) \rightarrow h(-\tau)", 
                    color=first_color, font_size=size_font),
            MathTex(r"\text{Step 3: Sliding window}", 
                    color=first_color, font_size=size_font),
        ).arrange(DOWN, aligned_edge = LEFT).to_corner(UL, buff = 0.3).shift(RIGHT)
        instructions[1:].shift(0.1*DOWN+0.5*RIGHT)
        
        box = Rectangle(
            height=instructions[0].get_height()+0.3, 
            width=instructions[0].get_width()+0.3, 
            fill_color=None, 
            fill_opacity=0.0, 
            stroke_color=second_color).move_to(instructions[0])


        # Drawing poles and their impulse responses
        omega = 5
        alpha = -1/2
        beta = 0.2

        # Creating the signals
        def signal_0(t, start=0, length=2):
            if t < 0:
                return 0
            else:
                return math.exp(alpha*t)
        def signal_1(t, start=0, length=2):
            if t < 0:
                return 0
            else:
                return math.cos(omega*t)
        def signal_2(t, start=0, length=2):
            if t < 0:
                return 0
            else:
                return math.exp(alpha*t)*math.cos(omega*t)
        def signal_3(t, start=0, length=2):
            if t < 0:
                return 0
            else:
                return math.exp(beta*t)*math.cos(omega*t)
            
        def signal_4(t, start=0, length = 2):
            if t < start:
                return 0
            elif t < start+length:
                return 1
            else:
                return 0

        # Generating singnals 

        impulse_response1 = make_signal_on_axes(signal_0, axes1, third_color, limit_x1)

        window_function = make_signal_on_axes(signal_4, axes1, 
                                              fourth_color, 
                                              limit_x1, 
                                              start=0)
        
        # Adding to scene
        self.add(axes1, axes2.x_axis,
                 title1, 
                 labels1)
        self.add(instructions, box)
        self.add(text4)
        self.add(impulse_response1)
        

        # Sliding window
        window_start_tracker = ValueTracker(-5)  

        window_function_graph = always_redraw(lambda: make_signal_on_axes(
            signal_4,
            axes1,
            fourth_color,
            limit_x1,
            start=window_start_tracker.get_value(),
            length=2
        ))
        integral_graph = always_redraw(lambda: create_integral_graph(
                    window_start_tracker.get_value(), 
                    axes2, 
                    signal_0,
                    limit_x1
                    ))
        area_between_graphs = always_redraw(lambda: get_clipped_area_under_graph(
            axes1,
            signal_0,  # Impulse response function
            window_start_tracker.get_value(),  # Start of the window
            window_start_tracker.get_value() + 2,  # End of the window
            color=fill_color
        ))

        # Add to scene
        self.add(window_function_graph)
        self.add(area_between_graphs)
        self.add(integral_graph)
        self.play(window_start_tracker.animate.set_value(5), run_time=10, rate_func=linear)
        self.wait(3)



def calculate_integral(func, start, end):
            integral_value, _ = quad(func, start, end)
            return integral_value
        
def create_integral_graph(start, axes2, signal_0,limit_x):
    end = start + 2  # The window length is 2 units

    # Create a graph showing how the integral value changes over time
    x_values = np.linspace(limit_x[0]+2, end, 100)
    integral_values = [calculate_integral(signal_0, t-2, t) for t in x_values]

    # Create the graph for the integral function
    integral_graph = VMobject()
    points = [axes2.c2p(x_values[i], integral_values[i]) for i in range(len(x_values))]
    integral_graph.set_points_as_corners(points)
    integral_graph.set_color(RED)
    return integral_graph
        

def make_signal_on_axes(function,axes_name,color, limit_x, start=0, length=2):
    num_points = 1000
    t_values = np.linspace(limit_x[0], limit_x[1], num=num_points)

    # Generate points for each function
    signal_values = np.array([function(t, start, length) for t in t_values])
    graph = VMobject()
    points = [axes_name.c2p(t_values[i], signal_values[i]) for i in range(num_points)]
    graph.set_points_as_corners(points)
    graph.set_color(color)

    return graph

def get_clipped_area_under_graph(axes, func, start, end, color=GREEN, opacity=0.4):
    num_points = 100
    x_values = np.linspace(start, end, num_points)
    points = [axes.c2p(x, func(x)) for x in x_values]  # Points for the function graph
    x_axis_points = [axes.c2p(x, 0) for x in reversed(x_values)]  # Reversed x-axis points for closing the area

    # Create the area object and fill with color
    area = VMobject()
    area.set_points_as_corners(points + x_axis_points)
    area.set_fill(color, opacity=opacity)
    area.set_stroke(width=0)  # No stroke
    return area