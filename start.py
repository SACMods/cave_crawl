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

cave_map = [[0 for i in range(5)] for i in range(5)]
player_position = (0,0)
treasure_position = (2, 4)


def play():
    global player_position, treasure_position
    print welcome
    game_on = True

    while game_on:
        start()
        update_map()
        if check_treasure():
            print "You found the treasure!"
            game_on = False

    print "Play again?"
    res = raw_input("(y/n) ")
    if res == 'y':
        play()
    else:
        print "Thanks for playing!"

def start():
    player_move = raw_input("Your move: ")
    move(player_move)

def update_map():
    global player_position, treasure_position
    x, y = player_position
    cave_map[x][y] = 'P'
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(cave_map)

def check_treasure():
    global player_position, treasure_position
    # px, py = player_position
    # tx, ty = treasure_position
    return player_position == treasure_position

def move(data):
    global player_position, cave_map
    x, y = player_position
    if data.lower() == 'up':
        if x == 0:
            return
        cave_map[x][y] = 0
        player_position = (x -1, y )
    elif data.lower() == 'down':
        if x == 4:
            return
        cave_map[x][y] = 0
        player_position = (x + 1, y)
    elif data.lower() == 'left':
        if y == 0:
            return
        cave_map[x][y] = 0
        player_position = (x, y - 1)
    elif data.lower() == 'right':
        if y == 4:
            return
        cave_map[x][y] = 0
        player_position = (x, y + 1)
    elif data.lower() == 'q':
        break

play()
