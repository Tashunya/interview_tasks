def print_possible_variants(variants_list: list, prefixes: list) -> None:
    sorted_list = process_variants(variants_list)
    for i, prefix in enumerate(prefixes):
        matches = search_by_prefix(prefix, sorted_list)
        for _ in range(10):
            try:
                print(next(matches)[0])
            except StopIteration:
                break
        if i != len(prefixes)-1:
            print()


def process_variants(variants_list: list) -> list:
    sorted_variants = sorted(variants_list, key=lambda x: (x[1] * -1, x[0]))
    return sorted_variants


def search_by_prefix(prefix: str, variants_list: list) -> filter:
    matching_iterator = filter(lambda x: x[0].startswith(prefix),
                               variants_list)
    return matching_iterator


variants_number = int(input().strip())
variants = []
for _ in range(variants_number):
    word, frequency = input().strip().split()
    variants.append((word, int(frequency)))


prefix_number = int(input().strip())
input_prefixes = []
for _ in range(prefix_number):
    input_prefix = input().strip()
    input_prefixes.append(input_prefix)


print_possible_variants(variants, input_prefixes)
