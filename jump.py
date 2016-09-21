#!/usr/bin/env python

import os
import sys

if os.name == 'nt':
    sys.exit('error: Don\'t know horrible hacks for Windows')


## insane and horrible hack by @mrdiskodave
#  http://stackoverflow.com/questions/431684/how-do-i-cd-in-python/16694919#16694919

def quote_against_shell_expansion(s):
    import pipes
    return pipes.quote(s)

def put_text_back_into_terminal_input_buffer(text):
    # use of this means that it only works in an interactive session
    # (and if the user types while it runs they could insert characters between the characters in 'text'!)
    import fcntl, termios
    for c in text:
        fcntl.ioctl(1, termios.TIOCSTI, c)

def change_parent_process_directory(dest):
    # the horror
    put_text_back_into_terminal_input_buffer("cd "+quote_against_shell_expansion(dest)+"\n")

## /insane and horrible hack

change_parent_process_directory('..')
