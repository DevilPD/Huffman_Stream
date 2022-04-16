from queue import PriorityQueue

class HuffNode:
    def __init__ (self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
        self.res = []

    def pre(self, parent=None, parent_ent=[], ent=None):
        if ent is not None:
            parent_ent.append(ent)
            print('==================')
            print(f'현재 {self.symbol}' , parent_ent)
            print('빈도수 ', self.freq)
            print('==================')
        else:
            parent = self

        if (self.left is not None):
            self.left.pre(parent, parent_ent, "0")
        if self.symbol == ' ':
            print('==================')
            print('중간트리 ', parent_ent)
            print('빈도수 ', self.freq)
            if len(parent_ent) == 1:
                del parent_ent[0]
            else:
                del parent_ent[-1]
            print('삭제후 ', parent_ent)
            print('==================')
        if (self.right is not None):
            self.right.pre(parent, parent_ent, "1")
        if self.symbol == ' ':
            print('==================')
            print('중간트리 ', parent_ent)
            print('빈도수 ', self.freq)
            if len(parent_ent) == 1:
                del parent_ent[0]
            else:
                del parent_ent[-1]
            print('삭제후 ', parent_ent)
            print('==================')

        if (self.left is None) and (self.right is None):
            res = ''.join(parent_ent)
            parent.res.append((self.symbol, res))

    def __eq__ (self, other):
            return self.freq == other.freq

    def __ne__ (self, other):
        return self.freq != other.freq

def huffman (n, PQ):
    for _ in range(n - 1):
        p = PQ.get()[1]
        q = PQ.get()[1]
        r = HuffNode(' ', p.freq + q.freq)
        r.left = p
        r.right = q
        PQ.put((r.freq, r))
    hn = PQ.get()[1]
    return hn

if __name__ == "__main__":
    data_set = [('A',100),['B',94],['C',48],('K',99)]
    PQ = PriorityQueue()
    for i in range(len(data_set)):
        node = HuffNode(data_set[i][0], data_set[i][1])
        PQ.put((node.freq, node))

    root = huffman(len(data_set), PQ)
    root.pre()
    for r in root.res:
        print(r, len(r[1]), 'bit')
    print(data_set)