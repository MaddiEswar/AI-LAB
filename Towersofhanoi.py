A = [3, 2, 1]
B = []
C = []

def move(n, source, target, auxiliary):
    if n > 0:
       
        move(n - 1, source, auxiliary, target)

        target.append(source.pop())

        print(A, B, C, "->",end="")

        move(n - 1, auxiliary, target, source)

move(3, A, C, B)
