
# Juju Log Analysis Tool

This repository contains a Python script, `main.py`, which serves as a command-line tool to analyze Juju debug log files. Juju logs can be verbose and contain a lot of extraneous information, making it challenging to extract meaningful insights. This tool simplifies that process by parsing the log file and providing summarized statistics based on severity levels and charm units.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Analyzing All Charms](#analyzing-all-charms)
  - [Analyzing a Specific Charm](#analyzing-a-specific-charm)
- [Output Explanation](#output-explanation)
- [Assumptions Made](#assumptions-made)
- [Time Spent](#time-spent)

## Features

- Parses Juju log files for specific severity levels: `INFO`, `DEBUG`, `WARNING`, and `ERROR`.
- Filters log entries by charm name if specified.
- Ignores log lines that do not conform to the expected format.
- Provides the following statistics:
  - Charms that produced warning messages.
  - Number of messages by severity.
  - Number of duplicate messages and their severities.
  - Proportions of each type of log message per charm.
  - Total number of log messages per charm.
  - Total number of log messages.

## Prerequisites

- **Python 3** installed on your system.
- No additional Python packages are required; the script uses only standard libraries.

## Usage

1. **Clone or Download the Repository**:

   ```bash
   git clone https://github.com/yourusername/juju-log-analysis.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd juju-log-analysis
   ```

3. **Ensure Your Log File is Ready**:

   Place your Juju log file (e.g., `juju_debug_log.txt`) in the same directory as `main.py`.

4. **Run the Script**:

   ```bash
   python main.py <log_filename> [--charm <charm_name>]
   ```

   - `<log_filename>`: The path to your Juju log file.
   - `--charm <charm_name>`: *(Optional)* Specify a charm name to filter the results.

### Analyzing All Charms

```bash
python main.py juju_debug_log.txt
```

### Analyzing a Specific Charm

```bash
python main.py juju_debug_log.txt --charm mysql
```

Replace `mysql` with the actual name of the charm you wish to analyze.

## Output Explanation

- **Charms with Warning Messages**: Lists charms that have produced warning messages (if not filtered by a specific charm).
- **Number of Messages by Severity**: Shows the count of log messages for each severity level.
- **Duplicate Messages**: Displays messages that appear more than once, along with their severity and occurrence count.
- **Proportions of Log Messages**: Presents the percentage distribution of each severity level per charm.
- **Total Number of Log Messages per Charm**: Indicates how many log messages each charm has produced.
- **Total Number of Log Messages**: The overall count of log messages processed.

## Assumptions Made

- **Log Line Format**: The log lines are expected to follow a specific format:

  ```
  unit: timestamp severity message
  ```

  Lines that do not match this pattern are ignored.

- **Charm Name Extraction**: The charm name is extracted from the unit name by splitting on the `'/'` character. For example, `mysql/0` gives `mysql`.

- **Severity Levels**: Only messages with the following severity levels are considered: `INFO`, `DEBUG`, `WARNING`, `ERROR`.

- **Standard Libraries**: Only standard Python libraries are used to maintain simplicity and avoid external dependencies.

## Time Spent

The development and testing of this script took approximately **3 hours**, which included:

- Understanding the log file structure.
- Writing the parsing logic.
- Handling optional parameters.
- Testing with sample data to ensure accuracy.

---

Feel free to contribute to this project by submitting issues or pull requests. Your feedback is welcome!
