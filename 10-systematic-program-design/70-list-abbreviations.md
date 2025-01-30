# List Abbreviations
These are a shorthand for the `cons` notation which allow you to create lists without having to write a `cons` expression for every element in the list.
```lisp
;; Both of the expressions below produce the same value.
(cons "a" (cons "b" (cons "c" empty)))
(list "a" "b" "c")
```

> Make sure you see the difference between the two! Given below is an example illustrating why you need to be conscious of which notation you are using.
> ```lisp
> (define L1 (list "b" "c"))
>
> (cons "a" L1)
> > (list "a" "b" "c")
>
> (list "a" L1)
> > (list "a" (list "b" "c"))
> ```

## Appending Lists
We use the `append` primitive for this purpose.
```lisp
(define L1 (list "b" "c"))
(define L2 (list "d" "e" "f"))

;; (append <list-0> <list-1> ...)
(append L1 L2)
> (list "b" "c" "d" "e" "f")
```

> Note that append only concatenates lists. It does **not** add new elements to a pre-existing list.
