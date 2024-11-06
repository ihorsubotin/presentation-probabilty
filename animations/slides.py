from manim import *
from manim_revealjs import PresentationScene

config.video_dir = "./videos"

class CreateCircle(PresentationScene):
	def construct(self):
		circle = Circle()  # create a circle
		circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
		self.play(Create(circle))  # show the circle on screen
		self.end_fragment()
		square = Square()
		self.play(Transform(circle, square))
		self.end_fragment()

class TextScene(PresentationScene):
	def construct(self):
		text = Text('Hello world')
		self.play(Write(text))
		self.end_fragment()
		self.play(Write(Square()))
		self.end_fragment()