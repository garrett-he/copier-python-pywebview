"""Integration tests for frontend template generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_copie.plugin import Copie


def test_index_html_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that index.html is generated with correct title."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir is not None

    index_html = result.project_dir / 'frontend' / 'index.html'
    assert index_html.exists()

    content = index_html.read_text()
    assert base_answers['project_name'] in content
    assert '<div id="app"></div>' in content


def test_package_json_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that package.json is generated with correct metadata."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    pkg_json = result.project_dir / 'frontend' / 'package.json'
    assert pkg_json.exists()

    content = pkg_json.read_text()
    assert base_answers['project_name'] in content
    assert base_answers['project_version'] in content
    assert base_answers['project_description'] in content
    assert base_answers['copyright_holder_name'] in content
    assert base_answers['copyright_holder_email'] in content
    assert base_answers['vcs_github_path'] in content


def test_package_json_contains_keywords(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that package.json contains project keywords."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / 'frontend' / 'package.json').read_text()
    keywords = base_answers['project_keywords'].split(',')
    for kw in keywords:
        assert kw.strip() in content


def test_package_json_contains_scripts(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that package.json contains required scripts."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    content = (result.project_dir / 'frontend' / 'package.json').read_text()
    assert '"dev": "vite"' in content
    assert '"build": "vite build"' in content
    assert '"check": "biome check src/"' in content
    assert '"typecheck": "vue-tsc --noEmit"' in content
    assert '"test": "vitest run"' in content


def test_vite_config_generated(copie: Copie, base_answers: dict[str, str]) -> None:
    """Test that vite.config.ts is generated with correct outDir."""
    result = copie.copy(extra_answers=base_answers)

    assert result.exit_code == 0
    assert result.project_dir is not None

    vite_config = result.project_dir / 'frontend' / 'vite.config.ts'
    assert vite_config.exists()

    content = vite_config.read_text()
    package = base_answers['project_package']
    assert f'../src/{package}/ui' in content
    assert 'vue' in content
    assert 'jsdom' in content
