import logging


class HashTable:
    def __init__(self):
        self.size = 8
        self.key_bucket = [[] for _ in range(self.size)]
        self.value_bucket = [[] for _ in range(self.size)]

    def __setitem__(self, key, value):
        index = hash(key) % self.size
        self.key_bucket[index].append(key)
        self.value_bucket[index].append(value)

    def __getitem__(self, key):
        print(f"looking up {key}")
        index = hash(key) % self.size
        try:
            key_index = self.key_bucket[index].index(key)
        except ValueError:
            logging.exception(f"{key} not found!")
            return None

        return self.value_bucket[index][key_index]

    def __str__(self):
        return f"keys\t- {self.key_bucket}\nvalues\t- {self.value_bucket}"


def main():
    # sourcery skip: extract-duplicate-method
    ht1 = HashTable()
    ht1["junde"] = "firefox"
    ht1["fred"] = "chrome"
    ht1["andre"] = "safari"
    print(ht1)

    print(ht1["andre"])
    print(ht1["yelin"])

    ht2 = HashTable()
    ht2["miranda"] = "apple"
    ht2["koksoon"] = "orange"
    print(ht2["miranda"])

    # search for 'andre' in namespace 2
    print(ht2["andre"])


if __name__ == "__main__":
    main()
