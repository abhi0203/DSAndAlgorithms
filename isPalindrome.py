def isPalindrome(strng):
    revStrng= reverse(strng)
    if strng.lower()==revStrng.lower():
        return True
    return False
def reverse(strng):
    if len(strng)==0:
        return ""
    else:
        return reverse(strng[1:]) + strng[0]


print(isPalindrome("Nit!in"))