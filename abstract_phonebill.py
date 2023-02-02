from abc import abstractmethod
from typing import TypeVar, List, final

from cis301.phonebill.abstract_phonecall import AbstractPhoneCall


class AbstractPhoneBill:
    """
     This abstract class represents a customer's phone bill that
     consists of multiple phone calls.
    """
    @abstractmethod
    def get_customer(self) -> str:
        pass

    @abstractmethod
    def add_phonecall(self, phonecall):
        """
         Adds a phone call to this phone bill
        """
        pass

    T = TypeVar(AbstractPhoneCall)
    @abstractmethod
    def get_phonecalls(self) -> List[T]:
        pass

    @final
    def __str__(self) -> str:
        """
         Returns:
              a brief textual description of this phone bill
        """
        return self.get_customer() + "'s phone bill with " + len(self.get_phonecalls()) + " phone calls"

