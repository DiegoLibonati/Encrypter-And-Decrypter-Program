import os
from unittest.mock import patch

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.DEBUG is False

    def test_testing_is_false(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert config.TESTING is False

    def test_tz_is_string(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert isinstance(config.TZ, str)
        assert len(config.TZ) > 0

    def test_tz_overridden_by_env(self) -> None:
        with patch.dict(os.environ, {"TZ": "Europe/London"}):
            config: DefaultConfig = DefaultConfig()
            assert config.TZ == "Europe/London"

    def test_env_name_is_string(self) -> None:
        config: DefaultConfig = DefaultConfig()
        assert isinstance(config.ENV_NAME, str)
        assert len(config.ENV_NAME) > 0

    def test_env_name_overridden_by_env(self) -> None:
        with patch.dict(os.environ, {"ENV_NAME": "my-custom-app"}):
            config: DefaultConfig = DefaultConfig()
            assert config.ENV_NAME == "my-custom-app"
