# Rom Patching
This project is the foundation code for creating a custom interactive game cartridge.

### A What? 
The cartridge will light up when events in game have been reached. The code provided is a script I can use to patch a game rom to make it write memory values of interest out the cartridge bus.

## How it works
Genesis games utilize a rom header to set system inturrupt vectors. This script will modify the Vertical Sync inturrupt vector and use a thunk function (https://en.wikipedia.org/wiki/Thunk) to attempt to write values to a specific ROM address. This ensures the value in memory will be accessible once per frame drawn on screen.

## Does it work?
Not sure. The patched rom does work in an emulator still but more work is needed on real hardware.
