from browser_use.browser.context import BrowserContext


async def select_store_zipcode(browser: BrowserContext, input_store_name: str, input_store_code: str, input_zip_code: str):
    try:
        print(f"---> In the select store function*********************")
        page = await browser.get_current_page()

        store_name = await page.locator('button[data-testid="my-store-button"] p').first.inner_text()
        print(f"---> Store name: {store_name}*********************")
        if store_name.strip() != input_store_name:
            # Open store selector
            await page.locator('[data-testid="StoreIcon"]').first.click()
            print(f"---> StoreIcon selected*********************")

            # 3. Wait for the drawer to open
            drawer = page.locator('[data-testid="header-drawer-content"]')
            await drawer.wait_for(state="attached", timeout=10000)
            await drawer.wait_for(state="visible", timeout=10000)


            input_box = drawer.locator('input[placeholder="ZIP Code, City, State, or Store #"]')
            await input_box.wait_for(state='visible')
            await input_box.fill(input_store_code)
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
            await page.wait_for_timeout(5000)
            store_element = await page.wait_for_selector('button[data-testid="my-store-button"] p')
            store_name = await store_element.inner_text()
            print(f"---> Store name selected now: {store_name}*********************")
        else:
            print(f"---> Required store {input_store_name} already selected *********************")

        zip_code = await page.locator('button[data-testid="delivery-zip-button"] p').first.inner_text()
        print(f"---> Zip code : {zip_code}*********************")
        if zip_code != input_zip_code:
            # Open store selector
            await page.locator('[data-testid="DeliveryIcon"]').first.click()
            print(f"---> Delivery Icon selected*********************")
            # 3. Wait for the drawer to open
            drawer = page.locator('[id="header-anchor-drawer"]')
            await drawer.wait_for(state="attached", timeout=10000)
            await drawer.wait_for(state="visible", timeout=10000)
            await drawer.locator('input[placeholder="Enter ZIP Code"]')
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
            print(f"{input_zip_code} already selected **************** ")
        if store_name.strip() != input_store_name or zip_code != input_zip_code:
            return False
        return True
    except Exception as e:
        print(f"---> Error in select_store: {e}")
        raise Exception(e)

