# Examples

This directory contains a collection of examples that demonstrate the usage of various modules and functionalities in this project. Each subfolder corresponds to a specific module and includes example scripts to help you understand how to use that module.

## Directory Structure

The examples are organized as follows:

```
examples/
    periodic_task/
        one_task.py
```

## How to Use

1. Navigate to the module folder of interest, e.g., `examples/module1/`.
2. Open the `README.md` in that folder to get detailed information about the examples.
3. Run the scripts directly using:
   ```bash
   python example1.py
   ```

## Modules and Examples

### periodic_task

#### Description
This module demonstrates specific functionalities.


- **one_task.py**: Example demonstrating functionality.
 ```python
import time
from wutils.periodic_task import PeriodicTask


def my_firts_periodic_function():
    print("Running my_firts_periodic_function task...")


def my_second_periodic_function():
    print("Running my_second_periodic_function task...")


# Create the periodic task with a 5-second interval and verbose logging enabled
task = PeriodicTask(5, my_firts_periodic_function, verbose=True)

# Start the task
task.start()

# Wait for some time and stop the task
time.sleep(15)
task.stop()

# Create another task with verbose logging disabled
silent_task = PeriodicTask(2, my_second_periodic_function, verbose=False)
silent_task.start()
time.sleep(10)
silent_task.stop()
  ```


