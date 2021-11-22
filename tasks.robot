# ## Simple web scraper robot
# Opens a web page and stores some content.

*** Settings ***
Documentation     A simple web scraper robot.
...               Opens a website.
...               Stores the web page text in a file in the output directory.
...               Saves a screenshot of an element in the output directory.
Library           RPA.Browser.Selenium
Library           RPA.FileSystem

*** Tasks ***
Store Web Page Content
    Open Available Browser    https://robotframework.org/
    ${text}=    Get Text    css:body
    Create File    ${OUTPUT_DIR}${/}text.txt    ${text}    overwrite=True
    Screenshot    css:h1    ${OUTPUT_DIR}${/}screenshot.png
    [Teardown]    Close Browser
