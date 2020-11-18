def grid_illumination(N, lamps, queries): 
    lit_rows = set()
    lit_cols = set()
    lit_digonals = set()
    for lamp in lamps: 
        x, y = lamp
        lit_rows.add(x)
        lit_cols.add(y)
        lit_digonals.add(abs(x - y), abs(x + y))

    answers = []
    for query in queries: 
        x, y = query 
        is_row_illuminated = x in lit_rows 
        is_col_illuminated = y in lit_cols 
        is_diagonal_illumniated = abs(x - y) in lit_digonals or (x + y) in lit_digonals
        is_illuminated = is_row_illuminated or is_col_illuminated or is_diagonal_illuminated
        answers.append(is_illuminated)
        #DO the rest, it's fuckin easy