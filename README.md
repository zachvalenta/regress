# 👋 TLDR

This is a repo to sort out how various types of regression work.

# 🎛️ USAGE

> [!NOTE]
> All commands are runnable via the `Makefile`; just run `make` to see the documentation

```sh
$ make

======================================================================

🚀  MAIN

run:       run app

📦 DEPENDENCIES

env:        show environment info
deps:       list prod dependencieso

======================================================================
```

# WORKLOG

## prompt

I want to create some toy regressions in Python. I want to plot these using plotext.

Scenario:
* you have a cafe
* linear regression: orders of iced tea to the weather that day
* multiple linear regression: orders of iced tea, the daily weather, price of iced tea, number of office workers in a 5-block radius

## completion

Want to adjust any parameters like:
* Amount of noise in the data?
* Baseline number of orders?
* Temperature response effect?
* Or try a non-linear relationship instead?
