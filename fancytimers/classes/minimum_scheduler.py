from .recent_checker import RecentChecker
from .scheduler import Scheduler
import time


class MinimumScheduler(Scheduler, RecentChecker):
    """
    Insert a single data entry if the most recent timestamp is greater than or equal to a given interval.
    """

    def check_and_insert(self) -> float | None:
        now = time.time()
        newest = self.get_newest_timestamp()
        dist = now - newest

        if dist >= self.interval:
            self.write(timestamp=now, callback_result=self.before_write(now))
            return now

        return None