# Server Health Monitor

A simple Linux server health monitoring project built with Python.

## Current Features

- Reads the real disk usage of the Linux root filesystem `/`
- Displays the disk usage percentage
- Returns a health status based on the following rule:

```text
Disk usage < 80%  -> OK
Disk usage >= 80% -> WARNING
