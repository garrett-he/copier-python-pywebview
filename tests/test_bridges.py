"""Integration tests for bridge adapter template generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_bridges_init_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that bridges __init__.py is generated with correct imports."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    package = base_answers['project_package']
    init_file = result.project_dir / 'src' / package / 'bridges' / '__init__.py'
    assert init_file.exists()

    content = init_file.read_text()
    assert 'AppBridge' in content
    assert 'GreetingBridge' in content
    assert 'JsApi' in content


def test_app_bridge_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that app_bridge.py is generated with correct imports."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    bridge_file = result.project_dir / 'src' / package / 'bridges' / 'app_bridge.py'
    assert bridge_file.exists()

    content = bridge_file.read_text()
    assert f'from {package}.services.app_service import AppService' in content
    assert 'class AppBridge' in content
    assert 'def getVersion' in content


def test_greeting_bridge_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that greeting_bridge.py is generated with correct imports."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    bridge_file = result.project_dir / 'src' / package / 'bridges' / 'greeting_bridge.py'
    assert bridge_file.exists()

    content = bridge_file.read_text()
    assert f'from {package}.bridges.event_emitter import EventEmitter' in content
    assert f'from {package}.services.greeting_service import GreetingService' in content
    assert 'class GreetingBridge' in content
    assert 'def sayHello' in content


def test_js_api_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that js_api.py is generated with correct composition."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    api_file = result.project_dir / 'src' / package / 'bridges' / 'js_api.py'
    assert api_file.exists()

    content = api_file.read_text()
    assert f'from {package}.bridges.app_bridge import AppBridge' in content
    assert f'from {package}.bridges.greeting_bridge import GreetingBridge' in content
    assert 'class JsApi' in content
    assert 'app = AppBridge()' in content
    assert 'greeting = GreetingBridge()' in content
