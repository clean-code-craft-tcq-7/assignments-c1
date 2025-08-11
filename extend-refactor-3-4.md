# Even more new features

Our product is popular! Customers have even more requests coming in!

Start with your code in the [complexity assignment](paradigms.md) and implement these new features.

## Extension: Early Warning

Care-givers need _early warnings_ to take action,
in addition to the alarm that you print after the limit is breached.
Introduce a 'warning' level with a tolerance of 1.5% of the upper-limit.

Example: If the body-temperature extremities are 95 and 102, the warning-tolerance is `1.5% of 102` = `1.53`.
Warnings need to be displayed in these ranges:
- `95` to `95+1.53` Warning: Approaching hypothermia
- `102-1.53` to `102` Warning: Approaching hyperthermia

Same for pulse-rate, SPO2 and other vitals.

Hint: Map the breach to the ranges. Keep the code common across parameters and vary the data.

Example: Design a data-structure with a series of numbers representing the boundary of each condition.
In the example above: 

- `up to 95`: `HYPO_THERMIA`
- `95 to 96.53`: `NEAR_HYPO`
- `96.54 to 100.47`: `NORMAL`
- `100.48 to 102`: `NEAR_HYPER`
- `102 and above`: `HYPER_THERMIA`

Then, translate the condition to a message in the appropriate language

What impact does this have on the overall vitals?

## Extension: Accept input in different units

Some sensors report the temperature in Celsius.
Make provision to express the unit along with the measurement.
Avoid repeating the limits in different units.
