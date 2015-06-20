## Import Grace (.agr) files into Inkscape

Plots prepared using the
[Grace](http://plasma-gate.weizmann.ac.il/Grace/ "Grace home page")
plotting package can be exported to EPS and imported into the
[Inkscape](https://inkscape.org/en/ "Inkscape home page") drawing
package, by hand.  This code  automates the process by wrapping
the necessary command line tools into an Inkscape extension.

### Installation

Copy the files `agr_import.py` and `agr_import.inx` into your local
Inkscape extension folder (eg `$HOME/.config/inkscape/extensions/` on
unix, or `%APPDATA%\inkscape\extensions\` on Windows).

In order to work, the command line tools `gracebat`, `epstool`, and
`ps2pdf` are required: `gracebat` usually comes with the Grace
package, `epstool` is often packaged as a standalone tool or can be
obtained [here](http://pages.cs.wisc.edu/~ghost/gsview/epstool.htm
"epstool home page"), and `ps2pdf` is part of Ghostscript core (if you
can already import EPS then you have this).

### Usage

In Inkscape, Grace (.agr) files should now appear under File &rarr;
Import, and can be selected for import.  The conversion to EPS (PDF)
is done automatically, and the subsequent dialogue is the standard one
for importing EPS (PDF) files.  The intermediate (temporary) EPS (PDF)
files are discarded.

---

Copyright &copy; 2015 Patrick B Warren.

Email: patrickbwarren{at}gmail{dot}com

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
