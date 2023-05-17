#!/usr/bin/env python3


class Person:
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")


from lib.person import Person

person = Person()
person.talk()
# Hello World!

person.walk()
# The person is walking.
