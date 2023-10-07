import sys

from view import ipv6_to_email, ipv6_to_email_anyway


def main():
    if len(sys.argv) == 1:
        ipv6_to_email()
        return
    if sys.argv[1] == "boot":
        ipv6_to_email_anyway()
        return
    print("--> 输入参数有误 <--")


if __name__ == '__main__':
    main()
