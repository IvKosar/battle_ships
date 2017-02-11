import random
import ship


class Field(object):
    def __init__(self):
        self.ships, self.field = generate_field()
        self.shoots = []

    def shoot_at(self, coordinates):
        if self.field[coordinates[0]][coordinates[1]]:
            self.field[coordinates[0]][coordinates[1]].shoot_at(coordinates)
            self.shoots.append(coordinates)
            return True
        else:
            self.shoots.append(coordinates)
            return False

    def field_without_ships(self):
        field = [[" " for i in range(10)] for j in range(10)]
        for line in range(10):
            for column in range(10):
                if (line, column) in self.shoots:
                    field[line][column] = "."
        return field

    def field_with_ships(self):
        field = [[" " for i in range(10)] for j in range(10)]
        for line in range(10):
            for column in range(10):
                if self.field[line][column]:
                    field[line][column] = self.field[line][column].print_point((line, column))
                elif (line, column) in self.shoots:
                    field[line][column] = "."
        return field

def generate_field():
    """
    None -> list(list(str))

    Generates random field.
    """
    ships = [[] for i in range(4)]
    field = [[None for i in range(10)] for i in range(10)]
    number_of_ships = [i for i in range(1, 5)]
    possible_coordinates = [(i, j) for i in range(10) for j in range(10)]
    for ship_type in range(len(number_of_ships)):
        for g_ship in range(number_of_ships[ship_type]):
            while True:
                bow = random.choice(possible_coordinates)
                length = tuple(random.sample([1, 4 - ship_type], 2))
                new_ship = ship.Ship(bow, length)
                if not new_ship.is_valid(possible_coordinates):
                    continue

                # Calculating new possible coordinates for next ships
                new_ship_area = new_ship.covered_area()
                for coordinates in new_ship_area:
                    if coordinates in possible_coordinates:
                        possible_coordinates.remove(coordinates)

                ships[4 - max(new_ship.length)].append(new_ship)
                for line in range(new_ship.bow[0], new_ship.bow[0] + new_ship.length[0]):
                    for column in range(new_ship.bow[1], new_ship.bow[1] + new_ship.length[1]):
                        field[line][column] = new_ship
                break
    return ships, field


'''field = Field()
print(field.field)'''

'''field = Field()
for i in range(len(field.field)):
    for j in range(len(field.field[i])):
        if field.field[i][j]:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

'''field = Field()
print(field.field)
print(field.field_without_ships())'''