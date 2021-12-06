from ..recent_checker import RecentChecker
from ..scheduler import Scheduler
from sqlalchemy import Column, func, Session
import abc


class SqlMixin(Scheduler, RecentChecker):
    def __init__(self, interval: float, time_col: Column, db: Session, flush=True):
        super().__init__()

        self.interval = interval
        self.time_col = time_col
        self.db = db
        self.flush = flush
    
    def write(self, timestamp: float, callback_result):
        self.db.add(callback_result)
        
        if self.flush:
            self.db.flush()

        return

    @abc.abstractmethod
    def before_write(timestamp: float):
        """Returns a new table row"""
        pass

    def get_newest_timestamp(self) -> float:
        return func.max(self.time_col)