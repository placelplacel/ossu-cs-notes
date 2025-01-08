# HtDW with Compound Data
We will be working through designing an example program to understand this.
> *We want a program that has a cow walking back and forth across the screen, bouncing off of edges, and displaying the appropriate image based on the direction it is moving in.*

## Domain Analysis
1. **Sketching out example scenarios:** Our diagrams will look something like this.
```lisp
; - - - - - - - -    - - - - - - - -    - - - - - - - -    - - - - - - - -    - - - - - - - -
; - - - - - - - -    - - - -^- - - -    - - - - - - - -    - - - - - - - ^    - - - - - - - -
; O>- - - - - - -    - - - -O> - - -    - - - - - - - O>   - - - - - - -<O    - - - <O- - - -
; v - - - - - - -    - - - - - - - -    - - - - - - - v    - - - - - - - -    - - - -v- - - -
; - - - - - - - -    - - - - - - - -    - - - - - - - -    - - - - - - - -    - - - - - - - -
```

2. **Identifying the constant information:** We can tell that we will be defining constants for the following.
    1. The width of the screen.
    2. The height of the screen.
    3. The y-position of the cow.
    4. The left facing image of the cow.
    5. The right facing image of the cow.
    6. The background.

4. **Identifying the varying/changing information:** Our list will consist of 2 things.
    1. The x-position of the cow.
    2. The x-velocity of the cow.

5. **Figuring out which `big-bang` options we will be using:** We have a value that changes over time, we will displaying something on the screen, and we will be taking in keyboard inputs.
    1. `on-tick`
    2. `on-draw`
    3. `on-key`

## Designing the Program
1. **Defining the constants:** Just the usual stuff, we go through our list of constants we need to define and actually define them!
```lisp
(define WIDTH  600)
(define HEIGHT 400)

(define CTR-Y (/ HEIGHT 2))

(define MTS (empty-scene WIDTH HEIGHT "white"))

(define LCOW <left-facing-image>)
(define RCOW <right-facing-image>)
```

2. **Defining the world state/changing values:** Since both the x-position and the x-velocity of the cow naturally belong together, we use a compound data definition.
```lisp
(define-struct cow (x dx))
;; Cow is (make-cow Natural[0, WIDTH] Integer)
;; interp. (make-cow x dx) is a cow where
;;         x          is the x-coordinate of its center in screen coordinates; and
;;         dx         is its x-velocity in pixels per tick;
;    -- EXAMPLES
(define C1 (make-cow 3   10))    ; at x=3,  moving from left -> right
(define C2 (make-cow 10 -5))     ; at x=10, moving from right -> left
;    -- TEMPLATE
#;
(define (fn-for-cow cow)
  (... (cow-x  cow)              ; Natural[0, WIDTH]
       (cow-dx cow)))            ; Integer
;; Template Rules Used:
;; - Compound: 2 fields
```

3. **Defining the `main` function:** We will be progressing every half a second so we pass in `0.5` as the `rate` argument for `on-tick`.
```lisp
;; Cow -> Cow
;; Start the program with ...
(define (main cow)
  (big-bang cow
    (on-tick next-cow 0.5)    ; Cow -> Cow
    (to-draw render-cow)      ; Cow -> Image
    (on-key  handle-key)))    ; Cow, KeyEvent -> Cow
```

4. **Defining the wishlist functions:** Once again, just the usual stuff.
```lisp
;; Cow -> Cow
;; Adds dx of the cow to its x (bounces off the edges)
;; !!!
;    -- STUB
(define (next-cow cow) cow)


;; Cow -> Image
;; Produces an image with the appropriate cow image placed at the appropriate x-position, vertically centered, on MTS.
;; !!!
;    -- STUB
(define (render-cow cow) MTS)


;; Cow, KeyEvent -> Cow
;; Flips the x-velocity of the cow when the space bar is pressed.
;; !!!
;    -- STUB
(define (handle-key cow ke) cow)
```

5. **Implementing the wishlist functions:** Once again, just the usual stuff, *except* we define a fourth wishlist function. Can you figure out where and why we did this before even looking at the code below?
```lisp
;; Cow -> Cow
;; Adds dx of the cow to its x (bounces off the edges)
;    -- STUB
; (define (next-cow cow) cow)
;    -- EXAMPLES
(check-expect (next-cow (make-cow 10 -10))
              (make-cow 0 -10))                      ; Reaches Left Edge
(check-expect (next-cow (make-cow (- WIDTH 5) 5))
              (make-cow WIDTH 5))                    ; Reaches Right Edge
(check-expect (next-cow (make-cow 3 -4))
              (make-cow 0 4))                        ; Tries to pass Left Edge
(check-expect (next-cow (make-cow (- WIDTH 7) 8))
              (make-cow WIDTH -8))                   ; Tries to pass Right Edge
(check-expect (next-cow (make-cow 12 -8))
              (make-cow 4 -8))                       ; Stays within bounds
(check-expect (next-cow (make-cow (- WIDTH 4) 3))
              (make-cow (- WIDTH 1) 3))              ; Stays within bounds
;    -- TEMPLATE
; Template from Cow
(define (next-cow cow)
  (cond [(> (+ (cow-x cow) (cow-dx cow)) WIDTH)
         (make-cow WIDTH (- (cow-dx cow)))]
        [(< (+ (cow-x cow) (cow-dx cow)) 0)
         (make-cow 0 (- (cow-dx cow)))]
        [else
         (make-cow (+ (cow-x cow) (cow-dx cow)) (cow-dx cow))]))


;; Cow -> Image
;; Produces an image with the appropriate cow image placed at the appropriate x-position, vertically centered, on MTS.
;    -- STUB
; (define (render-cow cow) MTS)
;    -- EXAMPLES
(check-expect (render-cow (make-cow 5   9)) (place-image RCOW 5  CTR-Y MTS))
(check-expect (render-cow (make-cow 11 -5)) (place-image LCOW 11 CTR-Y MTS))
;    -- TEMPLATE
; Template from Cow
(define (render-cow cow)
  (place-image (choose-image cow) (cow-x cow) CTR-Y MTS))


;; Cow -> Image
;; Produces LCOW if the velocity of the cow is 0 or negative, RCOW otherwise.
;; !!!
;    -- STUB
(define (choose-image cow) LCOW)


;; Cow, KeyEvent -> Cow
;; Flips the x-velocity of the cow when the space bar is pressed.
;    -- STUB
; (define (handle-key cow ke) cow)
;    -- EXAMPLES
(check-expect (handle-key (make-cow 12 -7) " ") (make-cow 12  7))
(check-expect (handle-key (make-cow 5   2) " ") (make-cow  5  -2))
(check-expect (handle-key (make-cow 14 -1) "a") (make-cow 14 -1))
(check-expect (handle-key (make-cow 25  9) "a") (make-cow 25  9))
;    -- TEMPLATE
; Template based on KeyEvent
(define (handle-key cow ke)
  (cond [(string=? ke " ") (make-cow (cow-x cow) (- (cow-dx cow)))]
        [else cow]))
```

> Notice how every example for a function has a completely different set of inputs and the variation is not just limited to the arguments that it actually uses for computation? This is to ensure that we don't accidentally end up tuning the function for a super specific set of inputs instead of implementing a general solution that we desire.

> Notice that `render-cow` has to perform two tasks.
>   1. Figuring out which image of the cow should be displayed on the screen.
>   2. Displaying that image on the screen.
>
> However, **a function should only perform a single task** so we "outsource" one of the tasks (figuring out which image to use) to a separate function. This is our new wishlist entry, `choose-image`, a **helper function** for `render-cow`.

6. **Implementing the new wishlist function:** We repeat this cycle of defining new wishlist functions that we need and implementing them as many times as we need to.
```lisp
;; Cow -> Image
;; Produces an image with the appropriate cow image placed at the appropriate position on MTS.
;    -- STUB
; (define (render-cow cow) MTS)
;    -- EXAMPLES
(check-expect (render-cow (make-cow 5   9  false)) (place-image RDCOW 5  CTR-Y MTS))
(check-expect (render-cow (make-cow 15  12 true))  (place-image RUCOW 15 CTR-Y MTS))
(check-expect (render-cow (make-cow 11 -5  true))  (place-image LUCOW 11 CTR-Y MTS))
(check-expect (render-cow (make-cow 21 -2  false)) (place-image LDCOW 21 CTR-Y MTS))
;    -- TEMPLATE
; Template from Cow
(define (render-cow cow)
  (place-image (choose-image cow) (cow-x cow) CTR-Y MTS))
```

7. **Recording the preferred initial world state:** We want the starting x-position of the cow to be `0` and the speed to be left up to the user to decide.
```lisp
;; Cow -> Cow
;; Start the program with (main (make-cow 0 dx)) where
;; dx is the initial velocity in pixels per tick.
(define (main cow)
  (big-bang cow
    (on-tick next-cow 0.5)    ; Cow -> Cow
    (to-draw render-cow)      ; Cow -> Image
    (on-key  handle-key)))    ; Cow, KeyEvent -> Cow
```

## Extending the Program
Suppose we were asked to add the following feature to the program.
> *We want you to make it so that the cow alternated between facing up and facing down in whichever direction it was facing.*

How we would go about doing this?

1. **Updating the analysis:** Not only do we have new constants to introduce, but also new variables! Our new lists will look something like this.
    
    **Constants**
    1. The width of the screen.
    2. The height of the screen.
    3. The y-position of the cow.
    4. The background.
    5. The left facing image of the cow.
    6. The right facing image of the cow.
    7. **The top-left facing image of the cow.**
    8. **The top-right facing image of the cow.**
    9. **The bottom-left facing image of the cow.**
    10. **The bottom-right facing image of the cow.**
    11. **The amount by which the images will be rotated in either direction.**

    **Variables**
    1. The x-position of the cow.
    2. The x-velocity of the cow.
    3. **The vertical direction in which the cow will be looking.**

2. **Defining the new constants:** Nothing super complicated.
```lisp
(define WIDTH  600)
(define HEIGHT 400)

(define CTR-Y (/ HEIGHT 2))

(define MTS (empty-scene WIDTH HEIGHT "white"))

(define LCOW <left-facing-image>)
(define RCOW <right-facing-image>)

(define ROT-AMOUNT 20)

(define LUCOW (rotate (- ROT-AMOUNT) LCOW))
(define LDCOW (rotate ROT-AMOUNT     LCOW))
(define RUCOW (rotate ROT-AMOUNT     RCOW))
(define RDCOW (rotate (- ROT-AMOUNT) RCOW))
```

3. **Introducing the new variable:** Our `Cow` data definition now looks like this.
```lisp
(define-struct cow (x dx facing-up?))
;; Cow is (make-cow Natural[0, WIDTH] Integer Boolean)
;; interp. (make-cow x dx facing-up?) is a cow where
;;         x          is the x-coordinate of its center in screen coordinates;
;;         dx         is its x-velocity in pixels per tick;
;;         facing-up? is if it is facing up or down.
;    -- EXAMPLES
(define C1 (make-cow 3   10 false))    ; at x=3,  moving from left -> right, facing down
(define C2 (make-cow 10 -5  true))     ; at x=10, moving from right -> left, facing up
;    -- TEMPLATE
#;
(define (fn-for-cow cow)
  (... (cow-x  cow)              ; Natural[0, WIDTH]
       (cow-dx cow)              ; Integer
       (cow-facing-up? cow)))    ; Boolean
;; Template Rules Used:
;; - Compound: 3 fields
```

4. **Updating the appropriate functions:** Now comes the tedious part. Because we modified the constructor of the `Cow` structure itself, we will now have to update **every. single.** test and function that uses it (which in this case, is literally almost every single function that we've written. Have fun! `:)`), and then also implement the new behaviors!
```lisp
;; Cow -> Cow
;; Adds dx of the cow to its x (bounces off the edges)
;    -- STUB
; (define (next-cow cow) cow)
;    -- EXAMPLES
(check-expect (next-cow (make-cow 10 -10 false))
              (make-cow 0 -10 true))                       ; Reaches Left Edge
(check-expect (next-cow (make-cow (- WIDTH 5) 5 true))
              (make-cow WIDTH 5 false))                    ; Reaches Right Edge
(check-expect (next-cow (make-cow 3 -4 false))
              (make-cow 0 4 true))                         ; Tries to pass Left Edge
(check-expect (next-cow (make-cow (- WIDTH 7) 8 true))
              (make-cow WIDTH -8 false))                   ; Tries to pass Right Edge
(check-expect (next-cow (make-cow 12 -8 true))
              (make-cow 4 -8 false))                       ; Stays within bounds
(check-expect (next-cow (make-cow (- WIDTH 4) 3 false))
              (make-cow (- WIDTH 1) 3 true))               ; Stays within bounds
;    -- TEMPLATE
; Template from Cow
(define (next-cow cow)
  (cond [(> (+ (cow-x cow) (cow-dx cow)) WIDTH)
         (make-cow WIDTH (- (cow-dx cow)) (false? (cow-facing-up? cow)))]
        [(< (+ (cow-x cow) (cow-dx cow)) 0)
         (make-cow 0 (- (cow-dx cow)) (false? (cow-facing-up? cow)))]
        [else
         (make-cow (+ (cow-x cow) (cow-dx cow)) (cow-dx cow) (false? (cow-facing-up? cow)))]))


;; Cow -> Image
;; Produces an image with the appropriate cow image placed at the appropriate x-position, vertically centered, on MTS.
;    -- STUB
; (define (render-cow cow) MTS)
;    -- EXAMPLES
(check-expect (render-cow (make-cow 5   9  false)) (place-image RDCOW 5  CTR-Y MTS))
(check-expect (render-cow (make-cow 15  12 true))  (place-image RUCOW 15 CTR-Y MTS))
(check-expect (render-cow (make-cow 11 -5  true))  (place-image LUCOW 11 CTR-Y MTS))
(check-expect (render-cow (make-cow 21 -2  false)) (place-image LDCOW 21 CTR-Y MTS))
;    -- TEMPLATE
; Template from Cow
(define (render-cow cow)
  (place-image (choose-image cow) (cow-x cow) CTR-Y MTS))


;; Cow -> Image
;; Produces the appropriate cow image based on the direction of the velocity.
;    -- STUB
; (define (choose-image cow) LUCOW)
;    -- EXAMPLES
(check-expect (choose-image (make-cow 33  5 true))  RUCOW)
(check-expect (choose-image (make-cow 15  8 false)) RDCOW)
(check-expect (choose-image (make-cow 10  0 false)) LDCOW)
(check-expect (choose-image (make-cow 60  0 true))  LUCOW)
(check-expect (choose-image (make-cow 12 -4 false)) LDCOW)
(check-expect (choose-image (make-cow 32 -6 true))  LUCOW)
;    -- TEMPLATE
; Template from Cow
(define (choose-image cow)
  (if (<= (cow-dx cow) 0)
      (if (cow-facing-up? cow)
          LUCOW
          LDCOW)
      (if (cow-facing-up? cow)
          RUCOW
          RDCOW)))


;; Cow, KeyEvent -> Cow
;; Flips the x-velocity of the cow when the space bar is pressed.
;    -- STUB
; (define (handle-key cow ke) cow)
;    -- EXAMPLES
(check-expect (handle-key (make-cow 12 -7 true)  " ") (make-cow 12  7 true))
(check-expect (handle-key (make-cow 5   2 false) " ") (make-cow  5 -2 false))
(check-expect (handle-key (make-cow 14 -1 false) "a") (make-cow 14 -1 false))
(check-expect (handle-key (make-cow 25  9 true)  "a") (make-cow 25  9 true))
;    -- TEMPLATE
; Template based on KeyEvent
(define (handle-key cow ke)
  (cond [(string=? ke " ") (make-cow (cow-x cow) (- (cow-dx cow)) (cow-facing-up? cow))]
        [else cow]))
```

## Extending the Program even more!
> *Now that we have the cow joyfully waddling across the screen, we want you to make it so that it turns around as soon as its nose hits the edge rather than its center.*

Let's see how we would go about implementing this. As always, the process remains the same!

1. **Updating the analysis:** We add the newly discovered constant to our constants list, which now looks like this.
    1. The width of the screen.
    2. The height of the screen.
    3. The y-position of the cow.
    4. **The half-width of the cow.**
    5. The background.
    6. The left facing image of the cow.
    7. The right facing image of the cow.
    8. The top-left facing image of the cow.
    9. The top-right facing image of the cow.
    10. The bottom-left facing image of the cow.
    11. The bottom-right facing image of the cow.
    12. The amount by which the images will be rotated in either direction.

2. **Defining the new constant:** Once again, nothing too complicated.
```lisp
(define WIDTH  600)
(define HEIGHT 400)

(define CTR-Y (/ HEIGHT 2))

(define MTS (empty-scene WIDTH HEIGHT "white"))

(define LCOW <left-facing-image>)
(define RCOW <right-facing-image>)

(define ROT-AMOUNT 20)

(define LUCOW (rotate (- ROT-AMOUNT) LCOW))
(define LDCOW (rotate ROT-AMOUNT     LCOW))
(define RUCOW (rotate ROT-AMOUNT     RCOW))
(define RDCOW (rotate (- ROT-AMOUNT) RCOW))

;; Assumes that the rotation amount for every rotated version of the cow image is the same
;; in magnitude.
(define COW-HALF-WIDTH (/ (image-width LUCOW) 2))
```

3. **Updating the appropriate function:** Just. the. usual. stuff. (I should just trademark this at this point.)
```lisp
;; Cow -> Cow
;; Adds dx of the cow to its x (bounces off the edges)
;    -- STUB
; (define (next-cow cow) cow)
;    -- EXAMPLES
(check-expect (next-cow (make-cow (+ 10 COW-HALF-WIDTH) -10 false))
              (make-cow COW-HALF-WIDTH -10 true))                         ; Reaches Left Edge
(check-expect (next-cow (make-cow (- WIDTH COW-HALF-WIDTH 5) 5 true))
              (make-cow (- WIDTH COW-HALF-WIDTH) 5 false))                ; Reaches Right Edge
(check-expect (next-cow (make-cow (+ 3 COW-HALF-WIDTH) -4 false))
              (make-cow COW-HALF-WIDTH 4 true))                           ; Tries to pass Left Edge
(check-expect (next-cow (make-cow (- WIDTH COW-HALF-WIDTH 7) 8 true))
              (make-cow (- WIDTH COW-HALF-WIDTH) -8 false))               ; Tries to pass Right Edge
(check-expect (next-cow (make-cow (+ 12 COW-HALF-WIDTH) -8 true))
              (make-cow (+ 4 COW-HALF-WIDTH) -8 false))                   ; Stays within bounds
(check-expect (next-cow (make-cow (- WIDTH COW-HALF-WIDTH 4) 3 false))
              (make-cow (- WIDTH COW-HALF-WIDTH 1) 3 true))               ; Stays within bounds
;    -- TEMPLATE
; Template from Cow
(define (next-cow cow)
  (cond [(> (+ (cow-x cow) (cow-dx cow) COW-HALF-WIDTH)     WIDTH)
         (make-cow (- WIDTH COW-HALF-WIDTH) (- (cow-dx cow)) (false? (cow-facing-up? cow)))]
        [(< (+ (cow-x cow) (cow-dx cow) (- COW-HALF-WIDTH)) 0)
         (make-cow COW-HALF-WIDTH (- (cow-dx cow)) (false? (cow-facing-up? cow)))]
        [else
         (make-cow (+ (cow-x cow) (cow-dx cow)) (cow-dx cow) (false? (cow-facing-up? cow)))]))
```

## End Result
```lisp
(require 2htdp/image)
(require 2htdp/universe)


(define WIDTH  600)
(define HEIGHT 400)

(define CTR-Y (/ HEIGHT 2))

(define MTS (empty-scene WIDTH HEIGHT "white"))

(define LCOW .)
(define RCOW .)

(define ROT-AMOUNT 20)

(define LUCOW (rotate (- ROT-AMOUNT) LCOW))
(define LDCOW (rotate ROT-AMOUNT     LCOW))
(define RUCOW (rotate ROT-AMOUNT     RCOW))
(define RDCOW (rotate (- ROT-AMOUNT) RCOW))

;; Assumes that the rotation amount for every rotated version of the cow image is the same
;; in magnitude.
(define COW-HALF-WIDTH (/ (image-width LUCOW) 2))


(define-struct cow (x dx facing-up?))
;; Cow is (make-cow Natural[0, WIDTH] Integer Boolean)
;; interp. (make-cow x dx facing-up?) is a cow where
;;         x          is the x-coordinate of its center in screen coordinates;
;;         dx         is its x-velocity in pixels per tick;
;;         facing-up? is if it is facing up or down.
;    -- EXAMPLES
(define C1 (make-cow 3   10 false))    ; at x=3,  moving from left -> right, facing down
(define C2 (make-cow 10 -5  true))     ; at x=10, moving from right -> left, facing up
;    -- TEMPLATE
#;
(define (fn-for-cow cow)
  (... (cow-x  cow)              ; Natural[0, WIDTH]
       (cow-dx cow)              ; Integer
       (cow-facing-up? cow)))    ; Boolean
;; Template Rules Used:
;; - Compound: 3 fields


;; Cow -> Cow
;; Start the program with (main (make-cow 0 dx false))
;; where dx is the speed of the cow in pixels per tick.
(define (main cow)
  (big-bang cow
    (on-tick next-cow 0.5)    ; Cow -> Cow
    (to-draw render-cow)      ; Cow -> Image
    (on-key  handle-key)))    ; Cow, KeyEvent -> Cow


;; Cow -> Cow
;; Adds dx of the cow to its x (bounces off the edges)
;    -- STUB
; (define (next-cow cow) cow)
;    -- EXAMPLES
(check-expect (next-cow (make-cow (+ 10 COW-HALF-WIDTH) -10 false))
              (make-cow COW-HALF-WIDTH -10 true))                         ; Reaches Left Edge
(check-expect (next-cow (make-cow (- WIDTH COW-HALF-WIDTH 5) 5 true))
              (make-cow (- WIDTH COW-HALF-WIDTH) 5 false))                ; Reaches Right Edge
(check-expect (next-cow (make-cow (+ 3 COW-HALF-WIDTH) -4 false))
              (make-cow COW-HALF-WIDTH 4 true))                           ; Tries to pass Left Edge
(check-expect (next-cow (make-cow (- WIDTH COW-HALF-WIDTH 7) 8 true))
              (make-cow (- WIDTH COW-HALF-WIDTH) -8 false))               ; Tries to pass Right Edge
(check-expect (next-cow (make-cow (+ 12 COW-HALF-WIDTH) -8 true))
              (make-cow (+ 4 COW-HALF-WIDTH) -8 false))                   ; Stays within bounds
(check-expect (next-cow (make-cow (- WIDTH COW-HALF-WIDTH 4) 3 false))
              (make-cow (- WIDTH COW-HALF-WIDTH 1) 3 true))               ; Stays within bounds
;    -- TEMPLATE
; Template from Cow
(define (next-cow cow)
  (cond [(> (+ (cow-x cow) (cow-dx cow) COW-HALF-WIDTH)     WIDTH)
         (make-cow (- WIDTH COW-HALF-WIDTH) (- (cow-dx cow)) (false? (cow-facing-up? cow)))]
        [(< (+ (cow-x cow) (cow-dx cow) (- COW-HALF-WIDTH)) 0)
         (make-cow COW-HALF-WIDTH (- (cow-dx cow)) (false? (cow-facing-up? cow)))]
        [else
         (make-cow (+ (cow-x cow) (cow-dx cow)) (cow-dx cow) (false? (cow-facing-up? cow)))]))


;; Cow -> Image
;; Produces an image with the appropriate cow image placed at the appropriate position on MTS.
;    -- STUB
; (define (render-cow cow) MTS)
;    -- EXAMPLES
(check-expect (render-cow (make-cow 5   9  false)) (place-image RDCOW 5  CTR-Y MTS))
(check-expect (render-cow (make-cow 15  12 true))  (place-image RUCOW 15 CTR-Y MTS))
(check-expect (render-cow (make-cow 11 -5  true))  (place-image LUCOW 11 CTR-Y MTS))
(check-expect (render-cow (make-cow 21 -2  false)) (place-image LDCOW 21 CTR-Y MTS))
;    -- TEMPLATE
; Template from Cow
(define (render-cow cow)
  (place-image (choose-image cow) (cow-x cow) CTR-Y MTS))


;; Cow -> Image
;; Produces the appropriate cow image based on the direction of the velocity.
;    -- STUB
; (define (choose-image cow) LUCOW)
;    -- EXAMPLES
(check-expect (choose-image (make-cow 33  5 true))  RUCOW)
(check-expect (choose-image (make-cow 15  8 false)) RDCOW)
(check-expect (choose-image (make-cow 10  0 false)) LDCOW)
(check-expect (choose-image (make-cow 60  0 true))  LUCOW)
(check-expect (choose-image (make-cow 12 -4 false)) LDCOW)
(check-expect (choose-image (make-cow 32 -6 true))  LUCOW)
;    -- TEMPLATE
; Template from Cow
(define (choose-image cow)
  (if (<= (cow-dx cow) 0)
      (if (cow-facing-up? cow)
          LUCOW
          LDCOW)
      (if (cow-facing-up? cow)
          RUCOW
          RDCOW)))


;; Cow, KeyEvent -> Cow
;; Flips the x-velocity of the cow when the space bar is pressed.
;    -- STUB
; (define (handle-key cow ke) cow)
;    -- EXAMPLES
(check-expect (handle-key (make-cow 12 -7 true)  " ") (make-cow 12  7 true))
(check-expect (handle-key (make-cow 5   2 false) " ") (make-cow  5 -2 false))
(check-expect (handle-key (make-cow 14 -1 false) "a") (make-cow 14 -1 false))
(check-expect (handle-key (make-cow 25  9 true)  "a") (make-cow 25  9 true))
;    -- TEMPLATE
; Template based on KeyEvent
(define (handle-key cow ke)
  (cond [(string=? ke " ") (make-cow (cow-x cow) (- (cow-dx cow)) (cow-facing-up? cow))]
        [else cow]))
```
