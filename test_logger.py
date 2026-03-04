from freel00p_colored_logger import get_logger

# 只用控制台
logger = get_logger("test_app", level="INFO")

logger.debug("這條不會顯示，因為 level 是 INFO")
logger.info("測試彩色輸出：應該看到綠色的 [INFO]")
logger.warning("黃色警告")
logger.error("紅色錯誤", exc_info=True)  # 會顯示 traceback

# 加檔案輸出測試
logger_file = get_logger(
    name="test_file",
    log_file="test.log",
    file_level="DEBUG"   # 檔案記錄更詳細
)

logger_file.info("這條會同時寫到 test.log")
logger_file.debug("檔案專屬的 debug 訊息")