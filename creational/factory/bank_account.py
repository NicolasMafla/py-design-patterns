from abc import ABC, abstractmethod
from pydantic import UUID4
from uuid import uuid4


class BankAccountInterface(ABC):

    def __init__(self, name: str, balance: float):
        self._account_number: UUID4 = uuid4()
        self._name: str = name
        self._balance: float = balance

    @property
    def balance(self) -> float:
        return self._balance

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def deposit(self, amount: float) -> None:
        raise NotImplementedError


class SavingsAccount(BankAccountInterface):
    def __init__(self, name: str, balance: float, cashback_rate: float):
        super().__init__(name=name, balance=balance)
        self._cashback_rate = cashback_rate

    def withdraw(self, amount: float) -> None:
        self._balance -= amount

    def deposit(self, amount: float) -> None:
        self._balance += amount * (1 + self._cashback_rate)


class CheckingAccount(BankAccountInterface):
    def __init__(self, name: str, balance: float, max_overdraft_rate: float):
        super().__init__(name=name, balance=balance)
        self._max_overdraft_rate = max_overdraft_rate

    def withdraw(self, amount: float) -> None:
        self._balance -= amount

    def deposit(self, amount: float) -> None:
        self._balance += amount


class BankAccountFactory:
    IMPLEMENTATIONS = {
        "savings": SavingsAccount,
        "checking": CheckingAccount
    }

    def create_account(self, account_type: str, **kwargs) -> BankAccountInterface:
        return self.IMPLEMENTATIONS.get(account_type)(**kwargs)
