"""Integration tests for justfile generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_justfile_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that justfile is generated."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    justfile = result.project_dir / 'justfile'
    assert justfile.exists()


def test_justfile_contains_backend_tasks(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that justfile contains backend tasks."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / 'justfile').read_text()
    assert 'be-install:' in content
    assert 'be-lint:' in content
    assert 'be-format:' in content
    assert 'be-test:' in content
    assert 'be-dev:' in content


def test_justfile_contains_frontend_tasks(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that justfile contains frontend tasks."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / 'justfile').read_text()
    assert 'fe-install:' in content
    assert 'fe-lint:' in content
    assert 'fe-format:' in content
    assert 'fe-test:' in content
    assert 'fe-build:' in content
    assert 'fe-dev:' in content


def test_justfile_contains_aggregate_tasks(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that justfile contains aggregate tasks."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / 'justfile').read_text()
    assert 'install:' in content
    assert 'lint:' in content
    assert 'format:' in content
    assert 'test:' in content


def test_justfile_contains_package_name(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that justfile be-dev uses the correct package name."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / 'justfile').read_text()
    package = base_answers['project_package']
    assert f'python -m {package}' in content


def test_justfile_contains_windows_shell(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that justfile sets windows-shell for cross-platform support."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / 'justfile').read_text()
    assert 'windows-shell' in content
