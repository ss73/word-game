import os
import sys

def usage():
    lines = ['\nDictionary Processing Utility. \n\nThe raw dictionary data is assumed to be in ../res/ folder relative to this file and named raw_<lang>.txt',
        ' - The raw data file should contain one word per line. Any characters after a slash (/) is discarded.',
        ' - The cleaned data will be saved to the same folder as words_<lang>.txt',
        '\nBesides the raw data, a valid character set should be defined in a separate file, chars_<lang>.txt in the res folder',
        'The chars file typically holds a single line with all allowed characters in the alphabet for the language.'
        '\nTo run this script, you need to pass the language code as an argument, for example:\n\tpython process_dict.py sv\n\n']
    return '\n'.join(lines)

def process_dict(language_code):
    raw_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../res/raw_' + language_code + '.txt'))
    allowed_chars_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../res/chars_' + language_code + '.txt'))

    with open(allowed_chars_file, 'r') as file:
        allowed_chars = list(file.read().strip())

    cleaned_words = []
    with open(raw_file, 'r') as file:
        for line in file:
            line = line.strip()
            # Some lines contain non-interesting information after a '/'
            if '/' in line:
                line = line.split('/')[0]
            # Discard words that are not 5 characters
            if len(line) != 5:
                continue
            # Discard words that contain uppercase letters
            if any(char.isupper() for char in line):
                continue
            # Discard words that contain non-alphabetical characters
            if not line.isalpha():
                continue
            if any(char not in allowed_chars for char in line):
                continue
            cleaned_words.append(line)

    cleaned_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../res/words_' + language_code + '.txt'))
    with open(cleaned_file, 'w') as file:
        for word in cleaned_words:
            file.write(word + '\n')

    return cleaned_file

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(usage())
        sys.exit(1)
    if sys.argv[1] == '--help':
        print(usage())
        sys.exit(0)
    language_code = sys.argv[1]
    cleaned_file = process_dict(language_code)
    print('Dictionary processed and saved to ' + cleaned_file)
