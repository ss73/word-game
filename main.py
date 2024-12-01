import sys
import glob
import json

from game import GameModel
from game import GameView
from game import GameController

if __name__ == '__main__':
    lang_code = ''
    locales = glob.glob('res/locale_*.json')
    # keep the lang code found between 'locale_' and '.json' in the localization files
    locales = [s[s.find('locale_')+7:s.find('.json')] for s in locales]

    if len(sys.argv) == 1:
        print('No language code was supplied as commandline parameter')
        lang_code = input(f'Please select language [{" ".join(locales)}]: ')
        lang_code = lang_code.lower().strip()

    if len(sys.argv) > 1:
        lang_code = sys.argv[1]

    if lang_code not in locales:
        raise ValueError('No such language code: ' + lang_code)

    # Load the dictionary for the selected language
    with open('res/words_' + lang_code + '.txt', 'r') as file:
        words = [line.strip() for line in file]
    model = GameModel(words)

    # Load the localization for the selected language
    with open('res/locale_' + lang_code + '.json') as file:
        messages = json.load(file)
    view = GameView(messages, lang_code)

    controller = GameController(model, view)
    controller.play()