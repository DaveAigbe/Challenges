def plusOne(digits: list[int]):
    into_string = [str(x) for x in digits]
    into_string = ''.join(into_string)
    into_string = int(into_string)
    into_string += 1
    into_string = str(into_string)
    digits = [int(x) for x in into_string]
    return digits


print(plusOne([0]))


class Solution(object):
    def plus_one2(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        complete = ''
        for i in digits:
            complete += str(i)

        addOne = list(str(int(complete) + 1))

        addOne = [int(num) for num in addOne]

        return addOne