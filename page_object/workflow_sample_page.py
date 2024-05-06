from base.base_page import BasePage


class WorkflowSamplePage(BasePage):
    # URL of the workflow sample page
    url = '/workflow'

    # Element locators of workflow sample page
    element_1 = ('css selector', 'input.element_1')
    element_2 = ('css selector', 'input.element_2')
    element_3 = ('css selector', 'input.element_3')

    def __init__(self, driver):
        super().__init__(driver)
