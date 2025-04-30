## 🖥️ System Resource Monitor

A real-time, terminal-based system resource monitor written in Python.  
Displays **CPU**, **Memory**, **Disk**, and **Network** usage in a live dashboard using the [`rich`](https://pypi.org/project/rich/) and [`psutil`](https://pypi.org/project/psutil/) libraries.


## 🚀 Features
- Real-time monitoring of:
  - 🧮 CPU usage
  - 🧠 Memory usage
  - 💾 Disk usage (default: `C:\` drive, can be changed)
  - 🌐 Network activity (sent/received)
- 📈 Historical graphs for each resource
- 📝 Auto-logging of performance stats to `system_performance.log`
- 🎨 Beautiful terminal interface with color and layout
- ⚡ Fast refresh rate for near-instant updates


## 📦 Requirements
- Python 3.8 or higher
- psutil
- rich

Install dependencies using: pip install psutil rich

## 🛠️ How to Run
To get started with the System Resource Monitor, follow these steps:

1. **Download the Project**  
   You can either clone the repository using Git or download it as a ZIP file:
   - **Clone with Git:**  
     git clone https://github.com/namanjain2136/System-resource-monitor.git
   - **Or download as ZIP:**  
     - Click the green **Code** button on the repo page.
     - Choose **Download ZIP** and extract it to a folder.

2. **Open a Terminal**  
   Open your terminal (Command Prompt, PowerShell, or Terminal app).

3. **Navigate to the Project Directory**  
   Change to the directory where you downloaded or extracted the project: cd path/to/System-resource-monitor

4. **Install Dependencies**  
Make sure you have Python 3.8 or newer installed. Then, install the required packages: pip install -r requirements.txt

*If you don’t have a `requirements.txt`, you can install manually:* pip install psutil rich

5. **Run the System Resource Monitor**  
Start the monitor with:
python system_monitor.py

6. **Stop the Monitor**  
To stop monitoring, press `Ctrl+C` in your terminal.

## ⚙️ Customization

- **Change monitored disk:**  
In the `get_disk_usage` method of `system_monitor.py`, change `'C:\\'` to your desired drive or path (e.g., `'/'` for Linux/macOS).

## 🤔 Why Use This Project?

- **Instant insight:** See your system’s health at a glance, right in your terminal.
- **Cross-platform:** Works on Windows, Linux, and macOS.
- **No setup hassle:** Just install dependencies and run-no extra config needed.
- **Open source:** Free to use and modify for your needs!
