"""Integration tests for __main__.py template generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_main_module_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that __main__.py is generated."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    package = base_answers['project_package']
    main_file = result.project_dir / 'src' / package / '__main__.py'
    assert main_file.exists()


def test_main_module_contains_webview(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that __main__.py imports and uses webview."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    content = (result.project_dir / 'src' / package / '__main__.py').read_text()
    assert 'import webview' in content
    assert 'webview.create_window' in content
    assert 'webview.start' in content


def test_main_module_contains_logging(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that __main__.py sets up logging."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    content = (result.project_dir / 'src' / package / '__main__.py').read_text()
    assert 'from loguru import logger' in content
    assert 'setup_logging' in content


def test_main_module_contains_js_api(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that __main__.py imports and uses JsApi."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    content = (result.project_dir / 'src' / package / '__main__.py').read_text()
    assert f'from {package}.bridges.js_api import JsApi' in content
    assert 'js_api=JsApi()' in content


def test_main_module_contains_dev_url(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that __main__.py uses localhost:5173 in debug mode."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    content = (result.project_dir / 'src' / package / '__main__.py').read_text()
    assert 'http://localhost:5173' in content


def test_main_module_contains_project_name(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that __main__.py uses project_name in window title."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    content = (result.project_dir / 'src' / package / '__main__.py').read_text()
    assert base_answers['project_name'] in content
