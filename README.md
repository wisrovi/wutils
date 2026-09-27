<p align="center">
  <a href="https://pypi.org/project/wutils/"><img src="https://img.shields.io/pypi/v/wutils?style=for-the-badge&logo=pypi&color=3b82f6" alt="PyPI version" /></a>
  <a href="https://linkedin.com/in/wisrovi-rodriguez"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://wisrovi.dev"><img src="https://img.shields.io/badge/Author-wisrovi.dev-111827?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Portal" /></a>
  <a href="https://orcid.org/0009-0005-0710-1861"><img src="https://img.shields.io/badge/ORCID-0009--0005--0710--1861-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License" /></a>
</p>

# Wutils

**WRedis** is a library for specific functions for various Python projects.

# Description

WRedis simplifies code reuse in Python projects. The library offers a number of modules that make using modules easier and simpler.

## Installation

To install the library, use `pip`:

```bash
pip install wutils
```

# Description

The **wutils** library offers a number of general-purpose modules.

# License

MIT

This project is licensed under the MIT License. See the ```LICENSE``` file for details.





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

---

## 👤 Autor & Afiliación Oficial

* **William Steve Rodriguez Villamizar (Wisrovi)**
* **Cargo:** Principal AI Engineer & Applied AI Solutions Architect | Scientific Researcher
* 📧 **Email:** [wisrovi.rodriguez@gmail.com](mailto:wisrovi.rodriguez@gmail.com)
* 🌐 **Portal Oficial:** [wisrovi.dev](https://wisrovi.dev)
* 💼 **LinkedIn:** [wisrovi-rodriguez](https://www.linkedin.com/in/wisrovi-rodriguez/)
* 🆔 **ORCID:** [0009-0005-0710-1861](https://orcid.org/0009-0005-0710-1861)
* 📦 **PyPI:** [pypi.org/user/wisrovi/](https://pypi.org/user/wisrovi/)
* 🐙 **GitHub:** [@wisrovi](https://github.com/wisrovi)
