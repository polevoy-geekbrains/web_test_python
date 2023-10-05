import yaml
from module import Site


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, error_code):

    input1 = site.find_element("xpath", x_selector1)
    