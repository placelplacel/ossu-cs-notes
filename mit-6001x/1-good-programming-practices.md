# Good Programming Practices

> **TL;DR**
> - Break the program into multiple modules/pieces which can be tested individually.
> - Write docstrings and specifications describing what the different functions/modules do.
> - Document the assumptions that you made while writing the code/designing the program.

You are trying to make soup but bugs keep falling into it from the ceiling. How do you make sure that your soup doesn't have bugs?
- Check the soup for bugs: **Testing**
- Keep the lid closed: **Defensive Programming**
- Clean the kitchen and remove the source of bugs: **Debugging**

## Defensive Programming
- **Write specifications for every function:** What do you expect the inputs to be, what will the function return when given the desired inputs, and so on...
- **Modularize the code:** Break it down into pieces which can be used and tested individually.
- **Enforce the assumptions:** Make sure that the code is getting the input (and returning the output) that meets the assumptions that you made while writing the code with tools like **assertions**.

## Testing/Validation
- **Compare the inputs and outputs:** Is the function return what I intended it to return? Is the output correct?
- **Think of how you can break the function:** What inputs can you give which will probably make the function... malfunction. (*badum thss*) What cases should you check to make sure that the code is working as intended?

## Debugging
- **Follow the trail:** What are the events that led up to the bug?
- **Fix the bug:** Couldn't get simpler.

## Testing (continued)
**Unit Testing:** Checking each module, each function, each piece of code individually.

**Regression Testing:** Checking for bugs, fixing them, then checking for bugs again, and so on until it works. (;w;)

**Integrated Testing:** Making sure that the program, as a single entity, works as intended.

> I felt so called out when the professor said that everyone jumps straight to integration testing instead of running unit and regression tests. (TwT)
>
> This is what the programming process should look like:
> - Write a function/module
> - Test and debug it
> - Write another function/module
> - Test and debug it as well
> - ...
> - Test the program (Integration Testing)
>
> DON'T DO THIS, or more accurately, STOP DOING THIS:
> - Write the entire program
> - Test and debug the entire program

> ALWAYS return to unit testing after you are done implementing fixes during regression or integration testing, and then work your way down the list again.
> 
> This might seem tedious but it is gonna save you soooo much time.

**Blackbox Testing:** Abstracting away the code and using the specification as a guide for designing tests.

**Glassbox Testing:** Using the code itself as a guide for figuring out what tests need to be run: checking every branch of the code, every loop, etc.

**Path-Complete Glassbox Testing:** Testing **every.** **single.** **path.** that the code can take.

# Things I didn't know
```python
# You can use 'else' and 'finally' blocks with a 'try' block.
try:
    # Code to execute
else:
    # Try block code did not throw any exceptions
finally:
    # We got out of the 'try' block. Doesn't matter if it was because of an exception, a break command, or whatever else you can use to break out of it. We just know we got out of it.
```
