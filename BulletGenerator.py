# This program generates simple geometric shapes that could be used in SHMUP games and other action games
# This software is FOSS 
# Written by RUOK, check out www.mbcentertainment.co.uk 


import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab
import random
import math

# This will initialise the main window
root = tk.Tk()
root.title("Geometric Bullet Generator")
root.geometry("1400x600")

# Setting up the Canvas where the shapes will be drawn
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Function to get a random color
def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Function to draw the shapes
def draw_shape(shape):
    canvas.delete("all")
    # Set shape dimensions and positions
    initial_x0, initial_y0, initial_x1, initial_y1 = 100, 200, 200, 300
    spacing_x = 200  # Horizontal space between shapes
    for i in range(6):  # This draws 6 variations of the shapes, this is so you can animate them as a spritesheet
        x_offset = i * spacing_x
        x0, y0, x1, y1 = initial_x0 + x_offset, initial_y0, initial_x1 + x_offset, initial_y1
        if shape == "Circle": # Setting for the circle bullet generator
            canvas.create_oval(x0, y0, x1, y1, fill=get_random_color(), outline=get_random_color(), width=5)
            canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill=get_random_color(), outline=get_random_color(), width=5)
        elif shape == "Square": # Setting for the square bullet generator
            canvas.create_rectangle(x0, y0, x1, y1, fill=get_random_color(), outline=get_random_color(), width=5)
            canvas.create_rectangle(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill=get_random_color(), outline=get_random_color(), width=5)
        elif shape == "Triangle": # Setting for the Triangle bullet generator
            canvas.create_polygon(x0 + 50, y0, x0, y1, x1, y1, fill=get_random_color(), outline=get_random_color(), width=5)
            canvas.create_polygon(x0 + 50, y0 + 25, x0 + 10, y1, x1 - 10, y1, fill=get_random_color(), outline=get_random_color(), width=5)
        elif shape == "Arrow": # Setting for the Arrow bullet generator
            # Creates the rectangle (shaft of the arrow)
            canvas.create_rectangle(x0 + 20, y0 + 100, x1 - 20, y1 - 50, fill=get_random_color(), outline=get_random_color(), width=5)
            # Creates the triangle (head of the arrow)
            canvas.create_polygon(x0 + 50, y0, x0, y0 + 50, x1, y0 + 50, fill=get_random_color(), outline=get_random_color(), width=5)
        elif shape == "Star": # Setting for the Star bullet generator
            points = []
            center_x, center_y = x0 + 50, y0 + 50
            radius1, radius2 = 50, 25
            for j in range(10):
                angle = j * math.pi / 5
                if j % 2 == 0:
                    x = center_x + radius1 * math.sin(angle)
                    y = center_y - radius1 * math.cos(angle)
                else:
                    x = center_x + radius2 * math.sin(angle)
                    y = center_y - radius2 * math.cos(angle)
                points.append(x)
                points.append(y)
            canvas.create_polygon(points, fill=get_random_color(), outline=get_random_color(), width=5)

# This will open explorer and allow the user to save the image as a .PNG 
def save_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        # Get the coordinates of the canvas
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        width = x + canvas.winfo_width()
        height = y + canvas.winfo_height()
        # Grab the image from the screen
        ImageGrab.grab().crop((x, y, width, height)).save(filename)

# Function to clear the canvas
def clear_screen():
    canvas.delete("all")

# Creating the buttons from tk frame
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)  # Position buttons at the bottom

shapes = ["Circle", "Square", "Triangle", "Arrow", "Star"]
for shape in shapes:
    btn = tk.Button(button_frame, text=shape, command=lambda s=shape: draw_shape(s))
    btn.pack(side=tk.LEFT, padx=10)  # Place buttons side by side

save_button = tk.Button(button_frame, text="Save Image", command=save_image)
save_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear Screen", command=clear_screen)
clear_button.pack(side=tk.LEFT, padx=10)

# Runs the Tkinter event loop
root.mainloop()