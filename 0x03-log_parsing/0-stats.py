#!/usr/bin/python3
import sys
import signal
import re

total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Prints current statistics based on accumulated data."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    """Handles SIGINT signal (Ctrl+C)
      to print statistics and exit gracefully."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

log_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] '
                         r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

for line in sys.stdin:
    line = line.strip()
    match = log_pattern.match(line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        total_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
    else:
        continue

print_statistics()
