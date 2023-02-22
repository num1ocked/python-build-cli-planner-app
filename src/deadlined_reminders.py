from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable

class DeadlineMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(Iterable, ABC):
    @abstractmethod
    def is_due(self):
        pass