# TinyLoggy - Lightweight Python Logging Utility

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

TinyLoggy is a minimal yet powerful logging utility designed for Python applications requiring simple, colorful terminal output with optional timestamping and caller inspection capabilities.

## Features

- **Colorful Terminal Output**: Visually distinct log levels with ANSI color coding
- **Timestamp Support**: Optional automatic timestamping for each log entry
- **Caller Inspection**: Optional source code location tracking (file, line number, function)
- **Lightweight**: Minimal dependencies (only requires `colorama`)
- **Configurable**: Enable/disable logging globally or customize display options
- **Cross-Platform**: Works on Windows, Linux, and macOS

## Installation

Install TinyLoggy using pip:

```bash
pip install tinnyloggy
```

## Quick Start

```python 
from tinnyloggy import Logger

# Basic usage
log = Logger(time_stamp=True, enabled=True, inspect_mode=False)
log.info("System initialized successfully")
log.warning("Disk space below recommended threshold")
log.error("Failed to connect to database")

# Advanced usage with caller inspection
debug_log = Logger(inspect_mode=True)
debug_log.info("Entering calculation function")
```

## Log Levels

TinyLoggy supports four standard log levels with distinctive colors:

- `info()`: Blue background - General information

- `warning()`: Yellow background - Potential issues

- `error()`: Red background - Recoverable errors

- `critical()`: Magenta background - Critical failures


## Command Line Integration

When used as a main module, TinyLoggy supports command line arguments:

```python 
python -m tinnyloggy --uselogs --inspect
```

- `--uselogs`: Enables logging output

- `--inspect`: Enables caller inspection mode


## Dependencies

- Python 3.6+

- `colorama` (automatic installation)

## License

TinyLoggy is released under the MIT License. See LICENSE file for details.

## Contributing 

Contributions are welcome! Please open an issue or submit a pull request on GitHub.





