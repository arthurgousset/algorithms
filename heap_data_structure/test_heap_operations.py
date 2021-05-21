# import library for Python testing
import unittest
from unittest import TestCase

# import library to facilitate testing
import random

# import functions to be tested
from heap_operations import *


class TestHeapOperations(TestCase):
    def test_parent_and_child(self):
        a = [1, 3, 5, 6, 7]
        test_heap = Heap(a)
        self.assertEqual(test_heap.parent(a.index(5)), 0)
        self.assertEqual(test_heap.left(0), test_heap.a.index(3))
        self.assertEqual(test_heap.right(0), test_heap.a.index(5))

    def test_max_heapify(self):
        a = [1, 3, 5, 6, 7]
        test_heap = Heap(a)
        test_heap.max_heapify(0)
        self.assertListEqual(test_heap.a, [5, 3, 1, 6, 7])

    def test_exchange(self):
        a = [1, 3, 5, 6, 7]
        test_heap = Heap(a)
        test_heap.exchange(0, 3)
        self.assertListEqual(test_heap.a, [6, 3, 5, 1, 7])

    def test_heapsort(self):
        # generate random length
        n = random.randint(1, 30)
        # generate random list
        randomlist = []
        sortedlist = []
        for i in range(n):
            x = random.randint(1, 30)
            randomlist.append(x)
            sortedlist.append(x)
        # create heap
        test_heap = Heap(randomlist)
        test_heap.heapsort()
        # sort list using in-built function
        sortedlist.sort()
        # compare results
        self.assertListEqual(test_heap.a, sortedlist)
        # Uncomment to debug
        # print('{} = {}'.format(test_heap.a, 'heapsort'))
        # print('{} = {}'.format(sortedlist, 'in-built sort'))

    def test_build_max_heap(self):
        # generate random length
        n = random.randint(1, 100)
        # generate random list
        a = []
        for i in range(n):
            x = random.randint(1, 1000)
            a.append(x)
        # create heap
        test_heap = Heap(a)
        # build heap
        test_heap.build_max_heap()
        # test heap condition
        random_node = random.randint(1, n // 2 - 1)
        self.assertGreater(a[random_node], a[test_heap.left(random_node)])
        self.assertGreater(a[random_node], a[test_heap.right(random_node)])
        # Uncomment to debug
        # print('{} = {} > {} = {}'.format('random node key', a[random_node],
        #                                  'left child key', a[test_heap.left(random_node)]))
        # print('{} = {} > {} = {}'.format('random node key', a[random_node],
        #                                  'right child key', a[test_heap.right(random_node)]))


class TestPriorityQueueOperations(TestCase):
    def test_max_priority_queue_initialisation_and_maximum(self):
        # generate random length
        n = random.randint(1, 100)
        # generate random list
        testlist = []
        comparablelist = []
        for i in range(n):
            x = random.randint(1, 1000)
            testlist.append(x)
            comparablelist.append(x)
        # create (max) priority queue
        test_pq = MaxPriorityQueue(testlist)
        # test priority queue
        comparablelist.sort(reverse=True)
        self.assertEqual(test_pq.a[0], comparablelist[0])
        # Uncomment to debug
        # print('{} = {}'.format(test_pq.a, 'test priority queue'))
        # print('{} = {}'.format(comparablelist, 'sorted comparable list'))
        # print('[{}]  {} = {} [{}]'.format('priority queue root', test_pq.a[0],
        #                                   comparablelist[0], 'largest element in list'))

    def test_extract_max(self):
        # generate random length
        n = random.randint(1, 100)
        # generate random list
        testlist = []
        for i in range(n):
            x = random.randint(1, 1000)
            testlist.append(x)
        # create (max) priority queue
        test_pq = MaxPriorityQueue(testlist)
        # test extract max multiple times
        for i in range(n - 4):
            test_pq.extract_max()
            # test heap condition
            random_node = random.randint(1, test_pq.heap_size // 2 - 1)
            self.assertGreaterEqual(test_pq.a[random_node],
                                    test_pq.a[test_pq.left(random_node)])
            self.assertGreaterEqual(test_pq.a[random_node],
                                    test_pq.a[test_pq.right(random_node)])
            # Uncomment to debug
            # print('{} = {} \n {} = {} \n {} = {}'.format(
            #     i, 'i',
            #     test_pq.heap_size, 'heap size',
            #     len(test_pq.a), 'list size')
            # )
            # print('{} = {} > {} = {}'.format('random node key', test_pq.a[random_node],
            #                                  'left child key', test_pq.a[test_pq.left(random_node)]))
            # print('{} = {} > {} = {}'.format('random node key', test_pq.a[random_node],
            #                                  'right child key', test_pq.a[test_pq.right(random_node)]))
            # print('{} = {} \n '.format('priority queue', test_pq.a))

    def test_increase_key(self):
        # generate random length
        n = random.randint(1, 100)
        # generate random list
        testlist = []
        for i in range(n):
            x = random.randint(1, 1000)
            testlist.append(x)
        # create (max) priority queue
        test_pq = MaxPriorityQueue(testlist)
        # test increase key multiple times
        for i in range(n // 2):
            # Uncomment to debug
            # print('\n{} = {}: {}'.format(test_pq.heap_size, 'heap size', test_pq.a))
            # Increase random element
            random_node: int = random.randint(0, n - 1)
            randon_addition = random.randint(0, 1000)
            previous_key = test_pq.a[random_node]
            new_key = test_pq.a[random_node] + randon_addition
            test_pq.increase_key(random_node, new_key)
            # test heap condition
            new_index = test_pq.a.index(new_key)
            # test (only if node has left child)
            if test_pq.left(new_index) < test_pq.heap_size:
                self.assertGreaterEqual(test_pq.a[new_index],
                                        test_pq.a[test_pq.left(new_index)])
            else:
                print('Has no left child')
            # test (only if node has right child)
            if test_pq.right(new_index) < test_pq.heap_size:
                self.assertGreaterEqual(test_pq.a[new_index],
                                        test_pq.a[test_pq.right(new_index)])
            else:
                print('Has no right child')
            # Uncomment to debug
            # print('{} = {}: {}'.format(test_pq.heap_size, 'heap size', test_pq.a))
            # print('{} = {} \n{} = {} \n{} = {} \n{} = {}'.format(
            #     random_node, 'random index',
            #     previous_key, 'previous key',
            #     new_key, 'new key',
            #     new_index, 'new_index'
            # )
            # )
            # if test_pq.left(new_index) < test_pq.heap_size:
            #     print('{} = {} > {} = {}'.format('random node key', test_pq.a[new_index],
            #                                      'left child key', test_pq.a[test_pq.left(new_index)]))
            # if test_pq.right(new_index) < test_pq.heap_size:
            #     print('{} = {} > {} = {}'.format('random node key', test_pq.a[new_index],
            #                                      'right child key', test_pq.a[test_pq.right(new_index)]))

    def test_max_insert(self):
        # generate random length
        n = random.randint(1, 100)
        # generate random list
        testlist = []
        for i in range(n):
            x = random.randint(1, 1000)
            testlist.append(x)
        # create (max) priority queue
        test_pq = MaxPriorityQueue(testlist)
        # Uncomment to debug
        # print('\n{} = {}: {}'.format(test_pq.heap_size, 'heap size', test_pq.a))
        # test insert multiple times
        for i in range(random.randint(1, 100)):
            # generate new key value
            new_key = random.randint(1, 1000)
            test_pq.max_insert(new_key)
            # test heap condition
            new_element_index = test_pq.a.index(new_key)
            if test_pq.left(new_element_index) < test_pq.heap_size:
                self.assertGreaterEqual(test_pq.a[new_element_index],
                                        test_pq.a[test_pq.left(new_element_index)])
            else:
                print('\n{}\n{} = {}\n{} = {} > {} = {}'.format('Has no left child',
                                                                new_element_index, 'index of new element',
                                                                test_pq.left(new_element_index), 'index of left child',
                                                                'heap size', test_pq.heap_size))
            # test heap condition (only if node has right child)
            if test_pq.right(new_element_index) < test_pq.heap_size:
                self.assertGreaterEqual(test_pq.a[new_element_index],
                                        test_pq.a[test_pq.right(new_element_index)])
            else:
                print('\n{}\n{} = {}\n{} = {} > {} = {}'.format('Has no right child',
                                                                new_element_index, 'index of new element',
                                                                test_pq.right(new_element_index), 'index of right child',
                                                                'heap size', test_pq.heap_size))
            # Uncomment to debug
            # print('\n{} = {}\n{} = {}'.format(new_key, 'key',
            #                                   new_element_index, 'index of new element'))
            # print('{} = {}: {}'.format(test_pq.heap_size, 'heap size', test_pq.a))


if __name__ == '__main__':
    unittest.main()
