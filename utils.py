class InvalidArgumentError(Exception):
    def __init__(self, arg, msg):
        super().__init__(f"The `{arg}` (type `{type(arg)}`) is invalid. {msg}")


def validate_positive_number(number):
    if not isinstance(number, (int, float)):
        raise InvalidArgumentError(
            number,
            "Only the following types are allowed: <class 'int'>, <class 'float'>",
        )
    if number <= 0:
        raise InvalidArgumentError(number, "The argument must be a positive number.)")


if __name__ == "__main__":

    print(validate_positive_number(False))
