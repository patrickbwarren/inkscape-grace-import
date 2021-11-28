#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
agr_input.py
Wrapper around gracebat and epstool

Copyright (c) 2015, 2020 Patrick B Warren
Email: patrickbwarren@gmail.com

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

import os
import inkex
from inkex.command import call as external

class GraceInput(inkex.CallExtension):
    """Load grace (.agr) files by converting them to pdf"""
    input_ext = 'agr'
    output_ext = 'pdf'

    def call(self, input_file, output_file):
        """Steps to convert input file (.agr) to output file (.pdf)"""
        eps_file = os.path.join(self.tempdir, 'output.eps')
        cropped_file = os.path.join(self.tempdir, 'cropped.eps')
        external('gracebat', '-hdevice', 'EPS', input_file, '-printfile', eps_file)
        external('epstool', '--bbox', '--copy', eps_file, cropped_file)
        external('ps2pdf', '-dEPSCrop', cropped_file, output_file)

if __name__ == '__main__':
    GraceInput().run()
