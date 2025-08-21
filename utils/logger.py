# utils/logger.py
import sys
from pathlib import Path
from loguru import logger

def setup_logger():
    """
    配置 loguru 日志记录器。

    - 移除默认的处理器，以完全控制日志输出。
    - 添加一个控制台输出，用于实时查看 INFO 级别以上的日志。
    - 添加一个文件输出，用于记录 DEBUG 级别以上的详细日志，并设置日志文件轮转。
    """
    # 移除默认的、简陋的控制台输出
    logger.remove()

    # 定义日志文件的路径
    log_path = Path("logs") / "test_run_{time:YYYY-MM-DD}.log"

    # 添加一个新的、格式化的控制台处理器
    logger.add(
        sys.stdout,
        level="INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )

    # 添加一个文件处理器，用于将所有 DEBUG 级别及以上的日志写入文件
    logger.add(
        log_path,
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="10 MB",  # 当文件超过 10MB 时，创建新文件
        retention="7 days", # 最多保留 7 天的日志
        encoding="utf-8",
        enqueue=True,      # 使日志写入异步，提高性能
        backtrace=True,    # 记录完整的异常堆栈
        diagnose=True      # 添加异常诊断信息
    )
    
    logger.info("Logger has been successfully configured.")