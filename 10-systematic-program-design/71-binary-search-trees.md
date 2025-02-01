# Searching through Data
If you have ever tried to implement an algorithm to look up the value with some key in a list, you know how inefficient things can get if the list is really large. You might recognize this problem from MIT-6001x and already know that if the list is sorted, we can just use binary search to very quickly find the value that we are looking for.

However, there is one key difference. Unlike in MIT-6001x, we can only use `first` and `rest` to traverse the list rather than directly accessing the value at a specific position. Perhaps lists aren't the way to go in the end... 

This prompts us to think of a new way of representing the information that will make it easier *and* more efficient to search through.

## Binary Search Trees
These are used for exactly what you think they will be used for. There are two invariants that define a binary search tree:
1. All nodes to the left of a given node are smaller in key than it; and
2. All nodes to the right of the said node are larger in key than it.

Given below is a diagram illustrating what such a tree of the numbers from 1 through 9 would look like.
```
                                5
                              /   \
                            2       8
                           / \     / \
                          1   3   7   9
                               \ /
                               4 6
```

The exhibit below houses an example data definition for a binary search tree with the examples representing the different sub-trees that make up the example tree that we can see above but with the numbers' names as the values.
```lisp
(define-struct bst (key value left right))
;; BST (Binary Search Tree) is one of:
;; - false
;; - (make-bst Natural[1, 9] String BST BST)
;; interp. false means no/empty tree
;;         (make-bst key value left right) represents a tree node where
;;         key   is the key/ID of the node
;;         value is the value of the node
;;         left  is the BST to the left of the node
;;         right is the BST to the right of the node
;; INVARIANT: For any given node:
;;            All nodes in left have a key less than key.
;;            All nodes in right have a key greater than key.
;;            No key appears twice.
;    -- EXAMPLES
(define BST0 false)
(define BST3 (make-bst 3 "three"
                       false
                       (make-bst 4 "four"
                                 false
                                 false)))
(define BST7 (make-bst 7 "seven"
                       (make-bst 6 "six"
                                 false
                                 false)
                       false))
(define BST2 (make-bst 2 "two"
                       (make-bst 1 "one"
                                 false
                                 false)
                       BST3))
(define BST8 (make-bst 8 "eight"
                       BST7
                       (make-bst 9 "nine"
                                 false
                                 false)))
(define BST5 (make-bst 5 "five"
                       BST2
                       BST8))
;    -- TEMPLATE
#;
(define (fn-for-bst bst)
  (cond [(false? bst) (...)]
        [else
         (... (bst-key   bst)
              (bst-value bst)
              (fn-for-bst (bst-left  bst))
              (fn-for-bst (bst-right bst)))]))
;; Template Rules Used:
;; - One of:          2 cases
;; - Atomic Distinct: false
;; - Compound:        (make-bst Natural[0, 9] String BST BST)
;; - Self-Reference:  (bst-left  bst) is a BST
;; - Self-Reference:  (bst-right bst) is a BST
```

### Search Algorithm
1. Check if the current node has the value that we are looking for.
    - If yes, then we are done!
    - If no, then we continue with the next step.
2. Compare its key with our desired key.
    - If the target key is smaller than the current node's key, then we discard the part of the tree to the right of the node and look for it in the left sub-tree.
    - If the target key is larger than the key of the current node, then we instead discard the left half, and repeat the algorithm from the node to the right.

The example below illustrates how this algorithm can be implemented.
```lisp
;; BST, Natural -> String or false
;; Try to find node with given key, if found produce value; if not found produce false.
;    -- STUB
; (define (lookup-key bst key) "")
;    -- EXAMPLES
(check-expect (lookup-key BST0 5) false)

(check-expect (lookup-key BST1 1) "one")
(check-expect (lookup-key BST1 0) false)      ; L Fail
(check-expect (lookup-key BST1 3) false)      ; R Fail

(check-expect (lookup-key BST5 1) "one")      ; L L Succeed
(check-expect (lookup-key BST5 3) "three")    ; L R Succeed
(check-expect (lookup-key BST5 7) "seven")    ; R L Succeed
(check-expect (lookup-key BST5 9) "nine")     ; R R Succeed
;    -- TEMPLATE
; Template from BST, with additional atomic parameter `key`
(define (lookup-key bst key)
  (cond [(false? bst) false]
        [else
         (cond [(= key (node-key bst)) (node-val bst)]
               [(< key (node-key bst)) (lookup-key (node-l bst) key)]
               [(> key (node-key bst)) (lookup-key (node-r bst) key)])]))
```

### Time Complexity
Since we are discarding half of the remaining search range on every step of the algorithm, it scales logarithmically and has a time complexity of `O(log(n))`, just like you might remember!

> Keep in mind that the tree illustrated above is not the only valid way to structure the information as a binary search tree. Given below is another example of how we could have implemented it.
> ```
>                           1
>                            \
>                             2
>                              \
>                               3
>                                \
>                                 4
>                                  \
>                                   5
>                                    \
>                                     6
>                                      .
>                                       .
>                                        .
> ```
> This is a perfectly valid tree, but it doesn't really offer any benefits over just using a list, does it? This should give you a good idea of why the way we structure data matters.
