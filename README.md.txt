System Resource Monitor: A real-time, terminal-based system resource monitor written in Python.  
Displays CPU, Memory, Disk, and Network usage in a live dashboard using the `rich` and `psutil` libraries.

## Features
- Real-time monitoring of:
  - CPU usage
  - Memory usage
  - Disk usage (default: C:\ drive, can be changed)
  - Network activity (sent/received)
- Historical graphs for each resource
- Auto-logging of performance stats to `system_performance.log`
- Beautiful terminal interface

## Requirements:
- Python 3.8 or higher
- psutil
- rich

Install dependencies using: pip install psutil rich

## How to Run:
1. Clone this repository or download the code.
2. Open a terminal and navigate to the project directory.
3. Run the monitor: python system_monitor.py
4. Press Ctrl+C to stop monitoring.

## Customization:
- **Change monitored disk:**  
  In the get_disk_usage method, change 'C:\\' to your desired drive or path (e.g., `'/'` for Linux/macOS).

## Example Output:
┏━━━━━━━━━━━ System Overview ━━━━━━━━━━━┓
┃ CPU: 18.2%                           ┃
┃ Memory: 65.7%                        ┃
┃ Disk: 45.8%                          ┃
┃ Network: 1.45 MB/s | 452.12 KB/s     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

## Logging

- All resource stats are logged to `system_performance.log` in the project directory.

