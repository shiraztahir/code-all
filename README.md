# All the code for Open Weather Map API Test Framework

The  Open Weather Map API() Test Framework consists of a library of python tests that are used to check the response of an API call to the server. It also runs basic system checks before calling API

## Usage
To run all the tests you just need to run the script ./run_tests. (`code/owm-api-tests/run_tests.py`). For running it from outside the directory, we can siply make simlink from `/usr/local/bin` to the desired location.
It is recommended to run it with a command line flag `'-v'` so that a detailed report can be seen. Please see below for details.

#### Options
There are a number of command line arguments that you can use:
`-h, --help` Print help text with the list of available options

`--tb` - this controls the error checking output if tests fail. 
Available options are:
 `'auto', 'long', 'short','no', 'line', 'native' `
 
 `-v, --verbose` - Output additional logging information
 
 `-q, --quiet` -   Reduce output verbosity
         
 
## Adding New Tests
To add a test you can either add a new file or a new test into an existing suite. The files and tests must be named such that they either start `test_...` or finish `..._test`.
To ensure execution ordering the convention chosen internally is to name files `1_*_test.py`. 
This literally means that the entire frameowrk is available, we just need to add the desired tests as per specific requirements. 

### Notes on Test Dependencies
The test framework should be robust to ensure it is reliable.
For this reason no tests should be accepted that rely on anything other than vanilla Python 3.6.5 (the default on Ubuntu 18.04) 

( TODO: If we decide to move on to making packages, these dependencies should be added to the package dependencies list.)

### Notes on Test Philosophy
The automated framework starts by checking internet connectivity and the health of open weather server by pinging it. If any of these fails, no further testing will be performed and the system will exit with an appropriate error message.
If connectivity is fine, tests will continue and will try fetching data from server via API calls. Exception handling was also considered while writing the tests. 
