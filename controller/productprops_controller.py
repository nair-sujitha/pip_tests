from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext

from agent_test_framework.controller.basecontroller import BaseController
from agent_test_framework.utils.decorators import action
import allure


class ProductPropsController(BaseController):

    @action("verify the user is on the product information page")
    async def check_product_info_page_url(self, browser: BrowserContext):
        try:
            page = await browser.get_current_page()
            product_information_page_url = page.url
            print(f"---> The PIP url is {product_information_page_url}")
            return ActionResult(
                extracted_content=f"PIP url: {product_information_page_url}"
            )
        except Exception as e:
            allure.attach(body="Unexpected error/exception in Custom Controller action check_plp_url",
                          name="Error log",
                          attachment_type=allure.attachment_type.TEXT)
            return ActionResult(extracted_content="ABORT: Critical Error. Stop the task now",
                                include_in_memory=True,
                                error="Error",
                                success=False)
