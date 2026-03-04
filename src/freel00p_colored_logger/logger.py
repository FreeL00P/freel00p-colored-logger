import logging
import sys
from pathlib import Path
from typing import Optional

# ANSI 顏色定義（你原來的配色）
TIMESTAMP_COLOR = "\033[94m"   # 亮藍
LEVEL_COLORS = {
    "DEBUG":    "\033[94m",
    "INFO":     "\033[92m",
    "WARNING":  "\033[93m",
    "ERROR":    "\033[91m",
    "CRITICAL": "\033[95m",
}
MESSAGE_COLOR = "\033[97m"     # 亮白
RESET = "\033[0m"


class TimestampLevelColoredFormatter(logging.Formatter):
    """控制台專用：時間戳 + 級別 彩色格式"""

    def format(self, record):
        ts = self.formatTime(record, self.datefmt or "%Y-%m-%d %H:%M:%S")
        timestamp = f"{TIMESTAMP_COLOR}{ts}{RESET}"
        level_colored = f"{LEVEL_COLORS.get(record.levelname, '')}[{record.levelname}]{RESET}"
        msg_colored = f"{MESSAGE_COLOR}{record.getMessage()}{RESET}"
        return f"{timestamp} {level_colored} {msg_colored}"


def get_logger(
    name: str = "app",
    level: int = logging.INFO,
    log_file: Optional[str | Path] = None,
    file_level: int = logging.DEBUG,
    datefmt: str = "%Y-%m-%d %H:%M:%S",
    propagate: bool = False,
) -> logging.Logger:
    """
    取得一個彩色控制台 + 可選檔案輸出的 logger。
    只在第一次呼叫時設定 handler，避免重複配置。
    """
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(level)
    logger.propagate = propagate

    # 控制台 - 彩色
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(level)
    ch.setFormatter(TimestampLevelColoredFormatter(datefmt=datefmt))
    logger.addHandler(ch)

    # 檔案 - 純文字（可選）
    if log_file:
        path = Path(log_file)
        path.parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(path, encoding="utf-8")
        fh.setLevel(file_level)
        fh.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)-8s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
        )
        logger.addHandler(fh)

    return logger