#coding=utf-8
import time
from random import Random
'''
    新的字符串匹配算法:以往的字符串匹配算法要么从前往后匹配(基于前缀 如KMP)，要么从后往前匹配(基于后缀如BM  Horspool Sunday),KR是利用hash函数进行字符串匹配，AC自动机也是从前往后读入待匹配串。
    考虑下分段匹配前进的思路:
        先匹配字符串的第一个字符，找出文本中所有的该字符的index
        在所有的1-index再继续筛选满足2-index，直到满足length-index即为所有的文本中满足该模式的字符串
'''


def random_str(random_length=8, chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'):
    ranstr = ''
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        ranstr += chars[random.randint(0, length)]
    return ranstr


def section_string_match(teststring, model):
    pos_index = []
    # 初始化pos_index
    for i in range(len(teststring)):
        if teststring[i] == model[0]:
            pos_index.append(i)
    # 筛选
    cur_check_pos = 1
    while len(pos_index) != 0 and cur_check_pos != len(model):
        pos_index = filter(lambda x: x+cur_check_pos < len(teststring) and teststring[x+cur_check_pos] == model[cur_check_pos], pos_index)
        cur_check_pos += 1
    # 检查结果
    return pos_index


def BM(teststring, model):
    pass


def Horspool(teststring, model):
    pass


def Sunday(teststring, model):
    pass


def KMP(teststring, model):
    pass

def AD(teststring, model):
    pass


def test(test_method):
    #调节chars的类型，使满足不同的测试数据要求: 1.重复字母较多的情况 2.重复字母较少的情况
    testdata=['abcde', 'abcdefghij', 'abcdefghijklmno', 'abcdefghijklmnopqrst','abcdefghijklmnopqrstuvwxyz']
    for i in testdata:
        teststring = random_str(10000000, i)
        model = random_str(3, i)
        print 'atom string: '+i
        print 'teststring: '+teststring
        print 'model: '+model
        begin_time = time.time()
        print test_method(teststring, model)
        end_time = time.time()
        print 'time: '+str(end_time-begin_time)

if __name__ == '__main__':
    test(section_string_match)
