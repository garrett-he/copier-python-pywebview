"""Integration tests for .gitignore generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_gitignore_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .gitignore is generated."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    gitignore = result.project_dir / '.gitignore'
    assert gitignore.exists()


def test_gitignore_contains_frontend_entries(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .gitignore contains frontend entries."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / '.gitignore').read_text()
    assert 'frontend/node_modules/' in content
    assert 'frontend/coverage/' in content


def test_gitignore_contains_package_ui(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .gitignore contains the package ui build output."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / '.gitignore').read_text()
    package = base_answers['project_package']
    assert f'src/{package}/ui' in content


def test_gitignore_contains_python_entries(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that .gitignore contains standard Python entries."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / '.gitignore').read_text()
    assert '__pycache__/' in content
    assert '.venv/' in content
    assert '.pytest_cache/' in content
