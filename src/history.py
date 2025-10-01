class BrowserHistory:
    def __init__(self):
        self._history = []       # stores visited URLs
        self._current_index = -1 # pointer to the current page (-1 means no page yet)

    def visit(self, url: str):
        """Visit a new URL and clear forward history."""
        # Remove any forward history when visiting a new URL
        if self._current_index < len(self._history) - 1:
            self._history = self._history[:self._current_index + 1]

        self._history.append(url)
        self._current_index += 1

    def back(self):
        """Go back one step in history. Returns the URL or None if not possible."""
        if self._current_index > 0:
            self._current_index -= 1
            return self._history[self._current_index]
        return None

    def forward(self):
        """Go forward one step in history. Returns the URL or None if not possible."""
        if self._current_index < len(self._history) - 1:
            self._current_index += 1
            return self._history[self._current_index]
        return None

    def current(self):
        """Return the current URL or None if empty."""
        if self._current_index >= 0:
            return self._history[self._current_index]
        return None

    def history(self):
        """Return the full history list."""
        return list(self._history)
