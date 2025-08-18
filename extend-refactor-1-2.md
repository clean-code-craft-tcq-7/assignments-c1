# Extend with new features

Start with your code in the [complexity assignment](paradigms.md) and implement these new features.

## Extension: Add three more vitals

Notice the amount of (repetitive) code you need to write for each vital. Can you minimize it?

| Parameter | Lower limit | Upper limit |
|-----------|-------------|-------------|
| blood-sugar | 70 | 110 |
| blood-pressure | 90 | 150 |
| respiratory-rate | 12 | 20 |

## Extension: Support a language in addition to English

Our market has expanded to German-speaking countries!
Switch the language of the printed user-messages based on a global variable.

Use [Google translate](https://translate.google.com/?sl=en&tl=de&op=translate)
if you aren't familiar with German.

Keep in mind: We could add more languages in future. We want to do so with minimal effort.

## The starting point

Write a failing test. The asserts will specify the data-models (inputs and outputs). Imagine a care-giver and ensure that the asserts reflect their need.

Experience the places where test / code gets more complex. Think of refactoring opportunities.

## Recommended Approach

- Treat the problem as a series of data-transformations.
- Each transformation is one function (or more).
- Do not mix different transformations in the same function.
- Have one function to chain ('compose') these transformation-functions.
