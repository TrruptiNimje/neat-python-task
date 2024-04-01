Report input generator
==============================

This is a Python application for generating report inputs.


Requirements
---------------

You need to process a pair of differently delimited string inputs to determine the parameters for generating a report. The report itself is outside of the scope of this task.

Given one input like:

    "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox"

And another input like:

    "Frog  apple    fox cat fish fish"

Find the set of common elements in the two inputs (case-insensitive). Return them as a unique list of lower case strings. Do not include partial matches (e.g. "pineapple" and "apple")

Setup
---------------

From this folder, install the stub of the `reportinput` Python package you will develop using the following `pip` command:

    pip install -e .

Tips
---------------

- Stubs have been created for you under the `src` and `test` directories
- Feel free to totally change any of the stubs - they are only there to help get you started.
- Adequate solutions to the problem will include a number of meaningful unit tests
- Don't hesitate to use an external library if you see fit
