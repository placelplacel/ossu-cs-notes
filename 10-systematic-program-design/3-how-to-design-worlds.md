# HtDW
Now let's see how we went about building the program in `3-introduction-to-interactive-programs-using-big-bang.md`.

## Domain Analysis
1. **Drawing example states of the program:** This helps determine which values will be changing, and which values will be constants.
```lisp
; - - - - - - - -    - - - - - - - -    - - - - - - - -
; - - - - - - - -    - - - - - - - -    - - - - - - - -
; O - - - - - - -    - - - -O- - - -    - - - - - - - O
; - - - - - - - -    - - - - - - - -    - - - - - - - -
; - - - - - - - -    - - - - - - - -    - - - - - - - -
```
2. **Identifying constant information:** From the example states that we drew, we can figure out what we will be defining constants for.
    1. The width of the screen.
    2. The height of the screen.
    3. The sprite.
    4. The y-coordinate of the sprite.
    5. The background.

3. **Identifying changing information:** Once again, from the exmaple states, we can figure out that the x-coordinate of the sprite is the value that will be changing.

4. **Deciding which `big-bang` options to use:** We have a value that will be changing over time, and we will be displaying something to the screen so we will be passing in the `on-tick` and `to-draw` arguments.

## Designing the Program
1. **Defining the constants:** We use the list of constants that we identified from the Domain Analysis for this.
```lisp
(define WIDTH  200)
(define HEIGHT 150)
(define CTR-Y  (/ HEIGHT 2))
(define MTS    (empty-scene WIDTH HEIGHT "black"))
(define SPRITE (circle 10 "solid" "white"))
```
> Notice how we used `(/ HEIGHT 2)` when defining `CTR-Y` instead of just writing `75`. This is to ensure that there is **only one point of control**. We wouldn't want to look through the code for instances that depend on the height of the screen and manually update them, would we?
>
> > *There are two kinds of programs: (i) programs that change; and (ii) programs that nobody uses.*
> 
> **Programs with users always change, and that is why it is important to make them easy to change.**

> Also notice how we can easily tell where each observation from our analysis ended up in the program? This is called **Traceability**.

2. **Defining the world state/the changing values:** In this case, it is the x-coordinate of the sprite.
```lisp
;; SpritePosition is Number
;; interp. The x-position of a sprite.
(define POS_1 0)            ; left edge
(define POS_2 (/ WIDTH 2))  ; middle
(define POS_3 WIDTH)        ; right edge
;    -- TEMPLATE
#;
(define (fn-for-sprite-position pos)
  (... pos))
;; Template Rules Used:
;; - Atomic Non-Distinct: Number
```

3. **Defining the `main` function:** This is the function that will serve as the entry point for our program.
```lisp
(define (main pos)
  (big-bang pos                  ; SpritePosition
    (on-tick next-sprite-pos)    ; SpritePosition -> SpritePosition
    (to-draw render-sprite)))    ; SpritePosition -> Image
```

4. **Defining the wishlist functions:** These are functions that we want in our program but haven't implemented *yet*. For these, we write the signature, the purpose (followed by `!!!`), and the stub, but **not** the tests, template, and implementation.
```lisp
;; SpritePosition -> SpritePosition
;; Produces the SpritePosition increased by 1.
;; !!!
(define (next-sprite-pos pos) 0)

;; SpritePosition -> Image
;; Produces an image by placing the sprite at the given position, vertically centered, and on MTS.
;; !!!
(define (render-sprite pos) MTS)
```

> Not only does the `!!!` tell us that these are wishlist functions and require implementation, it also makes them easier to find as we can just search for `!!!` and immediately jump to them.

> Just like with tests, the stubs are here make the program at least partially runnable.

5. **Implementing the wishlist functions:** This is where we work through the wishlist and implement the functions that we need.
```lisp
;; SpritePosition -> SpritePosition
;; Produces the SpritePosition increased by 1.
;    -- STUB
;  (define (next-sprite-pos pos) 0)
;    -- TESTS
(check-expect (next-sprite-pos 0) 1)
(check-expect (next-sprite-pos 50) 51)
;    -- TEMPLATE
#;
(define (next-sprite-pos pos)
  (... pos))
(define (next-sprite-pos pos)
  (+ pos 1))

;; SpritePosition -> Image
;; Produces an image by placing the sprite at the given position, vertically centered, and on MTS.
;    -- STUB
;  (define (render-sprite pos) (square 0 "solid" "white"))
;    -- TESTS
(check-expect (render-sprite -100) (place-image SPRITE -100 CTR-Y MTS))
(check-expect (render-sprite 0) (place-image SPRITE 0 CTR-Y MTS))
(check-expect (render-sprite 100) (place-image SPRITE 100 CTR-Y MTS))
;    -- TEMPLATE
#;
(define (render-sprite pos)
  (... pos))
(define (render-sprite pos)
  (place-image SPRITE pos CTR-Y MTS))
```

6. **Recording the preferred initial world state:** `0` seems like a good initial world state for this program so we write it down as a comment above the `main` function.
```lisp
;; Start the program with (main 0)
(define (main pos)
  (big-bang pos                  ; SpritePosition
    (on-tick next-sprite-pos)    ; SpritePosition -> SpritePosition
    (to-draw render-sprite)))    ; SpritePosition -> Image
```

## Extending the Program
Suppose we decide like the sprite was moving a bit too slow and want to be able to change it's speed. Looking through the program, we can see that there isn't really a defined constant that corresponds to the speed of the sprite. We hadn't thought of this constant!

> In more complicated programs, you might not be able to list all of the constants that you will need during this analysis phase, and instead discover them as you keep working on the program. That is completely fine!
>
> In such a situation, we just add the newly discovered constant to the list from the analysis, and continue on as if it was there from the beginning.

1. **Adding the new constant to the analysis:** Our list now looks like this.
    1. The width of the screen.
    2. The height of the screen.
    3. The sprite.
    4. The y-coordinate of the sprite.
    5. The speed of the sprite.
    6. The background.

2. **Defining the constant:** Our definitions for the constants now look like this.
```lisp
(define WIDTH  200)
(define HEIGHT 150)
(define CTR-Y  (/ HEIGHT 2))
(define MTS    (empty-scene WIDTH HEIGHT "black"))
(define SPRITE (circle 10 "solid" "white"))
(define SPEED  3)
```

3. **Modifying the appropriate function:** Our definition for `next-sprite-pos` now looks like this.
```lisp
;; SpritePosition -> SpritePosition
;; Produces the SpritePosition increased by/decreased by SPEED based on if the speed
;; is positive or negative.
;    -- STUB
;  (define (next-sprite-pos pos) 0)
;    -- TESTS
(check-expect (next-sprite-pos 0) SPEED)
(check-expect (next-sprite-pos 50) (+ 50 SPEED))
;    -- TEMPLATE
#;
(define (next-sprite-pos pos)
  (... pos))
(define (next-sprite-pos pos)
  (+ pos SPEED))
```
