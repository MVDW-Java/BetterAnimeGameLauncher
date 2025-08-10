from bagl.manager.api.hoyoverse import Hoyoverse

# Launch game
def launchTest():
    game = Hoyoverse(3)
    print(game.listDownload())
