# Traversal
- pre-order (cur -> left -> right)
- in-order (left -> cur -> right)
- post-order (left -> right -> cur)

## Recursive:
```java
void f(head) {
    if (head == null)
        return
    # 1 (pre-order)
    f(head.left);
    # 2 (in-order)
    f(head.right);
    # 3 (post-order)
}
```

## Non-Recursive:
### InOrder 
```python
cur = root
while cur or stack:
    ## 1. push the left boundary into stack
    while cur:
        stack.push(cur)
        cur = cur.left
    ## 2. pop cur & print cur, then cur = cur.right
    cur = stack.pop()
    ans.append(cur.val)
    cur = cur.right
```

### PreOrder
先右后左压，先左后右弹
```python
## push root
if root:
    stack.push(root)
while stack:
    ## 1. pop cur & print cur
    ## 2. push right, then push left （先右后左压）
```