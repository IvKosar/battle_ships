import field, player
from bomb import MadBomb

class Game():
    """
    Represents Battleship game.
    """
    def __init__(self, name1, name2):
        self._fields = [field.Field(), field.Field()]
        self._players = [player.Player(name1), player.Player(name2)]
        self._current_player = 0

    def read_position(self, index, next_index, landed, killed):
        """
        int, int, bool, bool -> int, int

        Requests user to enter coordinates.
        """
        if killed:
            message = "Killed!!!"
        elif landed:
            message = "Landed!"
        else:
            message = ""
        while True:
            try:
                coordinates =  self._players[index].read_position(message)
                if coordinates == "bomb":
                    bomb = MadBomb(0)
                    coordinates = bomb.detonate()
                if coordinates not in self._fields[next_index].shoots and\
                        coordinates[0]  in range(10):
                    return coordinates
                else:
                    message = "Incorrect coordinates. "
            except:
                message = "Incorrect coordinates. "

    def print_fields(self, index, next_index):
        """
        int -> None

        Prints user and their opponent _fields.
        """
        def print_line(line_list, line):
            if line < 9:
                res = "| " + str(line + 1) + " |"
            else:
                res = "| " + str(line + 1) + "|"
            for i in line_list:
                res += " " + i + " |"
            return res

        field1 = self._fields[index].field_with_ships()
        field2 = self._fields[next_index].field_without_ships()

        field_str = "\n" + " " * 5 + self._players[index]._name + ":" +\
                    " " * (49 - len(self._players[index]._name)) + self._players[next_index]._name + ":\n"
        field_str +=  "+---" * 11 + "+" + " " * 5 +  "+---" * 11 + "+\n"
        field_str += print_line("ABCDEFGHIJ", -1) + " " * 5 + print_line("ABCDEFGHIJ", -1) + "\n"
        field_str += "+---" * 11 + "+" + " " * 5 + "+---" * 11 + "+\n"
        for line in range(10):
            field_str += print_line(field1[line], line) + " " * 5 + print_line(field2[line], line) + "\n"
            field_str += "+---" * 11 + "+" + " " * 5 + "+---" * 11 + "+\n"
        print(field_str, end="")
