#!/usr/bin/env python

"""
agr_input.py
Python script for importing Grace (.agr) files into Inkscape

Copyright (C) 2015 Patrick B Warren

Email: patrickbwarren@gmail.com

Based on ps2pdf-ext.py and run_command.py
Python script for running ps2pdf in Inkscape extensions
Module for running SVG-generating commands in Inkscape extensions
Copyright (C) 2008 Stephen Silver

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see
<http://www.gnu.org/licenses/>.
"""

# In order to get a return code from the process, we use
# subprocess.Popen which is in Python 2.4 onwards (released 2004).  As
# the Inkscape package for Windows includes Python 2.6, this should
# cover all *modern* supported platforms.
# cf run_command.py in system-wide extensions directory

import os, sys
from tempfile import NamedTemporaryFile
from subprocess import Popen, PIPE

# Define a (trivial) exception class to catch some errors

class AgrInputError(Exception):
    pass

# Run a shell command and capture the output

def run(command):
    prog_name = command.split(' ')[0]
    try:
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        if p.returncode:
            raise AgrInputError("%s failed:\n%s\n%s\n" % (prog_name, out, err))
    except Exception, inst:
        raise AgrInputError("Error attempting to run %s: %s" % (prog_name, str(inst)))

# Make and keep a temporary file with a given suffix
    
def make_and_keep(suffix):
    f = NamedTemporaryFile(suffix=suffix, delete=False)
    f.close()
    return f.name

# Make some temporary files which will be deleted at the end

epsfile = make_and_keep(".eps")
epsnewbbfile = make_and_keep(".eps")
pdffile = make_and_keep(".pdf")

exit_code = 0

try:

    run("gracebat -nosafe -hdevice EPS %s -printfile %s" % (sys.argv[-1], epsfile))
    run("epstool --bbox --copy %s %s" % (epsfile, epsnewbbfile))
    run("ps2pdf -dEPSCrop %s %s" % (epsnewbbfile, pdffile))

    if os.name == 'nt':
        import msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

    try:
        f = open(pdffile, "rb")
        data = f.read()
        sys.stdout.write(data)
        f.close()
    except IOError, inst:
        raise AgrInputError("Error reading temporary file: %s" % str(inst))

except AgrInputError, msg:
    
    sys.stderr.write(str(msg) + "\n")
    exit_code = 1

for file in [epsfile, epsnewbbfile, pdffile]:
    if file and os.path.exists(file):
        os.unlink(file)

sys.exit(exit_code)
