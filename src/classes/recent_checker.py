import abc


class RecentChecker(abc.ABC):
    """Abstract mixin for schedulers that only check the most recent timestamp"""

    interval: float

    @abc.abstractmethod
    def get_newest_timestamp(self) -> float:
        pass