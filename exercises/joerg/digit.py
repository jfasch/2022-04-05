import sys


translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

try:
    digit = int(sys.argv[1])
    english_word = translation_table[digit]
    print(english_word)
except IndexError:
    print('Usage:', sys.argv[0], 'DIGIT', file=sys.stderr)
    sys.exit(3)
except ValueError:
    print(sys.argv[1], 'is not a number', file=sys.stderr)
    sys.exit(1)
except KeyError:
    print(sys.argv[1], 'is not a digit', file=sys.stderr)
    sys.exit(2)

