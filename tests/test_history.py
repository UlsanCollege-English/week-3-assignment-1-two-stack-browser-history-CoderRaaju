import pytest
from src.history import BrowserHistory

def test_visit_and_current():
    h = BrowserHistory()
    assert h.current() is None

    h.visit("google.com")
    assert h.current() == "google.com"

    h.visit("github.com")
    assert h.current() == "github.com"

def test_back_functionality():
    h = BrowserHistory()
    h.visit("google.com")
    h.visit("github.com")
    h.visit("openai.com")

    assert h.current() == "openai.com"
    assert h.back() == "github.com"
    assert h.current() == "github.com"
    assert h.back() == "google.com"
    assert h.current() == "google.com"
    assert h.back() is None  # can't go back further

def test_forward_functionality():
    h = BrowserHistory()
    h.visit("google.com")
    h.visit("github.com")
    h.visit("openai.com")

    h.back()   # now at github.com
    h.back()   # now at google.com
    assert h.current() == "google.com"

    assert h.forward() == "github.com"
    assert h.forward() == "openai.com"
    assert h.forward() is None  # can't go forward more

def test_visit_clears_forward_history():
    h = BrowserHistory()
    h.visit("google.com")
    h.visit("github.com")
    h.visit("openai.com")

    h.back()   # github.com
    h.visit("reddit.com")  # clears forward history

    assert h.current() == "reddit.com"
    assert h.forward() is None
    assert h.history() == ["google.com", "github.com", "reddit.com"]
