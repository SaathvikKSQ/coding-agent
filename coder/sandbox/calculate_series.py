
def calculate_series_sum(num_terms):
    series_sum = 0
    for i in range(num_terms):
        term = (-1)**i / (2 * i + 1)
        series_sum += term
    return series_sum

num_terms = 1000000
result = calculate_series_sum(num_terms) * 4
print(f"{result}")
