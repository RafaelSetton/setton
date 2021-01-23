from string import printable, whitespace

# Letras
A_ESPECIAL = 'áâãàÁÂÃÀ'
E_ESPECIAL = 'éêÉÊ'
I_ESPECIAL = 'íÍ'
O_ESPECIAL = 'óôõÓÔÕ'
U_ESPECIAL = 'úÚ'
VOGAIS = 'aeiou'
CONSOANTES = 'bcdfghjklmnpqrstvwxyz'
ALFABETO_MINUSCULO = ''.join(sorted(VOGAIS + CONSOANTES))
ALFABETO_MAIUSCULO = ''.join(letra.upper() for letra in ALFABETO_MINUSCULO)
ALFABETO_COMPLETO = ''.join(sorted(ALFABETO_MINUSCULO + ALFABETO_MAIUSCULO + ' '))
PONTUACAO = '.,;:?!'
CODABLE = ''.join([char for char in printable if char not in (whitespace + r"#%*<>[\]^_`{|}~")]) + ' '

# Código Morse
MORSE_MINUSCULO = (('a', '.-'), ('b', '-...'), ('c', '-.-.'),
                   ('d', '-..'), ('e', '.'), ('f', '..-.'),
                   ('g', '--.'), ('h', '....'), ('i', '..'),
                   ('j', '.---'), ('k', '-.-'), ('l', '.-..'),
                   ('m', '--'), ('n', '-.'), ('o', '---'),
                   ('p', '.--.'), ('q', '--.-'), ('r', '.-.'),
                   ('s', '...'), ('t', '-'), ('u', '..-'),
                   ('v', '...-'), ('w', '.--'), ('x', '-..-'),
                   ('y', '-.--'), ('z', '--..'))
MORSE_MAIUSCULO = tuple((code[0].upper(), '^'+code[1]) for code in MORSE_MINUSCULO)
MORSE_ESPECIAL = ((' ', '/'), ('0', '-----'), ('1', '.----'), ('2', '..---'),
                  ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'),
                  ('7', '--...'), ('8', '---..'), ('9', '----.'), ('.', '.-.-.-'),
                  (',', '--..--'), ('?', '..--..'), ('!', '-.-.--'), ('-', '-....-'),
                  ("'", '.----.'), ('/', '-..-.'), ('(', '-.--.'), (')', '-.--.-'),
                  ('&', '.-...'), (':', '---...'), (';', '-.-.-.'), ('=', '-...-'),
                  ('+', '.-.-.'), ('_', '..--.-'), ("\"", '.-..-.'), ('$', '...-..-'),
                  ('@', '.--.-.'))
MORSE_COMPLETO = MORSE_MINUSCULO + MORSE_MAIUSCULO + MORSE_ESPECIAL

# Outros
MESES = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
ADJACENTES_TECLADO = {'a': {'linha': 2, 'coluna': 1, 'adjacentes': ['q', 'w', 's', 'z']},
                      'b': {'linha': 3, 'coluna': 5, 'adjacentes': ['v', 'g', 'h', 'n']},
                      'c': {'linha': 3, 'coluna': 3, 'adjacentes': ['x', 'd', 'f', 'v']},
                      'd': {'linha': 2, 'coluna': 3, 'adjacentes': ['s', 'e', 'r', 'f', 'c', 'x']},
                      'e': {'linha': 1, 'coluna': 3, 'adjacentes': ['w', 's', 'd', 'r']},
                      'f': {'linha': 2, 'coluna': 4, 'adjacentes': ['d', 'r', 't', 'g', 'v', 'c']},
                      'g': {'linha': 2, 'coluna': 5, 'adjacentes': ['f', 't', 'y', 'h', 'b', 'v']},
                      'h': {'linha': 2, 'coluna': 6, 'adjacentes': ['g', 'y', 'u', 'j', 'n', 'b']},
                      'i': {'linha': 1, 'coluna': 8, 'adjacentes': ['u', 'j', 'k', 'o']},
                      'j': {'linha': 2, 'coluna': 7, 'adjacentes': ['h', 'u', 'i', 'k', 'm', 'n']},
                      'k': {'linha': 2, 'coluna': 8, 'adjacentes': ['j', 'i', 'o', 'l', ',', 'm']},
                      'l': {'linha': 2, 'coluna': 9, 'adjacentes': ['k', 'o', 'p', 'ç', '.', ',']},
                      'm': {'linha': 3, 'coluna': 7, 'adjacentes': ['n', 'j', 'k', ',']},
                      'n': {'linha': 3, 'coluna': 6, 'adjacentes': ['b', 'h', 'j', 'm']},
                      'p': {'linha': 1, 'coluna': 10, 'adjacentes': ['o', 'l', 'ç']},
                      'q': {'linha': 1, 'coluna': 1, 'adjacentes': ['w', 's', 'a']},
                      'r': {'linha': 1, 'coluna': 4, 'adjacentes': ['e', 'd', 'f', 't']},
                      's': {'linha': 2, 'coluna': 2, 'adjacentes': ['a', 'w', 'e', 'd', 'x', 'z']},
                      't': {'linha': 1, 'coluna': 5, 'adjacentes': ['r', 'f', 'g', 'y']},
                      'v': {'linha': 3, 'coluna': 4, 'adjacentes': ['c', 'f', 'g', 'b']},
                      'w': {'linha': 1, 'coluna': 2, 'adjacentes': ['q', 'a', 's', 'e']},
                      'x': {'linha': 3, 'coluna': 2, 'adjacentes': ['z', 's', 'd', 'c']},
                      'y': {'linha': 1, 'coluna': 6, 'adjacentes': ['t', 'g', 'h', 'u']},
                      'z': {'linha': 3, 'coluna': 1, 'adjacentes': ['a', 's', 'x', '\\']}}
