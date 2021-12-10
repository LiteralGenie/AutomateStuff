from .recent_checker import RecentChecker
from .scheduler import Scheduler
import itertools, time


class FixedScheduler(Scheduler, RecentChecker):
    """
    Insert new data at a fixed interval after the newest timestamp. 
    This is repeated while the timestamp-to-add is less than the current time.
    """

    def check_and_insert(self) -> list[float]:
        now = time.time()
        newest = self.get_newest_timestamp()

        intervals = (newest + i*self.interval for i in itertools.count(start=1))
        timestamps = itertools.takewhile(lambda ts: ts <= now, intervals)

        for ts in timestamps:
            print(ts)
            self.write(timestamp=ts, callback_result=self.before_write(ts))

        return timestamps
