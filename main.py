from tkinter import *
from PIL import Image, ImageDraw
import PIL

WIDTH, HEIGHT = 500, 500
center = WIDTH // 2
white = (255, 255, 255)


class PaintGUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Paint Clone")

        self.brush_width = 15
        self.current_color = "#000000"

        self.cnv = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg=white)
        self.cnv.pack()
        self.cnv.bind("<B1-Motion>", self.paint)

        self.image = PIL.Image.new("RGB", (WIDTH, HEIGHT), white)
        self.draw = ImageDraw(self.image)

        self.btn_frame = Frame(self.root)
        self.btn_frame.pack(fill=X)

    def paint(self):
        pass