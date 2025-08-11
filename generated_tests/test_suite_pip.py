import pytest
from agent_test_framework.core.base_test import BaseBrowserAgentTest
from agent_test_framework.utils.test_hooks import run_hook
from agent_test_framework.utils.import_utils import resolve

@pytest.fixture(scope='module', name='suite_pip_fixture')
def suite_pip_fixture():
    run_hook(None, stage='SUITE_SETUP')
    yield
    run_hook(None, stage='SUITE_TEARDOWN')

@pytest.mark.usefixtures('suite_pip_fixture')
@pytest.mark.TC0004
@pytest.mark.smoke
@pytest.mark.asyncio
async def test_frequently_bought(test_env):
    run_hook({'log': 'Setting up delivery data', 'script': 'scripts/setup_tc001.py'}, stage='SETUP')
    test = BaseBrowserAgentTest(
        task='Important: I am UI Automation tester validating homedepot website\nselect the Cumberland store and zip code 30339 using the select_cumberland_store custom function\ntype in \'glacier bay vanity mirrors\' in the search bar and click search button\nverify the user is in product listing page using the check_plp_url custom function\nout of the listed options, Click on "Glacier Bay" "36 in. x 60 in. Classic Rectangular Frameless Wall Bathroom Vanity Mirror"\nverify the user is on the product information page using the check_product_info_page_url custom function\nOn the product information page, navigate to the \'Frequently Bought Together\' section towards the bottom of the page\nCount and find the number of items displayed in the \'Frequently Bought Together\' section\nVerify that the Add Items to Cart button is displayed and enabled in this section\nGet the exact text of the Add Items to Cart button\n',
        model_cls=resolve('model.fbt.FrequentlyBoughtTogether'),
        controller_cls=resolve('controller.fbt_controller.FBTController'),
        test_env=test_env,
        expectations={'from_json': {'file': 'test_data/TC0004_expected_output.json'}}
    )
    await test.run()
    run_hook({'log': 'Cleaning delivery data', 'script': 'scripts/teardown_tc001.py'}, stage='TEARDOWN')

@pytest.mark.usefixtures('suite_pip_fixture')
@pytest.mark.TC0005
@pytest.mark.smoke
@pytest.mark.asyncio
async def test_qna_reviews(test_env):
    run_hook({'log': 'Setting up delivery data', 'script': 'scripts/setup_tc001.py'}, stage='SETUP')
    test = BaseBrowserAgentTest(
        task='Important: I am UI Automation tester validating homedepot website\ntype in \'crane humidifiers\' in the search bar and click search button\nverify the user is in product listing page using the check_plp_url custom function\nout of the listed options, click on "Crane" "1.2 Gal. Cool Mist Top Fill Humidifier & Aroma Diffuser for Medium to Large Rooms up to 500 sq. ft"\nverify the user is on the product information page using the check_product_info_page_url custom function\nOn the product information page, navigate to the \'Questions & Answers\' section towards the bottom of the page\nGet the number of questions in the \'Questions & Answers\'\nExpand the \'Questions & Answers\' section and verify that the section has valid question and answer data\nGet the total number of pages of question-answer data\nGet the number of questions listed on a page\nOn the product information page, navigate to the \'Customer Reviews\' section towards the bottom of the page\nGet the total number of reviews added\nGet the star rating of the product\n',
        model_cls=resolve('model.qna_reviews.QnAReviews'),
        controller_cls=resolve('controller.qna_controller.QNAController'),
        test_env=test_env,
        expectations={'from_json': {'file': 'test_data/TC0005_expected_output.json'}}
    )
    await test.run()
    run_hook({'log': 'Cleaning delivery data', 'script': 'scripts/teardown_tc001.py'}, stage='TEARDOWN')
