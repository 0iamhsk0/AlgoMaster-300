# Last updated: 11/2/2025, 11:08:50 PM
class MyHashMap:

    def __init__(self):
        self.hsh = {}

    def put(self, key: int, value: int) -> None:
        if key not in self.hsh:
            self.hsh[key] = value
        else:
            self.hsh[key] = value

    def get(self, key: int) -> int:
        return self.hsh[key] if key in self.hsh else -1

    def remove(self, key: int) -> None:
        if key in self.hsh:
            del self.hsh[key]
        