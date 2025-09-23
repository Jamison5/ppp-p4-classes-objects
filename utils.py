class InvalidArgumentError(Exception):
    def __init__(self, arg, msg):
        super().__init__(f"The `{arg}` (type `{type(arg)}`) is invalid. {msg}")


def validate_positive_number(arg):
    # if isinstance(arg, bool):
    #     raise InvalidArgumentError(arg, "The argument must be a positive number.")
    if not isinstance(arg, (int, float)):
        raise InvalidArgumentError(
            arg, "Only the following types are allowed: <class 'int'>, <class 'float'>"
        )
    if arg <= 0:
        raise InvalidArgumentError(arg, "The argument must be a positive number.)")


if __name__ == "__main__":

    print(validate_positive_number(False))
