from manimlib.imports import *

class SquareToCircle(Scene):
    def construct(self):
        AnimatedObject = Circle()

        AnimatedObject.set_fill(BLUE, opacity=0.5)
        AnimatedObject.set_stroke(BLUE_E, width=4)
        AnimatedObject.rotate(180*DEGREES)

        square = Square()

        square.set_fill(GREYISH_BLUE, opacity=0.5)
        square.set_stroke(GREYISH_BLUE_A, width=4)

        text = Text("These aresometransformation tests")
        #myexpression = Text("Smiley Face")
        #secondthing = Text("And I like this transformationasd")
        secondttop = Text("And I like this transformaiton")
        #secondttop.set_color("#333333")


        self.wait()

        self.play(Write(AnimatedObject))

        self.wait()

        self.play(Transform(Group(AnimatedObject), text))

        self.wait()

        self.remove(AnimatedObject)
        self.play(Transform(text, VGroup(square)))

        self.wait()

        # self.play(Transform(AnimatedObject, secondttop))

        # self.wait()

        #self.play(Write(secondttop))
        #self.remove(AnimatedObject, secondttop)

class TextTransformation(Scene):
    def construct(self):

        Bogd = Text("Arnaut Bogdan", font = "Latin Modern Roman")
        Alex = Text("Baca Alexei", font = "Latin Modern Roman")
        Andy = Text("Braga Andrian", font = "Latin Modern Roman")
        Miha = Text("Cobzac ‎Mihai", font = "Latin Modern Roman")
        Iana = Text("Cuciuc Iana", font = "Latin Modern Roman")
        Anas = Text("Furdui Anastasia", font = "Latin Modern Roman")
        Ilie = Text("Grapin Ilie", font = "Latin Modern Roman")
        Deni = Text("Gherasim Denis", font = "Latin Modern Roman")
        Ion = Text("Ilieș Ion", font = "Latin Modern Roman")
        Euge = Text("Mocanu Eugen", font = "Latin Modern Roman")
        Iuli = Text("Munteanu Iulian", font = "Latin Modern Roman")
        Adel = Text("Railean Adelina", font = "Latin Modern Roman")
        Laur = Text("Simon Laurențiu", font = "Latin Modern Roman")
        Mari = Text("Sârbu Maria", font = "Latin Modern Roman")
        Ilin = Text("Stegarescu ‎Ilinca", font = "Latin Modern Roman")
        Petr = Text("Vovniciuc Petru", font = "Latin Modern Roman")
        Nicu = Text("Vornicu Nicolae", font = "Latin Modern Roman")
        Augu = Text("Poiana Augustin", font = "Latin Modern Roman")
        # Etc = Text("...")
        LineIntro = Text("And here's a line", font = "Latin Modern Roman")
        LineIntroC = Text("And here's a line:", font = "Latin Modern Roman")
        LineIntroC.move_to([0,1,0])
        LineStart = (-2,-1,0)
        LineEnd =   (2,-1,0)
        line = Line(LineStart, LineEnd)

        Names = (
            Bogd,
            Alex,
            Andy,
            Miha,
            # Etc,
            Iana,
            Anas,
            Ilie,
            Deni,
            Ion,
            Euge,
            Iuli,
            Adel,
            Laur,
            Mari,
            Ilin,
            Petr,
            Nicu,
            # Etc,
            Augu,
        )

        def DeWrite(Object):
            print("Dewriting")
            ObjectTop = copy.deepcopy(Object)
            ObjectTop.set_fill("#333333")
            self.play(Write(ObjectTop))
            self.play(FadeOut(Object), run_time=.25)
            print("Dewritten")

        # def DeConstruct(Object):
        #     print("Deconstructing")
        #     ObjectTop = copy.deepcopy(Object)
        #     ObjectTop.set_fill(BLUE)
        #     ObjectTop.set_color(BLUE)
        #     ObjectTop.set_stroke(BLUE)
        #     print(ObjectTop.color())
        #     self.play(ShowCreation(ObjectTop))
        #     self.play(FadeOut(Object), run_time=.25)
        #     self.remove(ObjectTop)
        #     print("Deconstructed")

        def Change(FirstObject, SecondObject, WaitTime):
            print("Transforming")
            self.play(ReplacementTransform(FirstObject, SecondObject), run_time=.5)
            self.wait(WaitTime)

        self.play(Write(Names[0]))

        for i in range(0,len(Names)-1):
            print("Stage ", i)
            Change(Names[i], Names[i+1], 0)

        DeWrite(Names[-1])

        self.wait()

        self.play(ShowCreation(LineIntro))
        self.play(ReplacementTransform(LineIntro, LineIntroC))

        self.play(ShowCreation(line))

        self.wait()

        self.play(Uncreate(LineIntroC))
        self.play(Uncreate(line))

        self.wait()

class FourierSeries(Scene):
    def construct(self):
        time = 0
        wave = []


        x = 0
        y = 0

        for i in range(1, 5): 
            prevx = x
            prevy = y

            n = i * 2 + 1
            radius = 75 * (4 / (n * PI))
            x += radius * math.cos(n * time)
            y += radius * math.sin(n * time)

            radiusx2 = radius * 2

            circle = Circle()
            circle.move_to([prevx, prevy, 0])
            circle.set_stroke(WHITE)

            self.add(circle)

            # fill(255)
            # stroke(255)
            self.add(Line([prevx, prevy, 0], [x, y, 0]))
            # ellipse(x, y, 8)
        
        wave.append(y)

        

        self.add(Line([x - 200, y, 0], [0, wave[0], 0]))

        lineStart = [0, 0, 0]

        for i in range(0, len(wave) - 1):
            self.add(Line(lineStart, [i, wave[i], 0]))
            lineStart = [i, wave[i], 0]
        

        time += 0.05

        if (len(wave) > 250):
            wave.pop()
        
class Tests(Scene):
    def DeWrite(self, object, time=0.5):
        if isinstance(object, list):
            for i in range(0, len(object)):
                objectOverdraw = object[i].deepcopy()
                objectOverdraw.set_color("#333333")
                self.play(Write(objectOverdraw), run_time=time/2)
            for m in range(0, len(object)):
                self.play(FadeOut(object[m]), run_time=time/2)
            self.remove(objectOverdraw)
        else:
            objectOverdraw = object.deepcopy()
            objectOverdraw.set_color("#333333")
            self.play(Write(objectOverdraw), run_time=time/2)
            self.play(FadeOut(object), run_time=time/2)
            self.remove(objectOverdraw, object)
    def construct(self):
        
        fraction = Tex(r"{1}\over{7}")
        equal = Text("=")
        # fraction_moved = Tex(r"{1}\over{7}", color=RED).next_to(equal, LEFT)
        fraction1 = Tex(r"{1}\over{7}")
        fraction2 = Tex(r"{1}\over{7}")
        fraction_result = Tex(r"{2}\over{14}").next_to(equal, RIGHT)

        ellipse = Ellipse()
        ellipse2 = Ellipse(width=1, height=2)
        # ellipse2_code = Text([("ellipse2", color=), ("=", color="#c678dd"), "Ellipse(", "width", "=", "1", ",", "height", "=", "2", ")"])
        # ellipse2_code_bg = Rectangle()
        ellipse2_code = Text("ellipse2 = Ellipse(width=1, height=2)", 
                            t2c={'2':"#d19a66", 
                                'ellipse2':"#abb2bf", 
                                '=':"#c678dd", 
                                'Ellipse(':"#abb2bf", 
                                'width':"#d19a66", 
                                '1':"#d19a66", 
                                'height':"#d19a66",
                                ')':"#abb2bf"}, 
                            font="Monaco")
        
        ellipse2_code.bg = SurroundingRectangle(ellipse2_code, color="#282c34", fill_color="#282c34", fill_opacity=1)
        ellipse2_code_group = VGroup(ellipse2_code.bg, ellipse2_code)
        ellipse2_code_group.scale(0.6)
        ellipse2_code_group.to_corner(DR, buff=0)
        

        # self.wait(1)
        # self.play(Write(ellipse))
        # self.wait(0.5)
        # self.play(Transform(ellipse, ellipse2))
        # # self.play(Rotate(ellipse, 90*DEGREES))
        # self.wait(0.125)
        # # for i in range(0, len(ellipse2_code) - 1):
        # #     self.play(Write(ellipse2_code[i]))
        # self.play(Write(ellipse2_code_group))
        # # self.play(Write(text))
        # self.wait(0.5)
        # self.DeWrite(ellipse, 1)
        # self.play(FadeOut(ellipse2_code_group))
        # self.wait(1)
        # self.play(Write(fraction))
        # self.wait(1)
        # # self.play(Transform(fraction, fraction_moved), Transform(fraction1, equal), Transform(fraction2, fraction_result))
        # self.play(ApplyMethod(fraction.next_to, equal, LEFT), Transform(fraction1, equal), Transform(fraction2, fraction_result))
        # self.wait(1)
        # self.DeWrite([fraction,fraction1,fraction2])

        pointers = []
        for i in range(8):
            pointers.append(Line(ORIGIN, [math.cos(360/8*i*DEGREES),math.sin(360/8*i*DEGREES), 0],color=YELLOW))

        # for i in range(0, len(pointers)):
        self.play(ShowCreation(VGroup(*pointers)))
        self.add

class Math(Scene):
    def construct(self):
        math = Tex("\\frac{5}{8}kg*1000g")
        math1 = Tex("625g")
        multiply = Text("*")
        math2 = Tex("20").next_to(multiply,RIGHT)
        math3 = Tex("12500g")
        math4 = Tex("12\\frac{1}{2}kg")
        bigger = Text(">")
        math5 = Tex("10kg").next_to(bigger, RIGHT)

        self.wait()
        self.play(Write(math))
        self.play(Transform(math, math1))
        self.play(ApplyMethod(math.next_to,multiply,LEFT), ReplacementTransform(math.deepcopy(), multiply), ReplacementTransform(math.deepcopy(), math2))
        self.play(Transform(math, math3), Transform(math2, math3), Transform(multiply, math3))
        self.remove(multiply, math2)
        self.play(Transform(math, math4))
        self.play(ApplyMethod(math.next_to, bigger, LEFT), ReplacementTransform(math.deepcopy(), bigger), ReplacementTransform(math.deepcopy(), math5))
        self.wait(2)

class Math1(Scene):
    def construct(self):
        math = Tex("\\frac{2}{9}*\\frac{9}{2}")
        math1 = Tex("\\frac{2*9}{9*2}")
        math2 = Tex("1").next_to(math1[0][0], UP, buff=0.5)
        math3 = Tex("1").next_to(math1[0][6], DOWN, buff=0.5)
        math4 = Tex("1").next_to(math1[0][2], UP, buff=0.5)
        math5 = Tex("1").next_to(math1[0][4], DOWN, buff=0.5)
        math6 = Tex("\\frac{1*1}{1*1}")
        math7 = Tex("1")
        line = Line(math1[0][0].get_corner(DR), math1[0][0].get_corner(UL), color=RED)
        line1 = Line(math1[0][6].get_corner(DR), math1[0][6].get_corner(UL), color=RED)
        line2 = Line(math1[0][2].get_corner(DR), math1[0][2].get_corner(UL), color=RED)
        line3 = Line(math1[0][4].get_corner(DR), math1[0][4].get_corner(UL), color=RED)
        multiply = Tex("*").move_to(math[0][3])

        self.wait(1/3)
        self.play(Write(math))
        self.play(Transform(math[0][1], math1[0][3]), 
                  Transform(math[0][5], math1[0][3]), 
                  Transform(math[0][3], math1[0][1]),
                  ApplyMethod(multiply.move_to, math1[0][5]),
                  Transform(math[0][0], math1[0][0]),
                  Transform(math[0][4], math1[0][2]),
                  Transform(math[0][2], math1[0][4]),
                  Transform(math[0][6], math1[0][6]),
                  )
        self.play(ApplyMethod(math[0][0].set_color, RED), 
                  ApplyMethod(math[0][6].set_color, RED), 
                  ApplyMethod(math[0][2].set_color, RED),
                  ApplyMethod(math[0][4].set_color, RED), 
                  Write(line), 
                  Write(line1),
                  Write(line2),
                  Write(line3),
                  )
        self.play(Write(math2), 
                  Write(math3),
                  Write(math4),
                  Write(math5),
                  )
        self.play(FadeOut(math[0][0]), 
                  FadeOut(line), 
                  FadeOut(math[0][6]), 
                  FadeOut(line1),
                  FadeOut(math[0][2]), 
                  FadeOut(line2),
                  FadeOut(math[0][4]), 
                  FadeOut(line3),
                  ApplyMethod(math2.move_to, math6[0][0]),
                  ApplyMethod(math3.move_to, math6[0][6]),
                  ApplyMethod(math4.move_to, math6[0][2]),
                  ApplyMethod(math5.move_to, math6[0][4]),
                  )
        self.remove(math,
                    math2,
                    math3,
                    math4,
                    math5,
                    multiply,
                    )
        self.add(math6)
        math = Tex("\\frac{1}{1}")
        self.play(ReplacementTransform(math6[0][1], math[0][0]),
                  ReplacementTransform(math6[0][3], math[0][1]),
                  ReplacementTransform(math6[0][5], math[0][2]),
                  ApplyMethod(math6[0][0].move_to, math[0][0]),
                  ApplyMethod(math6[0][2].move_to, math[0][0]),
                  ApplyMethod(math6[0][4].move_to, math[0][2]),
                  ApplyMethod(math6[0][6].move_to, math[0][2]),
                  )
        self.remove(math6)
        self.play(ApplyMethod(math[0][0].move_to, math7),
                  Transform(math[0][1], math7),
                  ApplyMethod(math[0][2].move_to, math7),
                  )
        self.wait(1/3)
        # self.play(Write(math.deepcopy().set_color("#333333")))
        self.play(FadeOut(math), FadeOut(math7))
        self.wait(1/3)

class Math2(Scene):
    def construct(self):
        math = Tex("\\frac{5}{6}*\\frac{6}{5}")
        math1 = Tex("\\frac{5*6}{6*5}")
        math2 = Tex("1").next_to(math1[0][0], UP, buff=0.5)
        math3 = Tex("1").next_to(math1[0][6], DOWN, buff=0.5)
        math4 = Tex("1").next_to(math1[0][2], UP, buff=0.5)
        math5 = Tex("1").next_to(math1[0][4], DOWN, buff=0.5)
        math6 = Tex("\\frac{1*1}{1*1}")
        math7 = Tex("1")
        line = Line(math1[0][0].get_corner(DR), math1[0][0].get_corner(UL), color=RED)
        line1 = Line(math1[0][6].get_corner(DR), math1[0][6].get_corner(UL), color=RED)
        line2 = Line(math1[0][2].get_corner(DR), math1[0][2].get_corner(UL), color=RED)
        line3 = Line(math1[0][4].get_corner(DR), math1[0][4].get_corner(UL), color=RED)

        self.wait(1/3)
        self.play(Write(math))
        self.play(Transform(math, math1))
        self.play(ApplyMethod(math[0][0].set_color, RED), 
                  ApplyMethod(math[0][6].set_color, RED), 
                  ApplyMethod(math[0][2].set_color, RED), 
                  ApplyMethod(math[0][4].set_color, RED), 
                  Write(line), 
                  Write(line1),
                  Write(line2),
                  Write(line3),
                  )
        self.play(Write(math2), 
                  Write(math3),
                  Write(math4),
                  Write(math5),
                  )
        self.play(FadeOut(math[0][0]), 
                  FadeOut(line), 
                  FadeOut(math[0][6]), 
                  FadeOut(line1),
                  FadeOut(math[0][2]), 
                  FadeOut(line2),
                  FadeOut(math[0][4]), 
                  FadeOut(line3),
                  ApplyMethod(math2.move_to, math6[0][0]),
                  ApplyMethod(math3.move_to, math6[0][6]),
                  ApplyMethod(math4.move_to, math6[0][2]),
                  ApplyMethod(math5.move_to, math6[0][4]),
                  )
        self.remove(math,
                    math2,
                    math3,
                    math4,
                    math5,
                    )
        self.add(math6)
        math = Tex("\\frac{1}{1}")
        self.play(ReplacementTransform(math6, math))
        self.play(Transform(math, math7))
        self.wait(1/3)
        self.play(Write(math.deepcopy().set_color("#333333")))
        self.play(FadeOut(math))
        self.wait(1/3)

class Math3(Scene):
    def construct(self):
        math = Tex("\\frac{5}{6}*\\frac{6}{5}")
        math1 = Tex("\\frac{5*6}{6*5}")
        math2 = Tex("1").next_to(math1[0][0], UP, buff=0.5)
        math3 = Tex("1").next_to(math1[0][6], DOWN, buff=0.5)
        math4 = Tex("1").next_to(math1[0][2], UP, buff=0.5)
        math5 = Tex("1").next_to(math1[0][4], DOWN, buff=0.5)
        math6 = Tex("\\frac{1*1}{1*1}")
        math7 = Tex("1")
        line = Line(math1[0][0].get_corner(DR), math1[0][0].get_corner(UL), color=RED)
        line1 = Line(math1[0][6].get_corner(DR), math1[0][6].get_corner(UL), color=RED)
        line2 = Line(math1[0][2].get_corner(DR), math1[0][2].get_corner(UL), color=RED)
        line3 = Line(math1[0][4].get_corner(DR), math1[0][4].get_corner(UL), color=RED)
        multiply = Tex("*").move_to(math[0][3])

        self.wait(1/3)
        self.play(Write(math))
        self.play(Transform(math[0][1], math1[0][3]), 
                  Transform(math[0][5], math1[0][3]), 
                  Transform(math[0][3], math1[0][1]),
                  ApplyMethod(multiply.move_to, math1[0][5]),
                  Transform(math[0][0], math1[0][0]),
                  Transform(math[0][4], math1[0][2]),
                  Transform(math[0][2], math1[0][4]),
                  Transform(math[0][6], math1[0][6]),
                  )
        self.play(ApplyMethod(math[0][0].set_color, RED), 
                  ApplyMethod(math[0][6].set_color, RED), 
                  ApplyMethod(math[0][2].set_color, RED), 
                  ApplyMethod(math[0][4].set_color, RED), 
                  Write(line), 
                  Write(line1),
                  Write(line2),
                  Write(line3),
                  )
        self.play(Write(math2), 
                  Write(math3),
                  Write(math4),
                  Write(math5),
                  )
        self.play(FadeOut(math[0][0]), 
                  FadeOut(line), 
                  FadeOut(math[0][6]), 
                  FadeOut(line1),
                  FadeOut(math[0][2]), 
                  FadeOut(line2),
                  FadeOut(math[0][4]), 
                  FadeOut(line3),
                  ApplyMethod(math2.move_to, math6[0][0]),
                  ApplyMethod(math3.move_to, math6[0][6]),
                  ApplyMethod(math4.move_to, math6[0][2]),
                  ApplyMethod(math5.move_to, math6[0][4]),
                  )
        self.remove(math,
                    math2,
                    math3,
                    math4,
                    math5,
                    multiply,
                    )
        self.add(math6)
        math = Tex("\\frac{1}{1}")
        self.play(ReplacementTransform(math6, math))
        self.play(Transform(math, math7))
        self.wait(1/3)
        self.play(Write(math.deepcopy().set_color("#333333")))
        self.play(FadeOut(math))
        self.wait(1/3)

class March8(Scene):
    def construct(self):
        heart = SVGMobject("/home/alex/manim/assets/like_plain.svg")
        heart[0].set_color("#ff3636")
        heart[1].set_color("#f40000")

        text = Text("Te felicit cu 8 martie").move_to([0, 0.5, 0])
        text1 = Text("mama!").next_to(text, DOWN, buff=0.2)
        text2 = Text("Eu te iubesc!")
        # text = Text("I love you!")
        # text.rotate(30 * DEGREES)

        self.play(Write(heart), Write(text), Write(text1), run_time = 2)
        self.wait(2)
        self.play(Transform(text, text2), Transform(text1, text2))
        self.remove(text1)
        self.wait(2)
        # self.play(ApplyMethod(heart.move_to, [-1, 0, 0]))
        # self.play(ApplyMethod(heart.move_to, [1, 0, 0]))
        # self.play(ApplyMethod(heart[0].move_to, (heart[0].get_center() - [1, 0, 0])))
        # self.wait()
        # self.play(ApplyMethod(heart[1].move_to, (heart[1].get_center() - [1, 0, 0])))
        heart_top = heart.deepcopy()
        heart_top.set_color("#333333")
        text_top = text.deepcopy()
        text_top.set_color("#333333")
        self.play(Write(text_top), Write(heart_top), run_time=2)
        self.play(FadeOut(text), FadeOut(heart))

class March9(Scene):
    def construct(self):
        heart = SVGMobject("/home/alex/manim/assets/like_plain.svg")
        heart[0].set_color("#ff3636")
        heart[1].set_color("#f40000")

        text = Text("Te felicit cu 8 martie").move_to([0, 0.5, 0])
        text1 = Text("bunica!").next_to(text, DOWN, buff=0.2)
        text2 = Text("Eu te iubesc!")
        # text = Text("I love you!")
        # text.rotate(30 * DEGREES)

        self.play(Write(heart), Write(text), Write(text1), run_time = 2)
        self.wait(2)
        self.play(Transform(text, text2), Transform(text1, text2))
        self.remove(text1)
        self.wait(2)
        # self.play(ApplyMethod(heart.move_to, [-1, 0, 0]))
        # self.play(ApplyMethod(heart.move_to, [1, 0, 0]))
        # self.play(ApplyMethod(heart[0].move_to, (heart[0].get_center() - [1, 0, 0])))
        # self.wait()
        # self.play(ApplyMethod(heart[1].move_to, (heart[1].get_center() - [1, 0, 0])))
        heart_top = heart.deepcopy()
        heart_top.set_color("#333333")
        text_top = text.deepcopy()
        text_top.set_color("#333333")
        self.play(Write(text_top), Write(heart_top), run_time=2)
        self.play(FadeOut(text), FadeOut(heart))

class TowersOfHanoi(Scene):
    def construct(self):
        
        pegs = VGroup(Line([-1, -0.5, 0], [-1, 1, 0]),
                      Line([0, -0.5, 0], [0, 1, 0]),
                      Line([1, -0.5, 0], [1, 1, 0]),
                      Rectangle(3, 0.5, fill_opacity=1).move_to([0, -0.75, 0]))

        peg_x = [-1, 0, 1]

        moving_things = [1, 1, 1]

        things = []

        for i in range(len(moving_things)):
            if i == 1:
                color = BLUE 
            elif i == 2: 
                color = GREEN 
            else:
                color = PURPLE
            things.append(RoundedRectangle(
                width=(len(moving_things) - i)/3, 
                height=1/3, 
                fill_opacity=1, 
                fill_color=color, 
                stroke_color=color,
                corner_radius=0.1
                )
                .move_to(
                    [-1, 
                    (i/3) - 1/3+0.035, 
                    0]))

        things_y = []

        for i in range(len(things)):
            things_y.append(things[i].get_y()) 

        def Hanoi(n, start, end):

            if n == 1:
                m(start, end)
            else:
                other = 6 - (start + end)
                Hanoi(n-1, start, other)
                m(start, end)
                Hanoi(n-1, other, end)
        
        def m(start, end):
            moving_things_p = deepcopy(moving_things)
            stop_switch = True
            for i in range(len(moving_things)):
                if moving_things[i] == start and stop_switch == True:
                    moving_things[i] = end
                    print(moving_things)
                    stop_switch = False
            print(moving_things_p, moving_things, start, end)
            move_thing(moving_things_p, moving_things, things)

        def move_thing(thing_array_p, thing_array, thing):
            print("Thing started moving")
            for i in range(len(thing)):
                print(f"Moving {i}")
                if thing_array[i] != thing_array_p[i]:
                    print(f"If {thing_array[i]} is not equal to {thing_array_p[i]}")
                    # for n in range(len(thing)):
                    print(f"Actually moving thing")
                    self.play(ApplyMethod(thing[i].move_to, [peg_x[i], things_y[i], 0]))
                
                

        self.add(pegs)
        for i in range(len(things)):
            self.add(things[i])
        Hanoi(3, 1, 3)

        

        
