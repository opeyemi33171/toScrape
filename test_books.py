from books import get_category_links

class Driver:
    def __init__(self):
        self.findElementWasCalled = False

    def find_element_by_class_name(self, element):
        self.findElementWasCalled = True


def test_driver_find_element():
    driver = Driver()
    get_category_links(driver)

    assert driver.findElementWasCalled == True
