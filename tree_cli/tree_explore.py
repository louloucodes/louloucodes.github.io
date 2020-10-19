#! /Users/louisatran/lib/anaconda3/envs/tree_cli/bin/python

"""

Usage:
    tree_explore.py [--dir DIR|-d DIR]
                    [--level LEVEL|-l LEVEL]
                    [--file_color FILE_COLOR|-f FILE_COLOR]
                    [--dir_color DIR_COLOR|-r DIR_COLOR]
    tree_explore.py [-h|--help]

Options:
    -h --help                   What happens here?
    --dir -d DIR                Optional directory argument [default: .]
    --level -l LEVEL            Optional level argument [default: 3]
    --file_color -f FILE_COLOR  Optional file color in hex (in quotes) or valid name [default: deep_pink_2]
    --dir_color -r DIR_COLOR    Optional directory color in hex (in quotes) or valid name [default: thistle_1]

"""

import os
from docopt import docopt
from colored import fg, attr, stylize

def recursive_list(pathdir, level, indent):
    '''
    :param pathdir: string of path
    :param level: how deep to map the tree
    :param indent: how far to indent
    :return: to get out of recursive loop
    '''
    if indent == 0:
        print(stylize(os.path.abspath(pathdir), fg(dir_color) + attr('bold')))
    if level < 0:
        return
    #consider creating an option to sort by date, or size, but keep default alphabetical
    dir_list = sorted(os.listdir(pathdir))
    for d in dir_list:
        for i in range(0, indent):
            print(stylize('|   ', fg('#ffffff')), end='')
        print(stylize('|___', fg('#ffffff')), end='')
        if os.path.isdir(pathdir + '/' + d):
            print(stylize(d, fg(dir_color) + attr('bold')))
        else:
            print(stylize(d, fg(file_color)))
        if os.path.isdir(pathdir + '/' + d):
            try:
                recursive_list(pathdir + '/' + d, level - 1, indent + 1)
            except PermissionError:
                pass
    return

if __name__=='__main__':
    # docopt saves arguments and options as key:value pairs in a dictionary
    args = docopt(__doc__)
    # turn the arguments into global variables
    level = int(args['--level'])
    dir_color = args['--dir_color']
    file_color = args['--file_color']
    path_dir = args['--dir']
    recursive_list(path_dir, level, 0)


