from manim import *
import math
from convolution_3 import Convolution3  

class MultipleConvolutions(Scene): 
    def construct(self):
        
        # =========================== Signal Functions ===========================
        def signal_cosine(t):
            return math.cos(5 * t) if t >= 0 else 0

        def signal_exp_decay(t):
            return math.exp(-0.5 * t) if t >= 0 else 0

        def signal_rect(t):
            return 1 if 0 <= t <= 1 else 0

        def signal_sine(t):
            return math.sin(5 * t) if t >= 0 else 0

        def signal_triangular(t):
            return 1 - abs(t) if -1 <= t <= 1 else 0

        '''  
        # =========================== Signal Combinations ========================
        signals = [
            (signal_exp_decay, signal_sine, r"\text{Exponential Decay and Sine Functions}"),
            (signal_sine, signal_cosine, r"\text{Sine and Cosine Functions}"),
            (signal_cosine, signal_rect, r"\text{Cosine and Rectangle Functions}"),
            (signal_exp_decay, signal_sine, r"\text{Exponential Decay and Sine Functions}"),
            (signal_triangular, signal_cosine, r"\text{Triangular and Cosine Functions}"),
        ]
         # ============================ Animation Loop ============================
        
        for signal_1, signal_2, title in signals:
            # Create the convolution visualization
            convolution_scene = Convolution3(
                signal_1=signal_1,
                signal_2=signal_2,
                title_text=title,
                limit_x=[-6, 6],
                limit_y=[-3, 3],
            )
            convolution_scene.construct()
    
        '''        
         # =========================== Animation setup ============================
        convolution_scene = Convolution3(
            signal_1=signal_exp_decay,
            signal_2=signal_sine,
            signal_1_label=r"u(t)=\cos(5t)",
            signal_2_label=r"h(t)=\sin(5t)",
            title_text=r"\text{Convolution of Cosine and Sine signal}"
        )
        convolution_scene.construct()
        

        
        

