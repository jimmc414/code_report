#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess
import ast
import shutil
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print
from pathlib import Path

# Verbosity levels (can be changed later)
VERBOSITY_LEVEL = 1  # 1: minimal, 2: detailed

# Output formats (can be changed later)
AST_OUTPUT_FORMAT = '.txt'
CFG_OUTPUT_FORMAT = '.dot'
CALL_GRAPH_OUTPUT_FORMAT = '.dot'
DATA_FLOW_OUTPUT_FORMAT = '.txt'
LINT_OUTPUT_FORMAT = '.txt'
COMPLEXITY_OUTPUT_FORMAT = '.txt'
DEPENDENCY_GRAPH_FORMAT = '.dot'
COVERAGE_OUTPUT_FORMAT = '.html'
MEMORY_PROFILE_OUTPUT_FORMAT = '.txt'
PERFORMANCE_PROFILE_OUTPUT_FORMAT = '.txt'
TYPE_CHECK_OUTPUT_FORMAT = '.txt'
CLASS_VISUALIZATION_FORMAT = '.dot'
SEMANTIC_ANALYSIS_FORMAT = '.txt'
TEST_GENERATION_FORMAT = '.py'

def main():
    # Initialize Rich console
    console = Console()

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Code Analysis Tool")
    parser.add_argument('path', help='Path to the Python code repository')
    args = parser.parse_args()

    code_path = args.path

    # Check if path exists
    if not os.path.exists(code_path):
        console.print(f"[red]Error: Path '{code_path}' does not exist.[/red]")
        sys.exit(1)

    # Check for required tools
    check_requirements(console)

    # Start the analysis
    console.print(Panel("[bold blue]Starting Code Analysis[/bold blue]"))

    # List of analysis functions
    analysis_functions = [
        run_ast_analysis,
        run_cfg_analysis,
        run_call_graph_analysis,
        run_data_flow_analysis,
        run_static_code_analysis,
        run_cyclomatic_complexity_analysis,
        run_dependency_graph_analysis,
        run_code_coverage_analysis,
        run_memory_usage_profiling,
        run_execution_profiling,
        run_runtime_type_checking,
        run_class_inheritance_visualization,
        run_semantic_code_analysis,
        run_automated_test_generation
    ]

    for analysis_func in track(analysis_functions, description="Analyzing..."):
        analysis_func(code_path, console)

    console.print(Panel("[bold green]Code Analysis Completed[/bold green]"))

def check_requirements(console):
    console.print("[bold]Checking requirements...[/bold]")
    required_tools = [
        'mypy',
        'pylint',
        'radon',
        'pydeps',
        'coverage',
        'pyreverse',
        'dot',  # Graphviz
    ]
    missing_tools = []
    for tool in required_tools:
        if not shutil.which(tool):
            missing_tools.append(tool)
    if missing_tools:
        console.print(f"[red]The following required tools are missing: {', '.join(missing_tools)}[/red]")
        console.print("[red]Please install them before running the script.[/red]")
        sys.exit(1)
    else:
        console.print("[green]All required tools are installed.[/green]")

def run_ast_analysis(code_path, console):
    console.print("[bold]1. AST Analysis[/bold]")
    ast_output_dir = os.path.join(os.getcwd(), 'ast_output')
    os.makedirs(ast_output_dir, exist_ok=True)

    for root, dirs, files in os.walk(code_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        source = f.read()
                    tree = ast.parse(source, filename=file_path)
                    ast_output_file = os.path.join(ast_output_dir, file + AST_OUTPUT_FORMAT)
                    with open(ast_output_file, 'w', encoding='utf-8') as f:
                        f.write(ast.dump(tree, indent=4))
                    if VERBOSITY_LEVEL > 1:
                        console.print(f"AST for [cyan]{file_path}[/cyan] saved to [green]{ast_output_file}[/green]")
                except Exception as e:
                    console.print(f"[red]Failed to process {file_path}: {e}[/red]")

def run_cfg_analysis(code_path, console):
    console.print("[bold]2. Control Flow Graph Analysis[/bold]")
    console.print(f"[yellow]Control Flow Graph generation requires specific tools and configurations. Skipping this step.[/yellow]")

def run_call_graph_analysis(code_path, console):
    console.print("[bold]3. Call Graph Analysis[/bold]")
    call_graph_output_file = os.path.join(os.getcwd(), 'call_graph' + CALL_GRAPH_OUTPUT_FORMAT)
    try:
        cmd = ['pydeps', code_path, '--noshow', '--max-bacon=2', '--show-deps', '-T', 'dot', '-o', call_graph_output_file]
        subprocess.run(cmd, check=True)
        console.print(f"Call graph saved to [green]{call_graph_output_file}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to generate call graph: {e}[/red]")

def run_data_flow_analysis(code_path, console):
    console.print("[bold]4. Data Flow Analysis[/bold]")
    data_flow_output_file = os.path.join(os.getcwd(), 'data_flow_analysis' + DATA_FLOW_OUTPUT_FORMAT)
    try:
        cmd = ['mypy', code_path, '--show-error-codes', '--pretty']
        with open(data_flow_output_file, 'w') as f:
            subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, check=False)
        console.print(f"Data flow analysis report saved to [green]{data_flow_output_file}[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Data flow analysis failed:[/red]")
        console.print(e)

def run_static_code_analysis(code_path, console):
    console.print("[bold]5. Static Code Analysis (Linter)[/bold]")
    lint_output_file = os.path.join(os.getcwd(), 'lint_report' + LINT_OUTPUT_FORMAT)
    try:
        cmd = ['pylint', code_path]
        with open(lint_output_file, 'w') as f:
            subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, check=False)
        console.print(f"Linting report saved to [green]{lint_output_file}[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Linting failed:[/red]")
        console.print(e)

def run_cyclomatic_complexity_analysis(code_path, console):
    console.print("[bold]6. Cyclomatic Complexity Analysis[/bold]")
    complexity_output_file = os.path.join(os.getcwd(), 'cyclomatic_complexity' + COMPLEXITY_OUTPUT_FORMAT)
    try:
        cmd = ['radon', 'cc', code_path, '-s']
        with open(complexity_output_file, 'w') as f:
            subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, check=False)
        console.print(f"Cyclomatic complexity report saved to [green]{complexity_output_file}[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Cyclomatic complexity analysis failed:[/red]")
        console.print(e)

def run_dependency_graph_analysis(code_path, console):
    console.print("[bold]7. Dependency Graph Analysis[/bold]")
    dependency_graph_output_file = os.path.join(os.getcwd(), 'dependency_graph' + DEPENDENCY_GRAPH_FORMAT)
    try:
        cmd = ['pydeps', code_path, '--noshow', '--max-bacon=2', '-T', 'dot', '-o', dependency_graph_output_file]
        subprocess.run(cmd, check=True)
        console.print(f"Dependency graph saved to [green]{dependency_graph_output_file}[/green]")
    except Exception as e:
        console.print(f"[red]Dependency graph analysis failed: {e}[/red]")

def run_code_coverage_analysis(code_path, console):
    console.print("[bold]8. Code Coverage Analysis[/bold]")
    coverage_output_dir = os.path.join(os.getcwd(), 'htmlcov')
    try:
        # Check if tests directory exists
        tests_dir = os.path.join(code_path, 'tests')
        if os.path.exists(tests_dir):
            cmd = ['coverage', 'run', '-m', 'unittest', 'discover', '-s', tests_dir]
            subprocess.run(cmd, check=True)
            cmd = ['coverage', 'html', '-d', coverage_output_dir]
            subprocess.run(cmd, check=True)
            console.print(f"Coverage report saved to [green]{coverage_output_dir}[/green]")
        else:
            console.print(f"[yellow]No tests directory found. Skipping code coverage analysis.[/yellow]")
    except Exception as e:
        console.print(f"[red]Code coverage analysis failed: {e}[/red]")

def run_memory_usage_profiling(code_path, console):
    console.print("[bold]9. Memory Usage Profiling[/bold]")
    main_script = Prompt.ask("Enter the path to the main Python script to run for memory profiling (or press Enter to skip)", default="")
    if main_script.strip() == "":
        console.print("[yellow]No script provided. Skipping memory usage profiling.[/yellow]")
        return
    main_script_path = os.path.join(code_path, main_script)
    if not os.path.isfile(main_script_path):
        console.print(f"[red]The script '{main_script}' does not exist in the provided repository.[/red]")
        return
    memory_profile_output_file = os.path.join(os.getcwd(), 'memory_profile' + MEMORY_PROFILE_OUTPUT_FORMAT)
    try:
        cmd = ['mprof', 'run', '--include-children', 'python', main_script_path]
        console.print("[yellow]Running the program for memory profiling. Please interact with it as needed.[/yellow]")
        subprocess.run(cmd, check=True)
        cmd = ['mprof', 'plot', '--output', memory_profile_output_file]
        subprocess.run(cmd, check=True)
        console.print(f"Memory profile report saved to [green]{memory_profile_output_file}[/green]")
    except Exception as e:
        console.print(f"[red]Memory usage profiling failed: {e}[/red]")

def run_execution_profiling(code_path, console):
    console.print("[bold]10. Execution Profiling (Time and Performance)[/bold]")
    main_script = Prompt.ask("Enter the path to the main Python script to run for execution profiling (or press Enter to skip)", default="")
    if main_script.strip() == "":
        console.print("[yellow]No script provided. Skipping execution profiling.[/yellow]")
        return
    main_script_path = os.path.join(code_path, main_script)
    if not os.path.isfile(main_script_path):
        console.print(f"[red]The script '{main_script}' does not exist in the provided repository.[/red]")
        return
    performance_profile_output_file = os.path.join(os.getcwd(), 'performance_profile' + PERFORMANCE_PROFILE_OUTPUT_FORMAT)
    try:
        cmd = ['python', '-m', 'cProfile', '-o', performance_profile_output_file, main_script_path]
        console.print("[yellow]Running the program for execution profiling. Please interact with it as needed.[/yellow]")
        subprocess.run(cmd, check=True)
        console.print(f"Performance profile report saved to [green]{performance_profile_output_file}[/green]")
    except Exception as e:
        console.print(f"[red]Execution profiling failed: {e}[/red]")

def run_runtime_type_checking(code_path, console):
    console.print("[bold]11. Runtime Type Checking[/bold]")
    main_script = Prompt.ask("Enter the path to the main Python script to run with runtime type checking (or press Enter to skip)", default="")
    if main_script.strip() == "":
        console.print("[yellow]No script provided. Skipping runtime type checking.[/yellow]")
        return
    main_script_path = os.path.join(code_path, main_script)
    if not os.path.isfile(main_script_path):
        console.print(f"[red]The script '{main_script}' does not exist in the provided repository.[/red]")
        return
    type_check_output_file = os.path.join(os.getcwd(), 'runtime_type_checking' + TYPE_CHECK_OUTPUT_FORMAT)
    try:
        cmd = ['python', '-m', 'typeguard', main_script_path]
        console.print("[yellow]Running the program with runtime type checking. Please interact with it as needed.[/yellow]")
        with open(type_check_output_file, 'w') as f:
            subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, check=False)
        console.print(f"Type violation logs saved to [green]{type_check_output_file}[/green]")
    except Exception as e:
        console.print(f"[red]Runtime type checking failed: {e}[/red]")

def run_class_inheritance_visualization(code_path, console):
    console.print("[bold]12. Class Inheritance/Composition Visualization[/bold]")
    try:
        cmd = ['pyreverse', code_path, '-o', 'dot', '-p', 'classes']
        subprocess.run(cmd, check=True)
        # The output files are 'classes_classes.dot' and 'classes_packages.dot'
        diagram_files = ['classes_classes.dot', 'classes_packages.dot']
        for diagram in diagram_files:
            diagram_path = os.path.join(os.getcwd(), diagram)
            if os.path.exists(diagram_path):
                console.print(f"Class diagram saved to [green]{diagram_path}[/green]")
            else:
                console.print(f"[red]Failed to find generated diagram {diagram}[/red]")
    except Exception as e:
        console.print(f"[red]Class inheritance visualization failed: {e}[/red]")

def run_semantic_code_analysis(code_path, console):
    console.print("[bold]13. Semantic Code Analysis[/bold]")
    semantic_output_file = os.path.join(os.getcwd(), 'semantic_analysis' + SEMANTIC_ANALYSIS_FORMAT)
    try:
        cmd = ['mypy', code_path]
        with open(semantic_output_file, 'w') as f:
            subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, check=False)
        console.print(f"Semantic analysis report saved to [green]{semantic_output_file}[/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Semantic analysis failed:[/red]")
        console.print(e)

def run_automated_test_generation(code_path, console):
    console.print("[bold]14. Automated Test Generation[/bold]")
    console.print(f"[yellow]Automated test generation requires code-specific configuration and is not automated in this script.[/yellow]")

if __name__ == "__main__":
    main()
