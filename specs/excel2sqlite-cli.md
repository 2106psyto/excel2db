# Feature Specification: Excel to SQLite CLI Application

## Overview

Develop a Python command line application that generates a SQLite3 database from a specified Excel Workbook. Each worksheet in the workbook is converted into a table in the database. The application allows specifying the starting point (first row and first column) for each worksheet's data extraction. The worksheets to import and their respective starting points are described in a configuration file, which is provided as a command-line parameter.

## Motivation

Many users need to convert structured data from Excel workbooks into SQLite databases for further analysis, integration, or automation. This tool streamlines the process, allowing flexible selection of worksheets and data ranges, and automates table creation based on worksheet content.

## Requirements

- **Input:**
  - Excel Workbook file (e.g., `.xlsx`)
    - Must support Japanese characters in worksheet names, column headers, and cell data
    - No need to install Microsoft Excel to develop or use the program
  - Configuration file (`.yaml`) specifying:
    - Worksheets to import
    - Starting cell address (e.g., "C21", "AN7") for each worksheet's table data

- **Output:**
  - SQLite3 database file with tables corresponding to specified worksheets
    - Must preserve Japanese characters in table names, column names, and data

- **Functionality:**
  - Parse configuration file (YAML) for worksheet names and starting points
  - For each worksheet:
    - Extract data starting from specified row and column
    - Create a table in SQLite3 with appropriate column names and types
    - Insert extracted data into the table, preserving Japanese characters
  - Provide command-line interface to specify:
    - Excel file path
    - Configuration file path (YAML)
    - Output SQLite file path
  - The program must be distributed as a stand-alone executable file for Windows (no need to support Linux or MacOS)

## Implementation Plan

- Use Python 3.x
- Use `openpyxl` for reading Excel files (avoid using `pandas`)
- Use `sqlite3` (standard library) for database operations
- Use `argparse` for CLI parsing
- Support configuration in YAML (using `PyYAML`)
- Validate configuration and input files
- Log progress and errors to console

## Acceptance Criteria

- Given a valid Excel file and configuration, the CLI generates a SQLite database with tables matching the specified worksheets and data ranges.
- The CLI reports errors for missing files, invalid configuration, or data extraction issues.
- The tool is usable via command line with clear help and usage instructions.

## Out of Scope

- GUI interface
- Advanced data type inference beyond basic types
- Support for Excel formulas or complex cell formats

## Open Questions

- Should the tool support both `.xlsx` and `.xls` formats?
- Should the configuration support column type overrides?
- How to handle duplicate table or column names?

## References

- [openpyxl documentation](https://openpyxl.readthedocs.io/)
- [sqlite3 Python docs](https://docs.python.org/3/library/sqlite3.html)
