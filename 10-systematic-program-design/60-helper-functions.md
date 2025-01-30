# Helper Functions
## Function Composition
This is used when a function has to perform two or more distinct tasks (e.g. sorting a list of images by area in decreasing order and then laying them out side-by-side).

### Example Program
We will use an example program to illustrate the changes in HtDF when dealing with function composition. This exhibit is incomplete but still portrays the differences that we care about.
> *We want you to write a function that takes in a list of images, and displays them side-to-side such that the area decreases as we move from left to right.*
```lisp
(require 2htdp/image)

;; ==================================
;; CONSTANTS

;    -- FOR TESTS
(define IMG0 (square   5 "solid" "white"))
(define IMG1 (triangle 5 "solid" "red"))
(define IMG2 (circle   5 "solid" "blue"))

;; ==================================
;; DATA DEFINITIONS

;; ListOfImage is one of:
;; - empty
;; - (cons Image ListOfImage)
;; interp. A list of images
;    -- EXAMPLES
(define LOI0 empty)
(define LOI1 (cons (square 5 "solid" "white") empty))
(define LOI2 (cons (triangle 5 "solid" "red") (cons (square 5 "solid" "white") empty)))
;    -- TEMPLATE
#;
(define (fn-for-loi loi)
  (cond [(empty? loi) (...)]
        [else
         (... (first loi)
              (fn-for-loi (rest loi)))]))
;; Template Rules Used:
;; - One of: 2 cases
;; - Atomic Distinct: empty
;; - Compound: (cons Image ListOfImage)
;; - Self-Reference: (rest loi) is ListOfImage

;; ==================================
;; FUNCTIONS

;; ListOfImage -> Image
;; Consumes a list of images, sorts them by area in decreasing order, and then lays them out side-by-side.
;    -- STUB
; (define (arrange-images loi) empty-image)
;    -- EXAMPLES
(check-expect (arrange-images (cons IMG0 (cons IMG1 empty)))
              (beside IMG0 IMG1 empty-image))
(check-expect (arrange-images (cons IMG1 (cons IMG0 empty)))
              (beside IMG0 IMG1 empty-image))
(define (arrange-images loi)
  (layout-images (sort-images loi)))

;; ListOfImage -> ListOfImage
;; Sorts the list of images that is fed into it by area in decreasing order.
;; !!!
;    -- STUB
(define (sort-images loi) loi)

;; ListOfImage -> Image
;; Lays out the images in the given list from left to right in order of the list.
;; !!!
;    -- STUB
(define (layout-images loi) empty-image)

;; ==================================
```

> Notice how despite `arrange-images` taking in a `ListOfImage` as an input, we did not use its template. Instead, we just wrote the **function composition** for it and the wishlist functions.

> A more subtle change is the exclusion of some cases that we would consider to be indispensable when writing a regular function operating on a `ListOfImage`, e.g. the base case!
>
> The reason for this is that the different test cases will be handled by the tests for the two helper functions; so the examples for `arrange-images` are only there to make sure that the operations (`sort-images` and `layout-images` in this case) are being performed in the correct order. Though we still write tests to check if the function is actually performing the tasks that it is supposed to perform, e.g. the two test cases that we did write vary based on `sort-images`.

## Operating on Lists
A helper function must always be used when performing an operation on a list. An example of this can be seen in the implementation of `sort-images` in our example program.
```lisp
;; ListOfImage -> ListOfImage
;; Sorts the list of images that is fed into it by area in decreasing order.
;    -- STUB
; (define (sort-images loi) loi)
;    -- EXAMPLES
(check-expect (sort-images empty)
              empty)
(check-expect (sort-images (cons IMG1 (cons IMG0 empty)))
              (cons IMG0 (cons IMG1 empty)))
(check-expect (sort-images (cons IMG0 (cons IMG2 (cons IMG1 empty))))
              (cons IMG2 (cons IMG0 (cons IMG1 empty))))
;    -- TEMPLATE
; Template from ListOfImage
(define (sort-images loi)
  (cond [(empty? loi) empty]
        [else
         (insert (first loi)
                 (sort-images (rest loi)))]))

;; Image, ListOfImage -> ListOfImage
;; Inserts the given image into the list at some position such that that resulting list is sorted by
;; area in decreasing order.
;; !!!
;    -- STUB
(define (insert img loi) loi)
```
> Notice how we defined a separate helper function `insert` to insert the image into the list rather than operating on the list inside `sort-images` itself.

## Knowledge Domain Shift
If we run into a shift in the knowledge domain at any point while writing the code for a function, we write the code for that new domain in a separate helper. We illustrate this using an example implementation of `insert` from our previous exhibits.
```lisp
;; Image, ListOfImage -> ListOfImage
;; Inserts the given image into the list at some position such that that resulting list is sorted by
;; area in decreasing order.
;    -- STUB
; (define (insert img loi) loi)
;    -- EXAMPLES
(check-expect (insert IMG2 (cons IMG0 (cons IMG1 empty)))
              (cons IMG2 (cons IMG0 (cons IMG1 empty))))    ; In the beginning
(check-expect (insert IMG1 (cons IMG2 (cons IMG0 empty)))
              (cons IMG2 (cons IMG0 (cons IMG1 empty))))    ; In the end
(check-expect (insert IMG0 (cons IMG2 (cons IMG1 empty)))
              (cons IMG2 (cons IMG0 (cons IMG1 empty))))    ; In the middle
;    -- TEMPLATE
#;
(define (insert img loi)
  (cond [(empty? loi) (... img)]
        [else
         (... img
              (first loi)
              (insert (... img) (rest loi)))]))
(define (insert img loi)
  (cond [(empty? loi) (cons img empty)]
        [else
         (if (smaller? img (first loi))
              (cons (first loi) (insert img (rest loi)))
              (cons img loi))]))

;; Image, Image -> Boolean
;; Produces true if the first image that is fed into it is smaller in area than the second one.
;; !!!
;    -- STUB
(define (smaller? img1 img2) false)
```
> Notice the new helper function `smaller?`. Why do you think we introduced this new helper rather than writing all of the logic for it in `insert` itself?
>
> Of course, we did this to separate out code for the complicated task of comparing the areas of two images. However, we also did this because there was a **shift in the knowledge domain**: `insert` deals with inserting an image into a list, but the operation *we* wish to perform is a comparison between the area of two images. Both *very* different things.
