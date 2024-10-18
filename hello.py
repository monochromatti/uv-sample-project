from package_one.hello import say_hello as first_hello
from package_two.hello import say_hello as second_hello


def main():
    print("Hello from test-project!")


if __name__ == "__main__":
    main()
    first_hello()
    second_hello()
