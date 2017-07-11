class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        splitted = n.split(r'.')
        integer = ''
        float = ''

        a = splitted[0]
        if len(a) == 0 or a == '0':
            integer = '0'
            a = 0
        else:
            a = int(a)

        while a != 0:
            integer = str(a % 2) + integer
            a /= 2

        if len(splitted) != 1:
            b = splitted[1]
            if len(b) == 0 or b == '0':
                float = ''
                num = 0
            else:
                num = 1.0 * int(b) / (10 ** len(b))

            while num != 0:
                num *= 2
                if num >= 1:
                    float += '1'
                    num -= 1
                else:
                    float += '0'
                if len(float) > 32:
                    return 'ERROR'
            if float != '':
                return str(integer) + '.' + str(float)
        return str(integer)


if __name__ == '__main__':
    print(Solution().binaryRepresentation("3.72"))
    print(Solution().binaryRepresentation("3.5"))
    print(Solution().binaryRepresentation("3."))
    print(Solution().binaryRepresentation("0.5"))
