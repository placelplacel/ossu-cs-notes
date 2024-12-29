# HtDF with Data

## Intervals
These must have at least three test cases:
- The closed lower bound
- A value near the midpoint
- The closed upper bound

```lisp
;; PlayerAge is Natural[13, 19]
;; interp. a number representing the age of a player

(define PLAYER_AGE_1 13)
(define PLAYER_AGE_2 15)
(define PLAYER_AGE_3 19)

#;
(define (fn-for-player-age age)
    (... age))

;; Template Rules Used:
;; - Atomic Non-Distinct: Natural[13, 19]


;; PlayerAge -> boolean
;; Produces true if the given age is an edge age (13 or 19) and false otherwise

; (define (edge-age? age) false)    ; stub

(check-expect (edge-age? 13) true)
(check-expect (edge-age? 16) false)
(check-expect (edge-age? 19) true)

; template from PlayerAge

(define (edge-age age)
    (or (= age 13)
        (= age 19)))
```

## Enumeration
These must have at least as many test cases as there are cases in the enumeration.

```lisp
;; CwoseFwiend is one of:
;; - 0
;; - 1
;; - 2
;; interp. the name of a cwose fwiend of mine
;;          0 means sis, 1 means ume, 2 means aki

#;
(define (fn-for-cwose-fwiend cf)
    (cond [(= cf 0) (...)]
          [(= cf 1) (...)]
          [(= cf 2) (...)]))

;; Template Rules Used:
;; - One of:          3 cases
;; - Atomic Distinct: 0
;; - Atomic Distinct: 1
;; - Atomic Distinct: 2


;; CwoseFwiend -> String
;; Produces the name of the friend that the CwoseFriend fed into it corresponds to

; (define (name cf) "")    ; stub

(check-expect (name 0) "sis")
(check-expect (name 1) "ume")
(check-expect (name 2) "aki")

; Template from CwoseFwiend

(define (name cf)
    (cond [(= cf 0) "sis"]
          [(= cf 1) "ume"]
          [(= cf 2) "aki"]))

```

## Itemization
These must have at least as many test cases as there are cases in the itemization we are working with. This version of the recipe is just a mish-mash of the different HtDF-with-data recipes we have seen so far.

```lisp
(require 2htdp/image)

;; FreakScore is one of:
;; - false
;; - Number[1, 10]
;; interp.
;;     false          means not freaky at all
;;     Number[1, 10]  means the person is freaky, and represents their freak score

(define FREAK_SCORE_ANDY false)
(define FREAK_SCORE_1 1)
(define FREAK_SCORE_2 5)
(define FREAK_SCORE_AKI 10)

#;
(define (fn-for-freak-score score)
    (cond [(false? score) (... score)]
          [(and (number? score) (<= 1 score 10)) (... score)]))

;; Template Rules Used:
;; - One of:              2 cases
;; - Atomic Distinct:     false
;; - Atomic Non-Distinct: Number[1, 10]


;; FreakScore -> Image
;; Produces an image representing the freak score that is fed into it

; (define (freak-score->image score) (square 0 "solid" "white"))    ; stub

(check-expect (freak-score->image false)
    (square 0 "solid" "white"))
(check-expect (freak-score->image 5)
    (text (number->string 5) 30 "red"))

; Template from FreakScore

(define (freak-score->image score)
    (cond [(false? score)
            (square 0 "solid" "white")]
          [(and (number? score) (<= 1 score 10))
            (text (number->string score) 30 "red")]))
```

> Notice how we only had one test case for when the `FreakScore` is a `Number[1, 10]`. This is because we want to test every **point of variance** and there is really nothing different about how the function should act on for all the numbers in the given interval.
>
> However, we would have checked for boundary cases if we had been dealing with **adjoining** intervals.
> ```lisp
> ...
>
> ;; FreakScore -> Boolean
> ;; Returns true if the FreakScore fed into it is more than 5.
>
> ; (define (freaky-enough? score) false)    ; stub
>
> (check-expect (freaky-enough? false) false)
> (check-expect (freaky-enough? 3) false)
> (check-expect (freaky-enough? 5) false)
> (check-expect (freaky-enough? 6) true)
> (check-expect (freaky-enough? 8) true)
>
> ; Template from FreakScore
>
> (define (freaky-enough? score)
>     (cond [(false? score)
>             false]
>           [(and (number? score) (<= 1 score 10))
>             (> score 5)]))
> ```
>
> The tests with `5` and `6` as the arguments are the **most critical** out of the 4 with numeric inputs.

## Things to keep in mind
The fact that the data definition has so much influence over the tests that we write for the functions working with that data and their templates is what really underlines how important the way we represent the information that we are dealing with is.

> This also gives rise to the structural hierarchy:
> - Information
> - Data
> - Templates
> - Functions and Examples/Tests
> 
> where everything below any of the elements is dependent on that element. You can think of this as the pipeline through which we define the design of the program.
