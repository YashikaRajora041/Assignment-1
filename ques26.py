#. Write a program in python that checks if a string starts with a given prefix
#or ends with a given suffix.
def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)

    return starts_with_prefix, ends_with_suffix


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    prefix = input("Enter a prefix to check (press Enter if none): ")
    suffix = input("Enter a suffix to check (press Enter if none): ")

    starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix)

    if prefix:
        print(f"The string '{input_string}' starts with the prefix '{prefix}': {starts_with_prefix}")
    if suffix:
        print(f"The string '{input_string}' ends with the suffix '{suffix}': {ends_with_suffix}")

