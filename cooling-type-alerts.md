# From spec to delivery

Allow the tests to guide the design. Recognize concepts along the way.

## Problem outline

An automation usually has input (like data from IoT sensors) and actions.

Actions could be semi-automatic, like sending an email alert. They could be automatic, such as activating a controller.

A common problem is the variety at each stage:

- Multiple types of IoT devices, each with its own data format
- Multiple possibilities of implementation: rules-based, probabilistic (machine-learning)
- Multiple contexts (different customer environments)
- Multiple actuator types (email providers, controllers, etc)

This results in an explosion of combinations, with every additional variety being felt across all variations. By adding a rule, we may end up re-testing everything from sensors to actuators.

Let's try TDD to break down such a context.

## Pick a language for your assignment

[C](https://classroom.github.com/a/A0qHCg4r)

[C#](https://classroom.github.com/a/DdbnRBeZ)

[Java](https://classroom.github.com/a/p_iPvB6J)

[Python](https://classroom.github.com/a/c2TW5Zdz)

[JavaScript](https://classroom.github.com/a/YsZ24ONa)
