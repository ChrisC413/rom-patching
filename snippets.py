error_loop = b'\x4e\x71\x4e\x71\x60\xfa'

#thunk_function = bytearray.fromhex('103900ffffb111c001004a38f62a4ef80410')

new_function = bytearray.fromhex('48e7fffe103900ffffb111c001004ef8040c')

# From 0x40c
patched_function =   bytearray.fromhex('4ef9000fffec')
unpatched_function = bytearray.fromhex('4a38f62a6700')

# vertical interrupt 0x78
