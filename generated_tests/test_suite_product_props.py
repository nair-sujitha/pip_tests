import pytest
from agent_test_framework.core.base_test import BaseBrowserAgentTest
from agent_test_framework.utils.test_hooks import run_hook
from agent_test_framework.utils.import_utils import resolve

@pytest.fixture(scope='module', name='suite_product_props_fixture')
def suite_product_props_fixture():
    run_hook({'log': 'Setting up the prod props test suite', 'script': 'scripts/setup_suite.py'}, stage='SUITE_SETUP')
    yield
    run_hook({'log': 'Cleaning up prod props test suite', 'script': 'scripts/teardown_suite.py'}, stage='SUITE_TEARDOWN')

@pytest.mark.usefixtures('suite_product_props_fixture')
@pytest.mark.TC0002
@pytest.mark.dev
@pytest.mark.asyncio
async def test_product_price_check_HDPP_1(test_env):
    run_hook(None, stage='SETUP')
    test = BaseBrowserAgentTest(
        task='Important: I am UI Automation tester validating homedepot website\nType in \'flocked pre lit christmas trees\' in the search bar and click search button\nfrom the listed options, select - "Puleo International" "7.5 ft. Prelit Incandescent Aspen Green Fir Flocked Artificial Christmas Tree with 700 UL Clear Lights"\nverify the user is on the product information page using the custom function check_product_info_page_url\nget the price of the product\nverify that the product has a Home Depot Protection Plan by Allstate for 2 Year priced at $19\n',
        model_cls=resolve('model.product_props.ProductProps'),
        controller_cls=resolve('controller.productprops_controller.ProductPropsController'),
        test_env=test_env,
        expectations={'from_json': {'file': 'test_data/TC0002_expected_output.json'}}
    )
    await test.run()
    run_hook(None, stage='TEARDOWN')

@pytest.mark.usefixtures('suite_product_props_fixture')
@pytest.mark.TC0003
@pytest.mark.dev
@pytest.mark.smoke
@pytest.mark.asyncio
async def test_product_price_delivery_check(test_env):
    run_hook(None, stage='SETUP')
    test = BaseBrowserAgentTest(
        task="Important: I am UI Automation tester validating homedepot website\nType in 'JUST ADD ICE ORCHIDS' in the search bar and click search button\nfrom the listed options, select - Just Add Ice Premium Orchid (Phalaenopsis) Watercolor Blue Plant in 5 in. White Ceramic Pottery\nget the price of the product\nverify Delivery is free\n",
        model_cls=resolve('model.product_props.ProductProps'),
        controller_cls=resolve('browser_use.controller.service.Controller'),
        test_env=test_env,
        expectations={'from_json': {'file': 'test_data/TC0003_expected_output.json'}}
    )
    await test.run()
    run_hook(None, stage='TEARDOWN')
