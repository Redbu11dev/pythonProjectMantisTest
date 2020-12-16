import importlib
import json
import jsonpickle
import pytest
import os

from fixture.application import Application

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

# @pytest.fixture(scope="session")
@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    # if target is None:
    #     config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
    #     with open(config_file) as f:
    #         target = json.load(f)
    # base_url = request.config.getoption("--baseUrl")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    # parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target", action="store", default="target.json")
