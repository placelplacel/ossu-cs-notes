# HtDD for Compound Data
These hold multiple values, which naturally belong together, together. We use structures (structs) for these purposes.

## "Struct"-ures
Defined using the `define-struct` primitive.
```lisp
; (define-struct <name> (<field-names>))
(define-struct position (x y))
```
This also defines 3 kinds of primitives that we can use to manipulate/use the struct:
1. **Constructor:** The primitive for making the struct.
```lisp
; (make-<struct-name> <field-values>)
(make-pos 2 8)
> (make-pos 2 8)
```

2. **Selectors/Getters:** The primitives for getting specific values from the struct.
```lisp
(define P1 (make-pos 2 8))

; (<struct-name>-<field-name> <struct>)
(pos-x P1)
> 2

(pos-y P1)
> 8
```

3. **Predicate:** The primitive for type-checking.
```lisp
; (<struct-name>? <expression>)
(pos? (make-pos 2 8))
> #true

(pos? "foo")
> #false
```

## Example Data Definition
```lisp
(define-struct position (x y))
;; Position is (make-position Number Number)
;; interp. (make-position x y) represents the coordinates of a point where
;;         x is the x-coordinate of the point; and
;;         y is the y-coordinate of the point
;    -- EXAMPLES
(define P1 (make-position  2  8))
(define P2 (make-position -3 -4))
;    -- TEMPLATE
#;
(define (fn-for-position pos)
  (... (position-x pos)      ; Number
       (position-y pos)))    ; Number
;; Template Rules Used:
;; - Compound: 2 fields
```
