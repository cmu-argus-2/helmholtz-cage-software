#!/bin/bash

# Detect the operating system
OS=$(uname -s)
export ARGUS_ROOT=$(pwd)

# Set the correct mpy-cross executable based on the OS
if [ "$OS" == "Linux" ]; then
    MPY_EXEC="mpy-cross"
elif [ "$OS" == "Darwin" ]; then
    MPY_EXEC="mpy-cross-macos"
elif [[ "$OS" == *_NT* ]]; then
    MPY_EXEC="mpy-cross"
else
    echo "Unsupported OS: $OS"
    exit 1
fi

# Make the correct mpy-cross executable
if [[ ! "$OS" == *_NT* ]]; then 
    chmod +x build_tools/$MPY_EXEC

    echo "$MPY_EXEC is now executable"
fi

# Detect the appropriate Python command
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Python is not installed or not found in PATH."
    exit 1
fi

$PYTHON_CMD build_tools/build.py
$PYTHON_CMD build_tools/move_to_board.py