if __name__ == '__main__':
    n = int(input())
    result = 0
    if n > 0:
        for i in range(1, n + 1):
            digits = 1
            temp = i
            while temp >= 10:
                temp //= 10
                digits += 1
            result = result * (10 ** digits) + i
        print(result)
    else:
        print(0)

'''
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .

Constraints


Output Format

Print the list of integers from  through  as a string, without spaces.

Sample Input 0

3
Sample Output 0

123

'''