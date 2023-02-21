class ListNode:
     def __init__(self, x='last_page'):
         self.val = x
         self.next = None
         self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.last = ListNode()
        self.home.next = self.last
        self.last.prev = self.home
        self.view = self.home
        self.max_forward, self.max_backward = 0, 0
        
    # O(1)    
    def visit(self, url: str) -> None:
        prev, new, next = self.view, ListNode(url), self.last
        new.next = next
        new.prev = prev
        prev.next = new
        next.prev = new
        self.view = new
        self.max_forward = 1
        self.max_backward += 1
    
    # O(n)    
    def back(self, steps: int) -> str:
        cur = self.view
        steps = min(steps, self.max_backward)
        for i in range(steps):
            if cur.prev:
                cur = cur.prev
            else:
                break 
        self.max_backward -= steps
        self.max_forward += steps
        self.view = cur
        return cur.val
        
    # O(n)
    def forward(self, steps: int) -> str:
        cur = self.view
        steps = min(steps, self.max_forward)
        for i in range(steps):
            if cur.next != self.last:
                cur = cur.next
            else:
                break
        self.max_backward += steps
        self.max_forward -= steps
        self.view = cur
        return cur.val

class BrowserHistory_array:
    def __init__(self, homepage:str) -> None:
        self.curr = 0
        self.len = 1
        self.history = [homepage]
    
    # O(1)
    def visit(self, url:str):
        if len(self.history) < self.curr + 2:
            self.history.append(url)
        else:
            self.history[self.curr + 1] = url
        self.curr += 1
        self.len = self.curr + 1
    
    # O(1)
    def back(self, steps: int):
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    # O(1)
    def forward(self, steps: int):
        self.curr = min(self.curr + steps, self.len - 1)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory_array('leetcode.com')
obj.visit('google.com')
obj.visit("facebook.com")
obj.visit("youtube.com")
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit("linkedin.com")
print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))

