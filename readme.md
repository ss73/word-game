# Word game written in Python

This is an implementation of the popular game commonly known as _Wordle_. 
The game is played in the console. There is a Swedish and an English dictionary
available and it comes with a tool to add additional dictionaries for more languages. 

The game was developed as an optional assignment in the course 
[1NX002](https://www.umu.se/en/education/syllabus/1nx002/) given at Umeå University. The goal of the project has been to practice some of the skills gained troughout the course: 
 * Object Oriented Programming, in this case using a Model-View-Controller (MVC) pattern for the game implementation
 * Documenting Python code using the [Numpy style guide](https://numpydoc.readthedocs.io/en/latest/format.html)
 * Working with type hints
 * Avoiding code smells (hopefully there aren't too many)
 * Structuring code in packages and modules
 * Unit testing with the [unittest](https://docs.python.org/3/library/unittest.html) library

## Example gameplay

The snippet below shows the output of a game session, including game instructions that
are printed when the game is started
```
Welcome to the game of wordle!
I am thinking of a five-letter word.
You have 6 tries to guess the word.
After each guess, you will receive feedback on the correctness of the letters.
The feedback is given as follows:
 *X*  - correct letter in the correct position
 (X)  - correct letter, but in the wrong position
  X   - incorrect letter

Good luck!


Enter a word: pling
+-----+-----+-----+-----+-----+
| (P) |  L  |  I  |  N  |  G  |
+-----+-----+-----+-----+-----+
Enter a word: släkt
+-----+-----+-----+-----+-----+
| (P) |  L  |  I  |  N  |  G  |
|  S  |  L  |  Ä  | (K) |  T  |
+-----+-----+-----+-----+-----+
Enter a word: kropp
+-----+-----+-----+-----+-----+
| (P) |  L  |  I  |  N  |  G  |
|  S  |  L  |  Ä  | (K) |  T  |
| *K* | (R) |  O  | (P) |  P  |
+-----+-----+-----+-----+-----+
Enter a word: kupar
+-----+-----+-----+-----+-----+
| (P) |  L  |  I  |  N  |  G  |
|  S  |  L  |  Ä  | (K) |  T  |
| *K* | (R) |  O  | (P) |  P  |
| *K* | *U* | *P* | *A* | *R* |
+-----+-----+-----+-----+-----+


🏆 Congratulations 🏆 You won! Perhaps another game?
```

## How to install and run the game

You need a [python](https://www.python.org/downloads/) interpreter (v.3.9 or higher) to run the game, that's all.
Assuming you have installed Python, follow these steps to install and run the program:
 * Clone the repository into a directory of choice (or download zip)
 * Run the game: `python main.py [lang code]` e.g. `python main.py sv` for Swedish
 * If lang code is omitted, you will be prompted to choose one of the language codes for which there are translations available.

## How to add more languages

If you want to add another language (localization and dictionary), follow these steps:
  * Download a dictionary file for your language, for example from [here](https://github.com/titoBouzout/Dictionaries)
  * Place the dictionary file in the `res` folder and rename it `raw_<lang code>.txt`
  * Create a file called `chars_<lang_code>.txt`containing a single line with the allowed characters for the language
  * Run `python tools/process_dict.py <lang code>`
  * Provide a translation file for the in-game messages and store it as a JSON file `locale_<lang code>.json` in the `res` folder (copy/paste the `locale_en.json` file and use an editor to supply your translation)

If you _do_ take the effort to create a translation and dictionary for another language, it would be nice with a pull request to have it included in the repository, but that is completely voluntary.

## Credits
The Swedish [dictionary](https://github.com/titoBouzout/Dictionaries/blob/master/Swedish.dic) is based on "Den stora svenska ordlistan" by Göran Andersson complemented with the work of Tom Westerberg. [Information and license (in Swedish)](https://github.com/titoBouzout/Dictionaries/blob/master/Swedish.txt).

The English [dictionary](https://github.com/titoBouzout/Dictionaries/blob/master/English%20(American).dic) is created by Kevin Atkinson and is complemented wit the work of Alan Beale. [Information and licence](https://github.com/titoBouzout/Dictionaries/blob/master/English%20(American).txt)