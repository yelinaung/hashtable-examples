import pprint

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
    index = hash(key) % size
    print(index)
    try:
        return value_bucket[index]
    except ValueError:
        raise KeyError(f"{key} not found!")


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
