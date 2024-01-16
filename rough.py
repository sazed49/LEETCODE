def compare_total_values(map1, map2):
    all_keys = set(map1.keys()).union(set(map2.keys()))

    for key in all_keys:
        total_map1 = len(map1.get(key, []))
        total_map2 = len(map2.get(key, []))

        if total_map2 <= total_map1:
            print(f'Total values of key "{key}" in the second map are less than or equal to in the first map.')
        else:
            print(f'Total values of key "{key}" in the second map are greater than in the first map.')

# Example usage:
map1 = {'a': ['a', 'a'], 'b': ['b']}
map2 = {'a': ['a', 'a']}

compare_total_values(map1, map2)
