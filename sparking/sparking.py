'''
@author: lianying
'''
class Sparking:
    @staticmethod
    def testpoint(bits_num, key):
        cnt = 0
        while key:
            cnt += 1
            key &= key -1
        return bits_num - cnt
    # @staticmethod
    # def get_num_of_one(bits_num, key):
    #     cnt = 0
    #     while key:
    #         cnt += 1
    #         key &= key -1
    #     return cnt

def main():
    s = Sparking()
    s.testpoint(32, 5)

if __name__ == '__main__':
    main()
