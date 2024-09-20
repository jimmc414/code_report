# Software Analysis Test Battery

## Overview

This program is designed to perform a comprehensive set of software analysis tasks. The tests include parsing code, generating various graphical and textual representations of the program structure, profiling, type checking, and generating test cases. It provides an all-in-one solution for performing static analysis and profiling of Python codebases.

## Features

- **AST Generation**: Converts source code into an Abstract Syntax Tree.
- **Control Flow Graph (CFG)**: Generates a control flow graph of the code.
- **Call Graph**: Maps function calls in the source code.
- **Data Flow Analysis**: Tracks how data moves through the program.
- **Linting**: Provides a list of potential code issues.
- **Complexity Analysis**: Evaluates the complexity of the code.
- **Dependency Graph**: Shows dependencies between modules.
- **Code Coverage**: Generates a report showing which parts of the code are covered by tests.
- **Memory Profiling**: Analyzes memory usage during execution.
- **Performance Profiling**: Measures the performance characteristics of the code.
- **Type Checking**: Static type analysis of the source code.
- **Class Visualization**: Generates visual diagrams of class structures.
- **Semantic Analysis**: Evaluates the meaning of code structures.
- **Test Case Generation**: Automatically generates unit tests for the code.

## Requirements

- Python 3.x
- Dependencies:
  - `rich`: For enhanced console output and progress tracking.
  - Standard Python libraries: `os`, `sys`, `argparse`, `subprocess`, `shutil`, etc.

You can install the necessary packages by running:

```bash
pip install rich
```

## Usage

To run the program, simply execute the script with the appropriate command-line arguments. You can specify which analysis tasks you want to perform using flags.

### Basic Command:

```bash
python code_analysis_tool.py --source /path/to/source_code.py --output /path/to/output_directory
```

### Available Command-Line Arguments:

- `--source`: Path to the source code file to be analyzed.
- `--output`: Path to the directory where output files will be saved.
- `--verbosity`: Set the verbosity level (1 for minimal, 2 for detailed output).
- `--tasks`: Specify which tasks to perform (e.g., `ast`, `cfg`, `lint`, `memory_profile`, `test_generation`, etc.).

Example usage:

```bash
python code_analysis_tool.py --source main.py --output analysis_results --verbosity 2 --tasks ast,cfg,lint
```

## Output Formats

- **AST**: Text file (`.txt`)
- **CFG**: Image file (`.png`)
- **Call Graph**: Image file (`.png`)
- **Data Flow**: Text file (`.txt`)
- **Linting**: Text file (`.txt`)
- **Complexity**: Text file (`.txt`)
- **Dependency Graph**: Image file (`.png`)
- **Coverage**: HTML file (`.html`)
- **Memory Profile**: Text file (`.txt`)
- **Performance Profile**: Text file (`.txt`)
- **Type Check**: Text file (`.txt`)
- **Class Visualization**: Image file (`.png`)
- **Semantic Analysis**: Text file (`.txt`)
- **Test Case Generation**: Python file (`.py`)

![image](https://github.com/user-attachments/assets/e86222af-473b-4a8a-8a5e-ed4815643f3f)


