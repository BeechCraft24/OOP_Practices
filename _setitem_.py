# class UpperDict(dict):

#     def __setitem__(self, key, value):
#         super().__setitem__(key.upper(), value)

# d = UpperDict()
# d["alex"] = 100
# print(d)



# class Dict(dict):

#     def __setitem__(self, key, value):
#         super().__setitem__("AR", 42)

# d = Dict()
# d["alex"] = 100
# print(d)




class FormatDict(dict):

    def __setitem__(self, key, value):

        formatted_value = value.title()
        super().__setitem__(key, formatted_value)

students = FormatDict()
students["s1"] = "alexander reinoso"
students["s2"] = "jOhN doe"
print(students)