'''
Problem Statement: Write a Python program to create a Light class with three methods: turn_on() that switches the light on, turn_off) that switches it off, and status () that reports whether the light is currently on or off.
Purpose: This exercise models a simple stateful object, where the object remembers and changes its own condition over time. It introduces the concept of state management within a class, a pattern found everywhere from Ul components and loT devices to game objects and workflow engines.
Given Input: Create a Light object, call turn_on(), check status(), call turn_off), and check status() again.
Expected Output:
Current status: ON
Current status: OFF
'''


class Light:

    def __init__(self):
        self.status = "None"

    def on(self):
        self.status = "ON"
        return self.status

    def off(self):
        self.status = "OFF"
        return self.status


obj = Light()

res1 = obj.on()
print(res1)

res2 = obj.off()
print(res2)
