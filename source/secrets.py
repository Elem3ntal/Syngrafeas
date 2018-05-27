config = {
    'debug': True,
    'local_deploy': True,
    'books': {
        'TXT_PATH': 'books/txt/',
        'TXT_EXT': '.txt',
        'parser': [{'from':'\n','to':'.'},
                   {'from': '..', 'to': '.'},
                   {'from': ',.', 'to': ', '},
                   {'from': ':.', 'to': ': '},
                   {'from': '?.', 'to': '? '},
                   {'from': '¿.', 'to': '¿ '},
                   {'from': '¡.', 'to': '¡ '},
                   {'from': '!.', 'to': '! '},
                   {'from': ';.', 'to': '; '}]
    },
}