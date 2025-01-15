# Reference
Suppose we want to design a program in which we had to write data definitions for the names of different schools and their tuition costs.

## HtDD with References
It is fairly obvious that we will be defining a structure to represent each school. But notice that we are dealing with `schools` not `school`. This tells us that we will be defining an arbitrary sized data type. This is what it would look like.
```lisp
(define-struct tuition (name cost))
;; Tuition is (make-tuition String Number)
;; interp. (make-tuition name cost) represents a tuition option where
;;         name is the name of the school; and
;;         cost is the tuition cost in USD
;    -- EXAMPLES
(define T1 (make-tuition "School 1" 52352))
(define T2 (make-tuition "School 2" 25235))
;    -- TEMPLATE
#;
(define (fn-for-tuition tuition)
  (... (tuition-name tuition)
       (tuition-cost tuition)))
;; Template Rules Used:
;; - Compound: 2 fields

;; ListOfTuition is one of:
;; - empty
;; - (cons Tuition ListOfTuition)
;; interp. A list of tuitions
;    -- EXAMPLES
(define LOT1 empty)
(define LOT2 (cons (make-tuition "School 1" 53213) empty))
(define LOT3 (cons (make-tuition "School 2" 56212) (cons (make-tuition "School 1" 32124) empty)))
;    -- TEMPLATE
#;
(define (fn-for-lot lot)
  (cond [(empty? lot) (...)]
        [else
         (... (fn-for-tuition (first lot))
              (fn-for-lot (rest lot)))]))
;; Template Rules Used:
;; - One of: 2 cases
;; - Atomic Distinct: empty
;; - Compound: (cons Tuition ListOfTuition)
;; - Reference: (first lot) is Tuition
;; - Self-Reference: (rest lot) is ListOfTuition
```
> Notice how we used one of our custom data definitions to define another form of data? We are said to have **referenced** `Tuition` in the definition for `ListOfTuition`. This is why we wrapped `(first lot)` in a call to the appropriate **natural helper** (`fn-for-tuition`) when writing its template.

> The natural helper in the template tells us that if we need to do something complicated with the referred type (`Tuition` in this case), then we **do not** do it in the function itself; we instead use a separate helper function.

> A general rule of thumb to determine whether some behavior is complicated or not is to see how many operations you need to perform/functions you need to call with the given result (`(first lot)` in the given examples). If the answer is `more than 1`, then it is complicated.

## HtDF with References
Here is an example to give you a better idea of what the function implementations look like.
```lisp
;; ListOfTuition -> Image
;; Produces a bar chart showing the tuition costs of the different schools in the list that is fed into it.
;    -- STUB
; (define (plot-chart lot) (square 0 "solid" "white"))
;    -- EXAMPLES
(check-expect (plot-chart empty) (square 0 "solid" "white"))
(check-expect (plot-chart (cons (make-tuition "School1" 30293) empty))
              (beside/align "bottom"
                            (overlay/align "center" "bottom"
                                           (rotate 90 (text "School1" FONT_SIZE FONT_COLOR))
                                           (rectangle BAR_WIDTH (* 30293 Y_SCALING) "outline" BAR_OUTLINE_COLOR)
                                           (rectangle BAR_WIDTH (* 30293 Y_SCALING) "solid"   BAR_COLOR))
                            (square 0 "solid" "white")))
(check-expect (plot-chart (cons (make-tuition "School1" 40292) (cons (make-tuition "School2" 58291) empty)))
              (beside/align "bottom"
                            (overlay/align "center" "bottom"
                                           (rotate 90 (text "School1" FONT_SIZE FONT_COLOR))
                                           (rectangle BAR_WIDTH (* 40292 Y_SCALING) "outline" BAR_OUTLINE_COLOR)
                                           (rectangle BAR_WIDTH (* 40292 Y_SCALING) "solid"   BAR_COLOR))
                            (overlay/align "center" "bottom"
                                           (rotate 90 (text "School2" FONT_SIZE FONT_COLOR))
                                           (rectangle BAR_WIDTH (* 58291 Y_SCALING) "outline" BAR_OUTLINE_COLOR)
                                           (rectangle BAR_WIDTH (* 58291 Y_SCALING) "solid"   BAR_COLOR))
                            (square 0 "solid" "white")))
;    -- TEMPLATE
; Template from ListOfTuition
(define (plot-chart lot)
  (cond [(empty? lot) (square 0 "solid" "white")]
        [else
         (beside/align "bottom"
                       (plot-bar   (first lot))
                       (plot-chart (rest lot)))]))


;; Tuition -> Image
;; Produces a single bar representing the tuition cost of the Tuition that is fed into it.
;    -- STUB
; (define (plot-bar tuition) (square 0 "solid" "white"))
;    -- EXAMPLES
(check-expect (plot-bar (make-tuition "S1" 24334))
              (overlay/align "center" "bottom"
                             (rotate 90 (text "S1" FONT_SIZE FONT_COLOR))
                             (rectangle BAR_WIDTH (* 24334 Y_SCALING) "outline" BAR_OUTLINE_COLOR)
                             (rectangle BAR_WIDTH (* 24334 Y_SCALING) "solid"   BAR_COLOR)))
(check-expect (plot-bar (make-tuition "S2" 41253))
              (overlay/align "center" "bottom"
                             (rotate 90 (text "S2" FONT_SIZE FONT_COLOR))
                             (rectangle BAR_WIDTH (* 41253 Y_SCALING) "outline" BAR_OUTLINE_COLOR)
                             (rectangle BAR_WIDTH (* 41253 Y_SCALING) "solid"   BAR_COLOR)))
;    -- TEMPLATE
; Template from Tuition
(define (plot-bar tuition)
  (overlay/align "center" "bottom"
                 (rotate 90 (text (tuition-name tuition) FONT_SIZE FONT_COLOR))
                 (rectangle BAR_WIDTH (* (tuition-cost tuition) Y_SCALING) "outline" BAR_OUTLINE_COLOR)
                 (rectangle BAR_WIDTH (* (tuition-cost tuition) Y_SCALING) "solid"   BAR_COLOR)))
```
> Especially notice how `plot-bar` is the one that serves as the natural helper here; abstracting away the complicated logic to render just a single bar, and keeping `plot-chart` nice, clean, and maintainable.
