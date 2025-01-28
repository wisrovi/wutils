import sched
import time
from threading import Thread
from loguru import logger
from typing import Callable, Any


class PeriodicTask:
    def __init__(
        self,
        interval: float,
        function: Callable,
        verbose: bool = True,
        *args: Any,
        **kwargs: Any,
    ):
        """
        Initializes the periodic task.

        Args:
            interval (float): Time interval in seconds (must be positive).
            function (Callable): The function to execute periodically.
            verbose (bool): If True, enables detailed logging. Defaults to True.
            *args (Any): Positional arguments for the function.
            **kwargs (Any): Keyword arguments for the function.

        Raises:
            ValueError: If the interval is not a positive number.
        """
        if interval <= 0:
            raise ValueError("Interval must be a positive number.")
        self.interval = interval
        self.function = function
        self.verbose = verbose
        self.args = args
        self.kwargs = kwargs
        self.scheduler = sched.scheduler(
            time.time, time.sleep
        )  # Scheduler for periodic tasks
        self.thread = None
        self.running = False  # Indicator to control task execution

        # Configure loguru for logging
        logger.remove()  # Remove default handlers
        logger.add(
            sink=lambda msg: print(msg) if self.verbose else None,
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
            level="INFO" if self.verbose else "WARNING",
        )

    def _run_task(self) -> None:
        """
        Executes the periodic task and schedules the next execution.
        """
        if not self.running:
            return
        try:
            self.function(*self.args, **self.kwargs)  # Execute the function
        except Exception as e:
            logger.error(f"Error while executing the function: {e}")
        finally:
            # Reschedule the task if still running
            if self.running:
                self.scheduler.enter(self.interval, 1, self._run_task)

    def start(self) -> None:
        """
        Starts the periodic task in a separate thread.
        """
        if self.running:
            logger.warning("The task is already running.")
            return

        self.running = True
        logger.info(f"Starting periodic task every {self.interval} seconds.")
        self.thread = Thread(
            target=self._start_scheduler, daemon=True
        )  # Daemon thread to stop with the main program
        self.thread.start()

    def _start_scheduler(self) -> None:
        """
        Starts the scheduler for the periodic task.
        """
        self.scheduler.enter(0, 1, self._run_task)  # Schedule the first task execution
        self.scheduler.run()

    def stop(self) -> None:
        """
        Stops the periodic task.
        """
        if not self.running:
            logger.warning("The task is already stopped.")
            return

        self.running = False  # Stop the task execution
        self.scheduler.empty()  # Clear all scheduled tasks
        logger.info("Periodic task stopped.")
