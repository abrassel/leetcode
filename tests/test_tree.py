from indexed_tree import IndexedTree, EmptyIndexedTree

def test_insert():
    tree = EmptyIndexedTree()
    tree = tree.insert(2)
    assert tree.size == 1
    assert tree.get(0) == 2
    tree = tree.insert(1)
    assert tree.size == 2
    assert tree.left.size == 1
    assert tree.get(0) == 1
    assert tree.get(1) == 2
    tree = tree.insert(3)
    assert tree.get(0) == 1
    assert tree.get(1) == 2
    assert tree.get(2) == 3
    assert tree.size == 3
    assert tree.left.size == 1
    assert tree.right.size == 1

def test_remove():
    tree = EmptyIndexedTree()
    tree = tree.insert(2)
    tree = tree.insert(1)
    tree = tree.insert(4)
    tree = tree.insert(3)

    tree = tree.remove(2)
    assert tree.get(0) == 1
    assert tree.get(1) == 3
    assert tree.get(2) == 4

    tree = tree.remove(1)
    assert tree.get(0) == 3
    assert tree.get(1) == 4

    tree = tree.insert(1)
    tree = tree.insert(2)
    tree = tree.remove(4)
    assert tree.get(0) == 1
    assert tree.get(1) == 2
    assert tree.get(2) == 3

    tree = tree.remove(3)
    assert tree.get(0) == 1
    assert tree.get(1) == 2