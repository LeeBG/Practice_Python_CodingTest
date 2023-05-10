
"""
h, b, c, s 가 공백을 두고 입력된다.
h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.
bit 단위이기 때문에 MB로 표현하려면 /8/1024/1024 
"""

h,b,c,s = map(int,input().split())

total_bit = h * b * c * s
total_mb = total_bit/8/1024/1024
print("%.1f MB"%total_mb)
