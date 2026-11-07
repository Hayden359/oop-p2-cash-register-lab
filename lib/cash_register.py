#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discounts = []
        self.previous_transactions = []
        self.discount = discount

  def add_item(self, item_name, price, quantity=1):
    self.items.append((item_name, price, quantity))
    self.total += price * quantity

  def apply_discount(self, discount):
    self.discounts.append(discount)
    self.total -= discount

  def void_last_transaction(self):
    if self.items:
      last_item = self.items.pop()
      self.total -= last_item[1]
      self.previous_transactions.append(last_item)
