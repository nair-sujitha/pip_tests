import pytest
from agent_test_framework.core.base_test import BaseBrowserAgentTest
from agent_test_framework.utils.test_hooks import run_hook
from agent_test_framework.utils.import_utils import resolve

@pytest.fixture(scope='module', name='suite_delivery_fixture')
def suite_delivery_fixture():
    run_hook(None, stage='SUITE_SETUP')
    yield
    run_hook(None, stage='SUITE_TEARDOWN')

@pytest.mark.usefixtures('suite_delivery_fixture')
@pytest.mark.TC0001
@pytest.mark.smoke
@pytest.mark.asyncio
async def test_delivery_check(test_env):
    run_hook({'log': 'Setting up delivery data', 'script': 'scripts/setup_tc001.py'}, stage='SETUP')
    test = BaseBrowserAgentTest(
        task="Important: I am UI Automation tester validating homedepot website\nselect the Cumberland store and zip code 30339 using the select_cumberland_store custom function\ntype in 'claw hammer' in the search bar and click search button\nverify the user is in product listing page using the check_plp_url custom function\nClick on DEWALT 20 oz. Steel Rip Claw Nailing Hammer\nverify the user is on the product information page using the check_product_info_page_url custom function\nverify that the fulfillment 'Pickup Nearby' is available\nverify that the fulfillment 'Delivery' is available\nverify Delivery is free\n",
        model_cls=resolve('model.delivery.Delivery'),
        controller_cls=resolve('controller.delivery_controller.DeliveryController'),
        test_env=test_env,
        expectations={'is_delivery_available': {'type': 'equals', 'value': True}, 'is_pickup_nearby_available': {'type': 'equals', 'value': True}}
    )
    await test.run()
    run_hook({'log': 'Cleaning delivery data', 'script': 'scripts/teardown_tc001.py'}, stage='TEARDOWN')
