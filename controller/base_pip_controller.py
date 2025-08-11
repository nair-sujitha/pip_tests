from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
import allure

from agent_test_framework.controller.basecontroller import BaseController
from agent_test_framework.utils.decorators import action



class BasePIPController(BaseController):

    @action("select the Cumberland store and zip code 30339")
    async def select_cumberland_store(self, browser: BrowserContext):
        try:
            print(f"---> In the select store function*********************")
            page = await browser.get_current_page()

            store_name = await page.locator('button[data-testid="my-store-button"] p').first.inner_text()
            print(f"---> Store name: {store_name}*********************")
            if store_name.strip() != "Cumberland":
                # Open store selector
                await page.locator('[data-testid="StoreIcon"]').first.click()
                print(f"---> StoreIcon selected*********************")

                # 3. Wait for the drawer to open
                drawer = page.locator('[data-testid="header-drawer-content"]')
                await drawer.wait_for(state="attached", timeout=10000)
                await drawer.wait_for(state="visible", timeout=10000)


                input_box = drawer.locator('input[placeholder="ZIP Code, City, State, or Store #"]')
                await input_box.wait_for(state='visible')
                await input_box.fill("0121")
                print(f"---> Filled store code*********************")
                await drawer.locator('[data-testid="SearchIcon"]').first.click()
                print(f"---> search icon clicked selected*********************")

                # 6. Wait for search results to load (Cumberland)
                store_link = drawer.locator('a[href="/l/Cumberland/GA/Atlanta/30339/121"]')
                await store_link.wait_for(state='visible')
                print(f"---> href shown*********************")
                # Then click it
                await store_link.click()
                print(f"---> href selected*********************")

                await page.wait_for_selector('button[data-testid="store-pod-localize__button"]')
                print(f"---> waitign for shop for store selected*********************")
                await page.locator('button[data-testid="store-pod-localize__button"]').first.click()
                print(f"---> shop at store  selected*********************")
                await page.wait_for_timeout(2000)
                store_element = await page.wait_for_selector('button[data-testid="my-store-button"] p')
                store_name = await store_element.inner_text()
                print(f"---> Store name selected now: {store_name}*********************")
            else:
                print(f"---> Cumberland already selected *********************")

            zip_code = await page.locator('button[data-testid="delivery-zip-button"] p').first.inner_text()
            print(f"---> Zip code : {zip_code}*********************")
            if zip_code != "30339":
                # Open store selector
                await page.locator('[data-testid="DeliveryIcon"]').first.click()
                print(f"---> Delivery Icon selected*********************")
                # 3. Wait for the drawer to open
                drawer = page.locator('[id="header-anchor-drawer"]')
                await drawer.wait_for(state="attached", timeout=10000)
                await drawer.wait_for(state="visible", timeout=10000)
                await drawer.wait_for_selector('input[placeholder="Enter ZIP Code"]')
                print(f"---> input zip code  showing *********************")
                await drawer.fill('input[placeholder="Enter ZIP Code"]', "30339")
                print(f"---> Filled zip code*********************")
                await drawer.locator('[data-testid="SearchIcon"]').first.click()
                print(f"---> search icon clicked selected*********************")
                await page.wait_for_timeout(2000)
                zip_code_element = await page.wait_for_selector('button[data-testid="delivery-zip-button"] p')
                zip_code = await zip_code_element.inner_text()
                print(f"---> Zip code selected now: {zip_code}*********************")
            else:
                print(f"30339 already selected **************** ")
            if store_name.strip() != "Cumberland" or zip_code != "30339":
                return ActionResult(extracted_content="ABORT: Critical Error. "
                                                      "The right store and zip code could not get selected. "
                                                      "Stop the task now",
                                    include_in_memory=True,
                                    error="Error",
                                    success=False)
            return ActionResult(
                extracted_content=f"The store name is {store_name} and zip code is {zip_code}"
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

    @action("verify the user is in product listing page")
    async def check_plp_url(self, browser: BrowserContext):
        try:
            page = await browser.get_current_page()
            product_listing_page_url = page.url
            print(f"---> The PLP url is {product_listing_page_url}")
            if product_listing_page_url.startswith("https://www.homedepot.com/s/")\
                    or product_listing_page_url.startswith("https://www.homedepot.com/b/"):
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
            if product_information_page_url.startswith("https://www.homedepot.com/p/"):
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

