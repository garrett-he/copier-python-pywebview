"""Utility for dispatching custom events to the frontend."""

import json
from typing import Any

import webview


class EventEmitter:
    """Dispatches custom DOM events to the frontend via pywebview."""

    @staticmethod
    def emit(event: str, detail: Any = None) -> None:
        """Dispatch a CustomEvent on the frontend's window object.

        Args:
            event: The event name (e.g. 'pywebview-hello').
            detail: Optional data to pass as the event's detail property.
        """
        js_code = f"window.dispatchEvent(new CustomEvent('{event}', {{ detail: {json.dumps(detail)} }}))"
        webview.windows[0].evaluate_js(js_code)
