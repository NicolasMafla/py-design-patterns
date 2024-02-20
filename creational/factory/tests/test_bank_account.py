from creational.factory.bank_account import SavingsAccount, CheckingAccount, BankAccountFactory


def test_savings_account():
    account = SavingsAccount(name="Nico", balance=1000, cashback_rate=0.01)
    assert account.balance == 1000

    account.withdraw(amount=250)
    assert account.balance == 750

    account.deposit(amount=100)
    assert account.balance == 851


def test_bank_account_factory():
    factory = BankAccountFactory()
    account1 = factory.create_account(
        account_type="savings",
        name="Nico",
        balance=1000,
        cashback_rate=0
    )
    account2 = factory.create_account(
        account_type="checking",
        name="Nico",
        balance=1000,
        max_overdraft_rate=0
    )
    assert isinstance(account1, SavingsAccount)
    assert isinstance(account2, CheckingAccount)
