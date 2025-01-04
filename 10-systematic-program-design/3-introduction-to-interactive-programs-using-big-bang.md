# Introduction to Interactive Programs using `big-bang`
We will introduce this new primitive and how it works by going through the inner workings of an example program. We will use the `2htdp/universe` module to make our interactive programs.

```lisp
(require 2htdp/image)
(require 2htdp/universe)

(define WIDTH  200)
(define HEIGHT 150)
(define CTR-Y  (/ HEIGHT 2))
(define MTS    (empty-scene WIDTH HEIGHT "black"))
(define SPRITE (circle 10 "solid" "white"))
(define SPEED  3)

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

(big-bang 0
  (on-tick next-sprite-pos)
  (on-draw render-sprite))
```

### The `big-bang` primitive
This provides the UI framework which allows us to make interactive programs with Racket.
```lisp
(big-bang 0
  (on-tick next-sprite-pos)
  (on-draw render-sprite))
```
You will notice that there are 3 arguments that it is taking in:
- `0`: This is the initial value that will represent the state of the world (the position of `SPRITE` in this case).

- `(on-tick next-sprite-pos)`: This tells it that `next-sprite-pos` is the function that it should call with the current world state as the argument to get the next world state.
> In this case, it is just adding the value of `SPEED` to it and returning the sum.
> ```lisp
> ;; SpritePosition -> SpritePosition
> ;; Produces the SpritePosition increased by/decreased by SPEED based on if the speed
> ;; is positive or negative.
> ;;   -- STUB
> ;; (define (next-sprite-pos pos) 0)
> ;;   -- TESTS
> (check-expect (next-sprite-pos 0) SPEED)
> (check-expect (next-sprite-pos 50) (+ 50 SPEED))
> ;;   -- TEMPLATE
> #;
> (define (next-sprite-pos pos)
>   (... pos))
> (define (next-sprite-pos pos)
>   (+ pos SPEED))
> ```

- `(on-draw render-sprite)`: This tells it that `render-sprite` is the function that it should call with the new world state as the argument to get the next frame/image that it should draw onto the screen.
> Here, it is just placing `SPRITE` on the screen, vertically centered, with the new world state as the x-position.
> ```lisp
> ;; SpritePosition -> Image
> ;; Produces an image by placing the sprite at the given position, vertically centered, and on MTS.
> ;;   -- STUB
> ;; (define (render-sprite pos) (square 0 "solid" "white"))
> ;;   -- TESTS
> (check-expect (render-sprite -100) (place-image SPRITE -100 CTR-Y MTS))
> (check-expect (render-sprite 0) (place-image SPRITE 0 CTR-Y MTS))
> (check-expect (render-sprite 100) (place-image SPRITE 100 CTR-Y MTS))
> ;;   -- TEMPLATE
> #;
> (define (render-sprite pos)
>   (... pos))
> (define (render-sprite pos)
>   (place-image SPRITE pos CTR-Y MTS))
> ```
>
> > The `place-image` primitive produces an image with the first image that is fed into it, on top of the second one, at the specified coordinates.
> > ```lisp
> > ;; This returns a new image with 'SPRITE' (the circle) placed on top of 'MTS' (the eMpTy Scene) at (100, CTR-Y) where 'CTR-Y' stands for 'CenTeR-Y'.
> > (place-image SPRITE 100 CTR-Y MTS)
> > ```
>
> > **What happens if the x-position is much larger than the width of the screen?** It is the same as literally every other graphics API/program that you have worked with/on. The final image gets cropped to the size of the screen i.e. the image gets rendered outside of the screen and thus, is not visible.

From here, you can just use your understanding of and experience with video games and interactive programs to figure out what the end result will look like.

> The `big-bang` primitive is **polymorphic** i.e. it can take in data of any type as the world state, whether it be a number, a string, whatever!

> Of course, there are more `big-bang` options that we could use. Given below is a list of the ones that *we* will be using throughout this course. You should be able to figure out what the parameters are and what we will be returning from the signatures alone.
> |Option|Handler Signature|
> |------|-----------------|
> |`on-tick`|`WorldState -> WorldState`|
> |`on-draw`|`WorldState -> Image`|
> |`on-key`|`WorldState, KeyEvent -> WorldState`|
> |`on-mouse`|`WorldState, Integer, Integer, MouseEvent -> WorldState`|
> |`stop-when`|`WorldState -> Boolean`|
>
> Look up the documentation to see what else you could pass in!
