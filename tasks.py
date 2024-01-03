from robocorp import browser
from robocorp.tasks import task

from datetime import date


@task
def web_scraper_top_10_crypto() -> None:
    """
    Automate web scraping for the current Top 10 Cryptocurrency.
    Output would be printed out in this format:
        ##################################################
        ### Top 10 Cryptocurrencies:
        ##################################################
        ### 1  | Bitcoin USD              | $ 44,853.27
    Output will also be saved in a CSV file in the output folder.
    ---------------------------
    The Robocorp Web Inspector was used to generate the locator values/selectors/identifiers.
    """
    try:
        # initialize the browser and a new webpage
        page = browser.page()
        # moving to Yahoo Finance
        page.goto("https://finance.yahoo.com/crypto")
        page.wait_for_load_state()

        # make sure we get rid of the cookies permission popup
        try:
            reject_cookies = page.locator("[name=reject]")
            reject_cookies.click()
        except Exception:
            pass
        # ignore any issues if the popup doesn't show up

        # wait for the page to actually show the target table
        crypto_table = page.locator(
            "xpath=//span[contains(.,'Matching Cryptocurrencies')]"
        )
        crypto_table.wait_for(timeout=5000, state="visible")
        # making sure the element is visible
        assert crypto_table.is_visible()

        # scrape the web page and extract the top 10 crypto currencies
        print("#" * 50)
        print("### Top 10 Cryptocurrencies:")
        print("#" * 50)
        csv_content = ["Index,Crypto,Value"]
        for index in range(1, 11):
            # get 1st cell in first row - it contains the name of the crypto ticker
            crypto = page.locator(f".simpTblRow:nth-child({index}) > .Px\(10px\)")
            # make sure the element is visible
            crypto.wait_for(timeout=5000, state="visible")
            # making sure the element is visible
            assert crypto.is_visible()
            # grab the value
            crypto_ticker = crypto.inner_text()

            # get 2rd cell in first row - it contains the name of the crypto ticker
            crypto = page.locator(
                f".simpTblRow:nth-child({index}) > .Va\(m\):nth-child(3)"
            )
            crypto.wait_for(timeout=5000, state="visible")
            assert crypto.is_visible()
            crypto_value = crypto.inner_text()

            # save the content to the csv
            csv_content.append(f'{index},{crypto_ticker},"{crypto_value}"')

            # calculate how to space things to have a table look
            i_spaces = 3 - len(str(index))
            tab_spaces = 25 - len(crypto_ticker)
            print(
                f"### {index}{' '*i_spaces}| {crypto_ticker}{' '*tab_spaces}| $ {crypto_value}"
            )
        print("#" * 50)

        # save the CSV file to output folder
        csv_file = f"output/top-10-cryptos-{date.today()}.csv"
        print(f"### Saving to the CSV file: {csv_file}")
        with open(csv_file, mode="w") as csv:
            csv.writelines([line + "\n" for line in csv_content])
        print("### Done!")

    finally:
        browser.context().close()
        browser.browser().close()
