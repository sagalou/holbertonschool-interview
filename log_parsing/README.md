# Log Parsing

## Description

This project contains a Python script that reads log lines from `stdin` and computes metrics in real time. Statistics are printed every 10 lines and on keyboard interruption (`CTRL + C`).

## Requirements

- Python 3.4+
- Ubuntu 14.04 LTS

## File

| File | Description |
|------|-------------|
| `0-stats.py` | Reads stdin line by line and prints file size and status code statistics |

## Input Format

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Lines that do not match this format are skipped.

## Output

After every 10 lines and/or a keyboard interruption:

- **Total file size**: sum of all `<file size>` values
- **Number of lines per status code** (in ascending order): `200`, `301`, `400`, `401`, `403`, `404`, `405`, `500`

### Example

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

## Usage

```bash
./0-generator.py | ./0-stats.py
```

## Author

Sagalou