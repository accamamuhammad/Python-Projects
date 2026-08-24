# Python Projects

Small practice projects built while learning Python, following Bro Code's YouTube series — covering core fundamentals through object-oriented programming. Each project below combines a handful of concepts to help cement them.

**Concepts covered across these projects:**
Variables & Type Casting · User Input · Math Operators · If/Elif/Else · Loops (While & For) · Nested Loops · Lists, Sets & Dictionaries · String Methods & Slicing · Format Specifiers · Membership Operators (`in`) · Functions (Default Args, Global Variables) · Random Module · Classes & `__init__` · Instance Methods · Inheritance & `super()` · Method Overriding / Polymorphism · Abstract Classes · Duck Typing · Aggregation · Nested Classes

---

## Shopping Cart
**Concepts:** Dictionaries, Functions, While Loops, Membership Operators (`in`), Format Specifiers

A cart system storing items as a dictionary of dictionaries (`{name: {price, quantity}}`). Menu-driven add/remove/checkout loop, with a formatted itemized receipt showing subtotal, tax, and total.

---

## Credit Card Validator
**Concepts:** String Slicing, String Reversal, Loops, Math, Modulo Operator

Implements the Luhn algorithm to validate a credit card number: reverses the digit string, sums digits at odd/even positions with doubling and digit-sum rules on even positions, then checks if the total is divisible by 10.

---

## Python Banking Program
**Concepts:** Functions, Global Variables, While Loops, Input Validation, Password Protection, Format Specifiers

A menu-driven bank account simulator with password-gated deposits and withdrawals, account-number and bank-name validation for transfers, and a shared `update_balance()` function that adjusts and displays the running balance.

---

## Slot Machine
**Concepts:** Random Module, Lists, Conditional Logic, While Loops, Emoji/String Output

A 3-symbol slot machine using `random.choice()` to spin, with win/partial-match/no-win logic based on matching symbols, a balance system with deposits, and a replay loop.

---

## Library Book System
**Concepts:** Classes, `__init__`, Instance Methods, Lists of Objects, String Matching, Loops

Models a small library as a list of `Book` objects, each with its own checkout/return state. Menu-driven system to view all books, check availability, and toggle checkout status by searching for a matching title (case-insensitive).

---

## Shape Area Calculator
**Concepts:** Classes, Inheritance, `super()`, Method Overriding (Polymorphism), Format Specifiers

A `Shape` parent class with `Cube`, `Circle`, and `Rectangle` subclasses, each overriding `area()` with its own formula. Each subclass calls `super().__init__()` to reuse the parent's naming setup instead of repeating it.

---

## Hospital Appointment System
**Concepts:** Nested Classes, Aggregation, Dictionaries as Records, Object References Across Classes

A `Hospital` class managing independently-created `Staff` and `Patient` objects (aggregation — patients reference existing doctors by ID rather than owning them). Patients hold their own appointment history; appointment records store nested prescription notes. Menu-driven: register patients, book appointments, view history, and add prescription notes.
