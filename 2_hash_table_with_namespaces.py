import logging


def setup(ns):
    ns["size"] = 8
    ns["key_bucket"] = [[] for _ in range(ns["size"])]
    ns["value_bucket"] = [[] for _ in range(ns["size"])]


def insert(ns, key, value):
    index = hash(key) % ns["size"]
    ns["key_bucket"][index].append(key)
    ns["value_bucket"][index].append(value)


def lookup(ns, key):
    print(f"looking up {key}")
    index = hash(key) % ns["size"]
    try:
        key_index = ns["key_bucket"][index].index(key)
    except ValueError:
        logging.exception(f"{key} not found!")
        return None

    return ns["value_bucket"][index][key_index]


def print_buckets(ns):
    print("---- keys ----")
    print(ns["key_bucket"])
    print("---- values ----")
    print(ns["value_bucket"])
    print()


def main():
    ns1 = {}
    setup(ns1)
    insert(ns1, "junde", "firefox")
    insert(ns1, "fred", "chrome")
    insert(ns1, "andre", "safari")
    print_buckets(ns1)

    print(lookup(ns1, "andre"))
    print(lookup(ns1, "yelin"))

    ns2 = {}
    setup(ns2)
    insert(ns2, "miranda", "apple")
    insert(ns2, "koksoon", "orange")
    print_buckets(ns2)

    print(lookup(ns2, "miranda"))

    # search for 'andre' in namespace 2
    print(lookup(ns2, "andre"))


if __name__ == "__main__":
    main()
