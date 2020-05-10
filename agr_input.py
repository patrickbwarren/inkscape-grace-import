#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015, 2020 Patrick B Warren
# Email: patrickbwarren@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
"""
Wrapper around gracebat and epstool
"""

import os
import inkex
from inkex.command import call

class GraceInput(inkex.CallExtension):
    """Load grace (.agr) files by converting them to pdf"""
    input_ext = 'agr'
    output_ext = 'pdf'

    def call(self, input_file, output_file):
        eps_file = os.path.join(self.tempdir, 'output.eps')
        cropped_file = os.path.join(self.tempdir, 'cropped.eps')
        call('gracebat', '-hdevice', 'EPS', input_file, '-printfile', eps_file)
        call('epstool', '--bbox', '--copy', eps_file, cropped_file)
        call('ps2pdf', '-dEPSCrop', cropped_file, output_file)

if __name__ == '__main__':
    GraceInput().run()
