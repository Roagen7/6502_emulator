from Instruction import Instruction
import opcodes as opc
import addr_modes as amd
import interrupts as inr

def init_lookup(self):
    # decode opcodes


    self.lookup = {
       #opcd              addrmode  c  callback
        0x00: Instruction(amd.IMP, 7, opc.BRK),
        0x01: Instruction(amd.IZX, 6, opc.ORA),



        0x05: Instruction(amd.ZPG, 3, opc.ORA),  # OK
        0x06: Instruction(amd.ZPG, 5, opc.ASL),  # OK

        0x08: Instruction(amd.IMP, 3, opc.PHP),  # OK
        0x09: Instruction(amd.IMM, 2, opc.ORA),  # OK
        0x0a: Instruction(amd.IMP, 2, opc.ASL),  # OK

        0x0d: Instruction(amd.ABS, 4, opc.ORA),  # OK
        0x0e: Instruction(amd.ABS, 6, opc.ASL),  # OK

        0x10: Instruction(amd.REL, 2, opc.BPL),  # OK
        0x11: Instruction(amd.IZY, 5, opc.ORA),

        0x15: Instruction(amd.ZPX, 4, opc.ORA),
        0x16: Instruction(amd.ZPX, 6, opc.ASL),

        0x18: Instruction(amd.IMP, 2, opc.CLC),  # OK
        0x19: Instruction(amd.ABY, 4, opc.ORA),

        0x1d: Instruction(amd.ABX, 4, opc.ORA),
        0x1e: Instruction(amd.ABX, 7, opc.ASL),

        0x20: Instruction(amd.ABS, 6, opc.JSR),  # OK
        0x21: Instruction(amd.IZX, 6, opc.AND),


        0x24: Instruction(amd.ZPG, 3, opc.BIT),  # OK
        0x25: Instruction(amd.ZPG, 3, opc.AND),  # OK
        0x26: Instruction(amd.ZPG, 5, opc.ROL),  # OK

        0x28: Instruction(amd.IMP, 4, opc.PLP),  # OK
        0x29: Instruction(amd.IMM, 2, opc.AND),  # OK
        0x2a: Instruction(amd.IMP, 2, opc.ROL),  # OK

        0x2c: Instruction(amd.ABS, 4, opc.BIT),  # OK ?
        0x2d: Instruction(amd.ABS, 4, opc.AND),  # OK
        0x2e: Instruction(amd.ABS, 6, opc.ROL),  # OK ?

        0x30: Instruction(amd.REL, 2, opc.BMI),  # OK
        0x31: Instruction(amd.IZY, 6, opc.AND),

        0x35: Instruction(amd.ZPX, 4, opc.AND),
        0x36: Instruction(amd.ZPX, 6, opc.ROL),

        0x38: Instruction(amd.IMP, 2, opc.SEC),  # OK
        0x39: Instruction(amd.ABY, 4, opc.AND),

        0x3d: Instruction(amd.ABX, 4, opc.AND),
        0x3e: Instruction(amd.ABX, 7, opc.ROL),

        0x40: Instruction(amd.IMP, 6, opc.RTI),
        0x41: Instruction(amd.IZX, 6, opc.EOR),

        0x45: Instruction(amd.ZPG, 3, opc.EOR),  # OK
        0x46: Instruction(amd.ZPG, 5, opc.LSR),

        0x48: Instruction(amd.IMP, 3, opc.PHA),
        0x49: Instruction(amd.IMM, 2, opc.EOR),  # OK

        0x4a: Instruction(amd.IMP, 2, opc.LSR),

        0x4c: Instruction(amd.ABS, 3, opc.JMP),  # OK
        0x4d: Instruction(amd.ABS, 4, opc.EOR),  # OK
        0x4e: Instruction(amd.ABS, 6, opc.LSR),

        0x50: Instruction(amd.REL, 2, opc.BVC),  # OK
        0x51: Instruction(amd.IZY, 5, opc.EOR),

        0x55: Instruction(amd.ZPX, 4, opc.EOR),  # OK
        0x56: Instruction(amd.ZPX, 6, opc.LSR),

        0x58: Instruction(amd.IMP, 2, opc.CLI),  # OK
        0x59: Instruction(amd.ABY, 4, opc.EOR),  # OK

        0x5d: Instruction(amd.ABX, 4, opc.EOR),  # OK
        0x5e: Instruction(amd.ABX, 7, opc.LSR),

        0x60: Instruction(amd.IMP, 2, opc.RTS),  # OK
        0x61: Instruction(amd.IZX, 6, opc.ADC),

        0x65: Instruction(amd.ZPG, 3, opc.ADC),
        0x66: Instruction(amd.ZPG, 5, opc.ROR),

        0x68: Instruction(amd.IMP, 4, opc.PLA),
        0x69: Instruction(amd.IMM, 2, opc.ADC),  # OK
        0x6a: Instruction(amd.IMP, 2, opc.ROR),  # OK

        0x6c: Instruction(amd.IND, 5, opc.JMP),

        0x6e: Instruction(amd.ABS, 6, opc.ROR),  # OK

        0x70: Instruction(amd.REL, 2, opc.BVS),  # OK?
        0x71: Instruction(amd.IZY, 5, opc.ADC),

        0x76: Instruction(amd.ZPX, 6, opc.ROR),  # OK


        0x78: Instruction(amd.IMP, 2, opc.SEI),  # OK


        0x7e: Instruction(amd.ABX, 7, opc.ROR),

        0x81: Instruction(amd.IZX, 6, opc.STA),

        0x84: Instruction(amd.ZPG, 3, opc.STY),  # OK
        0x85: Instruction(amd.ZPG, 3, opc.STA),  # OK
        0x86: Instruction(amd.ZPG, 3, opc.STX),  # OK

        0x88: Instruction(amd.IMP, 2, opc.DEY),  # OK

        0x8a: Instruction(amd.IMP, 2, opc.TXA),  # OK

        0x8c: Instruction(amd.ABS, 4, opc.STY),  # OK
        0x8d: Instruction(amd.ABS, 4, opc.STA),  # OK
        0x8e: Instruction(amd.ABS, 4, opc.STX),  # OK

        0x90: Instruction(amd.REL, 2, opc.BCC),  # OK
        0x91: Instruction(amd.IZY, 6, opc.STA),

        0x94: Instruction(amd.ZPX, 4, opc.STY),  # OK
        0x95: Instruction(amd.ZPX, 4, opc.STA),  # OK
        0x96: Instruction(amd.ZPY, 4, opc.STX),  # OK

        0x98: Instruction(amd.IMP, 2, opc.TYA),  # OK
        0x99: Instruction(amd.ABY, 5, opc.STA),  # OK
        0x9a: Instruction(amd.IMP, 2, opc.TXS),  # OK


        0x9d: Instruction(amd.ABX, 5, opc.STA),  # OK

        0xa0: Instruction(amd.IMM, 2, opc.LDY),  # OK
        0xa1: Instruction(amd.IZX, 6, opc.LDA),
        0xa2: Instruction(amd.IMM, 2, opc.LDX),  # OK
        0xa4: Instruction(amd.ZPG, 3, opc.LDY),  # OK
        0xa5: Instruction(amd.ZPG, 3, opc.LDA),
        0xa6: Instruction(amd.ZPG, 3, opc.LDX),  # OK

        0xa8: Instruction(amd.IMP, 2, opc.TAY),  # OK
        0xa9: Instruction(amd.IMM, 2, opc.LDA),  # OK
        0xaa: Instruction(amd.IMP, 2, opc.TAX),  # OK

        0xac: Instruction(amd.ABS, 4, opc.LDY),

        0xad: Instruction(amd.ABS, 3, opc.LDA),  # OK

        0xb0: Instruction(amd.REL, 2, opc.BCS),  # OK
        0xb1: Instruction(amd.IZY, 5, opc.LDA),

        0xb4: Instruction(amd.ZPX, 4, opc.LDY),
        0xb5: Instruction(amd.ZPX, 4, opc.LDA),
        0xb6: Instruction(amd.ZPY, 4, opc.LDX),


        0xb8: Instruction(amd.IMP, 2, opc.CLV),  # OK
        0xb9: Instruction(amd.ABY, 4, opc.LDA),
        0xba: Instruction(amd.IMP, 2, opc.TSX),  # OK

        0xbc: Instruction(amd.ABX, 4, opc.LDY),
        0xbd: Instruction(amd.ABX, 4, opc.LDA),
        0xbe: Instruction(amd.ABY, 4, opc.LDX),

        0xc0: Instruction(amd.IMM, 2, opc.CPY),  # OK
        0xc1: Instruction(amd.IZX, 6, opc.CMP),

        0xc4: Instruction(amd.ZPG, 3, opc.CPY),
        0xc5: Instruction(amd.ZPG, 3, opc.CMP),
        0xc6: Instruction(amd.ZPG, 5, opc.DEC),

        0xc8: Instruction(amd.IMP, 2, opc.INY),  # OK
        0xc9: Instruction(amd.IMM, 2, opc.CMP),  # OK
        0xca: Instruction(amd.IMP, 2, opc.DEX),  # OK

        0xcc: Instruction(amd.ABS, 4, opc.CPY),
        0xcd: Instruction(amd.ABS, 4, opc.CMP),
        0xce: Instruction(amd.ABS, 6, opc.DEC),

        0xd1: Instruction(amd.IZY, 5, opc.CMP),

        0xd5: Instruction(amd.ZPX, 4, opc.CMP),
        0xd6: Instruction(amd.ZPX, 6, opc.DEC),

        0xd8: Instruction(amd.IMP, 2, opc.CLD),  # OK
        0xd9: Instruction(amd.ABY, 4, opc.CMP),

        0xdd: Instruction(amd.ABX, 4, opc.CMP),
        0xde: Instruction(amd.ABX, 7, opc.DEC),

        0xe8: Instruction(amd.IMP, 2, opc.INX),  # OK

        0xae: Instruction(amd.ABS, 4, opc.LDX),  # OK

        0xd0: Instruction(amd.REL, 2, opc.BNE),  # OK

        0xe0: Instruction(amd.IMM, 2, opc.CPX),  # OK
        0xe1: Instruction(amd.IZX, 6, opc.SBC),

        0xe4: Instruction(amd.ZPG, 3, opc.CPX),
        0xe5: Instruction(amd.ZPG, 3, opc.SBC),
        0xe6: Instruction(amd.ZPG, 5, opc.INC),  # OK


        0xe9: Instruction(amd.IMM, 2, opc.SBC),
        0xea: Instruction(amd.IMM, 2, opc.NOP),  # OK

        0xec: Instruction(amd.ABS, 4, opc.CPX),
        0xed: Instruction(amd.ABS, 4, opc.SBC),
        0xee: Instruction(amd.ABS, 6, opc.INC),  # OK

        0xf0: Instruction(amd.REL, 2, opc.BEQ),  # OK
        0xf1: Instruction(amd.IZY, 5, opc.SBC),

        0xf5: Instruction(amd.ZPX, 4, opc.SBC),

        0xf8: Instruction(amd.IMP, 2, opc.SED),  # OK
        0xf9: Instruction(amd.ABY, 4, opc.SBC),

        0xfd: Instruction(amd.ABX, 4, opc.SBC),
    }

    for key in self.lookup:
        self.lookup[key].opcode = key

