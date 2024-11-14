import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageTk
import datetime

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("p01nter")
        self.root.geometry("800x600")

        # Canvas settings
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        # Initialize variables
        self.current_shape = None
        self.current_color = "black"  # Default line color
        self.bg_color = "white"  # Default background color
        self.thickness = 2
        self.lines = []
        self.theme_mode = "Auto"  # "Light", "Dark", or "Auto"

        # Add menu bar
        self.create_menu_bar()

        # Add toolbar
        self.add_ui_elements()

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        # Bind keyboard shortcuts
        self.root.bind("<Control-z>", lambda event: self.undo())
        self.root.bind("<Control-y>", lambda event: self.redo())
        self.root.bind("<Control-s>", lambda event: self.save_canvas())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-e>", lambda event: self.export_as_png())  # Export as PNG

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.clear_canvas)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save as .ps", command=self.save_canvas)
        file_menu.add_command(label="Export as PNG", command=self.export_as_png)  # Export as PNG
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Tools menu
        tools_menu = tk.Menu(menu_bar, tearoff=0)
        tools_menu.add_command(label="Pick Line Color", command=lambda: self.pick_color("line"))
        tools_menu.add_command(label="Pick Background Color", command=lambda: self.pick_color("bg"))
        tools_menu.add_command(label="Set Line Thickness", command=self.update_thickness)
        menu_bar.add_cascade(label="Tools", menu=tools_menu)

        # Theme menu
        theme_menu = tk.Menu(menu_bar, tearoff=0)
        theme_menu.add_command(label="Light Mode", command=lambda: self.toggle_theme("Light"))
        theme_menu.add_command(label="Dark Mode", command=lambda: self.toggle_theme("Dark"))
        theme_menu.add_command(label="Auto Mode", command=lambda: self.toggle_theme("Auto"))
        menu_bar.add_cascade(label="Theme", menu=theme_menu)

        self.root.config(menu=menu_bar)

    def add_ui_elements(self):
        # Top Frame for Tools
        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(fill="x")

        # Color picker button for line
        color_btn = tk.Button(frame, text="Pick Line Color", command=lambda: self.pick_color("line"))
        color_btn.pack(side="left", padx=5, pady=5)

        # Background color picker button
        bg_color_btn = tk.Button(frame, text="Pick Background Color", command=lambda: self.pick_color("bg"))
        bg_color_btn.pack(side="left", padx=5, pady=5)

        # Thickness scale
        self.thickness_scale = tk.Scale(frame, from_=1, to=10, orient="horizontal", label="Thickness")
        self.thickness_scale.set(self.thickness)
        self.thickness_scale.pack(side="left", padx=5, pady=5)

        # Clear button
        clear_btn = tk.Button(frame, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side="left", padx=5, pady=5)

    def pick_color(self, target):
        color = filedialog.askcolor(title="Pick a color")[1]
        if color:
            if target == "line":
                self.current_color = color
            elif target == "bg":
                self.bg_color = color
                self.canvas.config(bg=self.bg_color)

    def update_thickness(self):
        # Update thickness based on scale value
        self.thickness = self.thickness_scale.get()

    def start_drawing(self, event):
        self.update_thickness()
        x, y = event.x, event.y
        self.current_shape = [x, y, x, y]  # Store start and end points

        # Draw a line and save it for editing
        line_id = self.canvas.create_line(x, y, x, y, fill=self.current_color, width=self.thickness)
        self.lines.append((line_id, self.current_shape, self.thickness, self.current_color))

    def draw(self, event):
        x, y = event.x, event.y
        self.current_shape[2], self.current_shape[3] = x, y
        line_id = self.lines[-1][0]
        self.canvas.coords(line_id, *self.current_shape)
        self.canvas.itemconfig(line_id, width=self.thickness)

    def stop_drawing(self, event):
        line_id, line_coords, line_thickness, line_color = self.lines[-1]

    def clear_canvas(self):
        self.canvas.delete("all")
        self.lines.clear()

    def undo(self):
        # Implement undo functionality
        pass

    def redo(self):
        # Implement redo functionality
        pass

    def save_canvas(self):
        file = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript files", "*.ps")])
        if file:
            self.canvas.postscript(file=file, colormode="color")

    def open_file(self):
        file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file:
            image = Image.open(file)
            self.loaded_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.loaded_image)

    def export_as_png(self):
        """Export the entire canvas as a PNG image."""
        # Create a blank image with white background
        canvas_bbox = self.canvas.bbox("all")
        if canvas_bbox:
            x1, y1, x2, y2 = canvas_bbox
            width = x2 - x1
            height = y2 - y1

            # Create a new image with white background (this is for the entire canvas)
            image = Image.new("RGB", (width, height), color=self.bg_color)
            draw = ImageDraw.Draw(image)

            # Draw the lines on the image
            for line_id, coords, thickness, color in self.lines:
                draw.line(coords, fill=color, width=thickness)

            # Save the image as PNG
            file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file:
                image.save(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
