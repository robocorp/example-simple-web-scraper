from RPA.Browser.Selenium import Selenium
from RPA.FileSystem import FileSystem

browser = Selenium()
file_system = FileSystem()
url = "https://robotframework.org/"


def store_web_page_content():
    browser.open_available_browser(url)
    text = browser.get_text("scroller")
    file_system.create_file("output/text.txt", text, overwrite=True)
    browser.screenshot("css:.img-fluid", "output/screenshot.png")


def main():
    try:
        store_web_page_content()
    finally:
        browser.close_browser()


if __name__ == "__main__":
    main()


