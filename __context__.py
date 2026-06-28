# try:
#     int("abc")

# except ValueError as e:
#     raise RuntimeError("with _context_ explanation") from e



# try:
#     int("abc")

# except ValueError:
#     raise RuntimeError("without _context_ explanation")



try:
    int("abc")

except ValueError as e:
    raise RuntimeError("without _context_ explanation")

except RuntimeError as r:
    print("context:", type(r.__context__), r.__context__)
    print("cause:", type(r.__cause__), r.__cause__)