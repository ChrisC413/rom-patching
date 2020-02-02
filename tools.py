from struct import *


def print_address(addr):
    print(hex(addr), " ", '{:,}'.format(int(addr)))


def unpack_address(addr):
    addr, = (unpack('>I', addr))
    return addr


def pack_address(int):
    addr = pack('>I', int)
    return addr

def create_rom(header, rom, path):
    data_size=len(header) + len(rom)
    required_size=header.get_rom_end_dec()
    padding_len = required_size - data_size + 1
    padding = b'\x00' * padding_len

    new_rom = open(path, "wb")
    new_rom.write(header.get_header())
    new_rom.write(rom)
    new_rom.write(padding)
    new_rom.close()

