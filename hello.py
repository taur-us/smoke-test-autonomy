def greet(name=None):
    """Return a greeting message.

    Args:
        name: Optional name to greet. If None, returns 'Hello, World!'

    Returns:
        A greeting string.
    """
    if name is None:
        return "Hello, World!"
    return f"Hello, {name}!"
