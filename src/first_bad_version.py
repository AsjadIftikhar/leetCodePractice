BAD = 1


def isBadVersion(version):
    return version >= BAD


def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return right

num = 5
print(firstBadVersion(num))
