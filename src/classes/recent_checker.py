import abc


class RecentChecker(abc.ABC):
    """Abstract mixin for schedulers that only check the most recent timestamp"""

    @abc.abstractmethod
    def get_newest_timestamp(self) -> float:
        pass

    @abc.abstractmethod
    @property
    def interval(self) -> float:
        """How long to wait before inserting new data"""
        pass