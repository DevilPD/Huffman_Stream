'''

n[2,1] = str(int(n[2,1]) + 1) # ex ) 값 'a' 의 개수 + 1


    # import numpy as np

    # def _read_txt(txt: str):
    #     res = []
    #     f = open(txt, 'r') # test.txt
    #     lines = f.readlines()
    #     f.close()

    #     return lines

    # def _create_arr():
    #     n = np.empty((0,2), int)  

    #     return n

    # default_arr = _create_arr()
    # lists_set = set()
    # txt = _read_txt(txt)

    # for r_t in txt:
    #     for r in r_t:
    #         lists_set.add(r) 
    # txt의 문자 list 생성 (중복x)

    # for l in lists_set:
    #     default_arr = np.append(default_arr, np.array([[l, 0]]), axis=0) 
    # 각 txt 마다 [txt, 0] 형태로 2차원 배열 생성 

    # for l_s in lists_set:
    #     cnt = 0
    #     for t in txt:
    #         tmp = t.count(l_s)
    #         cnt += tmp
    #     print('.')
    #     num = list(lists_set).index(l_s)
    #     default_arr[num,1] = int(default_arr[num,1]) + cnt 
    #########

'''

from collections import Counter

def get_charcnt(txt: str) -> list:

    test = Counter(txt)
    mst = test.most_common(len(txt))

    return mst