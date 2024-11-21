from manim import *
from manim_revealjs import PresentationScene, NORMAL, NO_PAUSE, LOOP, COMPLETE_LOOP
import math
import numpy as np
import random

config.video_dir = "./videos"

class Intro(PresentationScene):
	def construct(self):
		t1 = Text('Числові характеристики',  font_size=42).move_to(UP*3)
		t2 = Text('неперервних випадкових величин(НВВ)',  font_size=42).move_to(UP*2)
		t3 = Text('Підготував: Суботін Ігор, МПІ-241', font_size=32).move_to(UP+LEFT*2)
		text1 = VGroup(t1, t2, t3)
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
		f41 = MathTable('= F(b) - F(a)').scale(0.8).next_to(f40, RIGHT*0.4)
		self.play(Write(VGroup(f40, f41)))
		self.end_fragment()

		f42 = MathTex('P(a \le x < b) ').scale(0.8).next_to(f40, DOWN*1.2, aligned_edge=LEFT)
		f43 = MathTable('= \int_{a}^{b} f(x) \,dx').scale(0.8).next_to(f42, RIGHT*0.4)
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
		self.play(Transform(t1, t3), Unwrite(VGroup(text3, text2, l1, l1t, pl11, ax1)))
		self.end_fragment()

		
class NumbericalVariance(PresentationScene):
	def construct(self):
		t1 = Text('3.2 Дисперсія', font_size=32).align_on_border(UL)
		self.add(t1)
		self.end_fragment()
		n = 500


class TextScene(PresentationScene):
	def construct(self):
		text = Text('Hello world')
		self.play(Write(text))
		self.end_fragment()
		self.play(Write(Square()))
		self.end_fragment()