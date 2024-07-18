def multiply(num1: str, num2: str) -> str:
    ans = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            ans[i+j+1] += int(num1[i]) * int(num2[j])
    carry = 0
    for i in reversed(range(len(ans))):
        carry += ans[i]
        ans[i] = carry % 10
        carry //= 10
    j = 0
    while j < len(ans) - 1 and ans[j] == 0:
        j += 1
    return "".join([str(d) for d in ans[j:]])

if __name__ == '__main__':
    print(multiply('123', '456'))
    print(multiply('0', '1'))