import logging


class HashTable:
    def setup(self):
        self.size = 8
        self.key_bucket = [[] for size in range(self.size)]
        self.value_bucket = [[] for size in range(self.size)]

    def insert(self, key, value):
        index = hash(key) % self.size
        self.key_bucket[index].append(key)
        self.value_bucket[index].append(value)

    def lookup(self, key):
        print(f"looking up {key}")
        index = hash(key) % self.size
        try:
            key_index = self.key_bucket[index].index(key)
        except ValueError:
            logging.exception(f"{key} not found!")
            return None

        return self.value_bucket[index][key_index]

    def print_buckets(self):
        print("---- keys ----")
        print(self.key_bucket)
        print("---- values ----")
        print(self.value_bucket)
        print()


def main():
    # sourcery skip: extract-duplicate-method
    ht1 = HashTable()
    ht1.setup()
    ht1.insert("junde", "firefox")
    ht1.insert("fred", "chrome")
    ht1.insert("andre", "safari")
    ht1.print_buckets()

    print(ht1.lookup("andre"))
    print(ht1.lookup("yelin"))

    ht2 = HashTable()
    ht2.setup()
    ht2.insert("miranda", "apple")
    ht2.insert("koksoon", "orange")
    ht2.print_buckets()

    print(ht2.lookup("miranda"))

    # search for 'andre' in namespace 2
    print(ht2.lookup("andre"))


if __name__ == "__main__":
    main()
