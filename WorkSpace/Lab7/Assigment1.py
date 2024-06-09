#Assigment 1 - Regular Expression

import re


def is_valid_float(N):
    # Sayının tam olarak bir '.' sembolüne sahip olup olmadığını kontrol et
    if N.count('.') != 1:
        return False

    # Geçerli float deseniyle eşleşecek düzenli ifade
    pattern = r'^[+-]?(\d*\.\d+|\d+\.\d*)$'
    if not re.match(pattern, N):
        return False

    # İstisnasız bir floata dönüştürülüp dönüştürülemeyeceğini kontrol edin
    try:
        float(N)
        return True
    except ValueError:
        return False


# Test cases
test_cases = ["+6.9", "-1.0", ".7", "+.5", "-.8", "11.", "11.0", "-+8.7", "abc", "5.", ".5", "5.5", "5.5.5"]

for test in test_cases:
    print(f"{test}: {is_valid_float(test)}")
