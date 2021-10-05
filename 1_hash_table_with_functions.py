import pprint
import logging

pp = pprint.PrettyPrinter()


def setup():
    global size, key_bucket, value_bucket
    size = 8
    key_bucket = [[] for size in range(size)]
    value_bucket = [[] for size in range(size)]


def insert(key, value):
    index = hash(key) % size
    key_bucket[index].append(key)
    value_bucket[index].append(value)


def lookup(key):
    print(f"looking up {key}")
    index = hash(key) % size
    try:
        key_index = key_bucket[index].index(key)
    except ValueError:
        logging.exception(f"{key} not found!")
        return None

    return value_bucket[index][key_index]


def print_buckets():
    print("---- keys ----")
    print(key_bucket)
    print("---- values ----")
    print(value_bucket)


def main():
    setup()
    insert("junde", "firefox")
    insert("fred", "chrome")
    insert("andre", "safari")
    print_buckets()

    print(lookup("andre"))
    print(lookup("yelin"))


if __name__ == "__main__":
    main()
