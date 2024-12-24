# Beginning Student Language

## Expressions
`Expression` refers to either values or primitive calls.

```lisp
; These are values.
9
12
#i1.414...
```

> **Notice the weird `#i` at the beginning of the second value?** This is how Racket tells us that the given value is inexact, i.e., it is a close approximation but not the actual number.

```lisp
; These are primitive calls. These have two parts: the primitive (or the operator), and the operands.
(sqr 3)
(+ 4 (* 2 3) (/ 4 (- 3 1)))
(sqrt 2)
```

> You can think of the operator as the function being called, and the operands as arguments to that function.

## Strings
Defined just how you would define them in any other language: by enclosing characters with double quotes.

```lisp
"this is a string!"
```

Just like numbers, strings have some special primitives themselves that we can use to manipulate them.

```lisp
(string-append "Zapper" "oni")
> "Zapperoni"

(string-length "Apple")
> 5

(substring "Hhanyaaa :3" 3 11)
> "nyaaa :3"
```

## Modules
Modules can be imported using the `require` primitive.

```lisp
(require 2htdp/image)
```

## Drawing Images
These are defined in the `2htdp/image` module and houses primitives for drawing images.

```lisp
(require 2htdp/image)

; (circle <radius> <style> <color>)
(circle 20 "solid" "red")

; (rectangle <width> <height> <style> <color>)
(rectangle 20 20 "outline" "yellow")

; (regular-polygon <side-length> <side-count> <style> <color>)
(regular-polygon 20 8 "solid" "green")

; (text <string> <font-size> <color>)
(text "Ambey" 30 "green")

; This displays an image of the text "Ambey" in green with font size 30, referencing the fact that Ambey is a huge green flag.
```

## Combining Images
We can use `beside` to draw images beside each other from left to right such that they are all vertically centered.

```lisp
; (beside ...)
(beside (circle 20 "solid" "red")
        (circle 30 "solid" "green"))
```

Similarly, `above` draws images laid out from top to bottom such that their horizontal centers are aligned.
```lisp
; (above ...)
(above (circle 20 "solid" "red")
       (circle 30 "solid" "green"))
```

Obviously, we can combine these guys to make more complicated layouts.
```lisp
(above (beside ...)
       (above ...))
```

## Manipulating Images
`rotate` is a primitive that does exactly what its name suggests. It evaluates to a copy of the image that is fed into it, rotated by a given amount.

```lisp
; (rotate <amount> <image>)
(rotate -10 SOME_IMAGE)
```

> Keep in mind that rotating by a negative amount rotates the image clockwise while a positive amount rotates it in the other direction.

## Other Image Primitives
```lisp
; (image-width  <image_expression>)
; (image-height <image_expression>)
```

## Named Constants
Named constants are defined using the `define` primitive.

```lisp
; (define <name> <expression>)
(define HHANHHAN_FREAKINESS 9001)
```

> Remember that BSL allows you to use images as values as well. So you could define a constant which evaluates to an image!

## Functions
Functions are defined similar to how constants are, except we don't immediately provide a name. We instead write what looks like an expression containing the name of the function and the parameters that it takes in.

```lisp
; (define (<name> <parameters>) <expression>)
(define (catify message)
    (string-append message " :3"))
```

The function can then be called like any other primitive with the appropriate arguments.

```lisp
(catify "hewwo")
> "hewwo :3"
```

> You can think of functions in BSL as being equivalent to macros in C++.

## Booleans and Predicates
`Predicate` refers to any function that returns a `boolean` value. These include primitives that allow us to write tests.

```lisp
(> 3 9)
> #false

(<= 5 5)
> #true

(= 3 9)
> #false

(string=? "foo" "bar")
> #false
```

We can also do all of the classic logic that we are used to doing.

```lisp
; (and <predicates>)
; (or  <predicates>)
; (not <predicate>)
```

## If Statements
```lisp
; (if <predicate>
;     <true expression>
;     <false expression>)
(define ZAPZAP "smol")
(if (string=? ZAPZAP "smol")
    "yes"
    "no")
> "yes"
```

## Tests
These work like assert statements or any other usual test: they just compare the two arguments that they are given.

```lisp
; (check-expect <actual-result> <expected-result>)
(check-expect (double 3) 6)
```

## Multiple Conditions
These are like switch statements but with predicates instead of expected values. It runs through the list of clauses and keeps going until either one of the predicates returns true, or we reach the `else` clause at the end.

```lisp
; (cond [<predicate> <true expression>]
;       [<predicate> <true expression>]
;       ...
;       [else <false expression>])
(cond [(= JAYBLES_STATUS "sleepdrunk") "freaky"]
      [(= JAYBLES_STATUS "sober") "freaky"]
      [else "unknown status"])
```

> Note that the `else` clause is only necessary if none of the previous conditions is satisfied. If you are sure that at least one of the clauses that you have in place will return `true`, you can remove it.

> Keep in mind that the `else` clause can only be supplied as the last clause to the `cond` statement.
