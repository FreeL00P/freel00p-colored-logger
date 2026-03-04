# freel00p-colored-logger

簡單的 ANSI 彩色控制台 logger，支援可選的檔案輸出。

## 安裝

```bash
pip install freel00p-colored-logger
```
# 使用范例
# 
from freel00p_colored_logger import get_logger

# 只用彩色控制台
logger = get_logger("pymupdf", level=logging.INFO)

# 加檔案輸出（自動建立目錄）
logger = get_logger(
    name="pymupdf",
    log_file="logs/pymupdf.log",
    file_level=logging.DEBUG   # 檔案記錄更細
)

logger.info("開始處理...")
logger.warning("有警告！")
logger.error("出錯了", exc_info=True)


