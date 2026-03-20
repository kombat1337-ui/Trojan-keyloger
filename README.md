# Trojan-keyloger
Python Keylogger with Graceful Shutdown
A lightweight keyboard event listener built with Python's pynput library. This script captures keystrokes in real-time and ensures that the captured data is safely flushed to a local file upon program termination.

Key Features
Event-Driven Logging: Uses a non-blocking listener to capture alphanumeric keys and special characters (Space, Enter, Tab).

In-Memory Buffering: Stores keystrokes in a global string variable to minimize frequent disk I/O, improving performance.

Graceful Shutdown: * Uses atexit to ensure the log is saved when the script finishes normally.

Implements signal handling (SIGINT, SIGTERM) to catch manual interruptions like Ctrl+C and save the data before exiting.

Readable Formatting: Automatically translates special keys into a readable format (e.g., [shift] or [backspace]).

Technical Stack
Language: Python 3.x

Primary Library: pynput

System Modules: signal, atexit, sys

Installation & Usage
Install dependencies:

Bash
pip install pynput
Run the script:

Bash
python keylogger.py
Output: The keystrokes will be saved to keylog.txt in the same directory once the script is stopped.

Disclaimer: This project is created for educational purposes and authorized security testing only. Using this software against target systems without prior permission is illegal.
