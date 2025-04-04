# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/109-AA3pG0xb-1XTHtuKQGC8O4lI25XCi
"""

class Guest:
    def __init__(self, name, email, phone, loyalty_points=0):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__loyalty_points = loyalty_points

    def update_profile(self, name=None, email=None, phone=None):
        if name:
            self.__name = name
        if email:
            self.__email = email
        if phone:
            self.__phone = phone

    def add_loyalty_points(self, points):
        self.__loyalty_points += points

    def __str__(self):
        return f"Guest {self.__name}, Email: {self.__email}, Loyalty Points: {self.__loyalty_points}"