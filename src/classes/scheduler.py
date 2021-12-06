import abc, typing


class Scheduler(abc.ABC):
    """Periodically inserts new data into a dataset"""

    @abc.abstractmethod
    def check_and_insert(self) -> typing.Any:
        """Insert data if necessary. Otherwise, return falsey value."""
        pass

    @abc.abstractmethod
    def write(self, timestamp: float, callback_result: typing.Any = None) -> None:
        """Add timestamp to data"""
        pass

    def before_write(timestamp: float):
        """Return value is supplied to self.write()"""
        pass