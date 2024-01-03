# A simple web scraper example

The example task opens a web page, scrapes the web page for intended values and stores those values into a file.
The output will be stored in the "output" directory.

When run, the task will:

- Open a real web browser
- Navigate to `"https://finance.yahoo.com/crypto"`
- Brush off the Accept these Cookies pop-out.
- Detect if the targeted information is available - the Cryptocurrencies table
- Collect the Top 10 cryptocurrencies
- Pretty print them to the screen
- Save the collected data to a CSV file

## The Preparation

The `conda.yaml` file found in this project will contain the necessary python packages.
You'll find appropriate explanations or links.

The `robot.yaml` file found in this project will contain meta information that will configure the execution of the necessary tasks.

## The Main Task

The main robot file (`tasks.py`) contains the `task: web_scraper_top_10_crypto` your robot is going to complete when run.
This is indicated by the `@task` decorator that is imported from the `robocorp.tasks` library.

```python
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
    ...
```

The Python script doesn't need anything else to be executed with the `robocorp` library & CLI facilitators.
You can easily execute the `@task` using the [Robocorp Code VSCode Extension](https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code)

Find comments and helpful insights in the code itself.


When the `@task` finishes it's execution you can take a look inside the `output` folder and find different files related to the execution.
Be that log files, journals, but also the CSV output of the `@task`: `top-10-cryptos-(today's date).csv`

The screen output will look similar to this:
```
##################################################
### Top 10 Cryptocurrencies:
##################################################
### 1  | Bitcoin USD              | $ 42,383.66
### 2  | Ethereum USD             | $ 2,208.85
### 3  | Tether USDt USD          | $ 1.0007
### 4  | BNB USD                  | $ 304.37
### 5  | Solana USD               | $ 96.09
### 6  | XRP USD                  | $ 0.550529
### 7  | USD Coin USD             | $ 1.0002
### 8  | Lido Staked ETH USD      | $ 2,206.01
### 9  | Cardano USD              | $ 0.534951
### 10 | Avalanche USD            | $ 35.68
##################################################
```

> Note on creating locators: Simply put, a locator is an object constructed after a selector is executed.
> The selector value is usually pretty difficult to construct. As such, you can use the `Robocorp Web Inspector`
> from the [Robocorp Code VSCode Extension](https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code)
> to build valid selectors with ease.

## Summary

You executed a web scraper task, congratulations!

- How to set up a project and its dependencies
- How to define a task
- Use the `browser` library provided by `robocorp`
- Navigate to a new web page & wait for the load state
- Resolve intermediate steps before getting to the target content
- Ignore issues if elements are non existent
- Detect valid selectors by using the  `Robocorp Web Inspector` from [Robocorp Code VSCode Extension](https://marketplace.visualstudio.com/items?itemName=robocorp.robocorp-code)
- Wait and assert if the elements actually exist on the web page
- Scrape the values of the targeted elements
- Pretty print them to the screen output
- Save all to a CSV file
