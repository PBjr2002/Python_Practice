ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

tmp = list(ft_tuple)
tmp[1] = "Portugal!"
ft_tuple = tuple(tmp)

ft_set.discard("tutu!")
ft_set.add("Lisbon!")

ft_dict["Hello"] = "42Lisboa!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
