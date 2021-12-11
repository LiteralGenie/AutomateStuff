from sqlalchemy import Column, func
from sqlalchemy.orm import Session
import abc, typing


class SqlMixin:
    interval: float

    def __init__(
        self, interval: float, time_col: Column, db: Session, *args,
        flush=True, **kwargs
    ):
        super().__init__(*args, **kwargs)

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
    def before_write(timestamp: float) -> typing.Any:
        """Returns a new table row"""
        pass

    def get_newest_timestamp(self) -> float:
        expr = func.max(self.time_col)
        query = self.db.query(expr)
        result = query.scalar()
        return result or 0