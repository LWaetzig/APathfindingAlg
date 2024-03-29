import os
from manim import *


class ApplicationScene(MovingCameraScene):
    def construct(self):
        # set default font
        Text.set_default(font="Arial")

        # initialise objects
        ## Scene heading
        title = Text("Applications", font_size=70)

        ## Scene objects
        ### Icons for games
        pacman = SVGMobject(os.path.join("data", "icons", "pacman.svg"))
        counter_stike = SVGMobject(os.path.join("data", "icons", "csgo.svg")).scale(1.5)
        gta = SVGMobject(os.path.join("data", "icons", "gta.svg")).scale(1.5)

        ### Icons for logistics
        route = SVGMobject(os.path.join("data", "icons", "route.svg")).scale(1)
        logistic = SVGMobject(os.path.join("data", "icons", "truck.svg")).scale(1)
        dhl = SVGMobject(os.path.join("data", "icons", "dhl.svg")).scale(0.3)

        ### Icons for technology
        network = SVGMobject(os.path.join("data", "icons", "network.svg")).scale(1)
        robot = SVGMobject(os.path.join("data", "icons", "robot.svg")).scale(1)
        process = SVGMobject(os.path.join("data", "icons", "process.svg")).scale(1)

        ###############################
        # Start video timeline
        ###############################
        self.wait(2)
        self.play(FadeIn(title, shift=DOWN, scale=0.8), run_time=1)
        self.wait(1)
        self.play(title.animate.scale(0.5).to_corner(UL), run_time=1)
        self.wait(2)

        # show categories
        headings = (
            VGroup(
                Text("Games", color=WHITE),
                Text("Logistics", color=WHITE),
                Text("Technology", color=WHITE),
            )
            .arrange(buff=1.5)
            .move_to(ORIGIN)
        )
        self.play(FadeIn(headings), run_time=1)
        self.wait(5)
        self.play(FadeOut(headings), run_time=1)

        # games
        self.play(FadeIn(pacman), run_time=2)
        self.wait(2)
        self.play(pacman.animate.shift(LEFT * 4.2), FadeIn(counter_stike), run_time=2)
        self.wait(2)
        self.play(counter_stike.animate.shift(RIGHT * 4.2), FadeIn(gta), run_time=2)
        self.wait(3)
        self.play(
            pacman.animate.scale(0.4).shift(UP * 0.9),
            gta.animate.scale(0.4).shift(LEFT * 4.15, DOWN * 0.5),
            counter_stike.animate.scale(0.4).shift(LEFT * 8.3, DOWN * 2.1),
            run_time=2,
        )
        games_rect = SurroundingRectangle(
            VGroup(pacman, counter_stike, gta), buff=0.7, corner_radius=0.2, color=WHITE
        )
        games = Text("Games", color=WHITE, font_size=30).next_to(games_rect, UP)
        self.play(Create(games_rect), Write(games))
        self.wait(4)
        self.play(
            FadeOut(games_rect),
            FadeOut(VGroup(pacman, counter_stike, gta)),
            FadeOut(games),
        )
        self.wait(2)

        # logistics
        self.play(FadeIn(route))
        self.play(route.animate.shift(LEFT * 4.2), FadeIn(logistic))
        self.play(logistic.animate.shift(RIGHT * 4.2), FadeIn(dhl))
        self.wait(2)
        self.play(
            route.animate.scale(0.4).shift(RIGHT * 4.2, UP * 0.8),
            dhl.animate.scale(0.4).shift(DOWN * 0.6),
            logistic.animate.scale(0.4).shift(LEFT * 4.2, DOWN * 2.3),
        )
        logistics_rect = SurroundingRectangle(
            VGroup(route, logistic, dhl), buff=0.7, corner_radius=0.2, color=WHITE
        )
        logistics = Text("Logistics", color=WHITE, font_size=30).next_to(
            logistics_rect, UP
        )
        self.play(
            Create(logistics_rect),
            Write(logistics),
        )
        self.wait(2)
        self.play(
            FadeOut(logistics_rect),
            FadeOut(VGroup(route, logistic, dhl)),
            FadeOut(logistics),
        )
        self.wait(1)

        # technology
        self.play(FadeIn(network), run_time=2)
        self.play(network.animate.shift(LEFT * 4.2), FadeIn(robot), run_time=2)
        self.play(robot.animate.shift(RIGHT * 4.2), FadeIn(process), run_time=2)
        self.wait(4)
        self.play(
            network.animate.scale(0.4).shift(RIGHT * 8.4, UP * 0.8),
            process.animate.scale(0.4).shift(RIGHT * 4.2, DOWN * 0.7),
            robot.animate.scale(0.4).shift(DOWN * 2.3),
        )
        technology_rect = SurroundingRectangle(
            VGroup(network, robot, process), buff=0.7, corner_radius=0.2, color=WHITE
        )
        technology = Text("Technology", color=WHITE, font_size=30).next_to(
            technology_rect, UP
        )
        self.play(
            Create(technology_rect),
            Write(technology),
        )
        self.wait(4)
        # show all
        self.play(
            FadeIn(games_rect),
            FadeIn(VGroup(pacman, counter_stike, gta)),
            FadeIn(games),
            FadeIn(logistics_rect),
            FadeIn(VGroup(route, logistic, dhl)),
            FadeIn(logistics),
        )
        self.wait(4)
        self.play(
            FadeOut(technology_rect),
            FadeOut(VGroup(network, robot, process)),
            FadeOut(technology),
            FadeOut(games_rect),
            FadeOut(VGroup(pacman, counter_stike, gta)),
            FadeOut(games),
            FadeOut(logistics_rect),
            FadeOut(VGroup(route, logistic, dhl)),
            FadeOut(logistics),
            FadeOut(title),
        )
        self.wait(5)
