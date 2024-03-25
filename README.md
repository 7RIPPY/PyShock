## About
PyShock is a Python based tool made to easily integrate PiShock into a game, program, or application.

### Usage

- the .exe version can be found in the releases tab
- PyShockConfig.json (usually) must be in the same directory as PyShock.exe
- The file can be ran with or without args.

### Arguments

PyShock supports command line arguments: `python PyShock.py <operation> <intensity 1-100> <duration 1-15>`

**Valid Operations:**
- `shock`
- `vibrate`
- `beep`

### Troubleshooting

If PyShockConfig.json fails to be located in the directory and PyShock.exe is being called from a program in a different directory, try placing PyShockConfig.json in the directory of the program calling it.
