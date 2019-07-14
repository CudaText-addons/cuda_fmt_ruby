from . import rubybeautifier

def options():
    opt = rubybeautifier.default_options()

def do_format(text):
    return rubybeautifier.beautify(text, options())
