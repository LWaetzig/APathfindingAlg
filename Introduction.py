import os

from manim import *


class AStar(Scene):
    def construct(self):
        Text.set_default(font="Arial")

        """
        Text / Inhalt
        Was ist der A Star Pathfinding Algorithmus überhaupt?
        Der A*(star) Algorithmus ist ein intelligenter Suchalgorithmus, welcher es ermöglicht, den effizientesten Weg zwischen zwei Punkten in einem Graphen zu finden.
        Der Algorithmus wurde 1968 von Peter Hart, Nils Nilsson und Bertram Raphael beschrieben und gilt als Verallgemeinerung und Erweiterung des Dijkstra-Algorithmus.
        Das Hauptziel des A* Algorithmus ist es, den Pfad mit den geringsten Kosten zwischen einem Startknoten und einem Zielpunkt zu finden. 
        Die Kosten können verschiedene Kriterien wie Entfernung, Zeit oder Ressourcenverbrauch sein.
        Im Gegensatz zu uninformierten Suchalgorithmen verwendet der A*-Algorithmus eine Schätzfunktion bzw. Heuristik, um zielgerichtet zu suchen und damit die Laufzeit zu verringern.
        """

        # Create Graph
        p1 = Dot(color=GREEN, radius=0.4).move_to(2 * LEFT + 2 * UP)
        p2 = Dot(color=BLUE, radius=0.4).move_to(2 * RIGHT + 2 * UP)
        p3 = Dot(color=RED, radius=0.4).move_to(2 * RIGHT + 2 * DOWN)
        arrow1 = Arrow(p1.get_center(), p2.get_center(), buff=0.4)
        arrow2 = Arrow(p2.get_center(), p3.get_center(), buff=0.4)
        arrow3 = Arrow(p1.get_center(), p3.get_center(), buff=0.4)

        way = (
            VGroup(p1, p2, p3, arrow1, arrow2, arrow3).rotate(0.25 * PI).move_to(ORIGIN)
        )

        # Create Graph (again because of bug in animation)
        p10 = Dot(color=GREEN, radius=0.4).shift(2 * LEFT + 2 * UP)
        p20 = Dot(color=BLUE, radius=0.4).shift(2 * RIGHT + 2 * UP)
        p30 = Dot(color=RED, radius=0.4).shift(2 * RIGHT + 2 * DOWN)
        arrow10 = Arrow(p10.get_center(), p20.get_center(), buff=0.4)
        arrow20 = Arrow(p20.get_center(), p30.get_center(), buff=0.4)
        arrow30 = Arrow(p10.get_center(), p30.get_center(), buff=0.4)

        new_way = (
            VGroup(p10, p20, p30, arrow10, arrow20, arrow30)
            .rotate(0.25 * PI)
            .move_to(ORIGIN)
        )

        # Create Texts
        title = Text("A* Pathfinding Algorithm", font_size=70)

        text_1 = Text(
            "Find the most efficient path between nodes", font_size=30
        ).move_to(2.5 * DOWN)
        text_2 = Text("1968 described by", font_size=30).move_to(2.25 * UP)

        name1 = Text("Peter Hart", font_size=30).move_to(4 * LEFT + 2.5 * DOWN)
        name2 = Text("Nils Nilsson", font_size=30).move_to(2.5 * DOWN)
        name3 = Text("Bertram Raphael", font_size=30).move_to(4 * RIGHT + 2.55 * DOWN)

        text_3 = Text(
            "Generalization and extension of Dijkstra's algorithm", font_size=30
        )

        euro = Text("€↓", font_size=70).move_to(arrow30.get_center() + 1 * DOWN)

        # Create pictures
        pic_peter = (
            ImageMobject(os.path.join("data", "Peter.jpg")).scale(1).move_to(4 * LEFT)
        )
        pic_nils = ImageMobject(os.path.join("data", "Nils.png")).scale(1)
        pic_bertram = (
            ImageMobject(os.path.join("data", "Bertram.png"))
            .scale(1)
            .move_to(4 * RIGHT)
        )

        entf = (
            ImageMobject(os.path.join("data", "Entfernung.png"))
            .scale(0.8)
            .move_to(4 * LEFT + 2.5 * DOWN)
        )
        zeit = (
            ImageMobject(os.path.join("data", "Zeit.png"))
            .scale(0.64)
            .move_to(2.5 * DOWN)
        )
        res = (
            ImageMobject(os.path.join("data", "Ressourcen.png"))
            .scale(0.64)
            .move_to(4 * RIGHT + 2.5 * DOWN)
        )

        # Create some Groups and Elements for animation purposes
        g1 = VGroup(way, text_1)

        dateandnames = VGroup(name1, name2, name3, text_2)

        ###############################
        # Start with the video timeline
        ###############################

        self.play(FadeIn(title, shift=DOWN, scale=0.8), run_time=1)
        self.wait(2)
        self.play(title.animate.scale(0.5).to_corner(UL), run_time=1)
        self.wait(1)
        #5
        self.play(Create(p1), Create(p2), Create(p3), run_time=2)
        self.play(Create(arrow1), Create(arrow2), run_time=2)
        self.play(Write(text_1), Create(arrow3), run_time=2)
        self.wait(3)
        # 14
        self.play(ReplacementTransform(g1, text_2), run_time=1)
        self.wait(1)
        #16
        self.play(
            ReplacementTransform(text_2.copy(), name1), FadeIn(pic_peter), run_time=1
        )
        self.play(
            ReplacementTransform(name1.copy(), name2), FadeIn(pic_nils), run_time=1
        )
        self.play(
            ReplacementTransform(name2.copy(), name3), FadeIn(pic_bertram), run_time=1
        )
        self.wait(1)
        #20
        self.play(
            FadeOut(pic_peter),
            FadeOut(pic_nils),
            FadeOut(pic_bertram),
            ReplacementTransform(dateandnames, text_3),
            run_time=1,
        )
        self.wait(3)  
        # 24
        self.play(ReplacementTransform(text_3, new_way), run_time=1)
        self.wait(3)
        #28
        self.play(Write(euro), run_time=1)
        self.wait(4)
        self.play(FadeOut(euro), run_time=1)  # 34
        self.play(new_way.animate.move_to(1 * UP), run_time=1)

        self.play(FadeIn(entf), run_time=1)
        self.play(FadeIn(zeit), run_time=1)
        self.play(FadeIn(res), run_time=1)  # 38
        self.play(
            FadeOut(entf),
            FadeOut(zeit),
            FadeOut(res),
            FadeOut(new_way),
            run_time=1,
        )  # 39

        # Ab hier dann Heuristik animationen. Rest ist schon Synchron mit Audiospur
        self.wait(10)
