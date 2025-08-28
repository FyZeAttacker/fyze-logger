import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class FyzeLogger:
    def __init__(self, name="Fyze"):
        self.name = name

    def _time(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

    def success(self, msg):
        print(f"[{self._time()}] {Fore.GREEN}[{self.name} SUCCESS]{Style.RESET_ALL} » {msg}")

    def error(self, msg):
        print(f"[{self._time()}] {Fore.RED}[{self.name} ERROR]{Style.RESET_ALL} » {msg}")

    def debug(self, msg):
        print(f"[{self._time()}] {Fore.CYAN}[{self.name} DEBUG]{Style.RESET_ALL} » {msg}")

    def warn(self, msg):
        print(f"[{self._time()}] {Fore.YELLOW}[{self.name} WARN]{Style.RESET_ALL} » {msg}")

    def ratelimit(self, msg):
        print(f"[{self._time()}] {Fore.MAGENTA}[{self.name} RATELIMIT]{Style.RESET_ALL} » {msg}")


# Example usage
if __name__ == "__main__":
    log = FyzeLogger()
    log.success("Operation successful!")
    log.error("Something went wrong!")
    log.debug("Debug information")
    log.warn("Warning message")
    log.ratelimit("Ratelimit message")
