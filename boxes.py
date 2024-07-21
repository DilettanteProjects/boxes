class line():
    class light():
        vertical                                  = '│'
        horizontal                                = '─'
        class half():
            left                                  = '╴'
            up                                    = '╵'
            right                                 = '╶'
            down                                  = '╷'
        class dashed():
            class double():
                vertical                          = '╎'
                horizontal                        = '╌'
            class triple():  
                vertical                          = '┆'
                horizontal                        = '┄'
            class quadruple():
                vertical                          = '┊'
                horizontal                        = '┈'
    class heavy():
        vertical                                  = '┃'
        horizontal                                = '━'
        class half():
            left                                  = '╸'
            up                                    = '╹'
            right                                 = '╺'
            down                                  = '╻'
        class dashed():
            class double():
                vertical                          = '╏'
                horizontal                        = '╍'
            class triple():  
                vertical                          = '┇'
                horizontal                        = '┅'
            class quadruple():
                vertical                          = '┋'
                horizontal                        = '┉'
    class double():
        horizontal                                = '═'
        vertical                                  = '║'
        
class box():
    class upLeft():
        light                                             = '┌'
        heavy                                             = '┏'
        double                                            = '╔'
    class upRight():
        light                                             = '┐'
        heavy                                             = '┓'
        double                                            = '╗'
    class lowLeft():
        light                                             = '└'
        heavy                                             = '┗'
        double                                            = '╚'
    class lowRight():
        light                                             = '┘'
        heavy                                             = '┛'
        double                                            = '╝'
    class branchRight():
        light                                             = '├'
        heavy                                             = '┣'
        double                                            = '╠'
    class branchLeft():
        light                                             = '┤'
        heavy                                             = '┫'
        double                                            = '╣'
    class t():
        light                                             = '┬'
        heavy                                             = '┳'
        double                                            = '╦'
    class inverseT():
        light                                             = '┴'
        heavy                                             = '┻'
        double                                            = '╩'
    class cross():
        light                                             = '┼'
        heavy                                             = '╋'
        double                                            = '╬'    
    
    def mix(*args, left='blank', down='blank', up='blank', right='blank'):
        """ Call with left='single', down='single', etc, 
        or for short like so: '0110'
        Order: hjkl (left, down, up, right)
        Style codes:
        0       : Blank
        1       : Light
        2       : Double
        3       : Heavy
        Mix single and heavy OR single and double,
        NOT heavy and double
        """
        def encode(style):
            codes = {'blank'    : 0,
                     'light'    : 1,
                     'single'   : 1,
                     'double'   : 2,
                     'heavy'    : 3,
                     }
            return codes[style.lower()]
        if args:
            code = args[0]
        else:
            code = f'{encode(left)}{encode(down)}{encode(up)}{encode(right)}'
        symbols = {
            '0011'                                            : '└',
            '0012'                                            : '╘',
            '0013'                                            : '┕',
            '0021'                                            : '╙',
            '0022'                                            : '╚',
            '0031'                                            : '┖',
            '0033'                                            : '┗',
            '0101'                                            : '┌',
            '0102'                                            : '╒',
            '0103'                                            : '┍',
            '0111'                                            : '├',
            '0112'                                            : '╞',
            '0113'                                            : '┝',
            '0130'                                            : '╿',
            '0131'                                            : '┞',
            '0133'                                            : '┡',
            '0201'                                            : '╓',
            '0202'                                            : '╔',
            '0221'                                            : '╟',
            '0222'                                            : '╠',
            '0301'                                            : '┎',
            '0303'                                            : '┏',
            '0310'                                            : '╽',
            '0311'                                            : '┟',
            '0313'                                            : '┢',
            '0331'                                            : '┠',
            '0333'                                            : '┣',
            '1003'                                            : '╼',
            '1010'                                            : '┘',
            '1011'                                            : '┴',
            '1013'                                            : '┶',
            '1020'                                            : '╜',
            '1021'                                            : '╨',
            '1030'                                            : '┚',
            '1031'                                            : '┸',
            '1033'                                            : '┺',
            '1100'                                            : '┐',
            '1101'                                            : '┬',
            '1103'                                            : '┮',
            '1110'                                            : '┤',
            '1111'                                            : '┼',
            '1113'                                            : '┾',
            '1130'                                            : '┦',
            '1131'                                            : '╀',
            '1133'                                            : '╄',
            '1200'                                            : '╖',
            '1201'                                            : '╥',
            '1220'                                            : '╢',
            '1221'                                            : '╫',
            '1300'                                            : '┒',
            '1301'                                            : '┰',
            '1303'                                            : '┲',
            '1310'                                            : '┧',
            '1311'                                            : '╁',
            '1313'                                            : '╆',
            '1330'                                            : '┨',
            '1331'                                            : '╂',
            '1333'                                            : '╊',
            '2010'                                            : '╛',
            '2012'                                            : '╧',
            '2020'                                            : '╝',
            '2022'                                            : '╩',
            '2100'                                            : '╕',
            '2102'                                            : '╤',
            '2110'                                            : '╡',
            '2112'                                            : '╪',
            '2200'                                            : '╗',
            '2202'                                            : '╦',
            '2220'                                            : '╣',
            '2222'                                            : '╬',
            '3001'                                            : '╾',
            '3010'                                            : '┙',
            '3011'                                            : '┵',
            '3013'                                            : '┷',
            '3030'                                            : '┛',
            '3031'                                            : '┹',
            '3033'                                            : '┻',
            '3100'                                            : '┑',
            '3101'                                            : '┭',
            '3103'                                            : '┯',
            '3110'                                            : '┥',
            '3111'                                            : '┽',
            '3113'                                            : '┿',
            '3130'                                            : '┩',
            '3131'                                            : '╃',
            '3133'                                            : '╇',
            '3300'                                            : '┓',
            '3301'                                            : '┱',
            '3303'                                            : '┳',
            '3310'                                            : '┪',
            '3311'                                            : '╅',
            '3313'                                            : '╈',
            '3330'                                            : '┫',
            '3331'                                            : '╉',
            '3333'                                            : '╋',
            }
        return symbols[code]

class cell():
    class arcs():
        upLeft                                    = '╭'
        upRight                                   = '╮'
        lowRight                                  = '╯'
        lowLeft                                   = '╰'
    class diagonals():
        rising                                    = '╱'
        falling                                   = '╲'
        cross                                     = '╳'
        
class blocks():
    class block():
        upperHalf                                 = '▀'
        lowerOneEighth                            = '▁'
        lowerOneQuarter                           = '▂'
        lowerThreeEighths                         = '▃'
        lowerHalf                                 = '▄'
        lowerFiveEighths                          = '▅'
        lowerThreeQuarters                        = '▆'
        lowerSevenEighths                         = '▇'
        full                                      = '█'
        leftSevenEighths                          = '▉'
        leftThreeQuarters                         = '▊'
        leftFiveEighths                           = '▋'
        leftHalf                                  = '▌'
        leftThreeEighths                          = '▍'
        leftOneQuarter                            = '▎'
        leftOneEighth                             = '▏'
        rightHalf                                 = '▐'
        upperOneEighth                            = '▔'
        rightOneEighth                            = '▕'
    class shade():
        light                                     = '░' # 25%
        medium                                    = '▒' # 50%
        dark                                      = '▓' # 75%
        full                                      = '█' # 100% (Just a block)
        
    def quadrants(code):
        """ Pass a string containing every quadrant you want filled,
        in any order.
        The quadrants being:
        QW
        AS
        """
        # Sort
        letters = ['Q', 'W', 'A', 'S']
        sortedCode = ''
        for letter in letters:
            if letter in code.upper():
                sortedCode = sortedCode + letter
        
        symbols = {
        'QWAS'                                            : '█',
        'QWA'                                             : '▛',
        'QWS'                                             : '▜',
        'QW'                                              : '▀',
        'QAS'                                             : '▙',
        'QA'                                              : '▌',
        'QS'                                              : '▚',
        'Q'                                               : '▘',
        'WAS'                                             : '▟',
        'WA'                                              : '▞',
        'WS'                                              : '▐',
        'W'                                               : '▝',
        'AS'                                              : '▄',
        'A'                                               : '▖',
        'S'                                               : '▗',
        ''                                                : '',
        }
        
        return symbols[sortedCode]