# THE2-Tester
Simple automated test script for METU Ceng Homework (THE 2)

# Installation
Save test.py file to the folder which the2.py is saved

# Usage
cd to folder which the2.py and test.py is saved

Then run command: 
```
python test.py 
```
Or (in some cases)
```
python2 test.py 
```

# Options
Options can be changed by two way: By changing directly from the source file or By passing cli arguments. Additional information section describes first way. This section describes the second one.

## There are 3 CLI option right now
- By default, whole test log will be shown (Both fails and passes). This can be disabled using: -fo or --fails-only
- By default, minority shapes used in test will be shown. This can be disabled using:  -nms or --no-minority-shapes
- By default, calculations from your function will be shown. This can be disabled using:  -nci or --no-calculated-input

Example usage with cli options
```
python2 test.py -fo --no-minority-shapes
```
The command above will print only fails and will not print minority shapes used in the test

# Additional Information
Some tests can be disabled, and some additional information can be displayed or ignored. Those options can be changed by editing test.py. Information needed to change settings can be found inside test.py, and in comments

# Contribution
Anyone can fork this repo, edit content of test.py, add more tests, add more functionality. After doing so commit your changes and open a pull request. I will merge them after reviewing :)

# Good Luck Everyone :)
