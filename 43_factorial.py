def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)


def factorialTrailingZeroes(number):
    fac=factorial(number)
    count=0
    while (fac%10==0):
        count+=1
        fac=fac/10
        return count


if __name__ == '__main__':
  number=int(input("Enter a number: "))
  fac=factorial(number)
  print(f"The factorial of a {number} is {fac}")
  print(factorialTrailingZeroes(number))