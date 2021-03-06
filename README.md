## Import Grace (.agr) files into Inkscape

*May 2020: updated for Inkscape 1.0*

Plots prepared using the
[Grace](http://plasma-gate.weizmann.ac.il/Grace/ "Grace home page")
plotting package can be exported to EPS, cropped to bounding box, and
imported into the [Inkscape](https://inkscape.org/en/ "Inkscape home
page") drawing package.  This exension automates these intermediate
steps by wrapping the necessary command line tools into an Inkscape
extension.

### Installation

Copy the files `agr_import.py` and `agr_import.inx` into your local
Inkscape extension folder (eg `$HOME/.config/inkscape/extensions/` on
unix, or `%APPDATA%\inkscape\extensions\` on Windows).

The following tools are also required:

* `gracebat`, 'headless' (batch) mode tool which usually comes with
[Grace](http://plasma-gate.weizmann.ac.il/Grace/ "Grace home page") ;
* `epstool`, which is often packaged as a standalone tool and can be
obtained from the
[epstool](http://pages.cs.wisc.edu/~ghost/gsview/epstool.htm "epstool home page")
home page;
* `ps2pdf`, which is part of Ghostscript (if you
can already import EPS then you have this).

### Usage

In Inkscape, Grace (`.agr`) files should now appear under File &rarr;
Import, and can be selected for import.  The conversion to PDF via EPS
is done automatically, and the subsequent dialogue is the standard one
for importing PDF files.

### Copying

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see
<http://www.gnu.org/licenses/>.

### Copyright

This program is copyright &copy; 2015, 2020 Patrick B Warren.

### Contact

Email: <patrickbwarren@gmail.com>
