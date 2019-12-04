from dataclasses import dataclass
from typing import List, Dict


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            if not path_in(result[-1], folder[i]):
                result.append(folder[i])
        return result

    def removeSubfolders_slow(self, folder: List[str]) -> List[str]:
        root = Node(["0"])
        folders = list(map(parse, folder))
        for f in folders:
            root.add_to_tree(f)
        for f in folders:
            root.remove_children_if_more(f)
        result = []
        root.collect("", result)
        return result


@dataclass
class Node:
    word: str
    children: Dict[str, 'Node']

    def __init__(self, path):
        self.word = path[0]
        rest = path[1:]
        self.children = {}
        if rest:
            self.children[rest[0]] = Node(rest)

    def add_to_tree(self, path):
        head = path[0]
        rest = path[1:]
        if head not in self.children:
            self.children[head] = Node(path)
        elif head in self.children and rest:
            self.children[head].add_to_tree(rest)

    def remove_children_if_more(self, path):
        head = path[0]
        rest = path[1:]
        if not rest and head in self.children:
            self.children[head] = Node([head])
        elif head in self.children:
            self.children[head].remove_children_if_more(rest)

    def collect(self, path: str, result: List[str]):
        if self.word != '0':
            path += '/' + self.word
        if not self.children:
            result.append(path)
        else:
            for child in self.children.values():
                child.collect(path, result)


def path_in(a, b):
    for k, j in zip(parse(a), parse(b)):
        if k != j:
            return False
    return True


def parse(path: str) -> [str]:
    return path[1:].split("/")


if __name__ == "__main__":
    # folder = ["/a", "/a/b/c", "/a/b/d"]
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    # folder = ["/ah/al/am","/ah/al"]
    # folder = ["/ap/ax/ay", "/ap/aq/au", "/aa/ab/af", "/aa/ai/am", "/ap/ax", "/ap/aq/ar"]
    folder.sort()
    print(folder)
    print(Solution().removeSubfolders(folder))
