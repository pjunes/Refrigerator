import copy

class Heap:
    #######################
    ##### Heap Basics #####
    #######################

    def __init__(self):
        self.data = [None]
        self.last = 0

    def left_child(self, i):
        if 2 * i > self.last: # 왼쪽 자식이 없다면,
            return None # None
        return 2 * i

    def right_child(self, i):
        if 2 * i + 1 > self.last:  # 오른쪽 자식이 없다면,
            return None
        return 2 * i + 1

    def parent(self, i):
        if i == 1: # 부모가 없다면, (루트라면,)
            return None
        return int(i / 2)

    def swap_element(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        return

    # def downHeap(self, i):
    #     if not self.left_child(i):
    #         return
    #     greater = self.left_child(i) # 왼쪽 자식이 있다면, 우선 greater = left
    #
    #     if self.right_child(i): # 오른쪽 자식이 있다면,
    #         if self.data[self.right_child(i)] > self.data[greater]: # 오른쪽 자식과 왼쪽 자식의 key 비교, 오른쪽이 더 크다면,
    #             greater = self.right_child(i) # greater = right
    #
    #     if self.data[i] >= self.data[greater]: # downHeap의 대상과 자식 중 더 큰것을 비교, 대상이 더 크거나 같다면,
    #         return # Heap 속성을 만족하므로 종료.
    #
    #     self.swap_element(i, greater) # 자식이 더 크다면, 서로 위치를 바꾸고,
    #     self.downHeap(greater) # 바꾼 위치에서 다시 downHeap 수행.

    def downHeap_by_date(self, i):
        if not self.left_child(i):
            return
        greater = self.left_child(i) # 왼쪽 자식이 있다면, 우선 greater = left

        if self.right_child(i): # 오른쪽 자식이 있다면,
            if self.data[self.right_child(i)].get_date() > self.data[greater].get_date(): # 오른쪽 자식과 왼쪽 자식의 key 비교, 오른쪽이 더 크다면,
                greater = self.right_child(i) # greater = right

        if self.data[i].get_date() >= self.data[greater].get_date(): # downHeap의 대상과 자식 중 더 큰것을 비교, 대상이 더 크거나 같다면,
            return # Heap 속성을 만족하므로 종료.

        self.swap_element(i, greater) # 자식이 더 크다면, 서로 위치를 바꾸고,
        self.downHeap_by_date(greater) # 바꾼 위치에서 다시 downHeap 수행.

    # def downHeap_by_name(self, i):
    #     if not self.left_child(i):
    #         return
    #     greater = self.left_child(i) # 왼쪽 자식이 있다면, 우선 greater = left
    #
    #     if self.right_child(i): # 오른쪽 자식이 있다면,
    #         if self.data[self.right_child(i)].get_name > self.data[greater].get_name: # 오른쪽 자식과 왼쪽 자식의 key 비교, 오른쪽이 더 크다면,
    #             greater = self.right_child(i) # greater = right
    #
    #     if self.data[i].get_name >= self.data[greater].get_name: # downHeap의 대상과 자식 중 더 큰것을 비교, 대상이 더 크거나 같다면,
    #         return # Heap 속성을 만족하므로 종료.
    #
    #     self.swap_element(i, greater) # 자식이 더 크다면, 서로 위치를 바꾸고,
    #     self.downHeap_by_name(greater) # 바꾼 위치에서 다시 downHeap 수행.

    # def upHeap(self, i):
    #     if not self.parent(i): # i가 루트라면,
    #         return
    #
    #     if self.data[i] <= self.data[self.parent(i)]: # Heap 속성을 만족한다면,
    #         return
    #
    #     self.swap_element(i, self.parent(i)) # i가 root가 아니고 Heap 속성도 만족하지 않는다면, swap
    #     self.upHeap(self.parent(i)) # parent에서 upHeap 수행.

    def upHeap_by_date(self, i):
        if not self.parent(i): # i가 루트라면,
            return

        if self.data[i].get_date() <= self.data[self.parent(i)].get_date(): # Heap 속성을 만족한다면,
            return

        self.swap_element(i, self.parent(i)) # i가 root가 아니고 Heap 속성도 만족하지 않는다면, swap
        self.upHeap_by_date(self.parent(i)) # parent에서 upHeap 수행.

    # def upHeap_by_name(self, i):
    #     if not self.parent(i): # i가 루트라면,
    #         return
    #
    #     if self.data[i].get_name() <= self.data[self.parent(i)].get_name(): # Heap 속성을 만족한다면,
    #         return
    #
    #     self.swap_element(i, self.parent(i)) # i가 root가 아니고 Heap 속성도 만족하지 않는다면, swap
    #     self.upHeap_by_name(self.parent(i)) # parent에서 upHeap 수행.

    ################
    ##### CRUD #####
    ################

    # def insert_item(self, item):
    #     self.last += 1
    #     self.data.append(item)
    #     self.upHeap(self.last)

    def insert_item_by_date(self, item):
        self.last += 1
        self.data.append(item)
        self.upHeap_by_date(self.last)

    # def remove_max(self):
    #     if self.last == 0:
    #         return None
    #
    #     self.swap_element(1, self.last) # root와 last swap
    #     max = self.data.pop() # last 제거, max에 값 저장.
    #     self.last -= 1
    #
    #     self.downHeap(1) # Heap 속성 복구
    #     return max

    def remove_max_by_date(self):
        if self.last == 0:
            return None

        self.swap_element(1, self.last) # root와 last swap
        max = self.data.pop() # last 제거, max에 값 저장.
        self.last -= 1

        self.downHeap_by_date(1) # Heap 속성 복구
        return max

    # def remove_idx(self, i):
    #     if i > self.last:
    #         return None # index 범위 초과
    #
    #     self.swap_element(i, self.last)  # i와 last swap
    #     removed = self.data.pop()  # last 제거, removed에 값 저장.
    #     self.last -= 1
    #
    #     self.upHeap(i) # Heap 속성 복구
    #     self.downHeap(i)  # Heap 속성 복구
    #     return removed

    def remove_idx_by_date(self, i):
        if i > self.last:
            return None # index 범위 초과

        self.swap_element(i, self.last)  # i와 last swap
        removed = self.data.pop()  # last 제거, removed에 값 저장.
        self.last -= 1

        self.upHeap_by_date(i) # Heap 속성 복구
        self.downHeap_by_date(i) # Heap 속성 복구
        return removed


    ######################
    ##### Heap inout #####
    ######################

    # self.data 정렬된 상태로 바꿈.
    # def in_place_heap_sort(self):
    #     for i in range(self.last, 1, -1): # self.last 부터 2까지
    #         self.swap_element(1, i)
    #         self.last -= 1
    #         self.downHeap_by_date(1)
    #     return

    # 정렬된 새로운 list return
    # def get_sorted(self):
    #     result = copy.deepcopy(self)
    #     for i in range(result.last, 1, -1): # self.last 부터 2까지
    #         result.swap_element(1, i)
    #         result.last -= 1
    #         result.downHeap(1)
    #     return result

    def get_sorted_by_date(self):
        result = copy.deepcopy(self)
        for i in range(result.last, 1, -1): # self.last 부터 2까지
            result.swap_element(1, i)
            result.last -= 1
            result.downHeap_by_date(1)
        return result

    # def get_sorted_by_name(self):
    #     result = copy.deepcopy(self)
    #     for i in range(result.last, 1, -1): # self.last 부터 2까지
    #         result.swap_element(1, i)
    #         result.last -= 1
    #         result.downHeap_by_name(1)
    #     return result

    # def print_heap(self):
    #     print(self.data)

    # def print_heap_items(self):
    #     for item in self.data[1:]:
    #         print(item)

    # def build_heap(self, data_list): # 비재귀적 상향식 힙생성.
    #     self.data.extend(data_list)
    #     self.last = len(data_list)
    #     for i in range(self.last, 0, -1): # self.last 부터 1까지
    #         self.downHeap(i)
    #     return

    def build_heap_by_date(self, data_list): # 비재귀적 상향식 힙생성.
        self.data.extend(data_list)
        self.last = len(data_list)
        for i in range(self.last, 0, -1): # self.last 부터 1까지
            self.downHeap_by_date(i)
        return
