import pytest

from fixture.application import Application


def test_login(app: Application):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
