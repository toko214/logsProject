#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012, Jean-Rémy Bancel <jean-remy.bancel@telecom-paristech.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Chromagon Project nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Jean-Rémy Bancel BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Frontend script using Chrome Download parsing library
"""

import argparse
import sys
import textwrap

import chromagnon.classicalOutput
import chromagnon.columnOutput
import chromagnon.csvOutput
import chromagnon.jsonOutput
import chromagnon.downloadParse


def main():
    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent('''
\033[32mChromagnon Chrome Download Parser\033[0m

\033[4mInput File\033[0m
    The input file of this program is the Chrome history file. It is a simple
    SQLite3 file. It's usual name is 'History'.

\033[4mOutput Format\033[0m
    Four output formats are available. csv and json is what you expect to be.
    Classical is a format where fields are separated by a \\t and column is a
    format where every fields are displayed in columns. You can specify the
    format using the -f flags. Moreover, the delimiter can be change with -d
    flag.

\033[4mColumn Selection\033[0m
    To select which field to display, use the -c flag with the following options
        st : Start Time
        rb : Received Bytes
        tb : Total Bytes
        pt : Percent Received
        p : path
        u : url
        s : state
             '''))
    parser.add_argument("-f", "-format", action='store', default="classical",
                        choices=["csv", "column", "classical", "json"])
    parser.add_argument("-d", "-delimiter", action='store',
                        help="Delimiter used in output formating")
    parser.add_argument("-ul", "-urlLength", action='store', default=0,
                        help="Shrink urls display")
    parser.add_argument("-c", "-column", action='store', nargs='+',
                        choices=["st", "rb", "tb", "p", "u", "s", "pt",
                        "cc"], help="Choose columns to display",
                         default=["st", "u", "p"])
    parser.add_argument("filename", help="Path to History file",
                        action='store', type=str)
    args = parser.parse_args()

    # Getting data
    data = chromagnon.downloadParse.parse(args.filename, int(args.ul))

    # Creating a table according to chosen columns
    output = []
    for item in data:
        line = []
        for column in args.c:
            line.append(item.columnToStr(column))
        output.append(line)

    # Printing table
    if args.d == None:
        sys.modules["chromagnon." + args.f + "Output"].__getattribute__(
            args.f + "Output")(output)
    else:
        sys.modules["chromagnon." + args.f + "Output"].__getattribute__(
            args.f + "Output")(output, separator=args.d)

if __name__ == "__main__":
    main()
