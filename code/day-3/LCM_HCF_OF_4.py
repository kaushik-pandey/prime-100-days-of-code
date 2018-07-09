num1 = int(input("Enter 4 numbers: "))
num2 = int(input())
num3 = int(input())
num4 = int(input())


def rem_fun(n1, n2):
    r = n1 % n2
    return r


rem = 1

arg1 = max(num1, num2)
arg2 = min(num1, num2)


def lcm_hcf_finder(a1, a2, r):
    while r != 0:

        r = rem_fun(a1, a2)
        if rem == 0:
            return a2
            # print("HCF = ", arg2)
            # print("LCM = ", int((num1*num2)/arg2))
            break
        a1 = a2
        a2 = rem


arg1 = lcm_hcf_finder(arg1, arg2, 1)
arg2 = num3
arg1 = lcm_hcf_finder(arg1, arg2, 1)
arg2 = num4
arg1 = lcm_hcf_finder(arg1, arg2, 1)
print(arg1)
print("LCM = ", int((num1*num2)/arg1))
# while rem != 0:
#
#     rem = rem_fun(arg1, arg2)
#     if rem == 0:
#
#         # print("HCF = ", arg2)
#         # print("LCM = ", int((num1*num2)/arg2))
#         break
#     arg1 = arg2
#     arg2 = rem
