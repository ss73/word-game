import sys

from game import GameModel
from game import GameView
from game import GameController

if __name__ == '__main__':
    lang_code = 'sv'
    if len(sys.argv) > 1:
        lang_code = sys.argv[1]
   
    with open('res/words_' + lang_code + '.txt', 'r') as file:
        words = [line.strip() for line in file]
    model = GameModel(words)
    view = GameView(lang_code)
    controller = GameController(model, view)
    controller.play()