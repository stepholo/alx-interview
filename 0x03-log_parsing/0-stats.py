#!/usr/bin/python3

import sys


total_size = 0
stats = {}
allowed = [200, 301, 400, 401, 403, 404, 405, 500]
count = 0


def show_stats():
    '''Print the statistics'''
    print("File size: {}".format(total_size))

    for stat in sorted(stats.keys()):
        print("{}: {}".format(stat, stats.get(stat)))


try:
    for line in sys.stdin:
        line = line.strip().split()
        if (len(line) != 10 or line[5] != "GET" or line[6] != "/projects/260"
           or line[8] != "HTTPS/1.1"):
            continue

        status_code = int(line[7])
        file_size = int(line[9])

        if status_code not in allowed:
            continue

        stats[status_code] = stats.get(status_code, 0) + 1
        total_size += file_size

        count += 1
        if count == 10:
            show_stats()
            count = 0

except KeyboardInterrupt:
    pass
finally:
    show_stats()
