import argparse
import re
from collections import defaultdict, Counter
from typing import Dict, List, Tuple


def parse_log_line(line: str) -> Tuple[str, str, str]:
    match = re.match(r'^(\S+):\s+(\d+:\d+:\d+)\s+(\w+)\s+(.+)', line)
    if match:
        unit, timestamp, severity, message = match.groups()
        return unit, severity, message
    return None, None, None


def analyze_log(filename: str, target_charm: str = None) -> Dict:
    severities = ['INFO', 'DEBUG', 'WARNING', 'ERROR']
    results = {
        'charms_with_warnings': set(),
        'severity_counts': defaultdict(int),
        'duplicate_messages': defaultdict(lambda: defaultdict(int)),
        'charm_logs': defaultdict(lambda: defaultdict(int)),
        'total_logs_per_charm': defaultdict(int),
        'total_logs': 0
    }

    with open(filename, 'r') as file:
        for line in file:
            unit, severity, message = parse_log_line(line)
            if unit and severity in severities:
                charm = unit.split('/')[0]  # Changed from split('-')[0]

                if target_charm and charm != target_charm:
                    continue

                results['total_logs'] += 1
                results['severity_counts'][severity] += 1
                results['charm_logs'][charm][severity] += 1
                results['total_logs_per_charm'][charm] += 1
                results['duplicate_messages'][severity][message] += 1

                if severity == 'WARNING':
                    results['charms_with_warnings'].add(charm)

    return results


def print_results(results: Dict, target_charm: str = None):
    if results['total_logs'] == 0:
        print(f"No log entries found{' for the specified charm' if target_charm else ''}.")
        return

    if not target_charm:
        print("Charms with warning messages:", ', '.join(results['charms_with_warnings']))

    print("\nNumber of messages by severity:")
    for severity, count in results['severity_counts'].items():
        print(f"{severity}: {count}")

    print("\nDuplicate messages:")
    for severity, messages in results['duplicate_messages'].items():
        for message, count in messages.items():
            if count > 1:
                print(f"{severity} (x{count}): {message[:50]}...")

    print("\nProportions of log messages by charm and severity:")
    for charm, severities in results['charm_logs'].items():
        if target_charm and charm != target_charm:
            continue
        total = sum(severities.values())
        print(f"\n{charm}:")
        for severity, count in severities.items():
            percentage = (count / total) * 100
            print(f"  {severity}: {percentage:.2f}%")

    print("\nTotal number of log messages per charm:")
    for charm, count in results['total_logs_per_charm'].items():
        if target_charm and charm != target_charm:
            continue
        print(f"{charm}: {count}")

    print(f"\nTotal number of log messages: {results['total_logs']}")


def main():
    parser = argparse.ArgumentParser(description="Analyze Juju log files")
    parser.add_argument("filename", help="Path to the log file")
    parser.add_argument("--charm", help="Optional charm name to filter results")
    args = parser.parse_args()

    results = analyze_log(args.filename, args.charm)
    print_results(results, args.charm)


if __name__ == "__main__":
    main()