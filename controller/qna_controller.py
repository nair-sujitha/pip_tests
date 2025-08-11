from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
import allure

from agent_test_framework.controller.basecontroller import BaseController
from agent_test_framework.utils.decorators import action



class QNAController(BaseController):

    @action("verify the user is in product listing page")
    async def check_plp_url(self, browser: BrowserContext):
        try:
            page = await browser.get_current_page()
            product_listing_page_url = page.url
            print(f"---> The PLP url is {product_listing_page_url}")
            if product_listing_page_url.startswith("https://www.homedepot.com/s/crane%20humidifiers"):
                return ActionResult(extracted_content=f"PLP url {product_listing_page_url}")
            else:
                return ActionResult(extracted_content="ABORT: Critical Error. Stop the task now. The PLP page is not shown",
                                    include_in_memory=True,
                                    error="Error",
                                    success=False)
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
            if product_information_page_url.startswith("https://www.homedepot.com/p/Crane-1-2-Gal-Cool-Mist-Top-Fill-Humidifier-Aroma-Diffuser-for-Medium-to-Large-Rooms-up-to-500-sq-ft-EE-6909/313217837"):
                return ActionResult(extracted_content=f"PIP url {product_information_page_url}")
            else:
                return ActionResult(extracted_content="ABORT: Critical Error. Stop the task now. The PIP page is not shown",
                                    include_in_memory=True,
                                    error="Error",
                                    success=False)
        except Exception as e:
            allure.attach(body="Unexpected error/exception in Custom Controller action check_plp_url",
                          name="Error log",
                          attachment_type=allure.attachment_type.TEXT)
            return ActionResult(extracted_content="ABORT: Critical Error. Stop the task now",
                                include_in_memory=True,
                                error="Error",
                                success=False)

