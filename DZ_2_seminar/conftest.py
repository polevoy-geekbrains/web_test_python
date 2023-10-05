import pytest
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def x_selector1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector2():
    return