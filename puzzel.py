a, b, c , d  = map(int,(input().split()))
if a+b*c==d or a+b-c==d or a-b+c==d or a-b*c==d or a*b+c==d or a*b-c ==d:
    print("yes")
else:
    print("no")