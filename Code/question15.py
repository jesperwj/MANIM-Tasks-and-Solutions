from manim import *
import numpy as np
import math

def convolve_linear(signal, filter_array, output_size):
    out = np.zeros(output_size)
    out_list = []
    s = 0

    for i in range(output_size):
        for j in range(max(0, i - len(filter_array)), i + 1):
            if j < len(signal) and (i - j) < len(filter_array):
                s += signal[j] * filter_array[i - j]
        out[i] = s
        out_list.append(out.copy())
        s = 0
        
    for out in out_list:
        if (len(out) % 2) != 0:
            remove_index = int(np.floor(len(out)/2))
            print(remove_index)
            
            out = np.delete( out , remove_index )

    return out_list

class Question15(Scene):
    
    def func(self, t, width, func_array, n_elements):
            element_length = width/n_elements
            
            if t == 0:
                return 0
            
            index = int(np.floor(element_length/t))
            
            print(index)
            
            return func_array[index]
    
    def construct(self):
        
        # Defining axes
        axes = Axes(
            x_range=[0, 3, 0.5],
            y_range=[0, 1.2, 0.2],
            axis_config={"color": LIGHT_GRAY, "include_numbers": True},
            y_length = 6,
            x_length = 10
        ).move_to(0.2*LEFT+0.3*DOWN).scale(0.85)
        
        rectangle_heigh = 1
        rectangle_width = 2
        
        n = 4

        slices = np.ones(n)*(1/n)

        out_len = 2*n - 1

        func_test = convolve_linear(slices, slices, out_len )
        
        discontinuous_function = lambda x: self.func(x, 2*rectangle_width-1, func_test[0], len(func_test[0]))
        
        disc_plot = axes.plot(
            discontinuous_function,
            discontinuities=[0],  # discontinuous points
            dt=0.01,  # left and right tolerance of discontinuity
            color=GREEN,
        )
        
        self.add(axes, disc_plot)
        
        
        