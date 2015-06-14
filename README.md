## Import Grace (.agr) files into Inkscape

Plots prepared using the
[Grace](http://plasma-gate.weizmann.ac.il/Grace/ "Grace home page")
plotting package can be exported to EPS and imported into the
[Inkscape](https://inkscape.org/en/ "Inkscape home page") drawing
package, by hand.  This code  automates the process by wrapping
the necessary command line tools into an Inkscape extension.

### Installation

Copy the files `agr_import.py` and `agr_import.inx` into your local
Inkscape extension folder (eg `~/.config/inkscape/extensions/`).
That's it!

In order to work, the command line tools `gracebat`, `epstool`, and
`ps2pdf` are required.  The first allows Grace to be run in 'headless'
mode to generate the initial EPS file.  The second is used to refine
the EPS bounding box.  The third is used to generate a PDF for import into
Inkscape (if you can import PostScript or EPS files, then you are
already using `ps2pdf`).

To obtain these: `gracebat` usually comes with the Grace package,
`epstool` is often packaged as a standalone tool or can be obtained
[here](http://pages.cs.wisc.edu/~ghost/gsview/epstool.htm "epstool
home page"), and `ps2pdf` is part of Ghostscript core package (as
mentioned, if you can already import EPS then you have this).

### Usage

In Inkscape, Grace (.agr) files should now appear under File &rarr;
Import, and can be selected for import.  The conversion to EPS (PDF)
is done automatically, and the subsequent dialogue is the standard one
for importing EPS (PDF) files.  It's as simple as that!

The intermediate (temporary) EPS files are discarded.

Just a comment on the downstream workflow: once imported, I usually
lock the aspect ratio and reset the width to something more useful (eg
3.5 in).  This can be done with using the resizing options in the
'Tool Controls Bar' above the main drawing page in Inkscape.

---

Copyright &copy; 2015 Patrick B Warren.

Based on `eps_input.inx`, `ps2pdf-ext.py` (python script for running
`ps2pdf` in Inkscape extensions) and `run_command.py` (module for
running SVG-generating commands in Inkscape extensions) -- copyright
&copy; 2008 Stephen Silver.

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
