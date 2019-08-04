<!--
---
name: Some Board
class: board
type: other
formfactor: Custom
manufacturer: Some manufacturer inc.
description: Some board for a Raspberry pi
url: https://pinout.xyz
github: https://github.com/Frederic98/Custom_Pinout.xyz
schematic: https://github.com/Frederic98/Custom_Pinout.xyz
buy: http://pinout.xyz
image: 'some-board.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    name: Some pin
    mode: output
    active: high
  '10':
    name: Other pin
    mode: input
    active: high
i2c:
  '0x31':
    name: Some weird I2C device
    device: Some IC
-->
#Some board

This is an example board definition. You probably want to delete this file when you're running your own custom pinout.xyz server.

Use the template.md file (included in this repository, copied from [https://github.com/gadgetoid/Pinout.xyz](https://github.com/gadgetoid/Pinout.xyz)) to define your own boards.

Create a github repository with the directories `overlay` and `boards` to put the board definition and image.
