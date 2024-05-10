from manim import *            
from manim_voiceover import VoiceoverScene      
from manim_voiceover.services.gtts import GTTSService 

config.frame_size = (900,1600)
config.frame_width = 9
config.frame_height = 16     
config.background_color = "#1a1815"



class theorem(VoiceoverScene):
    def construct(self):
        
        self.set_speech_service(GTTSService(lang="en", tld="com.au", transcription_model='base'))


        text1 = Text('Let’s prove the Pythagorean theorem intuitively', font_size=30)

        with self.voiceover(text="Let’s prove the Pythagorean theorem intuitively") as tracker:
            self.play(Write(text1))

        self.play(FadeOut(text1))

        square1 = Square(color="white").scale(1.75)

        textd1 = MathTex('D', font_size=30)
        textd2 = MathTex('D', font_size=30)
        textd3 = MathTex('D', font_size=30)
        textd4 = MathTex('D', font_size=30)

        textd1.next_to(square1, LEFT )
        textd2.next_to(square1, RIGHT )
        textd3.next_to(square1, DOWN * 2)
        textd4.next_to(square1, UP )

        with self.voiceover(text="We will start with a square with side length d") as tracker:
            self.play(Create(square1))
            self.play(FadeIn(textd1,textd2,textd3,textd4))
        
        self.wait(1)

        squareTopLeft = square1.get_corner(UL)
        squareBottomLeft = square1.get_corner(DL)
        squareTopRight = square1.get_corner(UR)
        squareBottomRight = square1.get_corner(DR)

        squareLeftCenter = (squareTopLeft+squareBottomLeft)/2
        squareRightCenter = (squareTopRight+squareBottomRight)/2
        squareTopCenter = (squareTopRight+squareTopLeft)/2
        squareDownCenter = (squareBottomRight+squareBottomLeft)/2


        dot1 = Dot(squareLeftCenter, color=WHITE)
        dot2 = Dot(squareTopCenter, color=WHITE)
        dot3 = Dot(squareRightCenter, color=WHITE)
        dot4 = Dot(squareDownCenter, color=WHITE)

        brace = Brace(square1)


        self.play(FadeOut(textd1,textd2,textd4),FadeIn(brace),Create(dot1), Create(dot2), Create(dot3), Create(dot4))
        self.wait(2)

        text2 = Text('d = a+b', font_size=35).shift(DOWN * 3)

        self.play(FadeOut(textd3),Create(text2))

        self.wait(2)

        triangle1 = Polygon(squareLeftCenter, squareTopCenter, squareTopLeft).set_color(YELLOW)
        triangle2 = Polygon(squareTopCenter, squareRightCenter, squareTopRight).set_color(YELLOW)
        triangle3 = Polygon(squareRightCenter, squareDownCenter, squareBottomRight).set_color(YELLOW)
        triangle4 = Polygon(squareDownCenter, squareLeftCenter, squareBottomLeft).set_color(YELLOW)

        self.play(Create(triangle1),FadeOut(dot1),FadeOut(dot2))
        self.play(Create(triangle2))
        self.play(Create(triangle3),FadeOut(dot3),FadeOut(dot4))
        self.play(Create(triangle4))
        text2.set_color(YELLOW)
        brace.set_color(YELLOW)

        self.wait(1)
        self.remove(text2,brace)

        self.wait(1)

        triangle1.set_color(WHITE)
        triangle2.set_color(WHITE)
        triangle3.set_color(WHITE)
        triangle4.set_color(WHITE)

        self.wait(1)

        a = MathTex("a").next_to((squareLeftCenter+squareTopLeft)/2, LEFT)
        b = MathTex("b").next_to((squareTopLeft+squareTopCenter)/2, UP )
        c = MathTex("c").next_to((squareTopCenter+squareLeftCenter)/2, DOWN * 0.5 )

        self.play(Create(a),Create(b),Create(c))

        self.wait(2)

        mtext = MathTex('Area of Large Square = d^2 = (a+b)^2', font_size = 35).shift(DOWN*3)
        mtext1 = MathTex('= a^2 + b^2 + 2ab', font_size = 35).next_to(mtext,DOWN)

        self.play(Create(mtext), Create(mtext1))

        self.wait(5)

        self.remove(mtext,mtext1)

        triangle1.set_color(YELLOW)

        mtext2 = MathTex('Area\\ of\\ Triangle =\\frac{1}{2} \\times a \\times b ', color = YELLOW).shift(DOWN*3)

        self.play(Create(mtext2))

        self.wait(5)

        triangle1.set_color(WHITE)

        triangle1.set_fill(YELLOW, opacity=.60)
        triangle2.set_fill(YELLOW, opacity=.60)
        triangle3.set_fill(YELLOW, opacity=.60)
        triangle4.set_fill(YELLOW, opacity=.60)


        self.wait(2)

        mtext3 = MathTex("Area\\ of\\ 4\\ Triangles = 4 \\times \\left(\\frac{1}{2} \\times a \\times b\\right)", font_size = 35).next_to(mtext2, DOWN)
        mtext4 = MathTex('=\\ 2\\times a \\times b', font_size = 35). next_to(mtext3,DOWN)

        self.play(Create(mtext3),Create(mtext4))

        self.wait(3)

        lSquare = Polygon(squareLeftCenter,squareTopCenter,squareRightCenter,squareDownCenter).set_fill(YELLOW, opacity=0.3)

        self.play(FadeOut(triangle1), FadeOut(triangle2),FadeOut(triangle3), FadeOut(triangle4), FadeOut(mtext4), FadeOut(mtext2), FadeOut(mtext3))

        mtext5 = MathTex("Area\\ of\\ Smaller\\ Square\\ =\\ C^2 ", font_size = 30).shift(DOWN*3)
        mtext6 = MathTex("Area(Small)\\ =\\ Area(Larg)\\ -\\ Area(4\\ Triangles)", font_size = 30).next_to(mtext5,DOWN)
        mtext7 = MathTex("c^2 = (a^2+b^2+2ab) - (2ab)", font_size = 30).next_to(mtext6,DOWN)
        mtext8 = MathTex("= a^2 + b^2", font_size = 30).next_to(mtext7,DOWN)

        self.play(Create(lSquare), Create(mtext5), Create(mtext6),Create(mtext7),Create(mtext8))
        self.wait(2)








        







        







