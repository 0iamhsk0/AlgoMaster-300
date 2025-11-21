# Last updated: 11/21/2025, 4:56:28 PM
class MyHashMap:

    def __init__(self):
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        return self.hash_map[key] if key in self.hash_map else -1
        # return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        # self.hash_map.pop(key, -1)
        # self.hash_map.popitem()
        if key in self.hash_map:
            del self.hash_map[key] 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# class MyHashMap:

#     def __init__(self):
#         self.hsh = {}

#     def put(self, key: int, value: int) -> None:
#         if key not in self.hsh:
#             self.hsh[key] = value
#         else:
#             self.hsh[key] = value

#     def get(self, key: int) -> int:
#         return self.hsh[key] if key in self.hsh else -1

#     def remove(self, key: int) -> None:
#         if key in self.hsh:
#             del self.hsh[key]
