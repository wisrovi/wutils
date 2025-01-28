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
