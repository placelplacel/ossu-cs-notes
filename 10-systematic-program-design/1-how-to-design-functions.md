# HtDF

1. **Signature:** Shows the types of the parameters that the function takes in, and the type of its return value.

```lisp
;; Number -> Number
```

> When writing signatures, we try to be as specific as possible. Consider this scenario for example.
>
> ```lisp
> ;; Image -> Number
>
> (define (image-area img)
>     (* (image-width img) (image-height img)))
> ```
>
> If you think about it carefully, you realize that this function returns a number; sure, but it always returns a **natural** number. It can NEVER be a decimal point number!
>
> So, a better way to write the signature for this function will be this:
> 
> ```lisp
> ;; Image -> Natural
> ```

2. **Purpose:** States what the function will be used for. How is the output related to the inputs?

```lisp
;; Produces double the number that is fed into it.
```

3. **Stub:** Just like the stub you know from C++: a minimal function definition that takes in all the required parameters, and returns a dummy value of the appropriate type without any real implementation.

```lisp
(define (double n) 0)
```

> Comment this out when we get to writing the function body.

4. **Tests:** Yes, we write the tests (define the examples) before we code the function body. NOT the other way round like you do it.

```lisp
(check-expect (double 0)      0)
(check-expect (double 2)      4)
(check-expect (double 4.3)  8.6)
```

> The stub makes sure that the tests themselves work. Obviously they aren't gonna all miraculously succeed without properly implementing it, but writing the tests becomes much easier with a definition of the function being there.
>
> Remember to run these tests immediately after you write them at least once to verify if they execute properly.

5. **Template:** This step seems rather redundant, but for the sake of staying with the course: this is like a stub but with a `(... <some-parameter>)` as the body (implying that we will do something with the said parameter).

```lisp
; (define (double n)
;     (... n))
```

6. **Function Body:** After all of the steps above, we finally implement the function based on all of the information/requirements we have gathered up to this point. We use/modify the template for this.

```lisp
(define (double n)
    (* n 2))
```

7. **Testing and Debugging:** After we have a function body implemented, we can begin testing and debugging the code with the help of the tests we wrote earlier, and with the help of the requirements we've gathered so far to ensure that we get the results that we desire.

## End Result
```lisp
;; Number -> Number
;; Produces double the number that is fed into it.
; (define (double n) 0)    ; stub

(check-expect (double 0)      0)
(check-expect (double 2)      4)
(check-expect (double 4.3)  8.6)

; (define (double n)       ; template
;    (... n))

(define (double n)
    (* n 2))
```