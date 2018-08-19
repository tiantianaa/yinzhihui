'''
@author: lianying
'''
class Sparking:
    @staticmethod
    def testcase(bits_num, key):
        cnt = 0
        while key:
            cnt += 1
            key &= key -1
        return bits_num - cnt

def main():
    s = Sparking()
    s.testcase(5, 5)

if __name__ == '__main__':
    main()
