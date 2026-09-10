```python
def calculate_series_sum(num_terms):
    series_sum = 0
    for i in range(num_terms):
        term = (-1)**i / (2 * i + 1)
        series_sum += term
    return series_sum

num_terms = 1000000
result = calculate_series_sum(num_terms) * 4
print(f"{result}")
```I wrote a Python program named `calculate_series.py` to compute the sum of the first 1,000,000 terms of the series 1 - 1/3 + 1/5 - 1/7 + ... and then multiplied the total by 4.

The content of the `calculate_series.py` file was:

I then executed this file in the sandbox.

The final result of the calculation is: `3.1415916535897743`