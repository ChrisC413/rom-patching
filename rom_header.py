from tools import *
class RomHeader:

    def __init__(self, header):

        self.header = header
        self.stack_pointer = header[0x0:0x4]
        self.code_start = header[0x4:0x8]
        self.bus_error = header[0x8:0x0c]
        self.address_error = header[0x0c:0x10]
        self.illegal_instruction = header[0x10:0x14]
        self.gap = header[0x14:0x78]
        self.vert_int = header[0x78:0x7c]
        self.gap2 = header[0x7c:0x1a0]
        self.rom_start = header[0x1a0:0x1a4]
        self.rom_end = header[0x1a4:0x1a8]
        self.rest = header[0x1a8:]


    def set_catch_all_error_pointer(self,address):

        address = address.zfill(6)
        self.code_start = address
        self.bus_error = address
        self.address_error = address

    header = []

    def get_header(self):
        return  self.stack_pointer + \
                self.code_start + \
                self.bus_error + \
                self.address_error + \
                self.illegal_instruction + \
                self.gap + \
                self.vert_int + \
                self.gap2 + \
                self.bus_error + \
                self.rom_end + \
                self.rest

    def __len__(self):
        return len(self.header)

    def get_rom_end_dec(self):
        return int(unpack_address(self.rom_end))

    def set_rom_end(self, length):
        self.rom_end = pack_address(length)

    def set_bus_error(self, address):
        self.bus_error = pack_address(address)

    def set_address_error(self, address):
        self.address_error = pack_address(address)

    def set_illegal_instruction_error(self, address):
        self.illegal_instruction = pack_address(address)

    def set_vert_int(self, address):
        self.vert_int = pack_address(address)

def extract_rom_header(path):
    with open(path, "rb") as f:
        header = f.read(0x1FF+1)
        rom = f.read()
        f.close()
    return bytearray(header), bytearray(rom)
