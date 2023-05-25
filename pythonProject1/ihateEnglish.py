# 영어가 싫어요
def solution(numbers):
  nums = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
  answer = ""
  for i in list(nums.keys()):
    if i in numbers:
      numbers = numbers.replace(i, str(nums.get(i)))
  return int(numbers)

print(solution('onefourzerosixseven'))