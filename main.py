# https://kldp.org/node/155026 < 개똑똑하당
import base64

from queue import PriorityQueue

import pkg.CharCnt as charcnt
import pkg.HuffTree as huf 

res = []

def img_to_string(filename): # filename = "./testfiles/test.exe"
    ''' 파일명(filename)을 입력으로 받아 base64로 인코딩한 문자열을 리턴한다 '''
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read()) # base64.b64encode(f.read())

if __name__ == '__main__':
    PQ = PriorityQueue()
    img = './testfiles/test.bmp'
    data = img_to_string(img) # 파이썬에서 제공하는 base64 라이브러리를 이용하여 바이너리 파일을 읽고 인코딩
    data_set = charcnt.get_charcnt(data.decode()) # 문자별 빈도수 조사   

    for i in range(len(data_set)):
        node = huf.HuffNode(data_set[i][0], data_set[i][1]) # 문자, 빈도수를 인자로 하는 HuffNode 객체 생성
        PQ.put((node.freq, node)) # 빈도수를 기준으로 오름차순으로 객체를 저장하는 우선순위큐에 넣음

    root = huf.huffman(len(data_set), PQ) # 우선순위 큐에 있는 데이터를 기반으로 이중노드트리 생성
    root.pre() # root.res 값에 
    for r in root.res:
        print(r, len(r[1]), 'bit')

    res = []
    f = open("res.txt", 'w')
    for d in data.decode():
        for r in root.res:
            if d == r[0]:
                f.write(r[1])
                break
    f.close()