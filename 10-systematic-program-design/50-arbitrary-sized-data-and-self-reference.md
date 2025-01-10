# Arbitrary Sized Data
As the name suggests, these are for representing information that we do not know the count of beforehand.

## The `cons` primitive and Lists
```lisp
(cons <first> <rest>)
```
This represents a list constructed from 2 arguments:
1. `first`: This is the value to be added to the front of the list.
2. `rest`: This is a list representing the rest of the list.

```lisp
; An empty list.
; []
empty

; A list with `1` in front of an empty list.
; [1]
(cons 1 empty)

; A list with `2` in front of a list with `1` in front of an empty list.
; [2, 1]
(cons 2 (cons 1 empty))
```
You might have noticed that this is just like a structure with 2 fields and with `cons` as its constructor. The similarities don't stop there, it also provides us selectors and predicates to use and manipulate the list!
1. `first`: Primitive to get the first element of a list.
```lisp
(first (cons 1 empty))
> 1

(first (cons 2 (cons 1 empty)))
> 2
```

2. `rest`: Primitive to get the rest of a list.
```lisp
(rest (cons 1 empty))
> empty

(rest (cons 2 (cons 1 empty)))
> (cons 1 empty)
```

3. `empty?`: Primitive for checking if an expression represents an empty list.
```lisp
(empty? empty)
> true

(empty? (cons 1 empty))
> false

(empty? 1)
> false
```

## HtDD for Lists
```lisp
;; ListOfInt is one of:
;; - empty
;; - (cons Integer ListOfInt)
;; interp. A list of integers.
;    -- EXAMPLES
(define LOI1 empty)
(define LOI2 (cons 1 empty))
(define LOI3 (cons 2 (cons 1 empty)))
;    -- TEMPLATE
#;
(define (fn-for-loi loi)
  (cond [(empty? loi) (...)]
        [else (... (first loi)
                   (fn-for-loi (rest loi)))]))
;; Template Rules Used:
;; - One of: 2 cases
;; - Atomic Distinct: empty
;; - Compound: (cons Integer ListOfInt)
;; - Self-Reference: (rest loi) is ListOfInt
```
> You might notice that one of the cases for `ListOfInt` is `(cons Integer ListOfInt)`, in which it references itself! This is what we call **self-reference** and is the reason we implemented the recursive call in the template function. We call this kind of recursion, i.e. the one that is a consequence of self-reference, **natural recursion**.

> A self-referential data definition is well-formed if and only if it has at least one base case. It *must* have a termination condition.

## HtDF for Lists
```lisp
;; ListOfInt -> Boolean
;; Produces true if the list contains a negative integer, false otherwise.
;    -- STUB
; (define (contains-negative? loi) false)
;    -- EXAMPLES
(check-expect (contains-negative? empty)                     false)
(check-expect (contains-negative? (cons  1 empty))           false)
(check-expect (contains-negative? (cons -1 empty))           true)
(check-expect (contains-negative? (cons  2 (cons -1 empty))) true)
;    -- TEMPLATE
; Template from ListOfInt
(define (contains-negative? loi)
  (cond [(empty? loi) false]
        [else (if (negative? (first loi))
                  true
                  (contains-negative? (rest loi)))]))
```
> Keep in mind that the examples covering the base cases should be the first in the list of tests as they are the most fundamental and all the other tests depend on them.

> Adding on to the rules for the examples/tests for a function, you should always have at least 3 test cases for functions working with lists:
> 1. one for when it is empty;
> 2. one for when there is only a single element in it; and
> 3. one for when there are more than 1 element in the list.
> 
> The reason the first two examples aren't enough is because we also need to test the recursive behavior of the function; which is only possible when the length of the list is at least 2!
