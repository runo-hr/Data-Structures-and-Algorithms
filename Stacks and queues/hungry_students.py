from collections import deque, Counter

class Stack:
    def __init__(self, lst=[]) -> None:
        self.stack = lst[::-1]
    
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            return None
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1
    
    def __len__(self):
        return len(self.stack)

class Queue:
    def __init__(self, lst=[]) -> None:
        self.q = deque(lst)
    
    def push(self, x):
        self.q.append(x)
    
    def pop(self):
        if len(self.q) > 0:
            self.q.popleft()
    
    def top(self) -> int:
        if len(self.q) > 0:
            return self.q[0]
        else:
            return -1

    def go_back(self):
        self.q.append(self.q.popleft())
    
    def __len__(self):
        return len(self.q)
    


class Solution:
    # O(n ** 2)
    def countStudents(self, students, sandwiches) -> int:
        students = Queue(students)
        sandwiches = Stack(sandwiches)
        total_combinations = len(students) ** 2
        for i in range(total_combinations):
            if sandwiches.top() == students.top() and sandwiches.top != -1:
                sandwiches.pop()
                students.pop()
            else:
                students.go_back()
        return len(students)
    
    # O(n)
    def countStudents_2(self, students, sandwiches) -> int:
        preferences = Counter(students)
        for sandwich in sandwiches:
            if preferences[sandwich] == 0:
                break
            else:
                preferences[sandwich] -= 1
        return sum(preferences.values())



s = Solution()
ans = s.countStudents_2(students=[1,1,1,0,0,1], sandwiches=[1,0,0,0,1,1])
print(ans)
