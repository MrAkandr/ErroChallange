import json


class Labirint():
    def __init__(self, height, width):
        self.x_size = width
        self.y_size = height
        self.walls = WallContainer()

    def reprJSON(self):
        return dict(width=self.x_size, height=self.y_size, walls=self.walls)

    def get_width(self):
        return self.x_size

    def set_width(self, width):
        self.x_size = width

    def set_height(self, height):
        self.y_size = height

    def get_height(self):
        return self.y_size

    def get_walls(self):
        return self.walls.get_all_walls()

    def new_wall(self, input_params):
        self.walls.add_new_wall(input_params)


class WallContainer():
    def __init__(self):
        self.walls = []

    def reprJSON(self):
        return dict(walls=self.walls)

    def add_wall(self, wall):
        self.walls.append(wall)

    def get_all_walls(self):
        wall_group = []
        for wall in self.walls:
            wall_group.append(wall.get_wall_coordinates())
        return wall_group

    # TODO сделать через направления и вообще грязь
    def add_new_wall(self, input_params):
        start_height = input_params[0]
        start_width = input_params[1]
        end_height = input_params[2]
        end_width = input_params[3]
        new_wall = Wall(start_height, start_width, end_height, end_width)
        self.add_wall(new_wall)


class Wall():
    def __init__(self, start_width, start_height, end_width, end_height):
        if self.check_if_staight(start_width, start_height, end_width, end_height) == True:
            self.start_y = int(start_height)
            self.start_x = int(start_width)
            self.end_y =  int(end_height)
            self.end_x = int(end_width)
        else:
            raise ValueError("Wall is not straight")

    def reprJSON(self):
        return dict(sx=self.start_x, sy=self.start_y, ex=self.end_x, ey=self.end_y)

    def set_wall_coordinates(self, start_width, start_height, end_width, end_height):
        if self.check_if_staight(start_width, start_height, end_width, end_height) == True:
            self.start_y = int(start_height)
            self.start_x = int(start_width)
            self.end_y =  int(end_height)
            self.end_x = int(end_width)
        else:
            raise ValueError("Wall is not straight")


    def get_wall_coordinates(self):
        return [self.start_x, self.start_y, self.end_x, self.end_y]

    def check_if_staight(self, start_width, start_height, end_width, end_height):
        if start_width == end_width or start_height==end_height:
            return True
        else:
            return False


class LabirintEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.reprJSON()


class LabirintSaverLoader():
    def save_labirint(self, file_name, labirint):
        # encoded_labirint = self.save_encoder()
        encoded_labirint = json.dumps(labirint.reprJSON(), cls=LabirintEncoder)
        save = open(file_name, "w")
        save.write(encoded_labirint)
        save.close()
    def hook(self, obj):
        width = obj.width
        height = obj.height
    def load_labirint(self, file_name, labirint):
        with open (file_name) as save:
            obj = json.loads(save.read())
            labirint.set_width(obj.pop('width'))
            labirint.set_height(obj.pop('height'))
            walls = obj.pop('walls')
            walls = walls.pop('walls')
            for wall in walls:
                wall_coord = [wall['sx'], wall['sy'], wall['ex'], wall['ey']]
                labirint.new_wall(wall_coord)