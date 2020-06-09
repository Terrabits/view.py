#!/usr/bin/env python
import argparse
from   PySide2.QtWidgets          import QApplication
from   PySide2.QtWebEngineWidgets import QWebEngineView
import sys


# this is main.
# I mean it!
if __name__ != '__main__':
    sys.exit(1)


CENTER = -1

# command line interface

parser = argparse.ArgumentParser(description='Display a url in a window')
parser.add_argument('--title',            default='view.py')
parser.add_argument('--width',  type=int, default=1200)
parser.add_argument('--height', type=int, default=1024)
parser.add_argument('--x-pos',  type=int, default=CENTER, help='defaults to center of screen; requires --y-pos')
parser.add_argument('--y-pos',  type=int, default=CENTER, help='defaults to center of screen; requires --x-pos')
parser.add_argument('url')

args = parser.parse_args()

# additional cli rules

args.is_pos = args.x_pos != CENTER and args.y_pos != CENTER

if args.x_pos != CENTER and args.y_pos == CENTER:
    parser.print_usage()
    print('error: the --x-pos option requires --y-pos')
    sys.exit(1)

if args.y_pos != CENTER and args.x_pos == CENTER:
    parser.print_usage()
    print('error: the --y-pos option requires --x-pos')
    sys.exit(1)

if args.is_pos:
    if args.x_pos < 0:
        parser.print_usage()
        print('error: --x-pos must be ≥ 0')
        sys.exit(1)

    if args.y_pos < 0:
        parser.print_usage()
        print('error: --y-pos must be ≥ 0')
        sys.exit(1)

# create view

app    = QApplication(sys.argv)
window = QWebEngineView()

# apply args

window.setUrl(args.url)
window.resize(args.width, args.height)
window.setWindowTitle(args.title)

if args.is_pos:
    window.move(args.x_pos, args.y_pos)

# show

window.show()

sys.exit(app.exec_())
