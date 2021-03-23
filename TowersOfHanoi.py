from manimlib.imports import *

class TowersOfHanoi(Scene):
    def construct(self):
        
        peg_array = [[],[],[]]
        disk_array = []
        disk_y_array = [[],[],[]]
        disk_x_array = []

        def m(start, end):
            peg_array_p = deepcopy(peg_array)

            # print(start, "->", end)

            disk_to_move = peg_array[start - 1].pop()

            peg_array[end - 1].append(disk_to_move)

            move_thing(disk_to_move, start, end, peg_array)

            # print(peg_array)
            

        def move_thing(disk, start, end, peg_array):
            self.play(ApplyMethod(disk_array[-disk].move_to, [disk_x_array[start-1], 2, 0]), run_time=1/3)

            self.play(ApplyMethod(disk_array[-disk].move_to, [disk_x_array[end-1], 2, 0]), run_time=1/3)

            self.play(ApplyMethod(disk_array[-disk].move_to, disk_y_array[end-1][len(peg_array[end-1])-1]), run_time=1/3)



        # def hanoi(amount, start, end, move=None, start_hanoi=True):
        def hanoi(amount, start, end, start_hanoi=True):
            if start_hanoi:
                global peg_thing
                peg1 = RoundedRectangle(width=0.1, height=3, fill_opacity=1, corner_radius=0.05).move_to([-2, 1.5, 0])
                peg2 = RoundedRectangle(width=0.1, height=3, fill_opacity=1, corner_radius=0.05).move_to([0, 1.5, 0])
                peg3 = RoundedRectangle(width=0.1, height=3, fill_opacity=1, corner_radius=0.05).move_to([2, 1.5, 0])

                if end == 1:
                    peg3.set_color(YELLOW)
                elif end == 2:
                    peg2.set_color(YELLOW)
                else:
                    peg3.set_color(YELLOW)

                peg_thing = VGroup(
                    peg1,
                    peg2,
                    peg3,
                    RoundedRectangle(width=6, height=0.7, fill_opacity=1, corner_radius=0.1).move_to([0, -0.35, 0])
                ).move_to([0, -0.5, 0])
                # ).move_to(move)

                disk_x_array.append(peg1.get_x())
                disk_x_array.append(peg2.get_x())
                disk_x_array.append(peg3.get_x())

                self.play(Write(peg_thing))

                for i in range(0, amount):
                    peg_array[0].append(amount-i)

                    disk_y_array[0].append(peg1.get_edge_center(DOWN)+[0, ((3-0.5)/amount)/2+((3-0.5)/amount)*i, 0])
                    disk_y_array[1].append(peg2.get_edge_center(DOWN)+[0, ((3-0.5)/amount)/2+((3-0.5)/amount)*i, 0])
                    disk_y_array[2].append(peg3.get_edge_center(DOWN)+[0, ((3-0.5)/amount)/2+((3-0.5)/amount)*i, 0])

                    disk_array.append(RoundedRectangle(
                        width=2-(i/(amount/2))+0.15,
                        height=(3-0.5)/amount,
                        corner_radius=1/amount,
                        color=BLUE,
                        fill_opacity=1
                    )
                    .move_to(disk_y_array[0][i])
                    .set_stroke(BLUE_D)
                    )
                    # print(f"Disk {i}")
                for n in range(len(disk_array)):
                    self.play(Write(disk_array[n]), run_time=1/len(disk_array))

            if amount == 1:
                m(start ,end)

            else:
                other = 6 - (start + end)

                hanoi(amount - 1, start, other, start_hanoi=False)

                m(start, end)

                hanoi(amount - 1, other, end, start_hanoi=False)
        

        # print(peg_array)

        # hanoi(3, 1, 3, [3.5, -0.5, 0])
        # hanoi(3, 3, 1, [-3.5, -0.5, 0])
        # curve_arrow = CurvedArrow(start_point=np.array([-2.5, 3, 0]), end_point=np.array([2.5, 3, 0]))
        # curve_arrow.flip(RIGHT)
        # self.add(curve_arrow)
        # for i in range(len(disk_array)):
        #     self.play(Uncreate(disk_array[len(disk_array) - i - 1]), run_time=1/4)
        # self.play(Uncreate(peg_thing), run_time=1/4)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        hanoi(3, 1, 3)

