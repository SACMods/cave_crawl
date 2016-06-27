#python3
import pprint
welcome = """
    Welcome to Cave Crawl! Can you find the special treasure?
    To get around, you can type: up, down, left, right
    """

# Each 0 is a room. Treasure is denoted by the T
# x = up/down, array
# y = left/right, array position
# [
#   ['P',0,0,0,0],
#   [0,0,0,0,0],
#   [0,0,0,0,0],
#   [0,0,0,0,'T'],
#   [0,0,0,0,0]
# ]

class CaveCrawl(object):
    cave_map = [[0 for i in range(5)] for i in range(5)]
    player_position = (0,0)
    treasure_position = (2, 4)
    Rooms = ['Secret Room', 'Supply Room', 'Mushroom']

    def play(self):
        print welcome
        game_on = True

        while game_on:
            self.start()
            self.update_map()
            if self.check_treasure():
                print "You found the treasure!"
                game_on = False

        print "Play again?"
        res = raw_input("(y/n) ")
        if res == 'y':
            self.play()
        else:
            print "Thanks for playing!"

    def start(self):
        player_move = raw_input("Your move: ")
        move(player_move)

    def update_map(self):
        x, y = self.player_position
        self.cave_map[x][y] = 'P'
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.cave_map)

    def check_treasure(self):
        # px, py = player_position
        # tx, ty = treasure_position
        return self.player_position == self.treasure_position

    def move(self, data):
        x, y = self.player_position
        if data.lower() == 'up':
            if x == 0:
                return
            self.cave_map[x][y] = 0
            self.player_position = (x -1, y )
        elif data.lower() == 'down':
            if x == 4:
                return
            self.cave_map[x][y] = 0
            self.player_position = (x + 1, y)
        elif data.lower() == 'left':
            if y == 0:
                return
            self.cave_map[x][y] = 0
            self.player_position = (x, y - 1)
        elif data.lower() == 'right':
            if y == 4:
                return
            self.cave_map[x][y] = 0
            self.player_position = (x, y + 1)
        elif data.lower() == 'q':
            break


    def random_room(self):
        return random.choice(self.Rooms)

    def get_room(self, r):
        self.Room_Map[r]

play()
