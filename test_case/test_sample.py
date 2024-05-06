import allure
import pytest

from common.yaml_utils import read_yaml
from page_object.workflow_sample_page import WorkflowSamplePage


@allure.epic('XXXXXXXX')
class TestSample:
    @allure.feature('XXXXXXXX')
    @allure.story('XXXXXXXXXXXXXXXX')
    @allure.title('XXXXXXXX')
    @allure.description('XXXXXXXX')
    @pytest.mark.parametrize('login', read_yaml('./data/login_sample.yaml'), indirect=True)
    @pytest.mark.parametrize('sample', read_yaml('./data/workflow_sample.yaml'))
    def test_sample(self, driver, login, sample):
        workflow = WorkflowSamplePage(driver)

        with allure.step('1. Go to workflow page'):
            workflow.open(workflow.url)
        with allure.step('2. Enter value'):
            workflow.enter(workflow.element_1, sample['value1'])
        with allure.step('3. Click button'):
            workflow.click(workflow.element_2)
        with allure.step('4. Successful'):
            workflow.wait_for(workflow.element_3)
