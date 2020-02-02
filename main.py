import os
from rom import *
from rom_header import *
from snippets import *
from tools import *
import locale
locale.setlocale(locale.LC_ALL, '')

orig_rom_path = '~/Desktop/Sonic the Hedgehog 2_68k.bin'
emulator = '~/Downloads/Gens_KMod_v0.7.3/gens.exe'
out_rom = '~/Desktop/modified_s2.bin'

my_rom_header, rom = extract_rom_header(orig_rom_path)
my_rom = Rom(rom, my_rom_header)
# my_rom.patch_rom(unpatched_function, 0x40c)
# my_rom.patch_rom(patched_function, 0x40c)
my_rom.patch_rom(new_function, 0x100000)
# my_rom.patch_rom(error_loop, 0xfffec)
my_header = RomHeader(my_rom_header)
# (a, b, c) = (unpack('>BBBB',my_header.stack_pointer))
# stack_pointer=hex((a<<16)+(b<<8)+c)
# print_address(stack_pointer)

print("-------------")

print("stack_pointer")
i=unpack_address(my_header.stack_pointer)
print_address(i)

print("code_start")
code_start=unpack_address(my_header.code_start)
print_address(code_start)

print("address error location")
address_error=unpack_address(my_header.address_error)
print_address(address_error)

print("rom start")
rom_start=unpack_address(my_header.rom_start)
print_address(rom_start)

print("rom end")
rom_end=unpack_address(my_header.rom_end)
print_address(rom_end)

rom = rom + error_loop + error_loop + error_loop
my_header.set_vert_int(0x100000)
my_header.set_bus_error(0x100006)
my_header.set_address_error(0x100006)
my_header.set_illegal_instruction_error(0x10000c)

my_header.set_rom_end(0x1fffff)

create_rom(my_header, rom, out_rom)
os.system('wine /Users/christophercowin/Downloads/Gens_KMod_v0.7.3/gens.exe')