import sys
import colorama
import inspect
from datetime import datetime

colorama.init()

class Logger:
    def __init__(self, time_stamp=True, enabled=True, inspect_mode=False):
        self.time_stamp = time_stamp
        self.enabled = enabled
        self.inspect_mode = inspect_mode

    def colored_bg(self, text, bg_color_code, fg_color_code="30"):
        return f"\033[{fg_color_code};{bg_color_code}m{text}\033[0m"

    def _get_inspect_info(self):
        frame = inspect.stack()[3]
        filename = frame.filename
        lineno = frame.lineno
        func_name = frame.function
        return f"{filename}:{lineno} in {func_name}()"

    def _format_msg(self, level, msg, bg_color_code):
        if not self.enabled:
            return None
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if self.time_stamp else ""
        timestamp_colored = self.colored_bg(timestamp, "47", "30") if timestamp else ""
        level_tag = self.colored_bg(f"[{level}]", bg_color_code, "30")
        inspect_info = f"    {self.colored_bg(self._get_inspect_info(), '33', '40')}" if self.inspect_mode else ""
        return f"{timestamp_colored} {level_tag} {msg}{inspect_info}".strip()

    def info(self, msg):
        formatted = self._format_msg("INFO", msg, "44")
        if formatted:
            print(formatted)

    def error(self, msg):
        formatted = self._format_msg("ERROR", msg, "41")
        if formatted:
            print(formatted)

    def warning(self, msg):
        formatted = self._format_msg("WARNING", msg, "43")
        if formatted:
            print(formatted)

    def critical(self, msg):
        formatted = self._format_msg("CRITICAL", msg, "45")
        if formatted:
            print(formatted)

if __name__ == "__main__":
    use_log = "--uselogs" in sys.argv
    use_inspect = "--inspect" in sys.argv
    log = Logger(enabled=use_log, inspect_mode=use_inspect)

