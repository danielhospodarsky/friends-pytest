import pytest
from oop_loan_pmt import *

# Define unit tests for Loan class methods
def test_get_discount_factor():
    loan = oop_loan_pmt.Loan(100000, 30, 0.06)
    loan.discountFactor = 10
    assert loan.getDiscountFactor() == 10

def test_calculate_discount_factor():
    loan = oop_loan_pmt.Loan(100000, 30, 0.06)
    loan.calculateDiscountFactor()
    assert loan.discountFactor == (((1.0 + (0.06 / 12)) ** (30 * 12)) - 1.0) / ((0.06 / 12) * (1.0 + (0.06 / 12)) ** (30 * 12))

def test_calculate_loan_pmt():
    loan = oop_loan_pmt.Loan(100000, 30, 0.06)
    loan.calculateLoanPmt()
    assert loan.loanPmt == 599.55

def test_get_loan_pmt():
    loan = oop_loan_pmt.Loan(100000, 30, 0.06)
    loan.loanPmt = 500
    assert loan.getLoanPmt() == 500

# Define functional test for entire script
def test_collect_loan_details(monkeypatch):
    # Set up user input
    inputs = ["100000", "30", "0.06"]

    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    # Call function and check output
    loan = oop_loan_pmt.collectLoanDetails()
    assert loan.loanAmount == 100000
    assert loan.numberOfPmts == 360
    assert loan.periodicIntRate == 0.005
    assert loan.discountFactor == 0
    assert loan.loanPmt == 0

def test_main(monkeypatch, capsys):
    # Set up user input
    inputs = ["100000", "30", "0.06"]

    # Mock user input
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    # Call function and check output
    oop_loan_pmt.main()
    captured = capsys.readouterr()
    assert captured.out == "Your monthly payment is: $599.55\n"