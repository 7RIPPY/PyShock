## About
PyShock is a Python based executable made to easily integrate PiShock into a program.

### Usage

- the .exe version can be found in the releases tab
- PiShockConfig.json (usually) must be in the same directory as PyShock.exe
- The file can be ran with or without args.

### Arguments

`python PiShock.py <operation> <intensity 1-100> <duration 1-15>`

Valid Operations:
- `shock`
- `vibrate`
- `beep`

### Troubleshooting

If PiShockConfig.json fails to be located in the directory and PiShock.exe is being called from a program in a different directory, try placing PiShockConfig.json in the directory of the program calling it.
