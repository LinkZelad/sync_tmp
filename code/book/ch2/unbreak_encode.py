from secrets import token_bytes


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


origin_str = "Hello,world!"


def encode(origin: str):
    origin_bytes = origin.encode()
    origin_int = int.from_bytes(origin.encode(), "big")
    dummy = random_key(len(origin_bytes))
    except_str = origin_int ^ dummy
    return dummy, except_str


def decode(except_str: int, dummy: int):
    result_bytes = except_str ^ dummy
    result_int = result_bytes.to_bytes((result_bytes.bit_length() + 7) // 8, "big")
    return result_int.decode()


if __name__ == "__main__":
    a, b = encode(origin_str)
    print(a, b)
    print(decode(a, b))
