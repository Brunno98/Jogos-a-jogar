cores = {
    '': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'ciano': '\033[1;36m',
    'magenta': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'branco': '\033[1;37m',
    'reset': '\033[1;0;0m',
    'reverso': '\033[1;2m',
    'bgpreto': '\033[1;40m',
    'bgvermelho': '\033[1;41m',
    'bgverde': '\033[1;42m',
    'bgamarelo': '\033[1;43m',
    'bgazul': '\033[1;44m',
    'bgmagenta': '\033[1;45m',
    'bgciano': '\033[1;46m',
    'bgbranco': '\033[1;47m'
    }


def cor(txt='', cor=''):
    return f"{cores[cor]}{txt}{cores['']}"


def sucesso(txt):
    return cor(txt, "verde")


def aviso(txt):
    return cor(txt, "amarelo")


def erro(txt):
    return cor(txt, "vermelho")


def status(valor, texto):
    if valor:
        return sucesso(texto)
    return aviso(texto)

if __name__ == "__main__":
    for c in cores:
        print(cor("The quick brown fox jumps over the lazy dog", c))