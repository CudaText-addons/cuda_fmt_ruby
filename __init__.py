from . import rubybeautifier
from cuda_fmt import get_config_filename
from cudatext import *

def options():
    tab_is_spaces = ed.get_prop(PROP_TAB_SPACES)
    tab_size = ed.get_prop(PROP_TAB_SIZE)
    opt = rubybeautifier.default_options()
    opt.indent_char = " " if tab_is_spaces else "\t"
    opt.indent_size = tab_size if tab_is_spaces else 1
    return opt

def do_format(text):
    return rubybeautifier.beautify(text, options())
