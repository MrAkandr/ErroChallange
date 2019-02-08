import Labirint as lab


class Render():

    def draw_borders_horizontal(self, labirint_width):
        line = ""
        for width in range(labirint_width + 2):
            line += "#"
        print(line)

    def draw_coordinates_mesh_horizontal(self, labirint_width):
        line = " "
        position = 0
        for width in range(labirint_width + 1):
            line += str(position)
            line += " "
            position += 1
        print(line)

    def construct_walls(self, labirint):
        labirint_map = [["-"] * labirint.get_width() for i in range(labirint.get_height())]
        for wall in labirint.get_walls():
            labirint_map = self.construct_wall(wall, labirint_map)
        return labirint_map

    def construct_wall(self, coordinates, labirint_map):
        start_x = coordinates[0]
        start_y = coordinates[1]
        end_x = coordinates[2]
        end_y = coordinates[3]
        y_index = 0
        for y in labirint_map:
            x_index = 0
            if y_index in range(start_y, end_y) or y_index == start_y:
                for x in labirint_map[y_index]:
                    if x_index in range(start_x, end_x) or x_index == start_x:
                        labirint_map[y_index][x_index] = "%"
                    x_index += 1
            y_index += 1
        return labirint_map

    def draw_lines(self, labirint_map):
        y_index = 0
        for y in labirint_map:
            x_index = 0
            line = "#"
            for x in labirint_map[y_index]:
                line += labirint_map[y_index][x_index]
                x_index += 1
            y_index += 1
            line += "#"
            print(line)

    def draw_labirint(self, labirint):
        labirint_width = labirint.get_width()
        labirint_map = self.construct_walls(labirint)
        self.draw_borders_horizontal(labirint_width)
        self.draw_lines(labirint_map)
        self.draw_borders_horizontal(labirint_width)


class UI():
    def try_read_value(self, message, expected_number_of_values):
        success = False
        while (success == False):
            try:
                parced_values = self.read_values(message)
                partial_succes = True
                for value in parced_values:
                    if int(value) < 0:
                        partial_succes = False
                if len(parced_values) != expected_number_of_values:
                    partial_succes = False
                if partial_succes == True:
                    success = True
                    return parced_values
                else:
                    print("Number(s) must be positive")
            except:
                print("Invalid input, please input integer number(s)")

    def read_values(self, message):
        return input(message).split(",")

    def set_labirint_width(self):
        return self.try_read_value("Input labirint width", 1)

    def set_labirint_height(self):
        return self.try_read_value("Input labirint height", 1)

    def set_wall_start_width(self):
        return self.try_read_value("Input wall start width", 1)

    def set_wall_start_height(self):
        return self.try_read_value("Input wall start height", 1)

    def set_wall_end_width(self):
        return self.try_read_value("Input wall end width", 1)

    def set_wall_end_height(self):
        return self.try_read_value("Input wall end height", 1)

    def set_walls_coordinates(self):
        return self.try_read_value("Input start and end coordinates (example: x,y,x,y)", 4)


def main():
    ui = UI()
    render = Render()
    saver = lab.LabirintSaverLoader()
    labirint = lab.Labirint(10, 20)
    # labirint.set_height(ui.set_labirint_height())
    # labirint.set_width(ui.set_labirint_width())
    # labirint.new_wall(ui.set_walls_coordinates())
    #labirint.new_wall([18, 0, 18, 4])
    #labirint.new_wall([0, 5, 15, 5])
    #render.draw_labirint(labirint)
    #saver.save_labirint("lab.json", labirint)
    new_labirint = lab.Labirint(0,0)
    saver.load_labirint("lab.json", new_labirint)
    render.draw_labirint(new_labirint)


main()