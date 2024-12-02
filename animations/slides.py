from manim import *
from manim_revealjs import PresentationScene, NORMAL, NO_PAUSE, LOOP, COMPLETE_LOOP
import math
import numpy as np
import random

config.video_dir = "./videos"

def ChangingNumber(num: DecimalNumber, end, **kwargs):
	start = num.get_value()
	return ChangingDecimal(num, lambda alpha: (start + alpha*(end - start)), **kwargs)

class Intro(PresentationScene):
	def construct(self):
		t2 = Text('Неперервні випадкові величин(НВВ)',  font_size=42).move_to(UP*2.5)
		t3 = Text('Підготував: Суботін Ігор, МПІ-241', font_size=32).move_to(UP+LEFT*2)
		text1 = VGroup(t2, t3)
		self.add(text1)
		logo = SVGMobject('./animations/images/logo.svg', color=WHITE).set_fill(WHITE).move_to(RIGHT*4+DOWN*1.5)
		self.add(logo)
		ax = Axes(x_range=[-4, 4, 1], y_range=[0,0.5], x_length=5, y_length=3, ).move_to(LEFT*3 + DOWN*1.5)
		graph = ax.plot(lambda x: math.exp(-x*x/2)/2.5).set_fill(YELLOW, opacity= 0.5)
		self.add(ax, graph)
		self.end_fragment()
		self.play(Unwrite(text1, run_time=2, lag_ratio=0.1),
			Unwrite(graph, run_time=2), FadeOut(ax, run_time=2), Unwrite(logo, run_time=2))
		
		t4 = Text('Трохи про презентацію', font_size=42).move_to(UP*3)
		self.play(Write(t4))

		t5 = Text('Побудована за допомогою Manim', t2c={'[24:29]':BLUE}, 
			font_size=32).align_on_border(LEFT * 1).shift(UP*1.7)
		manim = SVGMobject('./animations/images/manim-logo.svg', width=1).next_to(t5, RIGHT, buff=0.5)
		self.play(Write(t5), Write(manim))

		t6 = Text('Автор бібліотеки 3Bule1Brown', t2c={'[17:28]':BLUE}, 
			font_size=32).align_on_border(LEFT * 1).shift(UP*0.5)
		l3b1b = SVGMobject('./animations/images/3B1B-logo.svg', width=1).next_to(t6, RIGHT, buff=0.5)
		self.play(Write(t6), FadeIn(l3b1b))
		self.end_fragment()

		t7 = Text('Вихідний код можна почитати на GitHub', t2c={'[31:37]':BLUE}, 
			font_size=32).align_on_border(LEFT * 1).shift(DOWN*0.6)
		t8 = Text('https://github.com/ihorsubotin/presentation-probabilty', font_size=20).next_to(t7, DOWN, buff=0.2)
		github = SVGMobject('./animations/images/github-icon.svg', width=1).next_to(t7, RIGHT, buff=0.5).shift(DOWN*0.3)
		self.play(Write(t7), Write(t8), Write(github))

		t9 = Text('Перегляд презентації доступний за посиланням', t2c={'[21:44]': BLUE},
			font_size=32).align_on_border(LEFT * 1).shift(DOWN*2)
		t10 = Text('https://ihorsubotin.github.io/presentation-probabilty/', font_size=20).next_to(t9, DOWN, buff=0.2)
		www = SVGMobject('./animations/images/www.svg', width=1).next_to(t9, RIGHT, buff=0.5).shift(DOWN*0.3)
		self.play(Write(t9), Write(t10), Write(www))
		self.end_fragment()

		text2 = VGroup(t4, t5, t6, t7, t8, t9, t10)
		logos = VGroup(manim, github, www)
		self.play(Unwrite(text2, run_time=2, lag_ratio=0.1),
			Unwrite(logos, run_time=2, lag_ratio=0.1), FadeOut(l3b1b, run_time=2))
		t11 = Text('Зміст', font_size=42).move_to(UP*3)
		t12 = Text('1. Визначення НВВ', font_size=32)
		t13 = Text('2. Властивості функцій розподілу', font_size=32)
		t14 = Text('3. Числові властивості НВВ', font_size=32)
		t15 = Text('4. Основні розподіли НВВ', font_size=32)
		text3 = VGroup(t12, t13, t14, t15).arrange(direction=DOWN, buff=0.5)
		self.play(Write(t11), Write(text3, run_time=3, lag_ratio=0.5))
		self.end_fragment()

		t16 = Text('1. Визначення НВВ', font_size=42).align_on_border(UL)
		text4 = VGroup(t11, t13, t14, t15)
		self.play(Transform(t12, t16, run_time=2.5), Unwrite(text4, run_time=1.5, lag_ratio=0.1))
		self.end_fragment()

class Definitions(PresentationScene):
	def construct(self):

		t1 = Text('1. Визначення НВВ', font_size=42).align_on_border(UL)
		self.add(t1)

		def get_arr_by_n(n):
			arr = np.array([math.sin(x*4/n) + 1 for x in range(n)])
			sum = arr.sum()
			return arr/sum
		def create_bar1(arr):
			return BarChart(arr, x_length=5, y_length=3, bar_width=1, y_axis_config={"include_ticks": False},
				   x_axis_config={"include_ticks": False}, bar_colors=[BLUE]).shift(UP+LEFT*3)
		arr1 = get_arr_by_n(6)
		arr2 = get_arr_by_n(12)
		arr3 = get_arr_by_n(24)
		arr4 = get_arr_by_n(48)
		arr5 = get_arr_by_n(96)
		arr6 = get_arr_by_n(192)

		def generate_squares(arr, ax):
			g = VGroup()
			for i in range(len(arr)):
				rec = Rectangle(height=arr[i],width=1/len(arr)).next_to(ORIGIN, UR, buff=0).shift(RIGHT*i/len(arr))
				sq = Polygon(*ax.coords_to_point(rec.get_all_points()), color=BLUE).set_fill(BLUE, opacity=0.7)
				g.add(sq)
			return g
		def get_str_from(arr, n):
			ar = ["{val:.2f}".format(val=arr[i]) for i in range(n)]
			return [*ar,"..."]
		def polygon_from_arr(arr, ax, x_range, to_0 = True):
			num_range = [x_range[0], x_range[1]]
			if x_range[0] < 0:
				num_range[0] = 0
			if x_range[1] > 1:
				num_range[1] = 1
			start_i = 0 if x_range[0] < 0 else math.floor(x_range[0]*len(arr))
			end_i =  len(arr)-1 if x_range[1] > 1 else math.ceil(x_range[1]*(len(arr)-1))
			coord = []
			if to_0:
				coord.extend([[x_range[0], 0], [x_range[0], arr[start_i]]])
			coord.extend(list(map(lambda i: [num_range[0] + (i-start_i)*(num_range[1] - num_range[0])/(end_i - start_i), arr[i]], range(start_i, end_i))))		
			coord.append([x_range[1], arr[end_i]])
			coord.append([x_range[1], 0 if to_0 else arr[start_i]])
			return Polygon(*ax.coords_to_point(coord), color=YELLOW).set_fill(YELLOW, opacity=0.7)

		#"""
		ax1 = Axes([0, 1], y_range=[0, 0.21, 0.05], x_length=5, y_length=3, 
			y_axis_config={"include_ticks": True, "include_numbers":True},
			x_axis_config={"include_ticks": False, "include_tip": False}).shift(DOWN*1.5+LEFT*3)
		g1 = generate_squares(arr1, ax1)
		tab1 = Table([["1", "2", "3", "..."], get_str_from(arr1, 3)], 
			 row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5)
		self.play(Write(g1), Write(ax1), Write(tab1))
		self.end_fragment()

		arr2 = get_arr_by_n(12)
		g2 = generate_squares(arr2, ax1)
		tab2 = Table([["0.5", "1", "1.5", "..."], get_str_from(arr2, 3)], 
			 row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5)
		self.play(Transform(g1, g2), Transform(tab1, tab2))
		self.end_fragment()

		arr3 = get_arr_by_n(24)
		g3 = generate_squares(arr3, ax1)
		tab3 = Table([["0.25", "0.5", "0.75", "..."], get_str_from(arr3, 3)], 
			 row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5)
		self.play(Transform(g1, g3),  Transform(tab1, tab3))

		arr4 = get_arr_by_n(48)
		g4 = generate_squares(arr4, ax1)
		tab4 = Table([["0.12", "0.25", "0.37", "..."], get_str_from(arr4, 3)], 
			 row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5)
		self.play(Transform(g1, g4), Transform(tab1, tab4))
		self.end_fragment()

		arr5 = get_arr_by_n(96)
		g5 = generate_squares(arr5, ax1)
		tab5 = Table([["0.06", "0.12", "0.18", "..."], get_str_from(arr5, 3)], 
			 row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5)
		self.play(Transform(g1, g5), Transform(tab1, tab5))

		arr6 = get_arr_by_n(192)
		g6 = generate_squares(arr6, ax1)
		tab6 = Table([["0.03", "0.06", "0.09", "..."], get_str_from(arr6, 3)],
			row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5)
		self.play(Transform(g1, g6), Transform(tab1, tab6))

		rect = Rectangle(height=1/100, width=5, color=BLUE).set_fill(BLUE).align_to(ax1, DL).shift(RIGHT*0.9)
		tab7 = Table([["0.03", "0.6", "1.7", "4"], ["0.00", "0.00", "0.00", "0.00"]],
			row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5)
		self.play(Transform(g1, rect), Transform(tab1, tab7))
		self.end_fragment()

		ar1 = Arrow(start=DOWN, end=DOWN+RIGHT*2.5)
		self.play(Write(ar1))
		f1 = MathTex("f(x) = 0\\text{ ?}").shift(DOWN+RIGHT*4)
		self.play(Write(f1))
		self.end_fragment()

		cross = Cross(scale_factor=0.8).shift(DOWN+RIGHT*1.25)
		self.play(Write(cross))
		self.end_fragment()

		ar2 = Arrow(start=ORIGIN, end=DOWN*2.5).next_to(ax1, DOWN)
		self.play(Unwrite(VGroup(f1, ar1, cross)), Write(ar2))
		scene1 = VGroup(ax1, g1, ar2, tab1, t1)
		self.play(scene1.animate.shift(UP*8.5))
		def calculate_integral(arr):
			s = 0
			res = []
			for el in arr:
				s+=el
				res.append(s)
			return res
		
		sarr1 = calculate_integral(arr1)
		tab8 = Table([["1", "2", "3", "..."], get_str_from(arr1, 3), get_str_from(sarr1, 3)], 
			 row_labels=[MathTex("X"), MathTex("P(x)"), MathTex("P(X<x)")]).scale(0.6).shift(LEFT*3+UP*1.5)
		ax2 = Axes([0, 1], y_range=[0, 1.01, 0.2], x_length=5, y_length=3, 
			y_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False},
			x_axis_config={"include_ticks": False, "include_tip": False}).shift(DOWN*1.5+LEFT*3.5)
		g8 = generate_squares(sarr1, ax2)
		self.play(Write(VGroup(tab8, ax2, g8), run_time=3))
		self.end_fragment()

		sarr2 = calculate_integral(arr2)
		tab9 = Table([["0.5", "1", "1.5", "..."], get_str_from(arr2, 3), get_str_from(sarr2, 3)], 
			 row_labels=[MathTex("X"), MathTex("P(x)"), MathTex("P(X<x)")]).scale(0.6).shift(LEFT*3+UP*1.5)
		g9 = generate_squares(sarr2, ax2)
		self.play(Transform(tab8, tab9), Transform(g8, g9))
		self.end_fragment()

		sarr3 = calculate_integral(arr3)
		tab10 = Table([["0.25", "0.50", "0.75", "..."], get_str_from(arr3, 3), get_str_from(sarr3, 3)], 
			 row_labels=[MathTex("X"), MathTex("P(x)"), MathTex("P(X<x)")]).scale(0.6).shift(LEFT*3+UP*1.5)
		g10 = generate_squares(sarr3, ax2)
		self.play(Transform(tab8, tab10), Transform(g8, g10))

		sarr4 = calculate_integral(arr4)
		tab11 = Table([["0.12", "0.25", "0.37", "..."], get_str_from(arr4, 3), get_str_from(sarr4, 3)], 
			 row_labels=[MathTex("X"), MathTex("P(x)"), MathTex("P(X<x)")]).scale(0.6).shift(LEFT*3+UP*1.5)
		g11 = generate_squares(sarr4, ax2)
		self.play(Transform(tab8, tab11), Transform(g8, g11))
		self.end_fragment()

		sarr5 = calculate_integral(arr5)
		tab12 = Table([["0.06", "0.12", "0.18", "..."], get_str_from(arr5, 3), get_str_from(sarr5, 3)], 
			 row_labels=[MathTex("X"), MathTex("P(x)"), MathTex("P(X<x)")]).scale(0.6).shift(LEFT*3+UP*1.5)
		g12 = generate_squares(sarr5, ax2)
		self.play(Transform(tab8, tab12), Transform(g8, g12))

		sarr6 = calculate_integral(arr6)
		tab13 = Table([["0.06", "0.6", "1.7", "4"], ["0.00", "0.00", "0.00", "0.00"], ["0.01", "0.09", "0.3", "0.81"]], 
			 row_labels=[MathTex("X"), MathTex("P(x)"), MathTex("P(X<x)")]).scale(0.6).shift(LEFT*3+UP*1.5)
		g13 = generate_squares(sarr6, ax2)
		self.play(Transform(tab8, tab13), Transform(g8, g13))
		self.end_fragment()

		ar3 = Arrow(start=DOWN*1.5+LEFT, end=DOWN*1.5+RIGHT)
		self.play(Write(ar3))
		f2 = MathTex("F(x)=P(X<x)").shift(UP+RIGHT*4)
		self.play(Write(f2))

		ax3 = Axes([0, 1], y_range=[0, 1.01, 0.2], x_length=5, y_length=3, 
			y_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False},
			x_axis_config={"include_ticks": False, "include_tip": False}).shift(DOWN*1.5+RIGHT*4)
		self.play(Write(ax3))
	
		pl1 = polygon_from_arr(sarr6, ax2, [0, 1])
		pl2 = polygon_from_arr(sarr6, ax3, [0, 1])
		self.play(Write(pl1))
		self.play(Transform(pl1, pl2, run_time=2))
		self.end_fragment()
		
		t2 = Text('2.1 Властивості інтегральної функції розподілу', font_size=32).align_on_border(UL).shift(RIGHT*8)
		scene2 = VGroup(ax1, ar2, t1, tab8, g8, ax2, ax3, pl1, f2, ar3, t2)
		self.play(Write(t2), ax3.animate.shift(RIGHT*0.5), f2.animate.shift(UP*0.7), pl1.animate.shift(RIGHT*0.5))
		self.play(scene2.animate.shift(LEFT*8))
		ax4 = Axes(x_range=[-0.5, 1.5], y_range=[0, 1], x_length=5, y_length=3).shift(LEFT*3.5+DOWN*1.5)
		pl3 = polygon_from_arr(sarr6, ax4, [-0.5, 1.5])
		pl4 = polygon_from_arr(sarr6, ax3, [0, 1])
		self.end_fragment()
		
		f3 = MathTex('1.\, 0\le F(x)\le 1',)
		f4 = MathTex('2.\, P(a \le x < b) = F(b) - F(a)')
		f5 = MathTex('3.\, \\text{If}\, x_{0}\le x_{1}, then\, F(x_{0})\le F(x_{1})')
		f6 = MathTex('4.\, \\text{If}\, X\in(a,b), then')
		f7 = MathTex('4.1.\, x\le a, F(x) = 0')
		f8 = MathTex('4.2.\, x\ge b, F(x) = 1')
		f9 = MathTex('5.\, P(X=x) = 0')

		text1 = VGroup(f3, f4, f5, f6, f7, f8, f9).scale(0.9).arrange(direction=DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT*3.5 + DOWN*0.5)
		self.play(Write(f3))
		self.end_fragment(fragment_type=NO_PAUSE)
		l1 = Line(ax3.coords_to_point(*(0, 1.01, 0)), ax3.coords_to_point(*(1, 1.01, 0)), color=BLUE, stroke_width=6)
		l2 = Line(ax3.coords_to_point(*(0, 0, 0)), ax3.coords_to_point(*(1, 0, 0)), color=BLUE, stroke_width=6)
		self.play(Transform(pl1, pl3))
		self.play(Write(VGroup(l1, l2),lag_ratio=0.9))
		self.wait()
		self.play(Unwrite(VGroup(l1, l2),lag_ratio=0.9))
		self.play(Transform(pl1, pl4))
		self.wait()
		self.end_fragment(fragment_type=LOOP)

		self.play(Write(f4))
		l3 = Line(ax3.coords_to_point(*(0.2, 0, 0)), ax3.coords_to_point(*(0.2, 1.01, 0)), color=BLUE, stroke_width=6)
		l3t = MathTex('a').shift(ax3.coords_to_point(*(0.2, -0.15)))
		l4 = Line(ax3.coords_to_point(*(0.6, 0, 0)), ax3.coords_to_point(*(0.6, 1.01, 0)), color=BLUE, stroke_width=6)
		l4t = MathTex('b').shift(ax3.coords_to_point(*(0.6, -0.15)))
		self.play(Write(VGroup(l3, l3t, l4, l4t)))
		self.end_fragment()
		
		pl5 = polygon_from_arr(sarr6, ax3, [0, 0.6], False).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		self.play(Write(pl5))
		self.wait()
		f10 = MathTex('F(b) = ').next_to(f4, DOWN*1.2, aligned_edge=LEFT)
		self.play(Write(f10))
		f11 = MathTex('P(x < b)').next_to(f10, RIGHT*0.5)
		self.play(Transform(pl5, f11))
		self.end_fragment()

		f12 = MathTex('F(b) = ').next_to(f10, DOWN*1.2, aligned_edge=LEFT)
		f13 = MathTex('P(x < a) + ').next_to(f12, RIGHT*0.25)
		f14 = MathTex('P(a \le x < b)').next_to(f13, RIGHT*0.25)
		self.play(Write(VGroup(f12, f13, f14)))
		self.end_fragment(fragment_type=NO_PAUSE)
		
		self.wait(2)
		pl6 = polygon_from_arr(sarr6, ax3, [0, 0.2], False).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		self.play(Write(pl6))
		self.wait()
		self.play(Transform(pl6, f13))
		pl7 = polygon_from_arr(sarr6, ax3, [0.2, 0.6], False).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		self.play(Write(pl7))
		self.wait()
		self.play(Transform(pl7, f14))
		self.end_fragment(fragment_type=LOOP)

		f15 = MathTex('F(b) = ').next_to(f12, DOWN*1.2, aligned_edge=LEFT)
		f16 = MathTex('F(a) +').next_to(f15, RIGHT*0.25)
		f17 = MathTex('P(a \le x < b)').next_to(f16, RIGHT*0.25)
		self.play(TransformFromCopy(f12, f15), TransformFromCopy(f13, f16), TransformFromCopy(f14, f17))
		self.end_fragment()

		f18 = MathTex('P(a \le x < b) = ').next_to(f15, DOWN*1.2, aligned_edge=LEFT)
		f19 = MathTex('F(b) ').next_to(f18, RIGHT*0.25)
		f20 = MathTex('- F(a)').next_to(f19, RIGHT*0.25)
		self.play(TransformFromCopy(f17, f18))
		self.play(TransformFromCopy(f15, f19))
		self.play(TransformFromCopy(f16, f20))
		self.end_fragment()

		self.play(Unwrite(VGroup(f10, f11, pl5, f12, f13, pl6, f14, pl7, f15, f16, f17, f18, f19, f20, l3, l3t, l4, l4t)))
		self.play(Write(f5))
		self.end_fragment()
		
		f21 = MathTex('F(x_{0})\le', ).scale(0.8).next_to(f5, DOWN*1.2, aligned_edge=LEFT)
		f22 = MathTex('F(x_{1})').scale(0.8).next_to(f21, RIGHT*0.25)
		self.play(Write(VGroup(f21, f22)))
		l5 = Line(ax3.coords_to_point(*(0.4, 0, 0)), ax3.coords_to_point(*(0.4, 1.01, 0)), color=BLUE, stroke_width=6)
		l5t = MathTex('x_{0}').shift(ax3.coords_to_point(*(0.4, -0.15)))
		l6 = Line(ax3.coords_to_point(*(0.7, 0, 0)), ax3.coords_to_point(*(0.7, 1.01, 0)), color=BLUE, stroke_width=6)
		l6t = MathTex('x_{1}').shift(ax3.coords_to_point(*(0.7, -0.15)))
		self.play(Write(VGroup(l5, l5t, l6, l6t)))
		self.end_fragment()

		f23 = MathTex('F(x_{0})\le').scale(0.8).next_to(f21, DOWN*1.2, aligned_edge=LEFT)
		f24 = MathTex('F(x_{0}) +').scale(0.8).next_to(f23, RIGHT*0.25)
		f25 = MathTex(' P(x_{0} < x \le x_{1})').scale(0.8).next_to(f24, RIGHT*0.25)
		self.play(TransformFromCopy(f21, f23))
		self.play(TransformFromCopy(f22, VGroup(f24, f25)))
		self.end_fragment(fragment_type=NO_PAUSE)
		
		self.wait(2)
		pl8 = polygon_from_arr(sarr6, ax3, [0.0, 0.4], False).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		self.play(Write(pl8))
		self.wait()
		self.play(Transform(pl8, f24))
		pl9 = polygon_from_arr(sarr6, ax3, [0.4, 0.7], False).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		self.play(Write(pl9))
		self.wait()
		self.play(Transform(pl9, f25))
		self.end_fragment(fragment_type=LOOP)


		f26 = MathTex('P(x_{0} < x \le x_{1})').scale(0.8).next_to(f23, DOWN*1.2, aligned_edge=LEFT)
		f27 = MathTex(' \ge 0').scale(0.8).next_to(f26, RIGHT*0.25)
		self.play(TransformFromCopy(f25, f26))
		self.play(TransformFromCopy(VGroup(f23, f24), f27))
		self.end_fragment()

		self.play(Unwrite(VGroup(f21, f22, f23, f24, pl8, f25, pl9, f26, f27, l5, l5t, l6, l6t)))
		self.play(Write(f6))
		self.play(Transform(pl1, pl3))
		l7 = Line(ax4.coords_to_point(*(0, 0, 0)), ax4.coords_to_point(*(0, 1.01, 0)), color=BLUE, stroke_width=6)
		l7t = MathTex('a').shift(ax4.coords_to_point(*(0, -0.15)))
		l8 = Line(ax4.coords_to_point(*(1, 0, 0)), ax4.coords_to_point(*(1, 1.01, 0)), color=BLUE, stroke_width=6)
		l8t = MathTex('b').shift(ax4.coords_to_point(*(1, -0.15)))
		self.play(Write(VGroup(l7, l7t, l8, l8t)))
		self.end_fragment()

		self.play(Write(f7))
		f28 = MathTex('F(x \le a) = P(\emptyset) = 0').scale(0.8).next_to(f7, DOWN*1.2, aligned_edge=LEFT)
		self.play(Write(f28))
		self.end_fragment()

		self.play(Unwrite(f28))
		self.play(Write(f8))
		f29 = MathTex('F(x \ge b) = P(\Omega) = 1').scale(0.8).next_to(f8, DOWN*1.2, aligned_edge=LEFT)
		self.play(Write(f29))
		self.end_fragment()

		self.play(Unwrite(f29))
		self.play(Unwrite(VGroup(l7, l7t, l8, l8t)))
		self.play(Transform(pl1, pl4))

		self.play(Write(f9))
		self.end_fragment()

		self.play(Unwrite(t2, run_time=0.7))
		scene3 = VGroup(scene2, text1)
		self.play(scene3.animate.shift(RIGHT*8))

		ar4 = Arrow(start=UP*2+RIGHT*4, end = UP*5+RIGHT*4)
		self.play(Write(ar4))
		self.remove(g1)
		self.remove(tab1)
		g14 = generate_squares(arr1, ax1)
		tab14 = Table([["1", "2", "3", "..."], get_str_from(arr1, 3)], 
			 row_labels=[MathTex("X"), MathTex("P")]).scale(0.6).shift(LEFT*3+UP*1.5).shift(UP*8.5)
		scene4 = VGroup(scene2, g14, tab14, ar4)
		self.play(scene4.animate.shift(DOWN*8.5))

		f30 = MathTex('f(x) = F\'(x)').shift(RIGHT*3+UP*2)
		self.play(Write(f30))
		ax5 = Axes([0, 6], y_range=[0, 0.21, 0.05], x_length=5, y_length=3, 
			y_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False},
			x_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(DOWN*1.5+RIGHT*3.5)
		ax6 = Axes([0, 1], y_range=[0, 0.21, 0.05], x_length=5, y_length=3).shift(DOWN*1.5+RIGHT*3.5)
		darr6 = arr6*32
		pl10 = polygon_from_arr(darr6, ax6, [0, 1])
		self.play(Write(VGroup(ax5, pl10)))
		self.end_fragment()

		t3 = Text('2.2 Властивості функції щільності імовірності', font_size=32).align_on_border(UL).shift(RIGHT*8)
		self.play(Write(t3))
		scene5 = VGroup(t1, t3, tab14, g14, ax1, f30)
		self.play(scene5.animate.shift(LEFT*8), VGroup(ax5, pl10).animate.shift(LEFT*7), 
			VGroup(ar2, ar4).animate.shift(DOWN*2))
		ax6.shift(LEFT*7)
		self.end_fragment()

		f31 = MathTex('1.\, P(a \le x < b) = \int_{a}^{b} f(x) \,dx')
		f32 = MathTex('2.\, f(x) \ge 0')
		f33 = MathTex('3.\, F(a) = \int_{-\infty}^{a} f(x) \,dx')
		f34 = MathTex('4.\, \int_{-\infty}^{\infty} f(x) \,dx = 1')
		text2 = VGroup(f31, f32, f33, f34).scale(0.9).arrange(direction=DOWN, buff=0.6, aligned_edge=LEFT).shift(RIGHT*3.5 + DOWN*0.5)
		
		self.play(Write(f31))
		pl11 = polygon_from_arr(darr6, ax6, [0.3, 0.7]).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		self.play(Write(pl11))
		f35 = MathTex('P(a \le x < b) =').scale(0.8).next_to(f31, DOWN*1.2, aligned_edge=LEFT)
		num1 = DecimalNumber(sarr6[math.floor(0.7*192)] - sarr6[math.floor(0.3*192)]).scale(0.8).next_to(f35, RIGHT*0.3)
		self.play(Write(VGroup(f35, num1)))
		self.end_fragment(fragment_type=NO_PAUSE)

		def transform_graph(old_range, new_range, polygon, number, itterations, time):
			for i in range(itterations):
				alpha = rate_functions.smooth((i+1)/itterations)
				i_values = [interpolate(old_range[0], new_range[0], alpha), interpolate(old_range[1], new_range[1], alpha)]
				polygon_new = polygon_from_arr(darr6, ax6, i_values).set_color(BLUE).set_fill(BLUE, opacity=0.7)
				p_value = sarr6[math.floor(i_values[1]*192)] - sarr6[math.floor(i_values[0]*192)]
				number.set_value(p_value)
				self.play(Transform(polygon, polygon_new, run_time = time))

		transform_graph([0.3, 0.7], [0.5, 0.9], pl11, num1, 60, 0.02)
		self.wait()

		transform_graph([0.5, 0.9], [0.7, 0.9], pl11, num1, 60, 0.02)
		self.wait()

		transform_graph([0.7, 0.9], [0.1, 0.3], pl11, num1, 60, 0.02)
		self.wait()
		
		transform_graph([0.1, 0.3], [0.3, 0.7], pl11, num1, 60, 0.02)
		self.wait()

		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(f35, num1, pl11)))

		f36 = MathTex('P(a \le x < b) ').scale(0.8).next_to(f31, DOWN*1.2, aligned_edge=LEFT)
		f37 = MathTex('= F(b) - F(a)').scale(0.8).next_to(f36, RIGHT*0.4)
		self.play(Write(VGroup(f36,f37)))
		self.end_fragment()

		f40  = MathTex('\int_{a}^{b} f(x) \,dx').scale(0.8).next_to(f36, DOWN*1.2, aligned_edge=LEFT)
		f41 = MathTex('= F(b) - F(a)').scale(0.8).next_to(f40, RIGHT*0.4)
		self.play(Write(VGroup(f40, f41)))
		self.end_fragment()

		f42 = MathTex('P(a \le x < b) ').scale(0.8).next_to(f40, DOWN*1.2, aligned_edge=LEFT)
		f43 = MathTex('= \int_{a}^{b} f(x) \,dx').scale(0.8).next_to(f42, RIGHT*0.4)
		self.play(TransformFromCopy(f36, f42))
		self.play(TransformFromCopy(f40, f43))
		self.end_fragment()

		self.play(Unwrite(VGroup(f36, f37, f40, f41, f42, f43)))
		self.play(Write(f32))
		self.end_fragment()
		
		f38 = MathTex('\\text{If}\, x_{0}\le x_{1}, then\, F(x_{0})\le F(x_{1})').scale(
			0.8).next_to(f32, DOWN*1.2, aligned_edge=LEFT)
		self.play(Write(f38))
		self.end_fragment()

		self.play(Unwrite(f38))
		self.play(Write(f33))
		pl12 = polygon_from_arr(darr6, ax6, [0, 0.5]).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		self.play(Write(pl12))
		f39 = MathTex('S = ').scale(0.8).shift(UP*2+LEFT*1.5)
		num2 = DecimalNumber(sarr6[math.floor(0.5*192)]).scale(0.8).next_to(f39, RIGHT*0.3)
		self.play(Write(VGroup(f39, num2)))
		self.end_fragment(fragment_type=NO_PAUSE)

		transform_graph([0, 0.5], [0, 0.7], pl12, num2, 60, 0.02)
		self.wait()

		transform_graph([0, 0.7], [0, 0.2], pl12, num2, 60, 0.02)
		self.wait()

		transform_graph([0, 0.2], [0, 0.5], pl12, num2, 60, 0.02)
		self.wait()
		self.end_fragment(fragment_type=LOOP)

		self.play(Write(f34))
		transform_graph([0, 0.5], [0, 0.999], pl12, num2, 60, 0.02)
		self.end_fragment()

		self.play(Unwrite(VGroup(text2, ax5, pl10, pl12, f30, f39, num2)))

		t4 = Text('Зміст', font_size=42).move_to(UP*3)
		t5 = Text('1. Визначення НВВ', font_size=32)
		t6 = Text('2. Властивості функцій розподілу', font_size=32)
		t7 = Text('3. Числові властивості НВВ', font_size=32)
		t8 = Text('4. Основні розподіли НВВ', font_size=32)
		text3 = VGroup(t5, t6, t7, t8).arrange(direction=DOWN, buff=0.5)
		self.play(Write(VGroup(t4, t5, t7, t8)), Transform(t3, t6))
		self.end_fragment()

		t9 = Text('3. Числові властивості НВВ', font_size=42).align_on_border(UL)
		self.play(Transform(t7, t9, run_time=2.5), Unwrite(VGroup(t4, t5, t3, t8)))
		self.end_fragment()

class NumericalMean(PresentationScene):
	def construct(self):
		t1 = Text('3. Числові властивості НВВ', font_size=42).align_on_border(UL)
		self.add(t1)
		
		t2 = Text('3.1 Математичне сподівання', font_size=32).align_on_border(UL)
		self.play(Transform(t1, t2))
		self.end_fragment()

		f1 = MathTex('M(X) = ')
		f2 = MathTex('\sum_{i = 1}^{\infty }')
		f3 = MathTex('x_{i}')
		f4 = MathTex('p_{i}')
		text1 = VGroup(f1, f2, f3, f4).arrange(RIGHT, buff=0.2).shift(UP)
		self.play(Write(text1))
		self.end_fragment()

		f5 = MathTex('M(X) = ')
		f6 = MathTex('\int_{-\infty}^{\infty}')
		f7 = MathTex('x')
		f8 = MathTex('f(x)\, dx')
		text2 = VGroup(f5, f6, f7, f8).arrange(RIGHT, buff=0.2).shift(DOWN)
		self.play(TransformFromCopy(f1, f5))
		self.end_fragment()
		self.play(TransformFromCopy(f2, f6))
		self.end_fragment()
		self.play(TransformFromCopy(f3, f7))
		self.end_fragment()
		self.play(TransformFromCopy(f4, f8))
		self.end_fragment()

		f9 = MathTex('\int_{a}^{b}').align_to(f6, UP)
		self.play(Transform(f6, f9))
		self.end_fragment()
		f10 = MathTex('\int_{-\infty}^{\infty}').align_to(f6, UP)
		self.play(Transform(f6, f10))

		self.play(text2.animate.next_to(t2, DOWN*2, aligned_edge=LEFT), Unwrite(text1))

		def polygon_from_arr(arr, ax, x_range, to_0 = True):
			num_range = [x_range[0], x_range[1]]
			if x_range[0] < 0:
				num_range[0] = 0
			if x_range[1] > 1:
				num_range[1] = 1
			start_i = 0 if x_range[0] < 0 else math.floor(x_range[0]*len(arr))
			end_i =  len(arr)-1 if x_range[1] > 1 else math.ceil(x_range[1]*(len(arr)-1))
			coord = []
			if to_0:
				coord.extend([[x_range[0], 0], [x_range[0], arr[start_i]]])
			coord.extend(list(map(lambda i: [num_range[0] + (i-start_i)*(num_range[1] - num_range[0])/(end_i - start_i), arr[i]], range(start_i, end_i))))		
			coord.append([x_range[1], arr[end_i]])
			coord.append([x_range[1], 0 if to_0 else arr[start_i]])
			return Polygon(*ax.coords_to_point(coord), color=YELLOW).set_fill(YELLOW, opacity=0.7)

		def calculate_integral(arr):
			s = 0
			res = []
			for el in arr:
				s+=el
				res.append(s)
			return res

		n = 500
		arr1 = np.array([math.exp(-((x-125)*9/n)**2)/2 + math.exp(-((x-325)*5/n)**2) for x in range(n)])
		sum = arr1.sum()
		arr1 = arr1/sum
		sarr1 = calculate_integral(arr1)
		darr1 = arr1*n/4

		ax1 = Axes([0, 4], y_range=[0, 0.51, 0.1], x_length=5, y_length=3, 
			y_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False},
			x_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(DOWN)
		ax2 = Axes([0, 1], y_range=[0, 0.51, 0.1], x_length=5, y_length=3, 
			y_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False},
			x_axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(DOWN)
		pl1 = polygon_from_arr(darr1, ax2, [0, 1])
		self.play(Write(VGroup(ax1, pl1)))
		self.end_fragment()

		M = 0
		for i in range(n):
			M += arr1[i] * i
		M = M*4/n
		f11 = MathTex('M(X) = ').shift(RIGHT*2+UP*2)
		num1 = DecimalNumber(M).next_to(f11, RIGHT*0.3)
		l1 = Line(ax1.coords_to_point(*(M, 0, 0)), ax1.coords_to_point(*(M, 0.51, 0)), color=RED, stroke_width=6)
		l1t = MathTex('M(X)', font_size=32, color=RED).shift(ax1.coords_to_point(*(M, -0.15)))

		self.play(Write(VGroup(f11, num1, l1, l1t)))
		self.end_fragment()

		f12 = MathTex('\overline{X} = ').shift(LEFT*6 + DOWN)
		num2 = DecimalNumber(0).next_to(f12, RIGHT*0.3)
		self.play(Write(VGroup(f12, num2)))

		l2 = Line(ax1.coords_to_point(*(0, 0, 0)), ax1.coords_to_point(*(0, 0.51, 0)), color=GREEN, stroke_width=6)
		l2t = MathTex('\overline{X}', font_size=32, color=GREEN).shift(ax1.coords_to_point(*(0, -0.2)))
		self.end_fragment(fragment_type=NO_PAUSE)

		current_total = 0
		for i in range(60):
			srand = random.random()
			res = -1
			for j in range(n):
				if(srand < sarr1[j]):
					res = j*4/n
					break
			l3 = Line(ax1.coords_to_point(*(res, 0, 0)), ax1.coords_to_point(*(res, 0.51, 0)), color=BLUE, stroke_width=4)
			l3t = MathTex('x', font_size=32).shift(ax1.coords_to_point(*(res, 0.6)))
			self.play(Write(VGroup(l3, l3t)))
			current_total += res
			avg = current_total/(i+1)
			num2.set_value(avg)
			l4 = Line(ax1.coords_to_point(*(avg, 0, 0)), ax1.coords_to_point(*(avg, 0.51, 0)), color=GREEN, stroke_width=6)
			l4t = MathTex('\overline{X}', font_size=32, color=GREEN).shift(ax1.coords_to_point(*(avg, -0.2)))
			self.play(Transform(l3t, num2), Unwrite(l3), Transform(l2, l4), Transform(l2t, l4t))
			self.remove(l3t)
		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(l2, l2t, f11, num1, f12, num2)))
		ax2.shift(LEFT*3.5)
		self.play(VGroup(ax1, pl1, l1, l1t).animate.shift(LEFT*3.5))
		self.end_fragment()

		f13 = MathTex('1.\,M(C) = C\,, C = const')
		f14 = MathTex('2.\,M(CX) = C M(X)')
		f15 = MathTex('3.\,M(\sum_{i=1}^{n}X_{i}) = \sum_{i=1}^{n}M(X_{i})')
		f16 = MathTex('4.\,M(aX + b) = a M(x) + b')
		f17 = MathTex('5.\,M(XY) = M(X) M(Y)')
		f18 = MathTex('6.\,M(X) = 0,\,if\, f(x) = f(-x)')
		text3 = VGroup(f13, f14, f15, f16, f17, f18).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT*3.3)

		self.play(Write(f13))
		self.end_fragment()
		f19 = MathTex('X\\neq f(x)!').next_to(f13, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f19))
		self.end_fragment()
		
		self.play(Unwrite(f19))
		self.play(Write(f14))
		self.end_fragment()

		f14_1 = MathTex('M(CX) = \int_{-\infty}^{\infty}C x f(x)dx').scale(0.9).next_to(f14, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f14_1))
		self.end_fragment()

		f14_2 = MathTex('M(CX) = C\int_{-\infty}^{\infty}x f(x)dx').scale(0.9).next_to(f14_1, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f14_1, f14_2))
		self.end_fragment()

		f14_3 = MathTex('M(CX) = CM(X)').scale(0.9).next_to(f14_2, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f14_2, f14_3))
		self.end_fragment()
		self.play(Unwrite(VGroup(f14_1, f14_2, f14_3)))

		f20 = MathTex('C = ').next_to(f14, DOWN*1.4, aligned_edge=LEFT)
		num3 = DecimalNumber(1).next_to(f20, RIGHT*0.4)
		self.play(Write(VGroup(f20, num3)))
		self.end_fragment()

		darr2 = np.concatenate((darr1, np.zeros(n)))
		for i in range(81):
			multilpyer = 1 + (rate_functions.smooth(i/80))
			cutarr = darr2[0:math.floor(n/multilpyer)]/multilpyer
			pl2 = polygon_from_arr(cutarr, ax2, [0, 1])
			num3.set_value(multilpyer)
			l1.move_to((ax1.coords_to_point(*(M*multilpyer, 0, 0))[0],l1.get_y(), 0))
			l1t.move_to((ax1.coords_to_point(*(M*multilpyer, 0, 0))[0],l1t.get_y(), 0))
			self.play(Transform(pl1, pl2, run_time=0.02))

		self.wait()	

		for i in range(81):
			multilpyer = 2 - 1.5*(rate_functions.smooth(i/80))
			cutarr = darr2[0:math.floor(n/multilpyer)]/multilpyer
			pl2 = polygon_from_arr(cutarr, ax2, [0, 1])
			num3.set_value(multilpyer)
			l1.move_to((ax1.coords_to_point(*(M*multilpyer, 0, 0))[0],l1.get_y(), 0))
			l1t.move_to((ax1.coords_to_point(*(M*multilpyer, 0, 0))[0],l1t.get_y(), 0))
			self.play(Transform(pl1, pl2, run_time=0.02))

		self.wait()

		for i in range(81):
			multilpyer = 0.5 + 0.5*(rate_functions.smooth(i/80))
			cutarr = darr2[0:math.floor(n/multilpyer)]/multilpyer
			pl2 = polygon_from_arr(cutarr, ax2, [0, 1])
			num3.set_value(multilpyer)
			l1.move_to((ax1.coords_to_point(*(M*multilpyer, 0, 0))[0],l1.get_y(), 0))
			l1t.move_to((ax1.coords_to_point(*(M*multilpyer, 0, 0))[0],l1t.get_y(), 0))
			self.play(Transform(pl1, pl2, run_time=0.02))
		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(f20, num3)))
		self.play(Write(f15))
		self.end_fragment()

		self.play(Unwrite(pl1))
		f21 = MathTex('M(\sum_{i=1}^{1}X_{i}) = 0.5').next_to(f15, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f21))

		ax3 = Axes([0, 4], y_range=[0, 1, 0.2], x_length=5, y_length=3, 
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}
			).shift(DOWN + LEFT*3.5)
		ax4 = Axes([0, 1], y_range=[0, 1], x_length=5, y_length=3).shift(DOWN + LEFT*3.5)
		ax5 = ax1.copy()
		self.play(Transform(ax1, ax3))
		darr3 = np.full(100, 1)
		pl5 = polygon_from_arr(darr3, ax3, [0, 1])
		self.play(Write(pl5))
		self.remove(VGroup(l1, l1t))
		self.add(l1, l1t)
		self.play(l1.animate.move_to((ax1.coords_to_point(*(0.5, 0, 0))[0],l1.get_y(), 0)),
			l1t.animate.move_to((ax1.coords_to_point(*(0.5, 0, 0))[0],l1t.get_y(), 0)))
		self.end_fragment()

		def convolution(arr1, arr2):
			res = []
			for i in range(len(arr1)+len(arr2)):
				s = 0
				for j in range(len(arr1)):
					if i - j >= 0 and i - j < len(arr2):
						s += arr1[j]*arr2[i-j]
				res.append(s)
			sum = np.array(res).sum()
			return	np.array(res)*50/sum
		
		darr4 = convolution(darr3, darr3)
		pl6 = polygon_from_arr(np.concatenate((darr4, np.zeros(200))), ax4, [0, 0.5])
		f22 = MathTex('M(\sum_{i=1}^{2}X_{i}) = 1').next_to(f15, DOWN*1.4, aligned_edge=LEFT)
		self.play(Transform(f21, f22))
		self.play(Transform(pl5, pl6),
			l1.animate.move_to((ax1.coords_to_point(*(1, 0, 0))[0],l1.get_y(), 0)),
			l1t.animate.move_to((ax1.coords_to_point(*(1, 0, 0))[0],l1t.get_y(), 0)))
		self.end_fragment()

		darr5 = convolution(darr3, darr4)
		pl7 = polygon_from_arr(np.concatenate((darr5, np.zeros(100))), ax4, [0, 0.75])
		f23 = MathTex('M(\sum_{i=1}^{3}X_{i}) = 1.5').next_to(f15, DOWN*1.4, aligned_edge=LEFT)
		self.play(Transform(f21, f23))
		self.play(Transform(pl5, pl7),
			l1.animate.move_to((ax1.coords_to_point(*(1.5, 0, 0))[0],l1.get_y(), 0)),
			l1t.animate.move_to((ax1.coords_to_point(*(1.5, 0, 0))[0],l1t.get_y(), 0)))
		self.end_fragment()

		darr6 = convolution(darr3, darr5)
		pl8 = polygon_from_arr(darr6, ax4, [0, 1])
		f24 = MathTex('M(\sum_{i=1}^{4}X_{i}) = 2').next_to(f15, DOWN*1.4, aligned_edge=LEFT)
		self.play(Transform(f21, f24))
		self.play(Transform(pl5, pl8),
			l1.animate.move_to((ax1.coords_to_point(*(2, 0, 0))[0],l1.get_y(), 0)),
			l1t.animate.move_to((ax1.coords_to_point(*(2, 0, 0))[0],l1t.get_y(), 0)))
		self.end_fragment()
		ax9 = Axes([0, 4], [0, 0.41, 0.1], x_length=5, y_length= 3, 
			 axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(DOWN+LEFT*3.5)
		ax6 = Axes([0, 1], [0, 0.41], x_length=5, y_length= 3).shift(DOWN+LEFT*3.5)
		pl9 = polygon_from_arr(darr6, ax6, [0, 1])
		self.play(Transform(ax1, ax9), Transform(pl5, pl9))
		# darr7 = np.array([math.exp(-((x/42.5-2.31)**2))/3 for x in range(200)])
		# pl10 = polygon_from_arr(darr7, ax6, [0, 1]).set_color(WHITE).set_fill(opacity=0)
		# self.play(Write(pl10))
		self.end_fragment()

		self.play(Unwrite(VGroup(f21, pl5)), Transform(ax1, ax5))
		self.play(Write(f16))

		pl10 = polygon_from_arr(darr1, ax2, [0, 1])
	
		self.play(Write(pl10),
			l1.animate.move_to((ax1.coords_to_point(*(M, 0, 0))[0],l1.get_y(), 0)),
			l1t.animate.move_to((ax1.coords_to_point(*(M, 0, 0))[0],l1t.get_y(), 0)))
		self.remove(VGroup(l1, l1t))
		self.add(VGroup(l1, l1t))
		self.end_fragment()
		f25 = MathTex('a = ').next_to(f16, DOWN*1.4, aligned_edge=LEFT)
		num4 = DecimalNumber(1).next_to(f25, RIGHT*0.4)
		f26 = MathTex('b = ').next_to(f25, DOWN*1.4, aligned_edge=LEFT)
		num5 = DecimalNumber(0).next_to(f26, RIGHT*0.4)
		self.play(Write(VGroup(f25, num4, f26, num5)))
		self.end_fragment(fragment_type=NO_PAUSE)

		for i in range(81):
			multilpyer = 1 + (rate_functions.smooth(i/80))*0.5
			shift = 0
			cutarr = darr2[math.floor(shift*n/4/multilpyer):math.floor((4 + shift)*n/4/multilpyer)]/multilpyer
			pl11 = polygon_from_arr(cutarr, ax2, [0, 1])
			num4.set_value(multilpyer)
			num5.set_value(-shift)
			l1.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1.get_y(), 0))
			l1t.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1t.get_y(), 0))
			self.play(Transform(pl10, pl11, run_time=0.02))

		self.wait()

		for i in range(81):
			multilpyer = 1.5
			shift = 0 + rate_functions.smooth(i/80)*2
			cutarr = darr2[math.floor(shift*n/4/multilpyer):math.floor((4 + shift)*n/4/multilpyer)]/multilpyer
			pl11 = polygon_from_arr(cutarr, ax2, [0, 1])
			num4.set_value(multilpyer)
			num5.set_value(-shift)
			l1.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1.get_y(), 0))
			l1t.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1t.get_y(), 0))
			self.play(Transform(pl10, pl11, run_time=0.02))
		self.wait()

		for i in range(81):
			multilpyer = 1.5 - rate_functions.smooth(i/80)*0.8
			shift = 2 - rate_functions.smooth(i/80)*3
			if(shift*n/4/multilpyer < 0):
				cutarr = np.concatenate((np.zeros(-math.floor(shift*n/4/multilpyer)),
					darr2[0:math.floor((4 + shift)*n/4/multilpyer)]/multilpyer))
			else:
				cutarr = darr2[math.floor(shift*n/4/multilpyer):math.floor((4 + shift)*n/4/multilpyer)]/multilpyer
			pl11 = polygon_from_arr(cutarr, ax2, [0, 1])
			num4.set_value(multilpyer)
			num5.set_value(-shift)
			l1.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1.get_y(), 0))
			l1t.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1t.get_y(), 0))
			self.play(Transform(pl10, pl11, run_time=0.02))
		self.wait()	

		for i in range(81):
			multilpyer = 0.7 + rate_functions.smooth(i/80)*0.3
			shift = - 1 + rate_functions.smooth(i/80)*1
			if(shift*n/4/multilpyer < 0):
				cutarr = np.concatenate((np.zeros(-math.floor(shift*n/4/multilpyer)),
					darr2[0:math.floor((4 + shift)*n/4/multilpyer)]/multilpyer))
			else:
				cutarr = darr2[math.floor(shift*n/4/multilpyer):math.floor((4 + shift)*n/4/multilpyer)]/multilpyer			
			pl11 = polygon_from_arr(cutarr, ax2, [0, 1])
			num4.set_value(multilpyer)
			num5.set_value(-shift)
			l1.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1.get_y(), 0))
			l1t.move_to((ax1.coords_to_point(*(M*multilpyer - shift, 0, 0))[0],l1t.get_y(), 0))
			self.play(Transform(pl10, pl11, run_time=0.02))

		self.end_fragment(fragment_type=LOOP)	

		self.play(Unwrite(VGroup(f25, num4, f26, num5)))
		self.play(Write(f17))
		f27 = Text('X та Y - незалежні').scale(0.8).next_to(f17, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f27))
		self.end_fragment()

		self.play(Unwrite(f27))
		self.play(Write(f18))
		self.play(Unwrite(pl10))
		ax7 = Axes([-2, 2], [0, 0.56, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(DOWN+LEFT*3.5)
		ax8 = Axes([0, 1], [0, 0.56, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(DOWN+LEFT*3.5)
		self.play(Transform(ax1, ax7))
		arr2  = np.array([math.exp(-((4*x/n-2)**4)) for x in range(n)])
		darr8 = arr2*n/4/arr2.sum()
		pl11 = polygon_from_arr(darr8, ax8, [0, 1])
		self.play(Write(pl11),
			l1.animate.move_to((ax1.coords_to_point(*(0, 0, 0))[0],l1.get_y(), 0)),
			l1t.animate.move_to((ax1.coords_to_point(*(0, 0, 0))[0],l1t.get_y(), 0)))
		self.remove(l1, l1t)
		self.add(l1, l1t)
		self.end_fragment()

		t3 = Text('3.2 Дисперсія', font_size=32).align_on_border(UL)
		self.play(Unwrite(VGroup(text3, text2, l1, l1t, pl11, ax1)))
		self.end_fragment()

	

		
class NumericalVariance(PresentationScene):
	def construct(self):
		def polygon_from_arr(arr, ax, x_range, to_0 = True):
			num_range = [x_range[0], x_range[1]]
			if x_range[0] < 0:
				num_range[0] = 0
			if x_range[1] > 1:
				num_range[1] = 1
			start_i = 0 if x_range[0] < 0 else math.floor(x_range[0]*len(arr))
			end_i =  len(arr)-1 if x_range[1] > 1 else math.ceil(x_range[1]*(len(arr)-1))
			coord = []
			if to_0:
				coord.extend([[x_range[0], 0], [x_range[0], arr[start_i]]])
			coord.extend(list(map(lambda i: [num_range[0] + (i-start_i)*(num_range[1] - num_range[0])/(end_i - start_i), arr[i]], range(start_i, end_i))))		
			coord.append([x_range[1], arr[end_i]])
			coord.append([x_range[1], 0 if to_0 else arr[start_i]])
			return Polygon(*ax.coords_to_point(coord), color=YELLOW).set_fill(YELLOW, opacity=0.7)
		
		t1 = Text('3.1 Математичне сподівання', font_size=32).align_on_border(UL)
		t0 = Text('3.2 Дисперсія', font_size=32).align_on_border(UL)
		self.add(t1)
		self.play(Transform(t1, t0))
		
		n = 500
		arr1 = np.array([1 if x > n/4 and x < 3*n/4 else 4*x/n if x < n/2 else 4*(n - x)/n  for x in range(n) ])
		darr1 = arr1*n/4/arr1.sum()
		ax1 = Axes(x_range=[0, 4], y_range=[0, 0.4, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN)
		ax2 = Axes(x_range=[0, 1], y_range=[0, 0.4], x_length=5, y_length=3,).shift(LEFT*3.5 + DOWN)
		ax3 = Axes(x_range=[0, 4], y_range=[0, 0.4, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(RIGHT*4 + DOWN)
		ax4 = Axes(x_range=[0, 1], y_range=[0, 0.4], x_length=5, y_length=3,).shift(RIGHT*4 + DOWN)
		ax_3 = Axes(x_range=[-2, 2], y_range=[0, 0.4, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(RIGHT*4 + DOWN)


		pl1 = polygon_from_arr(darr1, ax2, [0, 1])
		self.play(Write(ax1))
		self.play(Write(pl1))
		self.end_fragment()
		f1 = MathTex('|x - M(X)|f(x)', substrings_to_isolate=['|','x - M(X)', 'f(X)']).shift(2*UP)
		f_1 = MathTex('|x - M(X)|f(x)',).shift(2*UP)
		f2 = MathTex('[x - M(X)]^{2}f(x)', substrings_to_isolate=['[x - M(X)]^{2}']).shift(2*UP)
		f_2 = MathTex('M([x - M(X)]^{2})', substrings_to_isolate=['[x - M(X)]^{2}']).shift(2*UP+LEFT*0.5)
		f3 = MathTex('|x - M(X)|^{3}f(x)').shift(2*UP)
		f4 = MathTex('[x - M(X)]^{4}f(x)').shift(2*UP)
		f5 = MathTex('[x - M(X)]^{2}f(x)').shift(2*UP)
		f6 = MathTex('D(X) = \int_{a}^{b}[x - M(X)]^{2}f(x)dx', substrings_to_isolate=['[x - M(X)]^{2}f(x)']).shift(2*UP+LEFT)
		
		self.play(Write(f1[1]))
		arrow1 = Arrow(start=LEFT+DOWN, end=RIGHT+DOWN)
		self.play(Write(arrow1))
		pl_2 = polygon_from_arr(darr1, ax4, [0, 1])
		self.play(Write(VGroup(pl_2, ax_3)))
		self.end_fragment()

		self.play(Write(f1[0]), Write(f1[2]))
		ax_4 = Axes(x_range=[0, 4], y_range=[0, 0.8, 0.2], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(RIGHT*4 + DOWN)
		darr_2 = np.concatenate((darr1[math.floor(n/2):n],np.zeros(math.floor(n/2))))
		pl_3 = polygon_from_arr(darr_2, ax4, [0, 0.5])
		self.play(Transform(ax_3, ax_4), Transform(pl_2, pl_3))
		self.end_fragment()

		group0 = VGroup(f1[0], f1[1], f1[2])
		self.play(Transform(group0, f_2[1]))
		darr_3 = np.array([darr_2[math.floor(math.sqrt(i/n)*n/2)] for i in range(n)])
		pl_4 = polygon_from_arr(darr_3, ax4, [0, 1])
		self.play(Transform(pl_2, pl_4))
		self.end_fragment()

		self.play(Write(VGroup(f_2[0], f_2[2])))
		self.end_fragment()

		arr2 = np.array([4*abs(i - n/2)/n*darr1[i] for i in range(n)])
		pl2 = polygon_from_arr(arr2, ax4, [0, 1])
		arr3 = np.array([(4*(i - n/2)/n)**2*darr1[i] for i in range(n)])
		pl3 = polygon_from_arr(arr3, ax4, [0, 1])

		group1 = VGroup(group0, f_2[0], f_2[2])
		self.play(Transform(group1, f2))
		self.play(Unwrite(pl_2))
		self.play(Transform(ax_3, ax3))
		self.play(Write(pl3))
		self.end_fragment()

		self.play(Transform(group1, f_1))
		self.play(Transform(pl3, pl2))
		self.end_fragment()

		self.play(Transform(group1, f3))
		arr4 = np.array([(4*abs(i - n/2)/n)**3*darr1[i] for i in range(n)])
		pl4 = polygon_from_arr(arr4, ax4, [0, 1])
		self.play(Transform(pl3, pl4))
		self.end_fragment()

		self.play(Transform(group1, f4))
		arr5 = np.array([(4*(i - n/2)/n)**4*darr1[i] for i in range(n)])
		pl5 = polygon_from_arr(arr5, ax4, [0, 1])
		self.play(Transform(pl3, pl5))
		self.end_fragment()

		self.play(Transform(group1, f5))
		pl6 = polygon_from_arr(arr3, ax4, [0, 1])
		self.play(Transform(pl3, pl6))
		self.end_fragment()

		self.play(Write(VGroup(f6[0], f6[2])))
		var1 = arr3.sum()/n*4
		num1 = DecimalNumber(var1).next_to(f6, RIGHT*4)
		arrow2 = Arrow(start=ORIGIN, end=2*UP).next_to(num1, 2*DOWN)
		self.play(Write(VGroup(arrow2, num1)))
		self.end_fragment()

		arr6 = np.array([ 0.5 if x > n/4 and x < 3*n/4 else 1 - 2*x/n if x < n/2 else 1 - 2*(n - x)/n  for x in range(n) ])
		darr2 = arr6*n/4/arr6.sum()
		pl7 = polygon_from_arr(darr2, ax2, [0, 1])
		arr7 =  np.array([(4*(i - n/2)/n)**2*darr2[i] for i in range(n)])
		ax7 = ax3.copy()
		ax5 = Axes(x_range=[0, 4], y_range=[0, 1.5, 0.3], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(RIGHT*4 + DOWN)
		ax6 = Axes(x_range=[0, 1], y_range=[0, 1.5], x_length=5, y_length=3,).shift(RIGHT*4 + DOWN)
		pl8 = polygon_from_arr(arr7, ax6, [0, 1])
		var2 = 4*arr7.sum()/n
		self.play(Transform(pl1, pl7), Transform(pl3, pl8), Transform(ax_3, ax5), 
			ChangingDecimal(num1, lambda alpha: var1 + (var2 - var1)* alpha))
		self.wait(5)

		arr8 = np.array([math.exp(-((x-125)*9/n)**2)/2 + math.exp(-((x-325)*5/n)**2) for x in range(n)])
		darr3 = arr8*n/4/arr8.sum()
		pl9 = polygon_from_arr(darr3, ax2, [0, 1])
		arr9 =  np.array([((4*i - 2.24*n)/n)**2*darr3[i] for i in range(n)])
		pl10 = polygon_from_arr(arr9, ax4, [0, 1])
		var3 = 4*arr9.sum()/n
		self.play(Transform(pl1, pl9), Transform(pl3, pl10), Transform(ax_3, ax7), 
			ChangingDecimal(num1, lambda alpha: var2 + (var3 - var2)* alpha))
		self.wait(5)

		pl11 = polygon_from_arr(darr1 ,ax2, [0, 1])
		pl12 = polygon_from_arr(arr3, ax4, [0, 1])
		self.play(Transform(pl1, pl11), Transform(pl3, pl12), 
			ChangingDecimal(num1, lambda alpha: var3 + (var1 - var3)* alpha))
		self.wait(5)
		self.end_fragment(fragment_type=LOOP)

		self.remove(f2, group1)
		f7 = MathTex('D(X)=\,').next_to(t1, DOWN, buff=1.5, aligned_edge=LEFT)
		self.play(f6.animate.scale(0.8).next_to(t1, DOWN, aligned_edge=LEFT), 
			Write(f7),num1.animate.next_to(f7, RIGHT),
			Unwrite(VGroup(pl3, ax_3, arrow2, arrow1)))

		f8 = MathTex('1.\, D(C) = 0,\, C = const')
		f9 = MathTex('2.\, D(C+X)=D(X)')
		f10 = MathTex('3.\, D(CX)=C^{2}D(X)')
		f11 = MathTex('4.\, D(X)=M(X^{2})-M(X)^{2}')
		f12 = MathTex('5.\, D(\sum_{i=1}^{n}X_{i})=\sum_{i=1}^{n}D(X_{i})')
		f13 = MathTex('6.\, D(X - Y)= D(X) + D(Y)')
		text1 = VGroup(f8, f9, f10, f11, f12, f13).arrange(DOWN, buff=0.5, aligned_edge=LEFT).align_on_border(RIGHT)
		self.play(Write(f8))
		self.end_fragment()

		f8_0 = MathTex('D(X) = M([X - M(X)]^{2})').scale(0.8).next_to(f8, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f8_0))
		self.end_fragment()

		f8_1 = MathTex('D(C) = M([C - M(C)]^{2})').scale(0.8).next_to(f8_0, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f8_0, f8_1))
		self.end_fragment()

		f8_2 = MathTex('D(C) = M([C - C]^{2})').scale(0.8).next_to(f8_1, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f8_1, f8_2))
		self.end_fragment()

		f8_3 = MathTex('D(C) = M([0]^{2})').scale(0.8).next_to(f8_2, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f8_2, f8_3))
		self.end_fragment()

		f8_4 = MathTex('D(C) = 0').scale(0.8).next_to(f8_3, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f8_3, f8_4))
		self.end_fragment()

		self.play(Unwrite(VGroup(f8_0, f8_1, f8_2, f8_3, f8_4)))
		self.play(Write(f9))
		self.end_fragment()

		f9_1 = MathTex('D(X) = M([X - M(X)]^{2})').scale(0.8).next_to(f9, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f9_1))
		self.end_fragment()

		f9_2 = MathTex('D(X + C) = M([X + C - M(X + C)]^{2})').scale(0.8).next_to(f9, DOWN*1.4, aligned_edge=LEFT)
		self.play(Transform(f9_1, f9_2))
		self.end_fragment()

		f9_3 = MathTex('D(X + C) = M([X + C - M(X) - C]^{2})').scale(0.8).next_to(f9_2, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f9_2, f9_3))
		self.end_fragment()

		f9_4 = MathTex('D(X + C) = M([X - M(X)]^{2})').scale(0.8).next_to(f9_3, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f9_3, f9_4))
		self.end_fragment()

		f9_5 = MathTex('D(X + C) = D(X)').scale(0.8).next_to(f9_4, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f9_4, f9_5))
		self.end_fragment()

		self.play(Unwrite(VGroup(f9_1, f9_2, f9_3, f9_4, f9_5)))

		ax8 = Axes(x_range=[0, 10], y_range=[0, 0.4, 0.1], x_length=5, y_length=3,
			 axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5+DOWN)
		ax1c = ax1.copy()
		self.play(pl1.animate.stretch(0.4, 0, about_edge=LEFT), Transform(ax1, ax8))
		f9_6 = MathTex('C =\,').next_to(f9, DOWN*1.4, aligned_edge=LEFT)
		num2 = DecimalNumber(0).next_to(f9_6, RIGHT)
		f9_7 = MathTex('D(X+C) =\,').align_to(f7,UL)
		f7c = f7.copy()
		self.play(Write(VGroup(f9_6, num2)), Transform(f7, f9_7), num1.animate.next_to(f9_7, RIGHT))
		self.end_fragment(fragment_type=NO_PAUSE)

		self.play(pl1.animate.shift(ax8.c2p(*(RIGHT*6)) - ax8.c2p(*ORIGIN)), 
			ChangingDecimal(num2, lambda alpha: 0 + (6 - 0)* alpha))
		self.wait()
		self.play(pl1.animate.shift(ax8.c2p(*(LEFT*4)) - ax8.c2p(*ORIGIN)), 
			ChangingDecimal(num2, lambda alpha: 6 + (2 - 6)* alpha))
		self.wait()
		self.play(pl1.animate.shift(ax8.c2p(*(LEFT*2)) - ax8.c2p(*ORIGIN)), 
			ChangingDecimal(num2, lambda alpha: 2 + (0 - 2)* alpha))
		self.end_fragment(fragment_type=LOOP)
		
		self.play(Unwrite(VGroup(f9_6, num2)), Transform(f7, f7c), num1.animate.next_to(f7c, RIGHT))
		self.play(Write(f10))
		self.end_fragment()
		f10_1 = MathTex('D(CX) = M([CX - M(CX)]^{2})').scale(0.8).next_to(f10, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f10_1))
		self.end_fragment()

		f10_2 = MathTex('D(CX) = M([CX - CM(X)]^{2})').scale(0.8).next_to(f10_1, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f10_1, f10_2))
		self.end_fragment()
		
		f10_3 = MathTex('D(CX) = M(C^{2}[X - M(X)]^{2})').scale(0.8).next_to(f10_2, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f10_2, f10_3))
		self.end_fragment()
		
		f10_4 = MathTex('D(CX) = C^{2}M([X - M(X)]^{2})').scale(0.8).next_to(f10_3, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f10_3, f10_4))
		self.end_fragment()

		f10_5 = MathTex('D(CX) = C^{2}D(X)^{2}').scale(0.8).next_to(f10_4, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f10_4, f10_5))
		self.end_fragment()

		self.play(Unwrite(VGroup(f10_1, f10_2, f10_3, f10_4, f10_5)))

		f10_6 = MathTex('C = \,').next_to(f10, DOWN*1.4, aligned_edge=LEFT)
		num3 = DecimalNumber(1).next_to(f10_6)
		f10_7 = MathTex('D(CX) =\,').align_to(f7c,UL)
		self.play(Write(VGroup(f10_6, num3)), Transform(f7, f10_7), num1.animate.next_to(f10_7, RIGHT))
		self.end_fragment(fragment_type=NO_PAUSE)

		self.play(pl1.animate.stretch(2.5, 0, about_edge=LEFT).stretch(0.4, 1, about_edge=DOWN), 
			ChangingDecimal(num3, lambda alpha: 1 + (2.5 - 1)* alpha),
			ChangingDecimal(num1, lambda alpha: (1 + (2.5 - 1)* alpha)**2*var1))
		self.wait()
		self.play(pl1.animate.stretch(0.4/2.5, 0, about_edge=LEFT).stretch(2.5/0.4, 1, about_edge=DOWN), 
			ChangingDecimal(num3, lambda alpha: 2.5 + (0.4 - 2.5)* alpha),
			ChangingDecimal(num1, lambda alpha: (2.5 + (0.4 - 2.5)* alpha)**2*var1))
		self.wait()
		self.play(pl1.animate.stretch(1/0.4, 0, about_edge=LEFT).stretch(0.4/1, 1, about_edge=DOWN), 
			ChangingDecimal(num3, lambda alpha: 0.4 + (1 - 0.4)* alpha),
			ChangingDecimal(num1, lambda alpha: (0.4 + (1 - 0.4)* alpha)**2*var1))
		self.wait()

		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(f10_6, num3)), Transform(f7, f7c), num1.animate.next_to(f7c, RIGHT))		
		self.play(Write(f11))
		self.end_fragment()
		
		self.play(Write(f12))

		def convolution(arr1, arr2):
			res = []
			for i in range(len(arr1)+len(arr2)):
				s = 0
				for j in range(len(arr1)):
					if i - j >= 0 and i - j < len(arr2):
						s += arr1[j]*arr2[i-j]
				res.append(s)
			return np.array(res)
		
		f8c = f8.copy()
		f9c = f9.copy()
		f10c = f10.copy()
		self.play(Unwrite(VGroup(f8, f9, f10)))
		self.play(VGroup(f11, f12).animate.shift(UP*3))
		f12_1 = MathTex('=M([X+Y]^{2}) - [M(X+Y)]^{2} =').scale(0.8).next_to(f12, DOWN*1.4, aligned_edge=LEFT).shift(LEFT*0.5)
		f12_2 = MathTex('D(X+Y)\,').scale(0.8).next_to(f12_1, LEFT)
		self.play(Write(VGroup(f12_2, f12_1)))
		self.end_fragment()

		f12_3 = MathTex('= M(X^{2}+2XY+Y^{2})-[M(X)+M(Y)]^{2} =').scale(0.7
			).next_to(f12_1, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f12_1, f12_3))
		self.end_fragment()

		f12_4 = MathTex('=M(X^{2})+M(2XY)+M(Y^{2})-').scale(0.8
			).next_to(f12_3, DOWN*1.4, aligned_edge=LEFT)
		f12_5 = MathTex('-M(X)^{2}-2M(X)M(Y)-M(Y)^{2} =').scale(0.8
			).next_to(f12_4, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f12_3, VGroup(f12_4, f12_5)))
		self.end_fragment()

		f12_6 = MathTex('=M(X^{2})-M(X)^{2} +').scale(0.7
			).next_to(f12_5, DOWN*1.4, aligned_edge=LEFT)
		f12_7 = MathTex('M(Y^{2})-M(Y)^{2}=').scale(0.7
			).next_to(f12_6, RIGHT, buff=0)
		self.play(TransformFromCopy(VGroup(f12_4, f12_5), VGroup(f12_6, f12_7)))
		self.end_fragment()

		f12_8 = MathTex('=D(X) + ').scale(0.8).next_to(f12_6, DOWN*1.4, aligned_edge=LEFT)
		f12_9 = MathTex('D(Y)').scale(0.8).next_to(f12_8, RIGHT, buff=0)
		self.play(TransformFromCopy(f12_6, f12_8))
		self.play(TransformFromCopy(f12_7, f12_9))
		self.end_fragment()

		self.play(Unwrite(VGroup(f12_1, f12_3, f12_4, f12_5, f12_6, f12_7)))
		self.play(VGroup(f12_8, f12_9).animate.next_to(f12_2, RIGHT))
		self.end_fragment()

		f12_10 = MathTex('D(X+Y+Z) = D(X) + D(Y+Z)').scale(0.8).next_to(f12_8, DOWN, aligned_edge=LEFT)
		self.play(Write(f12_10))
		self.end_fragment()

		f12_11 = MathTex('D(X+Y+Z) = D(X) + D(Y) + D(Z)').scale(0.8).next_to(f12_10, DOWN, aligned_edge=LEFT)
		self.play(TransformFromCopy(f12_10, f12_11))
		self.end_fragment()
		self.play(Unwrite(VGroup(f12_2, f12_8, f12_9, f12_10, f12_11)))

		self.play(Write(VGroup(f8c, f9c, f10c)), VGroup(f11, f12).animate.shift(DOWN*3))
		f12_7 = MathTex('D(X + X) =\,').align_to(f7c, UL)
		self.play(Transform(f7, f12_7), num1.animate.next_to(f12_7, RIGHT))

		darr4 = convolution(darr1, darr1)
		darr4 = darr4/darr4.sum()*n/8
		pl13 = polygon_from_arr(np.concatenate((darr4, np.zeros(math.floor(n/4)))), ax2, [0,0.8])
		self.play(Transform(pl1, pl13), ChangingDecimal(num1, lambda alpha: var1 + (2*var1 - var1)* alpha))
		self.end_fragment()

		f12_8 = MathTex('D(X+X+X)=\,').align_to(f7c, UL)
		self.play(Transform(f7, f12_8), num1.animate.next_to(f12_8, RIGHT))
		darr5 = convolution(darr4, darr1)
		darr5 =  darr5/darr5.sum()*n/12
		pl13 = polygon_from_arr(darr5[0:1000], ax2, [0, 1])
		self.play(Transform(pl1, pl13), ChangingDecimal(num1, lambda alpha: 2*var1 + (3*var1 - 2*var1)* alpha))
		self.end_fragment()

		self.play(Transform(pl1, pl11),
			Transform(ax1, ax1c),
			Transform(f7, f7c),
			num1.animate.next_to(f7c, RIGHT),
			ChangingDecimal(num1, lambda alpha: 3*var1 + (var1 - 3*var1)* alpha),
			Unwrite(f12_7))
		self.play(Write(f13))
		self.end_fragment()
		
		ax9 = Axes(x_range=[-4, 4], y_range=[0, 0.2, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN)
		f13_1 = MathTex('D(X - X) =\,').align_to(f7c, UL)
		pl14 = polygon_from_arr(darr4*2, ax2, [0,1])
		self.play(
			Transform(f7, f13_1),
			num1.animate.next_to(f13_1, RIGHT),
		)
		self.play(
			Transform(ax1, ax9),
			Transform(pl1, pl14),
			ChangingDecimal(num1, lambda alpha: var1 + (2*var1 - var1)* alpha),
		)
		self.end_fragment()
		
		self.play(
			Unwrite(VGroup(f7, num1, f8c, f9c, f11, f12, f13)),
			Transform(ax1, ax1c),
			Transform(pl1, pl11),
		)
		self.end_fragment()

		t2 = Text('3.3 Середнє квадратичне відхилення',font_size=32).align_on_border(UL)
		self.play(Transform(t1, t2))
		f14 = MathTex('\sigma(X) = \sqrt{D(X)}').next_to(f6, DOWN*1.2, aligned_edge=LEFT)
		self.play(Write(f14))
		self.end_fragment()

		self.play(Unwrite(VGroup(f6, f10c)))
		self.play(f14.animate.next_to(t1, DOWN*1.4, aligned_edge=LEFT))

		f15 = MathTex('\sigma(X) =\,').next_to(f14, DOWN*1.4, aligned_edge=LEFT)
		sigma1 = math.sqrt(var1)
		num4 = DecimalNumber(sigma1).next_to(f15, RIGHT)
		self.play(Write(VGroup(f15, num4)))
		self.end_fragment()

		f16 = MathTex('1.\, \sigma(C) = 0')
		f17 = MathTex('2.\, \sigma(C + X) = \sigma(X)')
		f18 = MathTex('3.\, \sigma(CX) = C\sigma(X)')
		f19 = MathTex('4.\, \sigma(\sum_{i=1}^{n}X_{i}) = \sqrt{\sum_{i=1}^{n}\sigma^{2}(X_{i})}')
		text2 = VGroup(f16, f17, f18, f19).arrange(DOWN, buff=0.6, aligned_edge=LEFT).shift(RIGHT*3)
		self.play(Write(f16))
		self.end_fragment()

		f16_1 = MathTex('\sigma(C) =  \sqrt{D(C)} =  \sqrt{0} = 0').scale(0.8).next_to(f16, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f16, f16_1))
		self.end_fragment()

		self.play(Unwrite(f16_1))
		self.play(Write(f17))
		self.end_fragment()

		f17_1 = MathTex('\sigma(X + C) = \sqrt{D(X + C)}').scale(0.9).next_to(f17, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f17_1))
		self.end_fragment()
		
		f17_2 = MathTex('\sigma(X + C) = \sqrt{D(X)}').scale(0.9).next_to(f17_1, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f17_1, f17_2))
		self.end_fragment()

		f17_3 = MathTex('\sigma(X + C) = \sigma(X)').scale(0.9).next_to(f17_2, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f17_2, f17_3))
		self.end_fragment()

		self.play(Unwrite(VGroup(f17_1, f17_2, f17_3)))
		self.play(Write(f18))
		self.end_fragment()

		f18_1 = MathTex('\sigma(CX) = \sqrt{D(CX)}').scale(0.9).next_to(f18, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f18_1))
		self.end_fragment()

		f18_2 = MathTex('\sigma(CX) = \sqrt{C^{2}D(X)}').scale(0.9).next_to(f18_1, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f18_1, f18_2))
		self.end_fragment()

		f18_3 = MathTex('\sigma(CX) = C\sqrt{D(X)}').scale(0.9).next_to(f18_2, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f18_2, f18_3))
		self.end_fragment()

		f18_4 = MathTex('\sigma(CX) = C\sigma(X)').scale(0.9).next_to(f18_3, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f18_3, f18_4))
		self.end_fragment()

		self.play(Unwrite(VGroup(f18_1, f18_2, f18_3, f18_4)))
		f18_5 = MathTex('C =\,').next_to(f18, DOWN*1.4, aligned_edge=LEFT)
		num5 = DecimalNumber(1).next_to(f18_5, RIGHT)
		
		f18_6 = MathTex('D(X) =\,').next_to(f18_5, DOWN*1.4, aligned_edge=LEFT)
		num6 = DecimalNumber(var1).next_to(f18_6, RIGHT)

		self.play(Write(VGroup(f18_5, num5, f18_6, num6)))
		ax10 = Axes(x_range=[0,40, 4], y_range=[0, 0.4, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN)
		self.play(Transform(ax1, ax10), pl1.animate.stretch(0.1, 0, about_edge=LEFT))
		self.end_fragment()

		self.play(
			pl1.animate.stretch(2, 0, about_edge=LEFT).stretch(0.5, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: sigma1 + (2*sigma1 - sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 1 + (2 - 1)* alpha),
			ChangingDecimal(num6, lambda alpha: (1 + (2 - 1)* alpha)**2*var1),
		)
		self.wait(2)

		self.play(
			pl1.animate.stretch(2, 0, about_edge=LEFT).stretch(0.5, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: 2*sigma1 + (4*sigma1 - 2*sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 2 + (4 - 2)* alpha),
			ChangingDecimal(num6, lambda alpha: (2 + (4 - 2)* alpha)**2*var1),
		)
		self.wait(2)

		self.play(
			pl1.animate.stretch(2.5, 0, about_edge=LEFT).stretch(0.4, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: 4*sigma1 + (10*sigma1 - 4*sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 4 + (10 - 4)* alpha),
			ChangingDecimal(num6, lambda alpha: (4 + (10 - 4)* alpha)**2*var1),
		)
		self.wait(2)

		self.play(
			pl1.animate.stretch(0.1, 0, about_edge=LEFT).stretch(10, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: 10*sigma1 + (sigma1 - 10*sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 10 + (1 - 10)* alpha),
			ChangingDecimal(num6, lambda alpha: (10 + (1 - 10)* alpha)**2*var1),
		)
		self.wait(2)
		self.end_fragment(fragment_type=LOOP)

		ax11 = Axes(x_range=[0, 4], y_range=[0, 2, 0.5], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN)
		self.play(Transform(ax1, ax11),
			pl1.animate.stretch(10, 0, about_edge=LEFT).stretch(0.2, 1, about_edge=DOWN)
		)
		self.end_fragment(fragment_type=NO_PAUSE)

		self.play(
			pl1.animate.stretch(0.5, 0, about_edge=LEFT).stretch(2, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: sigma1 + (0.5*sigma1 - sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 1 + (0.5 - 1)* alpha),
			ChangingDecimal(num6, lambda alpha: (1 + (0.5 - 1)* alpha)**2*var1),
		)
		self.wait(2)

		self.play(
			pl1.animate.stretch(0.5, 0, about_edge=LEFT).stretch(2, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: 0.5*sigma1 + (0.25*sigma1 - 0.5*sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 0.5 + (0.25 - 0.5)* alpha),
			ChangingDecimal(num6, lambda alpha: (0.5 + (0.25 - 0.5)* alpha)**2*var1),
		)
		self.wait(2)

		self.play(
			pl1.animate.stretch(0.5, 0, about_edge=LEFT).stretch(2, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: 0.25*sigma1 + (0.125*sigma1 - 0.25*sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 0.25 + (0.125 - 0.25)* alpha),
			ChangingDecimal(num6, lambda alpha: (0.25 + (0.125 - 0.25)* alpha)**2*var1),
		)
		self.wait(2)

		self.play(
			pl1.animate.stretch(8, 0, about_edge=LEFT).stretch(0.125, 1, about_edge=DOWN),
			ChangingDecimal(num4, lambda alpha: 0.125*sigma1 + (sigma1 - 0.125*sigma1)* alpha),
			ChangingDecimal(num5, lambda alpha: 0.125 + (1- 0.125)* alpha),
			ChangingDecimal(num6, lambda alpha: (0.125 + (1 - 0.125)* alpha)**2*var1),
		)
		self.wait(2)

		self.end_fragment(fragment_type=LOOP)

		self.play(Transform(ax1, ax1c),
			pl1.animate.stretch(5, 1, about_edge=DOWN))
		
		self.end_fragment()

		self.play(Unwrite(VGroup(f18_5, num5, f18_6, num6)))
		self.play(Write(f19))
		self.end_fragment()

		self.play(Unwrite(VGroup(f16, f17, f18)))
		self.play(f19.animate.shift(UP*4.2))

		f19_1 = MathTex('\sigma(\sum_{i=1}^{n}X_{i}) = \sqrt{D(\sum_{i=1}^{n}X_{i})}').scale(0.8).next_to(f19, DOWN*1.4, aligned_edge=LEFT)
		self.play(Write(f19_1))
		self.end_fragment()

		f19_2 = MathTex('\sigma(\sum_{i=1}^{n}X_{i}) = \sqrt{\sum_{i=1}^{n}D(X_{i})}').scale(0.8).next_to(f19_1, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f19_1, f19_2))
		self.end_fragment()

		f19_3 = MathTex('\sigma(\sum_{i=1}^{n}X_{i}) = \sqrt{\sum_{i=1}^{n}\sigma^{2}(X_{i})}').scale(0.8).next_to(f19_2, DOWN*1.4, aligned_edge=LEFT)
		self.play(TransformFromCopy(f19_2, f19_3))
		self.end_fragment()

		self.play(Unwrite(VGroup(f19, f19_1, f19_2, f19_3, f14, f15, num4, ax1, pl1)))
		self.end_fragment()

class StatisticalMoment(PresentationScene):
	def construct(self):
		def polygon_from_arr(arr, ax, x_range, to_0 = True):
			num_range = [x_range[0], x_range[1]]
			if x_range[0] < 0:
				num_range[0] = 0
			if x_range[1] > 1:
				num_range[1] = 1
			start_i = 0 if x_range[0] < 0 else math.floor(x_range[0]*len(arr))
			end_i =  len(arr)-1 if x_range[1] > 1 else math.ceil(x_range[1]*(len(arr)-1))
			coord = []
			if to_0:
				coord.extend([[x_range[0], 0], [x_range[0], arr[start_i]]])
			coord.extend(list(map(lambda i: [num_range[0] + (i-start_i)*(num_range[1] - num_range[0])/(end_i - start_i), arr[i]], range(start_i, end_i))))		
			coord.append([x_range[1], arr[end_i]])
			coord.append([x_range[1], 0 if to_0 else arr[start_i]])
			return Polygon(*ax.coords_to_point(coord), color=YELLOW).set_fill(YELLOW, opacity=0.7)
		ax1 = Axes(x_range=[0, 6], y_range=[0, 0.8, 0.2], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN)
		ax1c = ax1.copy()
		ax2 = Axes(x_range=[0, 1], y_range=[0, 0.8], x_length=5, y_length=3,).shift(LEFT*3.5 + DOWN)
		n = 500
		#arr1 = np.array([4*x/n if x < n/2 else 4*(n - x)/n  for x in range(n)])
		#darr1 = arr1*n/4/arr1.sum()

		arr1 = np.array([1/((x+1)/n + 0.2) for x in range(n)])
		darr1 = arr1*n/4/arr1.sum()
		arr2 = np.ones(n)
		darr2 = arr2*n/4/arr2.sum()
		arr3 = np.array([1/(1.2 - x/n) for x in range(n)])
		darr3 = arr3*n/4/arr3.sum()
		arr4 = np.array([x/n if x<n/2 else 1-x/n for x in range(n)])
		darr4 = arr4*n/4/arr4.sum()


		pl1 = polygon_from_arr(np.concatenate((darr1, np.zeros(math.floor(n*0.5)))), ax2, [0, 2/3])
		pl1c = pl1.copy()
		pl2 = polygon_from_arr(np.concatenate((darr2, np.zeros(math.floor(n*0.5)))), ax2, [0, 2/3])
		pl3 = polygon_from_arr(np.concatenate((darr3, np.zeros(math.floor(n*0.5)))), ax2, [0, 2/3])
		pl4 = polygon_from_arr(np.concatenate((darr4, np.zeros(math.floor(n*0.5)))), ax2, [0, 2/3])
		t1 = Text('3.3 Середнє квадратичне відхилення',font_size=32).align_on_border(UL)
		t2 = Text('3.4 Початковий момент порядку',font_size=32).align_on_border(UL)
		self.add(t1)
		self.play(Transform(t1, t2))

		f1 = MathTex('\\nu_{k} = M(X^{k})\,').shift(UP*2)
		self.play(Write(f1))
		self.end_fragment()
		f2 = MathTex(' = \int_{-\infty}^{\infty}x^{k}f(x)dx').next_to(f1, RIGHT)
		self.play(Write(f2))
		self.end_fragment()

		self.play(Write(VGroup(ax1, pl1)))

		sequance = np.array(range(0, n, 1))/n
		nu1_1 = np.dot(darr1, sequance*4)/n*4
		nu1_2 = np.dot(darr1, (sequance*4)**2)/n*4
		nu1_3 = np.dot(darr1, (sequance*4)**3)/n*4
		nu1_4 = np.dot(darr1, (sequance*4)**4)/n*4
		f3_0 = MathTex('\\nu_{0} = 1').next_to(f2, DOWN*1.4, aligned_edge=LEFT)
		f3_1 = MathTex('\\nu_{1} =\,').next_to(f3_0, DOWN*1.4, aligned_edge=LEFT)
		num1_1 = DecimalNumber(nu1_1).next_to(f3_1, RIGHT)
		f3_2 = MathTex('\\nu_{2} =\,').next_to(f3_1, DOWN*1.4, aligned_edge=LEFT)
		num1_2 = DecimalNumber(nu1_2).next_to(f3_2, RIGHT)
		f3_3 = MathTex('\\nu_{3} =\,').next_to(f3_2, DOWN*1.4, aligned_edge=LEFT)
		num1_3 = DecimalNumber(nu1_3).next_to(f3_3, RIGHT)
		f3_4 = MathTex('\\nu_{4} =\,').next_to(f3_3, DOWN*1.4, aligned_edge=LEFT)
		num1_4 = DecimalNumber(nu1_4).next_to(f3_4, RIGHT)
		self.play(Write(VGroup(f3_0, f3_1, num1_1, f3_2, num1_2, f3_3, num1_3, f3_4, num1_4)))
		self.end_fragment()

		nu2_1 = np.dot(darr1, sequance*4 + 2)/n*4
		nu2_2 = np.dot(darr1, (sequance*4 + 2)**2)/n*4
		nu2_3 = np.dot(darr1, (sequance*4 + 2)**3)/n*4
		nu2_4 = np.dot(darr1, (sequance*4 + 2)**4)/n*4
		self.play(
			pl1.animate.shift(ax1.c2p(*(RIGHT*2))-ax1.c2p(*ORIGIN)),
			ChangingDecimal(num1_1, lambda alpha: nu1_1 + (nu2_1 - nu1_1)* alpha),
			ChangingDecimal(num1_2, lambda alpha: nu1_2 + (nu2_2 - nu1_2)* alpha),
			ChangingDecimal(num1_3, lambda alpha: nu1_3 + (nu2_3 - nu1_3)* alpha),
			ChangingDecimal(num1_4, lambda alpha: nu1_4 + (nu2_4 - nu1_4)* alpha),
		)
		self.wait(3)

		self.play(
			pl1.animate.shift(ax1.c2p(*(LEFT*2))-ax1.c2p(*ORIGIN)),
			ChangingDecimal(num1_1, lambda alpha: nu2_1 + (nu1_1 - nu2_1)* alpha),
			ChangingDecimal(num1_2, lambda alpha: nu2_2 + (nu1_2 - nu2_2)* alpha),
			ChangingDecimal(num1_3, lambda alpha: nu2_3 + (nu1_3 - nu2_3)* alpha),
			ChangingDecimal(num1_4, lambda alpha: nu2_4 + (nu1_4 - nu2_4)* alpha),
		)
		self.wait(3)

		nu3_1 = np.dot(darr2, sequance*4)/n*4
		nu3_2 = np.dot(darr2, (sequance*4)**2)/n*4
		nu3_3 = np.dot(darr2, (sequance*4)**3)/n*4
		nu3_4 = np.dot(darr2, (sequance*4)**4)/n*4
		self.play(
			Transform(pl1, pl2),
			ChangingDecimal(num1_1, lambda alpha: nu1_1 + (nu3_1 - nu1_1)* alpha),
			ChangingDecimal(num1_2, lambda alpha: nu1_2 + (nu3_2 - nu1_2)* alpha),
			ChangingDecimal(num1_3, lambda alpha: nu1_3 + (nu3_3 - nu1_3)* alpha),
			ChangingDecimal(num1_4, lambda alpha: nu1_4 + (nu3_4 - nu1_4)* alpha),
		)
		self.wait(3)

		nu5_1 = np.dot(darr4, sequance*4)/n*4
		nu5_2 = np.dot(darr4, (sequance*4)**2)/n*4
		nu5_3 = np.dot(darr4, (sequance*4)**3)/n*4
		nu5_4 = np.dot(darr4, (sequance*4)**4)/n*4
		self.play(
			Transform(pl1, pl4),
			ChangingDecimal(num1_1, lambda alpha: nu3_1 + (nu5_1 - nu3_1)* alpha),
			ChangingDecimal(num1_2, lambda alpha: nu3_2 + (nu5_2 - nu3_2)* alpha),
			ChangingDecimal(num1_3, lambda alpha: nu3_3 + (nu5_3 - nu3_3)* alpha),
			ChangingDecimal(num1_4, lambda alpha: nu3_4 + (nu5_4 - nu3_4)* alpha),
		)
		self.wait(3)

		self.play(
			Transform(pl1, pl2),
			ChangingDecimal(num1_1, lambda alpha: nu5_1 + (nu3_1 - nu5_1)* alpha),
			ChangingDecimal(num1_2, lambda alpha: nu5_2 + (nu3_2 - nu5_2)* alpha),
			ChangingDecimal(num1_3, lambda alpha: nu5_3 + (nu3_3 - nu5_3)* alpha),
			ChangingDecimal(num1_4, lambda alpha: nu5_4 + (nu3_4 - nu5_4)* alpha),
		)
		self.wait(3)

		nu4_1 = np.dot(darr3, sequance*4)/n*4
		nu4_2 = np.dot(darr3, (sequance*4)**2)/n*4
		nu4_3 = np.dot(darr3, (sequance*4)**3)/n*4
		nu4_4 = np.dot(darr3, (sequance*4)**4)/n*4
		self.play(
			Transform(pl1, pl3),
			ChangingDecimal(num1_1, lambda alpha: nu3_1 + (nu4_1 - nu3_1)* alpha),
			ChangingDecimal(num1_2, lambda alpha: nu3_2 + (nu4_2 - nu3_2)* alpha),
			ChangingDecimal(num1_3, lambda alpha: nu3_3 + (nu4_3 - nu3_3)* alpha),
			ChangingDecimal(num1_4, lambda alpha: nu3_4 + (nu4_4 - nu3_4)* alpha),
		)
		self.wait(3)

		self.play(
			Transform(pl1, pl1c),
			ChangingDecimal(num1_1, lambda alpha: nu4_1 + (nu1_1 - nu4_1)* alpha),
			ChangingDecimal(num1_2, lambda alpha: nu4_2 + (nu1_2 - nu4_2)* alpha),
			ChangingDecimal(num1_3, lambda alpha: nu4_3 + (nu1_3 - nu4_3)* alpha),
			ChangingDecimal(num1_4, lambda alpha: nu4_4 + (nu1_4 - nu4_4)* alpha),
		)		
		self.wait(3)
		self.end_fragment(fragment_type=LOOP)

		t2_1 = Text('3.5 Центральний момент порядку k',font_size=32).align_on_border(UL) 
		f4 = MathTex('\mu_{k} = M([X-M(X)]^{k})').shift(2*UP+LEFT*2)
		f5 = MathTex(' = \int_{-\infty}^{\infty}(x-M(X))^{k}f(x)dx').next_to(f4, RIGHT)

		self.play(Unwrite(VGroup(f2, f3_0, f3_1, num1_1, f3_2, num1_2, f3_3, num1_3, f3_4, num1_4)))
		self.play(Transform(t1, t2_1), Transform(f1, f4))

		
		self.end_fragment()
		self.play(Write(f5))

		self.end_fragment()

		mu1_1 = np.dot(darr1, sequance*4 - nu1_1)/n*4 
		mu1_2 = np.dot(darr1, (sequance*4 - nu1_1)**2)/n*4
		mu1_3 = np.dot(darr1, (sequance*4 - nu1_1)**3)/n*4
		mu1_4 = np.dot(darr1, (sequance*4 - nu1_1)**4)/n*4
		f6_0 = MathTex('\mu_{0} = 1').next_to(f5, DOWN*1.4, aligned_edge=LEFT).shift(RIGHT*1.5)
		f6_1 = MathTex('\mu_{1} =\,').next_to(f6_0, DOWN*1.4, aligned_edge=LEFT)
		num2_1 = DecimalNumber(mu1_1).next_to(f6_1, RIGHT)
		f6_2 = MathTex('\mu_{2} =\,').next_to(f6_1, DOWN*1.4, aligned_edge=LEFT)
		num2_2 = DecimalNumber(mu1_2).next_to(f6_2, RIGHT)
		f6_3 = MathTex('\mu_{3} =\,').next_to(f6_2, DOWN*1.4, aligned_edge=LEFT)
		num2_3 = DecimalNumber(mu1_3).next_to(f6_3, RIGHT)
		f6_4 = MathTex('\mu_{4} =\,').next_to(f6_3, DOWN*1.4, aligned_edge=LEFT)
		num2_4 = DecimalNumber(mu1_4).next_to(f6_4, RIGHT)
		self.play(Write(VGroup(f6_0, f6_1, num2_1, f6_2, num2_2, f6_3, num2_3, f6_4, num2_4)))
		self.end_fragment()

		self.play(pl1.animate.shift(ax1.c2p(*(RIGHT*2))-ax1.c2p(*ORIGIN)))
		self.wait(3)

		self.play(pl1.animate.shift(ax1.c2p(*(LEFT*2))-ax1.c2p(*ORIGIN)))
		self.wait(3)


		mu2_1 = np.dot(darr2, sequance*4 - nu3_1)/n*4
		mu2_2 = np.dot(darr2, (sequance*4 - nu3_1)**2)/n*4
		mu2_3 = np.dot(darr2, (sequance*4 - nu3_1)**3)/n*4
		mu2_4 = np.dot(darr2, (sequance*4 - nu3_1)**4)/n*4
		self.play(
			Transform(pl1, pl2),
			ChangingDecimal(num2_1, lambda alpha: mu1_1 + (mu2_1 - mu1_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu1_2 + (mu2_2 - mu1_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu1_3 + (mu2_3 - mu1_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu1_4 + (mu2_4 - mu1_4)* alpha),
		)
		self.wait(3)

		mu3_1 = np.dot(darr4, sequance*4 - nu5_1)/n*4
		mu3_2 = np.dot(darr4, (sequance*4 - nu5_1)**2)/n*4
		mu3_3 = np.dot(darr4, (sequance*4 - nu5_1)**3)/n*4
		mu3_4 = np.dot(darr4, (sequance*4 - nu5_1)**4)/n*4
		self.play(
			Transform(pl1, pl4),
			ChangingDecimal(num2_1, lambda alpha: mu2_1 + (mu3_1 - mu2_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu2_2 + (mu3_2 - mu2_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu2_3 + (mu3_3 - mu2_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu2_4 + (mu3_4 - mu2_4)* alpha),
		)
		self.wait(3)

		mu4_1 = np.dot(darr3, sequance*4 - nu4_1)/n*4
		mu4_2 = np.dot(darr3, (sequance*4 - nu4_1)**2)/n*4
		mu4_3 = np.dot(darr3, (sequance*4 - nu4_1)**3)/n*4
		mu4_4 = np.dot(darr3, (sequance*4 - nu4_1)**4)/n*4
		self.play(
			Transform(pl1, pl3),
			ChangingDecimal(num2_1, lambda alpha: mu3_1 + (mu4_1 - mu3_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu3_2 + (mu4_2 - mu3_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu3_3 + (mu4_3 - mu3_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu3_4 + (mu4_4 - mu3_4)* alpha),
		)
		self.wait(3)

		self.play(
			Transform(pl1, pl1c),
			ChangingDecimal(num2_1, lambda alpha: mu4_1 + (mu1_1 - mu4_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu4_2 + (mu1_2 - mu4_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu4_3 + (mu1_3 - mu4_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu4_4 + (mu1_4 - mu4_4)* alpha),
		)
		self.wait(3)
		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(f1, f5)))
		f7 = MathTex('\gamma_{1} = As=\\frac{\mu_{3}}{\sigma^{3}}=\,').shift(2*UP)
		t3 = Text('3.6 Коефіцієнт асиметрії',font_size=32).align_on_border(UL)
		self.play(TransformFromCopy(f6_3, f7), Transform(t1, t3))
		self.end_fragment()

		As_1 = mu1_3/math.pow(mu1_2, 1.5)
		num3 = DecimalNumber(As_1).next_to(f7, RIGHT).shift(UP*0.08)
		self.play(Write(num3))

		M3_1 = nu1_1
		l3_1 = Line(start=ax1.c2p(*(M3_1, 0.8, 0)), end=ax1.c2p(*(M3_1, 0, 0)), color=RED)
		l3_1t = MathTex('M(X)', font_size=24, color=RED).shift(ax1.c2p(*(M3_1, -0.22, 0)))
		self.play(Write(VGroup(l3_1, l3_1t)))
		self.end_fragment()

		As_2 = mu2_3/math.pow(mu2_2, 1.5)
		self.play(
			Transform(pl1, pl2),
			ChangingDecimal(num2_1, lambda alpha: mu1_1 + (mu2_1 - mu1_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu1_2 + (mu2_2 - mu1_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu1_3 + (mu2_3 - mu1_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu1_4 + (mu2_4 - mu1_4)* alpha),
			ChangingDecimal(num3, lambda alpha: As_1 + (As_2 - As_1)* alpha),
			l3_1.animate.set_coord(ax1.c2p(*(nu3_1, 0, 0))[0], 0),
			l3_1t.animate.set_coord(ax1.c2p(*(nu3_1, 0, 0))[0], 0)
		)
		self.wait(2)

		As_3 = mu4_3/math.pow(mu4_2, 1.5)
		self.play(
			Transform(pl1, pl3),
			ChangingDecimal(num2_1, lambda alpha: mu2_1 + (mu4_1 - mu2_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu2_2 + (mu4_2 - mu2_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu2_3 + (mu4_3 - mu2_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu2_4 + (mu4_4 - mu2_4)* alpha),
			ChangingDecimal(num3, lambda alpha: As_2 + (As_3 - As_2)* alpha),
			l3_1.animate.set_coord(ax1.c2p(*(nu4_1, 0, 0))[0], 0),
			l3_1t.animate.set_coord(ax1.c2p(*(nu4_1, 0, 0))[0], 0)
		)
		self.wait(2)

		self.play(
			Transform(pl1, pl1c),
			ChangingDecimal(num2_1, lambda alpha: mu4_1 + (mu1_1 - mu4_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu4_2 + (mu1_2 - mu4_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu4_3 + (mu1_3 - mu4_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu4_4 + (mu1_4 - mu4_4)* alpha),
			ChangingDecimal(num3, lambda alpha: As_3 + (As_1 - As_3)* alpha),
			l3_1.animate.set_coord(ax1.c2p(*(M3_1, 0, 0))[0], 0),
			l3_1t.animate.set_coord(ax1.c2p(*(M3_1, 0, 0))[0], 0)
		)
		self.wait(2)
		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(l3_1, l3_1t)))
		self.play(Unwrite(VGroup(f7, num3)))
		f8 = MathTex('\\frac{\mu_{4}}{\sigma^{4}}=\,').shift(2*UP)
		self.play(TransformFromCopy(f6_4, f8))
		self.end_fragment()

		E_1 = mu1_4/math.pow(mu1_2, 2)
		num4 = DecimalNumber(E_1).next_to(f8, RIGHT).shift(UP*0.08)
		self.play(Write(num4))
		self.end_fragment()

		arr5 = np.array([math.exp((-(x*4/n-4)**2)/2) for x in range(n*2)])
		darr5 = arr5*n/4/arr5.sum()
		pl5 = polygon_from_arr(darr5[math.floor(n/2):], ax2, [0, 1])

		sequance2 = np.array(range(n*2))*4/n - 2
		mean = np.dot(darr5, sequance2)*8/n/2
		mu5_1 = np.dot(darr5, (sequance2 - mean))*4/n
		mu5_2 = np.dot(darr5, (sequance2 - mean)**2)*4/n
		mu5_3 = np.dot(darr5, (sequance2 - mean)**3)*4/n
		mu5_4 = 3 #np.dot(darr5, (sequance2 - mean)**4)*4/n
		E_2 = 3 #mu5_4/math.pow(mu5_2, 2)
		self.play(
			Transform(pl1, pl5),
			ChangingDecimal(num2_1, lambda alpha: mu1_1 + (mu5_1 - mu1_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu1_2 + (mu5_2 - mu1_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu1_3 + (mu5_3 - mu1_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu1_4 + (mu5_4 - mu1_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_1 + (E_2 - E_1)* alpha)
		)
		self.end_fragment()

		arr6 = np.array([math.exp((-(x*4/n-4)**2)/8) for x in range(n*2)])
		darr6 = arr6*n/4/arr6.sum()
		pl6 = polygon_from_arr(darr6[math.floor(n/2):], ax2, [0, 1])

		mu6_1 = np.dot(darr6, (sequance2 - mean))*4/n
		mu6_2 = np.dot(darr6, (sequance2 - mean)**2)*4/n
		mu6_3 = 0#np.dot(darr6, (sequance2 - mean)**3)*4/n
		mu6_4 = (mu6_2**2)*3#np.dot(darr6, (sequance2 - mean)**4)*4/n
		E_3 = mu6_4/math.pow(mu6_2, 2)
		self.play(
			Transform(pl1, pl6),
			ChangingDecimal(num2_1, lambda alpha: mu5_1 + (mu6_1 - mu5_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu5_2 + (mu6_2 - mu5_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu5_3 + (mu6_3 - mu5_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu5_4 + (mu6_4 - mu5_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_2 + (E_3 - E_2)* alpha)
		)
		self.wait(2)

		arr7 = np.array([math.exp((-(x*4/n-4)**2)/0.5) for x in range(n*2)])
		darr7 = arr7*n/4/arr7.sum()
		pl7 = polygon_from_arr(darr7[math.floor(n/2):], ax2, [0, 1])

		mu7_1 = np.dot(darr7, (sequance2 - mean))*4/n
		mu7_2 = np.dot(darr7, (sequance2 - mean)**2)*4/n
		mu7_3 = np.dot(darr7, (sequance2 - mean)**3)*4/n
		mu7_4 = np.dot(darr7, (sequance2 - mean)**4)*4/n
		E_4 = mu7_4/math.pow(mu7_2, 2)
		self.play(
			Transform(pl1, pl7),
			ChangingDecimal(num2_1, lambda alpha: mu6_1 + (mu7_1 - mu6_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu6_2 + (mu7_2 - mu6_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu6_3 + (mu7_3 - mu6_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu6_4 + (mu7_4 - mu6_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_3 + (E_4 - E_3)* alpha)
		)
		self.wait(2)

		self.play(
			Transform(pl1, pl5),
			ChangingDecimal(num2_1, lambda alpha: mu7_1 + (mu5_1 - mu7_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu7_2 + (mu5_2 - mu7_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu7_3 + (mu5_3 - mu7_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu7_4 + (mu5_4 - mu7_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_4 + (E_2 - E_4)* alpha)
		)
		self.wait(2)

		self.end_fragment(fragment_type=LOOP)
		f9 = MathTex('\gamma_{2} =E = \\frac{\mu_{4}}{\sigma_{4}} - 3=\,').next_to(num4, LEFT).shift(DOWN*0.08)
		t4 = Text('3.7 Коефіцієнт ексцесу',font_size=32).align_on_border(UL)
		self.play(Transform(f8, f9), Transform(t1, t4),
			ChangingDecimal(num4, lambda alpha: E_4 + (0 - E_4)* alpha)
		)
		self.end_fragment()

		arr8 = np.array([x/n if x < n/2 else 1-x/n for x in range(n)])
		darr8 = arr8*n/4/arr8.sum()
		pl8 = polygon_from_arr(np.concatenate((darr8, np.zeros(math.floor(n/2)))), ax2, [0, 2/3])
		mean = np.dot(darr8, sequance*4)*4/n
		mu8_1 = np.dot(darr8, (sequance*4 - mean))*4/n
		mu8_2 = np.dot(darr8, (sequance*4 - mean)**2)*4/n
		mu8_3 = np.dot(darr8, (sequance*4 - mean)**3)*4/n
		mu8_4 = np.dot(darr8, (sequance*4 - mean)**4)*4/n
		E_5 = mu8_4/math.pow(mu8_2, 2)
		self.play(
			Transform(pl1, pl8),
			ChangingDecimal(num2_1, lambda alpha: mu6_1 + (mu8_1 - mu6_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu6_2 + (mu8_2 - mu6_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu6_3 + (mu8_3 - mu6_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu6_4 + (mu8_4 - mu6_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_2 + (E_5 - E_2)* alpha - 3)
		)
		self.wait(2)

		arr9 = np.array([1 if x>n/4 or x<3*n/4 else 0 for x in range(n)])
		darr9 = arr9*n/4/arr9.sum()
		pl9 = polygon_from_arr(np.concatenate((darr9, np.zeros(math.floor(n/2)))), ax2, [0, 2/3])
		mean = np.dot(darr9, sequance*4)*4/n
		mu9_1 = np.dot(darr9, (sequance*4 - mean))*4/n
		mu9_2 = np.dot(darr9, (sequance*4 - mean)**2)*4/n
		mu9_3 = np.dot(darr9, (sequance*4 - mean)**3)*4/n
		mu9_4 = np.dot(darr9, (sequance*4 - mean)**4)*4/n
		E_6 = mu9_4/math.pow(mu9_2, 2)
		self.play(
			Transform(pl1, pl9),
			ChangingDecimal(num2_1, lambda alpha: mu8_1 + (mu9_1 - mu8_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu8_2 + (mu9_2 - mu8_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu8_3 + (mu9_3 - mu8_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu8_4 + (mu9_4 - mu8_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_5 + (E_6 - E_5)* alpha - 3)
		)
		self.wait(2)

		arr10 = np.array([math.exp(-abs(x*4/n-2)/0.5) for x in range(n)])
		darr10 = arr10*n/4/arr10.sum()
		pl10 = polygon_from_arr(np.concatenate((darr10, np.zeros(math.floor(n/2)))), ax2, [0, 2/3])
		mean = np.dot(darr10, sequance*4)*4/n
		mu10_1 = np.dot(darr10, (sequance*4 - mean))*4/n
		mu10_2 = np.dot(darr10, (sequance*4 - mean)**2)*4/n
		mu10_3 = np.dot(darr10, (sequance*4 - mean)**3)*4/n
		mu10_4 = np.dot(darr10, (sequance*4 - mean)**4)*4/n
		E_7 = mu10_4/math.pow(mu10_2, 2)
		self.play(
			Transform(pl1, pl10),
			ChangingDecimal(num2_1, lambda alpha: mu9_1 + (mu10_1 - mu9_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu9_2 + (mu10_2 - mu9_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu9_3 + (mu10_3 - mu9_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu9_4 + (mu10_4 - mu9_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_6 + (E_7 - E_6)* alpha - 3)
		)
		self.wait(2)

		self.play(
			Transform(pl1, pl5),
			ChangingDecimal(num2_1, lambda alpha: mu10_1 + (mu5_1 - mu10_1)* alpha),
			ChangingDecimal(num2_2, lambda alpha: mu10_2 + (mu5_2 - mu10_2)* alpha),
			ChangingDecimal(num2_3, lambda alpha: mu10_3 + (mu5_3 - mu10_3)* alpha),
			ChangingDecimal(num2_4, lambda alpha: mu10_4 + (mu5_4 - mu10_4)* alpha),
			ChangingDecimal(num4, lambda alpha: E_7 + (E_2 - E_7)* alpha - 3)
		)
		self.wait(2)

		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(f8, num4, f6_0, f6_1, num2_1, f6_2, num2_2, f6_3, num2_3, f6_4, num2_4)))
		t5 = Text('3.8 Мода',font_size=32).align_on_border(UL)
		f10 = MathTex('Mo(X) = max(f(x))').shift(UP*2)
		self.play(Write(f10), Transform(t1, t5))
		self.end_fragment()

		l1 = Line(ax1.coords_to_point(*(2, 0, 0)), ax1.coords_to_point(*(2, 1.01, 0)), color=RED, stroke_width=6)
		l1t = MathTex('Mo(X)', font_size=32, color=RED).shift(ax1.coords_to_point(*(2, -0.25)))
		self.play(Write(VGroup(l1, l1t)))
		self.end_fragment()
		
		arr11 = np.array([math.exp(-((x-125)*7/n)**2)+ math.exp(-((x-325)*7/n)**2) for x in range(n)])
		darr11 = arr11*n/4/arr11.sum()
		pl11 = polygon_from_arr(darr11*8/6, ax2, [0, 1])

		ax3 = Axes(x_range=[0, 4], y_range=[0, 0.6, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN)
		self.play(Transform(ax1, ax3),Transform(pl1, pl11), Unwrite(VGroup(l1, l1t)))

		l2 = Line(ax3.coords_to_point(*(1, 0, 0)), ax3.coords_to_point(*(1, 0.61, 0)), color=RED, stroke_width=6)
		l2t = MathTex('Mo(X)', font_size=32, color=RED).shift(ax3.coords_to_point(*(1, -0.15)))
		l3 = Line(ax3.coords_to_point(*(2.6, 0, 0)), ax3.coords_to_point(*(2.6, 0.61, 0)), color=RED, stroke_width=6)
		l3t = MathTex('Mo(X)', font_size=32, color=RED).shift(ax3.coords_to_point(*(2.6, -0.15)))

		self.play(Write(VGroup(l2, l2t, l3, l3t)))
		self.end_fragment()

		arr12 = np.array([1 for x in range(n)])
		darr12 = arr12*n/4/arr12.sum()
		pl12 = polygon_from_arr(darr12*8/6, ax2, [0, 1])

		self.play(Transform(pl1, pl12), Unwrite(VGroup(l2, l2t, l3, l3t)))

		f11  = MathTex('Mo(X) = [a, b]').shift(RIGHT*3)
		self.play(Write(f11))
		self.end_fragment()

		self.play(Unwrite(VGroup(f11, f10, ax1, pl1)))

		t6 = Text('3.9 Медіана',font_size=32).align_on_border(UL)
		self.play(Transform(t1, t6))

		f12 = MathTex('F(Me) = 0.5').shift(2*UP)
		self.play(Write(f12))
		self.end_fragment()

		arr13 = np.array([math.exp(-((x-125)*9/n)**2)/2 + math.exp(-((x-325)*5/n)**2) for x in range(n)])
		darr13 = arr13*n/4/arr13.sum()
		def calculate_integral(arr):
			s = 0
			res = []
			for el in arr:
				s+=el
				res.append(s)
			return np.array(res)
		sarr13 = calculate_integral(arr13/arr13.sum())
		ax4 = Axes(x_range=[0, 4], y_range=[0, 1, 0.25], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN)
		ax5 = Axes(x_range=[0, 1], y_range=[0, 1], x_length=5, y_length=3).shift(LEFT*3.5+DOWN)
		ax6 = Axes(x_range=[0, 4], y_range=[0, 0.5, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(RIGHT*3.5 + DOWN)
		ax7 = Axes(x_range=[0, 1], y_range=[0, 0.5], x_length=5, y_length=3).shift(RIGHT*3.5+DOWN)
		pl13_1 = polygon_from_arr(sarr13, ax5, [0, 1])
		pl13_2 = polygon_from_arr(darr13, ax7, [0, 1])
		self.play(Write(ax4))
		self.play(Write(pl13_1))
		self.end_fragment()

		arrow1 = Arrow(start=ax4.c2p(*UP*0.5), end=ax4.c2p(*(UP*0.5+2.4*RIGHT)), buff=0)
		arrow2 = Arrow(start=ax4.c2p(*(UP*0.5+2.4*RIGHT)), end=ax4.c2p(*RIGHT*2.4), buff=0)
		l4t = MathTex('Me').shift(ax4.c2p(*(2.45, -0.3, 0)))
		self.play(Write(arrow1))
		self.play(Write(arrow2))
		self.play(Write(l4t))
		self.end_fragment()

		self.play(Write(ax6))
		self.play(Write(pl13_2))
		self.end_fragment()

		f13 = MathTex('S=\,').next_to(ax6, UP, buff=1).shift(LEFT*0.3)
		num5 = DecimalNumber(0).next_to(f13,RIGHT)
		self.play(Write(VGroup(f13, num5)))
		pl13_3 = polygon_from_arr([0], ax7, [0, 0])
		current_ind = 0
		for i in range(1, 81):
			alpha = rate_functions.smooth(i/80)*0.5
			while(sarr13[current_ind] < alpha):
				current_ind+=1
			pl13_4 = polygon_from_arr(np.concatenate((darr13[0:current_ind],np.zeros(n-current_ind))), 
							 ax7, [0, current_ind/n]).set_color(BLUE).set_fill(BLUE, opacity=0.7)
			num5.set_value(alpha)
			self.play(Transform(pl13_3, pl13_4, run_time=0.02))
		l5 = Line(start=ax6.c2p(*(2.4, 0.6, 0)), end=ax6.c2p(*(2.4, 0, 0)))
		l5t = MathTex('Me').shift(ax6.c2p(*(2.4, -0.15, 0)))
		self.play(Write(VGroup(l5, l5t)))
		self.end_fragment()

		t7 = Text('3.10 Квантіль рівня p',font_size=32).align_on_border(UL)
		f14 = MathTex('F(x_{p}) = p').shift(UP*2)
		f15 = MathTex('p =\,').next_to(num5, LEFT).shift(UP*1)
		f16 = MathTex('F(p) =\,').next_to(f15, DOWN*1.4, aligned_edge=LEFT)
		num6 = DecimalNumber(4*299/500).next_to(f16, RIGHT)
		self.play(Transform(f12, f14), Transform(t1, t7))
		self.play(Transform(f13, f15), num5.animate.next_to(f15, RIGHT))
		self.play(Write(VGroup(f16, num6)))
		self.end_fragment()
		def transform_quantil(p, dt = 0.02):
			ind = 0
			while(sarr13[ind] < p):
				ind+=1
			position = ind*4/n
			arrow3 = Arrow(start=ax4.c2p(*UP*p), end=ax4.c2p(*(UP*p+position*RIGHT)), buff=0)
			arrow4 = Arrow(start=ax4.c2p(*(UP*p+position*RIGHT)), end=ax4.c2p(*RIGHT*position), buff=0)
			l4t.set_coord(ax4.c2p(*(position, 0, 0))[0], 0)
			l5.set_coord(ax6.c2p(*(position, 0, 0))[0], 0)
			l5t.set_coord(ax6.c2p(*(position, 0, 0))[0], 0)
			pl13_5 = polygon_from_arr(np.concatenate((darr13[0:ind], np.zeros(n-ind))), 
				ax7, [0, ind/n]).set_color(BLUE).set_fill(BLUE, opacity=0.7)
			self.play(
				Transform(arrow1, arrow3, run_time=dt),
				Transform(arrow2, arrow4, run_time=dt),
				Transform(pl13_3, pl13_5, run_time=dt))
			num5.set_value(p)
			num6.set_value(position)

		def quantil_transformation(start_val, end_val, dt=0.02):
			for i in range(1, 81):
				alpha = start_val + rate_functions.smooth(i/80)*(end_val - start_val)
				transform_quantil(alpha)

		quantil_transformation(0.5, 0.25)
		self.wait()
		quantil_transformation(0.25, 0.9)
		self.wait()
		quantil_transformation(0.9, 0.1)
		self.wait()
		quantil_transformation(0.1, 0.02)
		self.wait()
		quantil_transformation(0.02, 0.15)
		self.wait()
		quantil_transformation(0.15, 0.99)
		self.wait()
		quantil_transformation(0.99, 0.5)
		self.wait()
		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(f14, ax4, pl13_1, arrow1, arrow2, l4t, 
			ax6, pl13_2, pl13_3, l5, l5t, f13, num5, f16, num6, f12)))

		t8 = Text('Зміст', font_size=42).move_to(UP*3)
		t9 = Text('1. Визначення НВВ', font_size=32)
		t10 = Text('2. Властивості функцій розподілу', font_size=32)
		t11 = Text('3. Числові властивості НВВ', font_size=32)
		t12 = Text('4. Основні розподіли НВВ', font_size=32)
		text3 = VGroup(t9, t10, t11, t12).arrange(direction=DOWN, buff=0.5)
		self.play(Write(VGroup(t8, t9, t10, t12)), Transform(t1, t11, run_time=3))
		self.end_fragment()

		t13 = Text('4. Основні розподіли НВВ').align_on_border(UL)
		self.play(Unwrite(VGroup(t8, t9, t10, t1)), Transform(t12, t13, run_time=3))
		self.end_fragment()

class Distributions(PresentationScene):
	def construct(self):
		def polygon_from_arr(arr, ax, x_range, to_0 = True):
			num_range = [x_range[0], x_range[1]]
			if x_range[0] < 0:
				num_range[0] = 0
			if x_range[1] > 1:
				num_range[1] = 1
			start_i = 0 if x_range[0] < 0 else math.floor(x_range[0]*len(arr))
			end_i =  len(arr)-1 if x_range[1] > 1 else math.ceil(x_range[1]*(len(arr)-1))
			coord = []
			if to_0:
				coord.extend([[x_range[0], 0], [x_range[0], arr[start_i]]])
			coord.extend(list(map(lambda i: [num_range[0] + (i-start_i)*(num_range[1] - num_range[0])/(end_i - start_i), arr[i]], range(start_i, end_i))))		
			coord.append([x_range[1], arr[end_i]])
			coord.append([x_range[1], 0 if to_0 else arr[start_i]])
			return Polygon(*ax.coords_to_point(coord), color=YELLOW).set_fill(YELLOW, opacity=0.7)
		n = 500
		t1 = Text('4. Основні розподіли НВВ').align_on_border(UL)
		self.add(t1)
		self.end_fragment()
		
		t2 = Text('4.1 Рівномірний розподіл', font_size=32).align_on_border(UL)
		self.play(Transform(t1, t2))
		template = TexTemplate()
		template.add_to_preamble(r"\\usepackage{amsmath}")
		f1 = MathTex('f(x) = \{\,',substrings_to_isolate=['\{'])
		f1_1 = MathTex('0,\,x < a')
		f1_2 = MathTex('\\frac{1}{b-a},\, a\le x\le b')
		f1_3 = MathTex('0,\,x > b')
		VGroup(f1_1, f1_2, f1_3).arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(LEFT*3+UP*1.5)
		f1.next_to(f1_2, LEFT)
		f1[1].stretch(5, 1)
		
		ax_l1 = Axes(x_range=[0, 5], y_range=[0, 0.7, 0.1], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN*1.5)
		ax_r1 = Axes(x_range=[0, 5], y_range=[0, 1, 0.2], x_length=5, y_length=3,
			axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(RIGHT*3.5 + DOWN*1.5)
		ax_ln = Axes(x_range=[0, 1], y_range=[0, 0.7], x_length=5, y_length=3).shift(LEFT*3.5 + DOWN*1.5)
		ax_rn = Axes(x_range=[0, 1], y_range=[0, 1], x_length=5, y_length=3).shift(RIGHT*3.5 + DOWN*1.5)
		ax_l1c = ax_l1.copy()
		ax_r1c = ax_r1.copy()
		ax_r1cc = ax_r1.copy()


		self.play(Write(VGroup(f1)))
		self.play(Write(ax_l1))
		
		l1 = Line(ax_l1.c2p(*(1, 0, 0)), ax_l1.c2p(*(1, 0.71, 0)), color=BLUE, stroke_width=6)
		l1t = MathTex('a', font_size=32, color=BLUE).shift(ax_l1.c2p(*(1, -0.15, 0)))
		l2 = Line(ax_l1.c2p(*(4, 0, 0)), ax_l1.c2p(*(4, 0.71, 0)), color=BLUE, stroke_width=6)
		l2t = MathTex('b', font_size=32, color=BLUE).shift(ax_l1.c2p(*(4, -0.15, 0)))
		self.play(Write(VGroup(l1, l1t, l2, l2t)))
		self.end_fragment()

		arr1_1 = np.array([1 if x >= 0.2*n and x <= 0.8*n else 0 for x in range(n)])
		darr1_1 = arr1_1*n/5/arr1_1.sum()

		self.play(Write(f1_1))
		self.play(Write(f1_3))
		pl1_1 = polygon_from_arr([0], ax_ln, [0, 0.2])
		pl1_2 = polygon_from_arr([0], ax_ln, [0.8, 1])
		self.play(Write(VGroup(pl1_1, pl1_2)))
		self.end_fragment()

		self.play(Write(f1_2))
		pl1_3 = polygon_from_arr(darr1_1, ax_ln, [0,1])
		self.play(Write(pl1_3))
		self.end_fragment()

		f1_4 = MathTex('F(x) = \{\,',substrings_to_isolate=['\{'])
		f1_5 = MathTex('0,\,x < a')
		f1_6 = MathTex('\\frac{x-a}{b-a},\, a\le x\le b')
		f1_7 = MathTex('1,\,x > b')
		VGroup(f1_5, f1_6, f1_7).arrange(DOWN, buff=0.3, aligned_edge=LEFT).shift(RIGHT*5+UP*1.5)
		f1_4.next_to(f1_6, LEFT)
		f1_4[1].stretch(5, 1)

		self.play(Write(VGroup(f1_4)))
		self.play(Write(ax_r1))

		l3 = Line(ax_r1.c2p(*(1, 0, 0)), ax_r1.c2p(*(1, 1.01, 0)), color=BLUE, stroke_width=6)
		l3t = MathTex('a', font_size=32, color=BLUE).shift(ax_r1.c2p(*(1, -0.22, 0)))
		l4 = Line(ax_r1.c2p(*(4, 0, 0)), ax_r1.c2p(*(4, 1.01, 0)), color=BLUE, stroke_width=6)
		l4t = MathTex('b', font_size=32, color=BLUE).shift(ax_r1.c2p(*(4, -0.22, 0)))
		self.play(Write(VGroup(l3, l3t, l4, l4t)))
		self.end_fragment()


		self.play(Write(f1_5))
		pl1_4 = polygon_from_arr([0], ax_rn, [0, 0.2])
		self.play(Write(pl1_4))
		self.end_fragment()

		self.play(Write(f1_7))
		pl1_5 = polygon_from_arr([1], ax_rn, [0.8, 1])
		self.play(Write(pl1_5))
		self.end_fragment()

		def calculate_integral(arr):
			s = 0
			res = []
			for el in arr:
				s+=el
				res.append(s)
			return np.array(res)

		sarr1_1 = calculate_integral(arr1_1/arr1_1.sum())
		self.play(Write(f1_6))
		pl1_6 = polygon_from_arr(sarr1_1, ax_rn, [0,1])
		self.play(Write(pl1_6))
		self.remove(pl1_4, pl1_5)
		self.end_fragment()

		def transform_d1(a, b):
			arr = np.array([1 if x >= a/5*n and x <= b/5*n else 0 for x in range(n)])
			darr = arr*n/5/arr.sum()
			sarr = calculate_integral(arr/arr.sum())
			pl1 = polygon_from_arr(darr, ax_ln, [0, 1])
			pl2 = polygon_from_arr(sarr, ax_rn, [0, 1])
			self.play(
				Transform(pl1_3, pl1),
				Transform(pl1_6, pl2),
				l1.animate.set_coord(ax_l1.c2p(*(a, 0, 0))[0], 0),
				l1t.animate.set_coord(ax_l1.c2p(*(a, 0, 0))[0], 0),
				l2.animate.set_coord(ax_l1.c2p(*(b, 0, 0))[0], 0),
				l2t.animate.set_coord(ax_l1.c2p(*(b, 0, 0))[0], 0),
				l3.animate.set_coord(ax_r1.c2p(*(a, 0, 0))[0], 0),
				l3t.animate.set_coord(ax_r1.c2p(*(a, 0, 0))[0], 0),
				l4.animate.set_coord(ax_r1.c2p(*(b, 0, 0))[0], 0),
				l4t.animate.set_coord(ax_r1.c2p(*(b, 0, 0))[0], 0)
			)

		transform_d1(1, 2.5)
		self.wait(2)
		transform_d1(0, 1.5)
		self.wait(2)
		transform_d1(2, 5)
		self.wait(2)
		transform_d1(1, 4)
		self.wait(2)

		self.end_fragment(fragment_type=LOOP)

		f1_8 = MathTex('M(X) = \\frac{b - a}{2}')

		f1_9 = MathTex('D(X) = \\frac{(b - a)^{2}}{12}')

		f1_10 = MathTex('As = 0')

		f1_11 = MathTex('E = -1.2')

		VGroup(f1_8, f1_9).scale(0.9).arrange(RIGHT, buff=0.6).shift(DOWN*1+RIGHT*3)
		VGroup(f1_10, f1_11).arrange(RIGHT, buff=2).shift(DOWN*2.6+RIGHT*3)

		self.play(Unwrite(VGroup(ax_r1, pl1_6, l3, l3t, l4, l4t)))
		self.play(Write(f1_8))
		self.end_fragment()

		self.play(Write(f1_9))
		self.end_fragment()

		self.play(Write(f1_10))
		self.end_fragment()

		self.play(Write(f1_11))
		self.end_fragment()

		self.play(Unwrite(VGroup(pl1_1, pl1_2, pl1_3, l1, l1t, l2, l2t)))
		self.play(Unwrite(VGroup(f1, f1_1, f1_2, f1_3, f1_4, f1_5, f1_6, f1_7, f1_8, f1_9, f1_10, f1_11)))
		self.end_fragment()

		t4 = Text('4.2 Показниковий розподіл', font_size=32).align_on_border(UL)

		self.play(Transform(t1, t4))

		f3_1 = MathTex('F(X) = e^{-x}').shift(2*UP)

		self.play(Write(f3_1))
		ax_r3 = ax_r1c.copy()
		self.play(Write(ax_r3))
		plot3_1 = ax_r1c.plot(lambda x: math.exp(-x), color=BLUE)
		self.play(Write(plot3_1))
		self.end_fragment()

		f3_2 = MathTex('F(X) = 1 - e^{-x}', substrings_to_isolate=['F(X) =']).shift(2*UP)
		plot3_2 = ax_r1c.plot(lambda x: 1 - math.exp(-x), color=BLUE)
		self.play(Transform(f3_1, f3_2), Transform(plot3_1, plot3_2))
		self.end_fragment()

		ax_r2 = Axes(x_range=[-1, 4], y_range=[0, 1, 0.2], x_length=5, y_length=3,
			   axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(RIGHT*3.5 + DOWN*1.5)
		plot3_3 = ax_r2.plot(lambda x: 1 - math.exp(-x), color=BLUE)
		self.play(Transform(ax_r3, ax_r2), Transform(plot3_1, plot3_3))
		self.end_fragment()

		f3_3 = MathTex('F(X) = \{', substrings_to_isolate=['\{']).shift(2*UP+LEFT)
		f3_4 = MathTex('1 - e^{-x}, x \ge 0')
		f3_5 = MathTex('0, x < 0')
		VGroup(f3_4, f3_5).arrange(DOWN, buff=0.4, aligned_edge=LEFT).next_to(f3_3, RIGHT)
		f3_3[1].stretch(3, 1)
		self.remove(f3_1)
		self.play(Transform(f3_2[0], f3_3), Transform(f3_2[1], f3_4))
		self.end_fragment()

		plot3_4 = ax_r2.plot(lambda x: 0 if x <= 0 else 1 - math.exp(-x), color=BLUE)
		self.play(Write(f3_5), Transform(plot3_1, plot3_4))
		arr3_1 = np.array([0 if x <= n/5 else 1 - math.exp(-x*5/n + 1) for x in range(n)])
		pl3_1 = polygon_from_arr(arr3_1, ax_rn, [0, 1])

		self.play(Write(pl3_1))
		self.remove(plot3_1)
		self.end_fragment()

		arr3_2 = np.array([1 - math.exp(-x*5/n) for x in range(n)])
		pl3_2 = polygon_from_arr(arr3_2, ax_rn, [0, 1])
		self.play(Transform(ax_r3, ax_r1c), Transform(pl3_1, pl3_2))

		f3_6 = MathTex('1 - e^{-\lambda x}, x > 0').move_to(f3_4, aligned_edge=LEFT)
		f3_7 = MathTex('\lambda =\,').next_to(t4, DOWN*2, aligned_edge=LEFT)
		num3_1 = DecimalNumber(1).next_to(f3_7, RIGHT)
		self.play(Write(VGroup(f3_7, num3_1)), Transform(f3_2[1], f3_6))
		self.end_fragment(fragment_type=NO_PAUSE)
		
		arr3_3 = np.array([1 - math.exp(-2*x*5/n) for x in range(n)])
		pl3_3 = polygon_from_arr(arr3_3, ax_rn, [0, 1])
		self.play(Transform(pl3_1, pl3_3), ChangingNumber(num3_1, 2))
		self.wait(2)

		arr3_4 = np.array([1 - math.exp(-0.4*x*5/n) for x in range(n)])
		pl3_4 = polygon_from_arr(arr3_4, ax_rn, [0, 1])
		self.play(Transform(pl3_1, pl3_4), ChangingNumber(num3_1, 0.4))
		self.wait(2)

		self.play(Transform(pl3_1, pl3_2), ChangingNumber(num3_1, 1))
		self.wait(2)

		self.end_fragment(fragment_type=LOOP)

		group2 = VGroup(f3_2[0], f3_2[1], f3_5)
		self.play(group2.animate.shift(RIGHT*3))

		f3_8 = MathTex('f(X) = \{', substrings_to_isolate=['\{']).shift(2*UP+LEFT*3.5)
		f3_8[1].stretch(3, 1)
		f3_9 = MathTex('\lambda e^{-\lambda x}, x \ge 0')
		f3_10 = MathTex('0, x < 0')
		VGroup(f3_9, f3_10).arrange(DOWN, buff=0.4, aligned_edge=LEFT).next_to(f3_8, RIGHT)

		group3 = VGroup(f3_8, f3_9, f3_10)
		self.play(TransformFromCopy(group2, group3))

		ax_l3 = Axes(x_range=[0, 5], y_range=[0, 1, 0.2], x_length=5, y_length=3,
			   axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN*1.5)
		ax_l3n = Axes(x_range=[0, 1], y_range=[0, 1], x_length=5, y_length=3).shift(LEFT*3.5 + DOWN*1.5)
		self.play(Transform(ax_l1, ax_l3))
		
		arr3_5 = np.array([math.exp(-x*5/n) for x in range(n)])
		pl3_5 = polygon_from_arr(arr3_5, ax_l3n, [0, 1])
		self.play(Write(pl3_5))
		self.end_fragment()
		
		
		def transform_d3(l):
			arr3_6 = np.array([l*math.exp(-l*x*5/n) for x in range(n)])
			pl3_6 = polygon_from_arr(arr3_6, ax_l3n, [0, 1])

			arr3_7 = np.array([1 - math.exp(-l*x*5/n) for x in range(n)])
			pl3_7 = polygon_from_arr(arr3_7, ax_rn, [0, 1])
			self.play(Transform(pl3_5, pl3_6), Transform(pl3_1, pl3_7), ChangingNumber(num3_1, l))
		
		transform_d3(0.5)
		self.wait(2)

		transform_d3(3)
		self.wait(2)

		transform_d3(1.5)
		self.wait(2)

		transform_d3(1)

		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(ax_r3, pl3_1)))

		f3_11 = MathTex('M(X) =  \\frac{1}{\lambda}')
		f3_12 = MathTex('D(X) = \\frac{1}{\lambda^{2}}')
		f3_13 = MathTex('As = 2')
		f3_14 = MathTex('E = 6')

		VGroup(f3_11, f3_12).scale(0.9).arrange(RIGHT, buff=0.6).shift(DOWN*1+RIGHT*3)
		VGroup(f3_13, f3_14).arrange(RIGHT, buff=2).shift(DOWN*2.6+RIGHT*3)

		self.play(Write(f3_11))
		self.end_fragment()

		self.play(Write(f3_12))
		self.end_fragment()

		self.play(Write(f3_13))
		self.end_fragment()

		self.play(Write(f3_14))
		self.end_fragment()

		self.play(Unwrite(VGroup(pl3_5, f3_7, num3_1, group2, group3, f3_11, f3_12, f3_13, f3_14)))

		
		ax_l2 = Axes(x_range=[-1, 4], y_range=[0, 0.7, 0.1], x_length=5, y_length=3,
			   axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False}).shift(LEFT*3.5 + DOWN*1.5)

		t3 = Text('4.3 Нормальний розподіл', font_size=32).align_on_border(UL)
		self.play(Transform(t1, t3), Transform(ax_l1, ax_l2))

		f2_1 = MathTex('f(x) = e^{-x^{2}}').shift(UP*2)
		self.play(Write(f2_1))

		arr2_1 = np.array([math.exp(-(5*x/n - 1)**2) for x in range(n)])
		pl2_1 = polygon_from_arr(arr2_1, ax_ln, [0, 1])
		pl2_1c = pl2_1.copy()
		self.play(Write(pl2_1))
		self.end_fragment()

		f2_s = MathTex('S =\,').shift(RIGHT*2)
		num2_1 = DecimalNumber(0).next_to(f2_s, RIGHT)
		self.play(Write(VGroup(f2_s, num2_1)))
		self.play(ChangingDecimal(num2_1, lambda alpha: alpha*1.772))
		self.end_fragment()
		f2_s2 = MathTex('= \sqrt{\pi}').next_to(num2_1, RIGHT)
		self.play(Write(f2_s2))
		self.end_fragment()

		f2_2 = MathTex('f(x) = \\frac{1}{\sqrt{\pi}}e^{-x^{2}}').shift(UP*2)
		group1 = VGroup(f2_1, f2_s2)
		self.play(Transform(group1, f2_2))
		self.play(
			pl2_1.animate.stretch(0.564189, 1, about_edge=DOWN),
			ChangingDecimal(num2_1, lambda alpha: 1.772 - 0.772*alpha)
		)
		self.play(Unwrite(VGroup(f2_s, num2_1)))
		self.end_fragment()

		f2_mu = MathTex('\mu =\,').next_to(t3, DOWN*1.4, aligned_edge=LEFT)
		num2_2 = DecimalNumber(0).next_to(f2_mu, RIGHT)
		f2_3 = MathTex('f(x) = \\frac{1}{\sqrt{\pi}}e^{-(x-\mu)^{2}}').shift(UP*2)
		self.play(Transform(group1, f2_3), Write(VGroup(f2_mu, num2_2)))
		self.end_fragment()

		for i in range(1, 81):
			alpha = rate_functions.smooth(i/80)
			mu = 2.5*alpha
			num2_2.set_value(mu)
			arr2_2 = np.array([math.exp(-(5*x/n - 1 - mu)**2)/1.772 for x in range(n)])
			pl2_2 = polygon_from_arr(arr2_2, ax_ln, [0, 1])
			self.play(Transform(pl2_1, pl2_2, run_time=0.02))
		
		arr2_3 = np.array([math.exp(-(5*x/n - 2.5)**2)/1.772 for x in range(n)])
		pl2_3 = polygon_from_arr(arr2_3, ax_ln, [0, 1])
		self.play(Transform(pl2_1, pl2_3), Transform(ax_l1, ax_l1c))
		self.end_fragment()

		sequance = np.array(range(n))*5/n
		D2_1 = np.dot(arr2_3, (sequance-2.5)**2)*5/n
		sigma2_1 = math.sqrt(D2_1)
		f2_sigma = MathTex('\sigma =\,').next_to(f2_mu, DOWN*1.4, aligned_edge=LEFT)
		num2_3 = DecimalNumber(sigma2_1).next_to(f2_sigma, RIGHT)
		self.play(Write(VGroup(f2_sigma, num2_3)))
		self.end_fragment()

		f2_4 = MathTex('f(x) = \\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\\frac{(x-\mu)^{2}}{2\sigma^{2}}}').shift(UP*2)
		self.play(Transform(group1, f2_4))
		self.end_fragment()

		arr2_4 = np.array([math.exp(-((5*x/n - 2.5)**2)/2)/2.5066 for x in range(n)])
		pl2_4 = polygon_from_arr(arr2_4, ax_ln, [0, 1])
		self.play(
			Transform(pl2_1, pl2_4), 
			ChangingDecimal(num2_3, lambda alpha: 0.7071 + (1 - 0.7071)*alpha)
		)
		self.end_fragment()

		f2_5 = MathTex('\Phi(x) = \\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x}e^{-t^2/2}dt').shift(UP*2.5+RIGHT*3.5)
		self.play(group1.animate.shift(LEFT*2), TransformFromCopy(group1, f2_5))
		self.end_fragment()

		f2_6 = MathTex('F(x) = \Phi(\\frac{x-\mu}{\sigma})').next_to(f2_5, DOWN*1.8)
		self.play(Write(f2_6))
		self.end_fragment()

		darr2_1 = calculate_integral(arr2_4)*5/n
		pl2_5 = polygon_from_arr(darr2_1, ax_rn, [0, 1])
		self.play(Write(VGroup(ax_r1c, pl2_5)))
		self.end_fragment(fragment_type=NO_PAUSE)
		
		def transform_d2(mu, sigma, dt = 0.1):
			arr = np.array([math.exp(-((5*x/n - mu)**2)/(2*sigma**2))/math.sqrt(2*math.pi*sigma**2) for x in range(n)])
			darr = arr*n/5/arr.sum()
			sarr = calculate_integral(arr/arr.sum())
			pl1 = polygon_from_arr(darr, ax_ln, [0, 1])
			pl2 = polygon_from_arr(sarr, ax_rn, [0, 1])
			mu_orig = num2_2.get_value()
			sigma_orig = num2_3.get_value()
			self.play(
				Transform(pl2_1, pl1, run_time = dt),
				Transform(pl2_5, pl2, run_time = dt),
				ChangingDecimal(num2_2, lambda alpha: (mu_orig + alpha*(mu - mu_orig)), run_time= dt),
				ChangingDecimal(num2_3, lambda alpha: (sigma_orig + alpha*(sigma - sigma_orig)), run_time= dt)
			)

		def iterate_transform2(mu, sigma):
			mu_orig = num2_2.get_value()
			sigma_orig = num2_3.get_value()
			for i in range(1, 81):
				alpha = rate_functions.smooth(i/80)
				mu_val = mu_orig + alpha*(mu - mu_orig)
				sigma_val = sigma_orig + alpha*(sigma - sigma_orig)
				transform_d2(mu_val, sigma_val, 0.02)

		iterate_transform2(2.5, 0.5)
		self.wait(2)

		iterate_transform2(4, 0.5)
		self.wait(2)

		iterate_transform2(1, 0.5)
		self.wait(2)

		iterate_transform2(2.5, 2)
		self.wait(2)

		iterate_transform2(2.5, 1)
		self.wait(2)

		self.end_fragment(fragment_type=LOOP)

		iterate_transform2(2.5, 0.7)

		f2_11 = MathTex('P(|X - \mu|<').next_to(f2_sigma, DOWN*1.6, aligned_edge=LEFT) 
		num2_4 = DecimalNumber(0).next_to(f2_11, RIGHT)
		f2_12 = MathTex('\sigma) =\,').next_to(num2_4, RIGHT,buff=0.05)
		num2_5 = DecimalNumber(0, 4).next_to(f2_12, RIGHT)

		self.play(Write(VGroup(f2_11, num2_4, f2_12, num2_5)))
		self.end_fragment()
		
		arr2_5 = np.array([math.exp(-((5*x/n - 2.5)**2)/(2*0.7**2))/math.sqrt(2*math.pi*0.7**2) for x in range(n)])
		darr2_5 = arr2_5*n/5/arr2_5.sum()
		sarr2_5 = calculate_integral(arr2_5/arr2_5.sum())
		pl2_6 = polygon_from_arr(darr2_5, ax_ln, [0.5, 0.5]).set_color(BLUE)
		self.play(Write(pl2_6))

		l5 = Line(ax_l1.c2p(*(1.8, 0, 0)), ax_l1.c2p(*(1.8, 0.61, 0)), color=RED, stroke_width=6)
		l5t = MathTex('\mu - \sigma', font_size=32, color=RED).shift(ax_l1.c2p(*(1.8, -0.15, 0)))
		l6 = Line(ax_l1.c2p(*(3.2, 0, 0)), ax_l1.c2p(*(3.2, 0.61, 0)), color=RED, stroke_width=6)
		l6t = MathTex('\mu + \sigma', font_size=32, color=RED).shift(ax_l1.c2p(*(3.2, -0.15, 0)))

		self.play(Write(VGroup(l5, l5t, l6, l6t)))

		def generate_percentage(val):
			start = num2_4.get_value()
			for i in range(1, 81):
				alpha = rate_functions.smooth(i/80)
				current = start + alpha*(val - start)
				a = 2.5 - current*0.7
				b = 2.5 + current*0.7
				num2_4.set_value(current)
				pl2_7 = polygon_from_arr(darr2_5, ax_ln, [a/5, b/5]
					).set_color(BLUE).set_fill(BLUE, opacity=0.7)
				self.play(Transform(pl2_6, pl2_7, run_time=0.02))
				num2_5.set_value(sarr2_5[math.floor(n*b/5)] - sarr2_5[math.floor(n*a/5)])
			
			num2_5.set_value(0.6827 if val == 1 else 0.9545 if val==2 else 0.9973)

		generate_percentage(1)
		self.end_fragment()

		generate_percentage(2)
		self.end_fragment()

		generate_percentage(3)
		self.end_fragment()

		generate_percentage(1)
		arr2_6 = np.array([math.exp(-((5*x/n - 2.5)**2)/(2*1.5**2))/math.sqrt(2*math.pi*1.5**2) for x in range(n)])
		darr2_6 = arr2_6*n/5/arr2_6.sum()
		sarr2_6 = calculate_integral(arr2_6/arr2_6.sum())
		pl2_8 = polygon_from_arr(darr2_6, ax_ln, [0, 1])
		pl2_9 = polygon_from_arr(darr2_6, ax_ln, [0.2, 0.8]).set_color(BLUE).set_fill(BLUE, opacity=0.7)
		pl2_10 = polygon_from_arr(sarr2_6, ax_rn, [0, 1])
		
		self.play(
			Transform(pl2_1, pl2_8),
			Transform(pl2_6, pl2_9),
			Transform(pl2_5, pl2_10),
			VGroup(l5, l5t).animate.set_coord(ax_l1.c2p(*(1, 0, 0))[0], 0),
			VGroup(l6, l6t).animate.set_coord(ax_l1.c2p(*(4, 0, 0))[0], 0),
			ChangingNumber(num2_3, 1.5)
		)
		self.end_fragment()
		
		for i in range(1, 81):
			alpha = rate_functions.smooth(i/80)
			current = 1 - alpha
			a = 2.5 - current*1.5
			b = 2.5 + current*1.5
			num2_4.set_value(current)
			pl2_7 = polygon_from_arr(darr2_6, ax_ln, [a/5, b/5]
				).set_color(BLUE).set_fill(BLUE, opacity=0.7)
			self.play(Transform(pl2_6, pl2_7, run_time=0.02))
			num2_5.set_value(sarr2_5[math.floor(n*b/5)] - sarr2_5[math.floor(n*a/5)])
		
		self.play(Unwrite(VGroup(pl2_6, l5, l5t, l6, l6t)))
		self.play(Unwrite(VGroup(f2_11, num2_4, f2_12, num2_5)), 
			Transform(pl2_1, pl2_4), ChangingNumber(num2_3, 1))

		f2_7 = MathTex('M(X) = \mu')

		f2_8 = MathTex('D(X) = \sigma^{2}')

		f2_9 = MathTex('As = 0')

		f2_10 = MathTex('E = 0')

		VGroup(f2_7, f2_8).scale(0.9).arrange(RIGHT, buff=0.6).shift(DOWN*1+RIGHT*3)
		VGroup(f2_9, f2_10).arrange(RIGHT, buff=2).shift(DOWN*2.6+RIGHT*3)

		self.play(Unwrite(VGroup(ax_r1c, pl2_5, l3, l3t, l4, l4t)))
		self.play(Write(f2_7))
		self.end_fragment()

		self.play(Write(f2_8))
		self.end_fragment()

		self.play(Write(f2_9))
		self.end_fragment()

		self.play(Write(f2_10))
		self.end_fragment()

		self.play(Unwrite(VGroup(f2_5, f2_7, f2_8, f2_9, f2_10)))

		self.play(f2_6.animate.shift(UP))

		t5 = Text('4.4 Логнормальний розподіл', font_size=32).align_on_border(UL)
		self.play(Transform(t1, t5))

		f4_1 = MathTex('X = e^{Y}, Y -\,').shift(RIGHT)
		f4_2 = Text('нормальний розподіл', font_size=32).next_to(f4_1)
		self.play(Write(VGroup(f4_1, f4_2)))
		self.end_fragment()
		
		ax_l4 = Axes(x_range=[0, 1, 0.2], y_range=[0, 0.7, 0.1], x_length=5, y_length=3,
		   axis_config={"include_ticks": True, "include_numbers":True, "include_tip": False},
		   x_axis_config={"scaling": LogBase(5)}).shift(LEFT*3.5 + DOWN*1.5)
		def lognormal(mu, sigma):
			return np.array([math.exp(-((math.log(5*x/n, math.e)-mu)**2)/2/(sigma**2))*n/x/5/sigma/2.5066 for x in range(1, n)])
		arr4_1 = lognormal(0.41, 0.5)
		pl4_1 = polygon_from_arr(arr4_1, ax_ln, [0, 1])

		self.play(Transform(pl2_1, pl4_1), Transform(ax_l1, ax_l4))
		self.end_fragment()
		
		self.play(Transform(ax_l1, ax_l1c), Unwrite(VGroup(f4_1, f4_2)))
		self.end_fragment()

		f4_2 = MathTex('f(x) = \\frac{1}{x\sqrt{2\pi\sigma^{2}}}e^{-\\frac{(ln x-\mu)^{2}}{2\sigma^{2}}}').shift(UP*2+LEFT*1.7)
		self.play(Transform(group1, f4_2))
		self.end_fragment()

		f4_3 = MathTex('f(x) = 0, x \le 0').next_to(f4_2, DOWN*1.2)
		self.play(Write(f4_3))
		self.end_fragment()

		self.play(ChangingNumber(num2_2, 0.41), ChangingNumber(num2_3, 0.5))
		self.end_fragment()

		f4_4 = MathTex('F(X) = \Phi(\\frac{ln x-\mu}{\sigma})').next_to(f4_2, RIGHT, buff=0.7)
		self.play(Transform(f2_6, f4_4))

		darr4_1 = calculate_integral(arr4_1)/arr4_1.sum()
		pl4_2 = polygon_from_arr(darr4_1, ax_rn, [0, 1])
		self.play(Write(VGroup(ax_r1cc,pl4_2)))
		self.end_fragment()

		f4_5 = MathTex('F(x) = 0, x \le 0').next_to(f4_4, DOWN*1.2)
		self.play(Write(f4_5))
		self.end_fragment()
		
		def transform_d4 (mu, sigma):
			arr4_2 = lognormal(mu, sigma)
			darr4_2 = calculate_integral(arr4_2)*5/n
			print(arr4_2.sum())
			pl4_3 = polygon_from_arr(arr4_2, ax_ln, [0, 1])
			pl4_4 = polygon_from_arr(darr4_2, ax_rn, [0, 1])
			self.play(Transform(pl2_1, pl4_3), 
				Transform(pl4_2, pl4_4), 
				ChangingNumber(num2_2, mu),
				ChangingNumber(num2_3, sigma)
			)

		transform_d4(0, 0.5)
		self.wait(2)

		transform_d4(1, 0.5)
		self.wait(2)
				
		transform_d4(0.2, 0.5)
		self.wait(2)

		transform_d4(0.2, 1)
		self.wait(2)

		transform_d4(0, 1)
		self.wait(2)

		transform_d4(0, 2)
		self.wait(2)

		transform_d4(1, 1)
		self.wait(2)

		transform_d4(0.41, 0.5)
		self.wait(2)

		self.end_fragment(fragment_type=LOOP)

		self.play(Unwrite(VGroup(ax_r1cc, pl4_2)))

		f4_6 = MathTex('M(X) = e^{\mu+\\frac{\sigma^{2}}{2}}')

		f4_7 = MathTex('Me = e^{\mu}')

		f4_8 = MathTex('Mo = e^{\mu - \sigma^{2}}')

		group4 = VGroup(f4_6, f4_7, f4_8).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT*3+DOWN*1.5)
		self.play(Write(group4))

		f4_9 = MathTex('D(X) = (e^{\sigma^{2}}-1)e^{2\mu +\sigma^{2}}')

		f4_10 = MathTex('As = (e^{\sigma^{2}}+2)\sqrt{e^{\sigma^{2}}-1}')

		f4_11 = MathTex('E = e^{4\sigma^{2}}+2e^{3\sigma^{2}}+3e^{2\sigma^{2}}-6')
		self.end_fragment()

		group5 = VGroup(f4_9, f4_10, f4_11).arrange(DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT*3+DOWN*1.5)
		self.play(Unwrite(group4))
		self.play(Write(group5))
		self.end_fragment()

		t6 = Text('Дякую за перегляд!')

		self.play(Transform(VGroup(t1, ax_l1, pl2_1, f2_mu, num2_2, f2_sigma, num2_3, group1, f2_6, f4_3, f4_5, group5), t6))
		self.end_fragment()
