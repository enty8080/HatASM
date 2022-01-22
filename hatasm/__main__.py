#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020-2022 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from .assembler import Assembler
from .disassembler import Disassembler


class HatAsm(Assembler, Disassembler):
    def assemble(self, arch, code, mode=None):
        return self.assemble_code(arch, code, mode)

    def assemble_to(self, arch, code, mode=None, filename='a.bin'):
        with open(filename, 'wb') as f:
            f.write(self.assemble_code(arch, code, mode))

    def assembler_cli(self, arch, mode=None):
        self.assemble_cli(arch, mode)

    def disassemble(self, arch, code, mode=None):
        return self.disassemble_code(arch, code, mode)

    def disassemble_to(self, arch, code, mode=None, filename='a.asm'):
        code = self.disassemble_code(arch, code, mode)

        with open(filename, 'w') as f:
            f.write("start:\n")
            f.write(f"    {code['mnemonic']} {code['operand']}\n")

    def disassembler_cli(self, arch, mode=None):
        self.disassemble_cli(arch, mode)

    def hexdump(self, code, length=16, sep='.'):
        return self.hexdump(code, length, sep)
