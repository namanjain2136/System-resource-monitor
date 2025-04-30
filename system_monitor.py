import psutil
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from collections import deque
import os

class SystemResourceMonitor:
    def __init__(self):
        self.cpu_history = deque(maxlen=50)
        self.mem_history = deque(maxlen=50)
        self.disk_history = deque(maxlen=50)
        self.network_send_history = deque(maxlen=50)
        self.network_recv_history = deque(maxlen=50)
        self.last_network_stats = psutil.net_io_counters()
        self.console = Console()
        self.log_file = os.path.join(os.getcwd(), "system_performance.log")

    def _convert_bytes(self, num):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return f"{num:.2f} {unit}"
            num /= 1024.0
        return f"{num:.2f} PB"

    def get_disk_usage(self):
        # Change the path to the drive you want to monitor, e.g., 'C:\\'
        disk = psutil.disk_usage('C:\\')
        self.disk_history.append(disk.percent)
        return {
            'total': self._convert_bytes(disk.total),
            'used': self._convert_bytes(disk.used),
            'percent': disk.percent
        }

    def get_system_stats(self):
        cpu_percent = psutil.cpu_percent(interval=0.1)
        self.cpu_history.append(cpu_percent)

        mem = psutil.virtual_memory()
        self.mem_history.append(mem.percent)

        disk = self.get_disk_usage()

        current_network_stats = psutil.net_io_counters()
        sent_diff = current_network_stats.bytes_sent - self.last_network_stats.bytes_sent
        recv_diff = current_network_stats.bytes_recv - self.last_network_stats.bytes_recv
        self.network_send_history.append(sent_diff / 1024)
        self.network_recv_history.append(recv_diff / 1024)
        self.last_network_stats = current_network_stats

        stats = {
            'cpu': cpu_percent,
            'memory': mem.percent,
            'disk': disk['percent'],
            'network': {
                'sent': self._convert_bytes(sent_diff) + '/s',
                'received': self._convert_bytes(recv_diff) + '/s'
            }
        }
        self.log_performance(stats)
        return stats

    def log_performance(self, stats):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as log:
            log.write(f"[{timestamp}] CPU: {stats['cpu']}%, Memory: {stats['memory']}%, Disk: {stats['disk']}%, "
                      f"Network Sent: {stats['network']['sent']}, Network Received: {stats['network']['received']}\n")

    def create_graph(self, history, title, color):
        graph_str = "".join(["█" * (int(v) // 2) + " " * (50 - int(v) // 2) + "\n" for v in history])
        return Panel(graph_str, title=title, border_style=color)

    def create_dashboard(self):
        stats = self.get_system_stats()

        layout = Layout()
        overview_panel = Panel(
            f"[bold blue]CPU:[/] {stats['cpu']}%\n"
            f"[bold red]Memory:[/] {stats['memory']}%\n"
            f"[bold yellow]Disk:[/] {stats['disk']}%\n"
            f"[bold cyan]Network:[/] {stats['network']['sent']} | {stats['network']['received']}",
            title="System Overview",
            border_style="blue"
        )

        cpu_graph = self.create_graph(self.cpu_history, "CPU Usage", "green")
        mem_graph = self.create_graph(self.mem_history, "Memory Usage", "red")
        disk_graph = self.create_graph(self.disk_history, "Disk Usage", "yellow")
        net_graph = self.create_graph(self.network_send_history, "Network Activity", "cyan")

        layout.split_column(
            Layout(overview_panel, name="overview", ratio=1),
            Layout(name="bottom")
        )
        layout["bottom"].split_row(
            Layout(cpu_graph, name="cpu", ratio=1),
            Layout(mem_graph, name="memory", ratio=1),
            Layout(disk_graph, name="disk", ratio=1),
            Layout(net_graph, name="network", ratio=1)
        )
        return layout

    def run(self):
        with Live(self.create_dashboard(), refresh_per_second=4, screen=True) as live:
            try:
                while True:
                    live.update(self.create_dashboard())
                    time.sleep(0.25)
            except KeyboardInterrupt:
                print("\nMonitoring stopped.")

def main():
    monitor = SystemResourceMonitor()
    monitor.run()

if __name__ == "__main__":
    main()
