class Rom:

    def __init__(self, rom_data, header):
        self.rom_data = rom_data
        self.header = header

    def patch_rom(self, bytes, address):
        start_address = address - len(self.header)
        end_address = start_address + len(bytes)
        self.rom_data[start_address:end_address] = bytes

    def add_to_rom(self, bytes):
        header_size = len(self.header)
        self.rom_data = self.rom_data + bytes
        return header_size + len(self.rom_data)

    def get_bytes(self):
        return self.rom_data
