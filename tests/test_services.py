"""Integration tests for service template generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_services_init_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that services __init__.py is generated with correct imports."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    package = base_answers['project_package']
    init_file = result.project_dir / 'src' / package / 'services' / '__init__.py'
    assert init_file.exists()

    content = init_file.read_text()
    assert 'AppService' in content
    assert 'GreetingService' in content
    assert base_answers['project_name'] in content


def test_app_service_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that app_service.py is generated with correct imports."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    package = base_answers['project_package']
    service_file = result.project_dir / 'src' / package / 'services' / 'app_service.py'
    assert service_file.exists()

    content = service_file.read_text()
    assert f'from {package} import __version__' in content
    assert 'class AppService' in content
    assert 'def get_version' in content
