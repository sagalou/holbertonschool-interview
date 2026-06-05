#!/usr/bin/python3
"""Read stdin lines and print stats every 10 lines or on KeyboardInterrupt."""
import sys

STATUS_CODES = ["200", "301", "400", "401", "403", "404", "405", "500"]

def print_stats(total_size, counts):
    print("File size: {}".format(total_size))
    for code in sorted(counts.keys()):
        if counts[code]:
            print("{}: {}".format(code, counts[code]))


def main():
    total_size = 0
    counts = {code: 0 for code in STATUS_CODES}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            # try to parse status code and file size from the end
            try:
                file_size = int(parts[-1])
            except (IndexError, ValueError):
                continue
            try:
                status_code = parts[-2]
            except IndexError:
                continue

            total_size += file_size
            if status_code in counts:
                counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, counts)

    except KeyboardInterrupt:
        pass

    print_stats(total_size, counts)


if __name__ == '__main__':
    main()