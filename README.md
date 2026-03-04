```markdown
# freel00p-colored-logger

一个极简、轻量的 Python 日志工具，提供：

- 控制台输出带 ANSI 颜色的时间戳 + 日志级别
- 可选的纯文本文件日志输出
- 零额外依赖（只依赖标准库 `logging`）
- 简单易用，一行代码获取 logger

## 特性

- 彩色控制台输出（时间戳蓝色、INFO 绿色、WARNING 黄色、ERROR 红色、CRITICAL 紫色）
- 支持自定义日志名称、级别、文件路径
- 自动创建日志文件所在目录
- 防止重复添加 handler（适合 Jupyter、多模块使用）
- 完全兼容 Python 3.8+

## 安装

```bash
pip install freel00p-colored-logger
```

或使用 uv（推荐，更快）：

```bash
uv pip install freel00p-colored-logger
```

## 快速使用

```python
from freel00p_colored_logger import get_logger

# 1. 只输出到控制台（带颜色）
logger = get_logger("my_app", level="INFO")

logger.debug("这条不会显示（级别太低）")
logger.info("开始处理数据...")
logger.warning("内存使用率较高")
logger.error("文件读取失败", exc_info=True)
```

输出示例（控制台彩色效果）：
```
2025-03-04 18:45:23 [INFO] 开始处理数据...
2025-03-04 18:45:24 [WARNING] 内存使用率较高
2025-03-04 18:45:25 [ERROR] 文件读取失败
Traceback (most recent call last): ...
```

```python
# 2. 同时输出到文件（文件是纯文本格式）
logger = get_logger(
    name="pdf_processor",
    level="INFO",
    log_file="logs/pdf.log",         # 自动创建目录
    file_level="DEBUG"               # 文件记录更详细
)

logger.debug("详细调试信息，只写到文件")
logger.info("这条同时出现在控制台和文件")
```

## 完整参数说明

```python
get_logger(
    name: str = "app",                      # logger 名称
    level: int | str = logging.INFO,        # 控制台最低级别（可传字符串 "INFO"）
    log_file: str | Path | None = None,     # 文件路径，None 则不写文件
    file_level: int | str = logging.DEBUG,  # 文件最低级别
    datefmt: str = "%Y-%m-%d %H:%M:%S",     # 时间格式
    propagate: bool = False                 # 是否向上传播（通常设为 False）
) -> logging.Logger
```

## 推荐用法

在项目入口文件或主模块中：

```python
# main.py
from freel00p_colored_logger import get_logger

logger = get_logger("my_project", log_file="logs/app.log")

# 全项目共用这个 logger
def some_function():
    logger.info("函数开始执行")
```

## 为什么选择这个库？

- 极简：只有 ~100 行代码，无任何第三方依赖
- 颜色直观：适合开发/调试阶段快速定位问题
- 安全：避免重复配置 handler 的常见坑
- 跨平台：ANSI 颜色在大多数终端（Windows Terminal、VS Code、iTerm 等）正常显示

## 贡献

欢迎提交 issue 或 PR！

1. Fork 本仓库
2. 创建 feature 分支 (`git checkout -b feature/xxx`)
3. 提交代码 (`git commit -m 'Add some feature'`)
4. Push 到分支 (`git push origin feature/xxx`)
5. 提交 Pull Request

## 许可证

MIT License

Copyright (c) 2025 FreeL00P

详见 [LICENSE](LICENSE) 文件。
```

### 建议后续可以添加的元素

1. **控制台彩色截图**（强烈推荐）
   - 运行你的 test_logger.py，把控制台输出截图
   - 上传到仓库的 `images/` 文件夹
   - 在 README 加入：

     ```markdown
     ## 控制台效果预览

     ![控制台彩色日志输出](images/console-output.png)
     ```

2. **PyPI 下载徽章**
   在 README 最上面加：

   ```markdown
   [![PyPI version](https://badge.fury.io/py/freel00p-colored-logger.svg)](https://badge.fury.io/py/freel00p-colored-logger)
   [![Python versions](https://img.shields.io/pypi/pyversions/freel00p-colored-logger.svg)](https://pypi.org/project/freel00p-colored-logger/)
   ```



