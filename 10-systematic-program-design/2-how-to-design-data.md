# HtDD

1. **Type Definition:** Tells us how we are choosing to represent the information as data.

```lisp
;; PlayerName is String
```

2. **Interpretation:** Tells us how to interpret the data to get the information that it represents.

```lisp
;; interp. the name of a player
```

3. **Examples:** Some examples to help us understand the way it works by seeing it in action.

```lisp
(define PLAYER_1 "jaybles")
(define PLAYER_2 "ambey")
```

4. **Template:** The template for a function that consumes the given data type.

```lisp
(define (fn-for-player-name name)
    (... name))
```

> There are multiple kinds of templates based on the kind of data being used to represent the information! The template above is just one of many, and is called the `Atomic Non-Distinct` template rule.

> If you are writing a function that consumes a custom data type that you have defined, using HtDF, and decide to borrow the template from the data definition of the type, then make sure to mention where you got the template from.
> 
> ```lisp
> ; template from PlayerName
>
> (define (banned? name) (...))
> ```

## End Result
```lisp
;; PlayerName is String
;; interp. the name of a player

(define PLAYER_1 "jaybles")
(define PLAYER_2 "ambey")

#;
(define (fn-for-player-name name)
    (... name))
```

## Intervals
These are used for representing numeric information within a specific range.

```lisp
;; Byte is Integer[0, 255]
;; interp. a positive integer that can be represented with just 8 bits.

(define BYTE_1 0)
(define BYTE_2 196)
(define BYTE_3 255)

#;
(define (fn-for-byte byte)
    (... byte))

; Template Rules Used:
; - Atomic Non-Distinct: Integer[0, 255]
```

> We use the mathematical interval notation for representing ranges: `[]` is inclusive, and `()` is exclusive.

> Notice how there are 3 examples: one for each end point; and one somewhere in the middle.

## "Enum"erations
These are used for representing one of multiple distinct values (you know how enums work).

```lisp
;; CwoseFwiend is one of:
;; - 0
;; - 1
;; - 2
;; interp. the name of a close friend of mine
;;         0 means sis, 1 means ume, 2 means aki

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
```

> Notice how there are no examples? This is because we already know how `CwoseFwiend` is going to work. Heck, we even listed out all of the possible values! So, examples will be redundant.

> Notice how the template function for an enumeration covers all of the possible values with a `cond` (switch) expression?

## Itemization
These are like enums but at least one of the "classes" is not represented by a single distinct value.

```lisp
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
    (cond [(false? score) (...)]
          [(and (number? score) (<= 1 score) (<= score 10)) (... score)]))

;; Template Rules Used:
;; - One of:              2 cases
;; - Atomic Distinct:     false
;; - Atomic Non-Distinct: Number[1, 10]
```

> Notice how we explicitly checked to see if the score was a number before proceeding with the interval checks? Think about why we might have done this.
> 
> (**Hint:** Mixed Data Itemization/Multiple Types)

> Keep in mind that we did not have to worry about `false?` breaking like we had to for the interval checks because it accepts arguments of all (primitive) types.

> We can simplify the template if we assume that the arguments being passed match the signature of the function, i.e., a `Number[1, 10]` parameter will never be anything except those values, an enum parameter will never have any value other than the values that it contains, etc.
>
> ```lisp
> ;; FreakScore is one of:
> ;; - false
> ;; - Number[1, 10]
> ;; interp.
> ;;     false          means not freaky at all
> ;;     Number[1, 10]  means the person is freaky, and represents their freak score
> 
> (define FREAK_SCORE_ANDY false)
> (define FREAK_SCORE_1 1)
> (define FREAK_SCORE_2 5)
> (define FREAK_SCORE_AKI 10)
> 
> #;
> (define (fn-for-freak-score score)
>     (cond [(false? score) (...)]
>           [else (... score)]))
> 
> ;; Template Rules Used:
> ;; - One of:              2 cases
> ;; - Atomic Distinct:     false
> ;; - Atomic Non-Distinct: Number[0, 10]
> ```
>
> We don't need the number or the interval guards because the argument being passed cannot be anything other than a number between 1 and 10 inclusive if it is not `false` (which we check for in the first `cond` clause).

> Looking at the code from the previous exhibits, you might notice this:
> ```lisp
> (define (fn-for-freak-score score)
>     (cond [(false? score) (...)]
>           [else (... score)]))
> ```
> One of the branches has `(...)` as the true expression while the other has `(... score)`. How did we decide which one we should use? The answer lies in the next few lines that we left out:
> ```lisp
> ;; Template Rules Used:
> ;; - One of:              2 cases
> ;; - Atomic Distinct:     false
> ;; - Atomic Non-Distinct: Number[0, 10]
> ```
> Did you catch it? We used `(...)` when the data type we were dealing with was **distinct**, and `(... score)` when it was **non-distinct**. This took me days to figure out as well so don't worry if you weren't able to figure it out by yourself.
