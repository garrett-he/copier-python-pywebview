"""Greeting message service."""


class GreetingService:
    """Generates greeting messages."""

    def greet(self, name: str) -> str:
        """Generate a greeting message for the given name.

        Args:
            name: The name to greet.

        Returns:
            A greeting string.
        """
        return f'Hello, {name}'
