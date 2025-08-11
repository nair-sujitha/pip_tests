from agent_test_framework.controller.basecontroller import BaseController
from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
import allure
from utils.store_selector import select_store_zipcode

from agent_test_framework.utils.decorators import action


class DeliveryController(BaseController):

    @action("verify the user is in product listing page")
    async def check_plp_url(self, browser: BrowserContext):
        try:
            page = await browser.get_current_page()
            product_listing_page_url = page.url
            print(f"---> The PLP url is {product_listing_page_url}")
            return ActionResult(extracted_content=f"PLP url {product_listing_page_url}")
        except Exception as e:
            allure.attach(body="Unexpected error/exception in Custom Controller action check_plp_url",
                          name="Error log",
                          attachment_type=allure.attachment_type.TEXT)
            return ActionResult(extracted_content="ABORT: Critical Error. Stop the task now",
                                include_in_memory=True,
                                error="Error",
                                success=False)

    @action("verify the user is on the product information page")
    async def check_product_info_page_url(self, browser: BrowserContext):
        try:
            page = await browser.get_current_page()
            product_information_page_url = page.url
            print(f"---> The PIP url is {product_information_page_url}")
            return ActionResult(extracted_content=f"PIP url: {product_information_page_url}")
        except Exception as e:
            allure.attach(body="Unexpected error/exception in Custom Controller action check_plp_url",
                          name="Error log",
                          attachment_type=allure.attachment_type.TEXT)
            return ActionResult(extracted_content="ABORT: Critical Error. Stop the task now",
                                include_in_memory=True,
                                error="Error",
                                success=False)

    @action("select the Cumberland store and zip code 30339")
    async def select_cumberland_store(self, browser: BrowserContext):
        try:
            is_store_zip_code_selected \
                = await select_store_zipcode(browser,
                                         "Cumberland",
                                         "0121",
                                         "30339")
            print(f"result from select store function {is_store_zip_code_selected}")
            if not is_store_zip_code_selected:
                allure.attach(body="Unexpected error/exception in Custom Controller action select_cumberland_store",
                              name="Error log",
                              attachment_type=allure.attachment_type.TEXT)
                return ActionResult(extracted_content="ABORT: Critical Error. "
                                                      "The right store and zip code could not get selected. "
                                                      "Stop the task now",
                                    include_in_memory=True,
                                    error="Error",
                                    success=False)
            else:
                return ActionResult(
                    extracted_content=f"The store name is Cumberland and zip code is 30339"
                )
        except Exception as e:
            print(f"---> Error in select_store: {e}")
            allure.attach(body="Unexpected error/exception in Custom Controller action select_cumberland_store",
                          name="Error log",
                          attachment_type=allure.attachment_type.TEXT)
            return ActionResult(extracted_content="ABORT: Critical Error. Stop the task now",
                                include_in_memory=True,
                                error="Error",
                                success=False)

