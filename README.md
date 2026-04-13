# MarkPad
A 4-key macropad with a rotary encoder, built with a Seeeduino XIAO microcontroller. I made this for the Hack Club Blueprint project. I wanted a small dedicated pad for shortcuts I actually use day-to-day (copy, paste, mute, and a shortcut to open claude). The encoder controls volume.

I am new to electronics design so this was a very fun interesting project for me to work on.

## How to use it

Plug it in over USB-C. The XIAO runs KMK firmware (CircuitPython), so you can remap the keys by editing `main.py`. The default layout is:

- **SW2**: Copy (⌘C)
- **SW3**: Paste (⌘V)
- **SW4**: Mic mute (⌘⇧M)
- **SW5**: Opens claude in a new tab
- **Encoder twist**: Volume up/down
- **Encoder press**: Mute

## CAD

The case is a single 3D-printed part. There’s no lid as it's an open-top design. The switches and encoder are exposed on top, so one part is all you need. I designed it in fusion 360.

![3D model](https://github.com/user-attachments/assets/58e76b07-bd6e-4096-8258-25ca6deec124)

## PCB

Designed in KiCad. The encoder is at the top, XIAO in the middle, four switches in a column below.

**Schematic**

![Schematic](https://github.com/user-attachments/assets/529fd325-4f94-4036-aa46-656bd95f4d46)

**PCB layout**


## Firmware

KMK on CircuitPython. The main file is `Firmware/main.py`. It uses direct-wired scanning (no matrix) since there are only 5 inputs. The encoder is handled by the `EncoderHandler` module.

## BOM

| Qty | Part | Price | Notes | Link |
|-----|------|-------|-------|------|
| 4 | Cherry MX-compatible switch | £5.19 | 10x Cherry MX Blue Switches | [Amazon](https://amzn.eu/d/0bAqqb6x) |
| 4 | Keycaps (1u) | £5.69 | 5x White keycaps | [Amazon](https://amzn.eu/d/0er6c40q) |
| 1 | EC11 rotary encoder | £3.99 | 1x 360 degree rotary encoder | [Amazon](https://amzn.eu/d/0evqXiXo) |
| 1 | Encoder knob | — | Included in the EC11 rotary encoder | — |
| 1 | Seeeduino XIAO (SAMD21) | £5.44 | USB-C microcontroller | [Seeed Studio](https://www.seeedstudio.com/Seeeduino-XIAO-Arduino-Microcontroller-SAMD21-Cortex-M0+-p-4426.html) |
| 1 | Custom PCB | — | Order from JLCPCB using gerbers | [JLCPCB](https://jlcpcb.com/) |
| 1 | 3D-printed case | — | PLA or PETG | N/A |