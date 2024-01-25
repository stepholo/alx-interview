#!/usr/bin/python3
import sys
import signal

total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
lines_processed = 0


def print_statistics():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes_count.keys()):
        count = status_codes_count[code]
        if count > 0:
            print("{}: {}".format(code, count))
    print()


def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        _, _, _, _, _, status_code_str, file_size_str = line.split()[3:10]
        status_code = int(status_code_str)
        file_size = int(file_size_str)
    except (ValueError, IndexError):
        # Skip lines with incorrect format
        continue

    total_size += file_size
    status_codes_count[status_code] += 1
    lines_processed += 1

    if lines_processed % 10 == 0:
        print_statistics()
