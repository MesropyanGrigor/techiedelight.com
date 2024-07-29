def number_to_excel_column(num):
    result = []
    
    while num > 0:
        num -= 1  # Adjust to 0-based index
        remainder = num % 26
        result.append(chr(65 + remainder))  # Convert remainder to corresponding ASCII character
        num //= 26
    
    return ''.join(result[::-1])


print(number_to_excel_column(17577))