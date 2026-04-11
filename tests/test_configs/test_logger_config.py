import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger(name="my-app")
        assert logger.name == "my-app"

    def test_has_handlers(self) -> None:
        logger: logging.Logger = setup_logger(name="test-logger-with-handlers")
        assert len(logger.handlers) > 0

    def test_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger(name="test-logger-debug-level")
        assert logger.level == logging.DEBUG

    def test_calling_twice_does_not_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger(name="test-no-duplicate-handlers")
        count_first: int = len(logger.handlers)
        setup_logger(name="test-no-duplicate-handlers")
        assert len(logger.handlers) == count_first

    def test_handler_is_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger(name="test-stream-handler")
        assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
