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

import os, sys, tempfile
from subprocess import Popen, PIPE

msg = None

def run(command):
    prog_name = command.split(' ')[0]
    try:
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        rc = p.wait()
        out = p.stdout.read()
        err = p.stderr.read()
        if rc:
            msg = "%s failed:\n%s\n%s\n" % (prog_name, out, err)
    except Exception, inst:
        msg = "Error attempting to run %s: %s" % (prog_name, str(inst))
        
epsfile = tempfile.mktemp(".eps")
epsnewbbfile = tempfile.mktemp(".eps")
pdffile = tempfile.mktemp(".pdf")

try:
    os.chdir(tempfile.gettempdir())
except Exception:
    pass

run("gracebat -nosafe -hdevice EPS " + sys.argv[-1] + " -printfile " + epsfile)
    
if msg is None: run("epstool --bbox --copy " + epsfile + " " + epsnewbbfile)

if msg is None: run("ps2pdf -dEPSCrop " + epsnewbbfile + " " + pdffile)

if msg is None:
    if os.name == 'nt':
        import msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    try:
        f = open(pdffile, "rb")
        data = f.read()
        sys.stdout.write(data)
        f.close()
    except IOError, inst:
        msg = "Error reading temporary file: %s" % str(inst)

os.remove(epsfile)
os.remove(epsnewbbfile)
os.remove(pdffile)

if msg is not None:
    sys.stderr.write(msg + "\n")
    sys.exit(1)
else:
    sys.exit(0)
