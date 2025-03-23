Certainly! Here is the content again in Markdown format:

```markdown
# Python Command Line Arguments and Environment Variables

## Python Command Line Arguments

**Command line arguments** are parameters passed to a Python script when executed from the terminal or command prompt. These arguments can be used to customize the behavior of the script without modifying its source code. Python provides a module called `sys` to handle command line arguments.

- **`sys.argv`** is a list in Python that contains the command line arguments passed to a script. The first element (`sys.argv[0]`) is always the name of the script itself, and the subsequent elements are the arguments passed to it.

### Example of Python Command Line Arguments:

Consider a Python script named `greet.py`:

```python
import sys

# Checking if the script has been passed any arguments
if len(sys.argv) < 2:
    print("Usage: python greet.py <name>")
else:
    name = sys.argv[1]  # The first argument after the script name
    print(f"Hello, {name}!")
```

- Save this code in a file named `greet.py`.
- Now, run this script from the command line like this:

  ```bash
  python greet.py John
  ```

**Output:**

```
Hello, John!
```

If no argument is passed, it will show the usage instruction:

```bash
python greet.py
```

**Output:**

```
Usage: python greet.py <name>
```

## Python Environment Variables

**Environment variables** are variables that are set in the operating system, and they provide a way for scripts to access configuration information and system properties. These variables can store information like system paths, user configurations, or sensitive credentials (such as API keys).

In Python, environment variables can be accessed using the `os` module.

- **`os.environ`** is a dictionary that allows you to access and modify environment variables.

### Example of Python Environment Variables:

```python
import os

# Accessing an environment variable
home_directory = os.environ.get("HOME")
print(f"Your home directory is: {home_directory}")

# Setting an environment variable
os.environ["MY_VARIABLE"] = "some_value"

# Retrieving the newly set environment variable
print(f"My custom variable is: {os.environ['MY_VARIABLE']}")
```

In the example above:
- The `os.environ.get("HOME")` retrieves the value of the `HOME` environment variable (which contains the user's home directory in Unix-like systems).
- The `os.environ["MY_VARIABLE"] = "some_value"` sets a custom environment variable.

**Note**: When running the script, you may not see permanent changes to the environment variables unless explicitly exported or set globally for the system session.

### Setting Environment Variables in Command Line:

Before running the Python script, you can set an environment variable in the command line.

**Linux/Mac:**

```bash
export MY_VAR="hello"
python script.py
```

**Windows Command Prompt:**

```cmd
set MY_VAR=hello
python script.py
```

In the Python script, you can then access this value with:

```python
import os

print(os.environ.get("MY_VAR"))
```

## Summary

- **Command Line Arguments**: Values passed when running a Python script from the command line that help customize the script's behavior.
- **Environment Variables**: System-wide settings that are accessible by Python, often used for configurations or sensitive data.
```

