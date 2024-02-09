# num = [1, 5, 6, 3]
# rezult = 0
# for number in num:
#     rezult = rezult + number
# print(rezult)

# number = [2,4,6,5,7,8,9]
# a = 1/2
# def numbers():
#     for b in number:
#         d = b * a
#         print(d)
# numbers()

# names1 = ["Olim","Yusuf","Sanjar"]
# nam = []
# for name in names1:
# a = nam.join(names1)
# print(a)


# name1 ="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
# lst = (name1.split(" "))
# print(len(lst))

# a = [1,2,3,"a",5,7]#->a
# for b in a:
#     if type(b) == str:
#         print(b)

# a = 3
# b = 4
# # c = (a^2 + b^2)^2
# # print(c)
#
# z = ((a**2 + b**2)**(1/2))
# print(int(z))





# # 1_masala
# a = "Ruxshona"
# b = a[0:3]
# print(f"{b}..   {b}..   {a}")

# #2_masala
# a = input("ism: ")
# if a == "Darth Vader":
#     print("Leia, men sizning otangizman")
# elif a == "Leia":
#     print("Leia, men sening singlingman")
#
# elif a == "Han":
#     print("Leia, men sizning qaynotangizman")
# else:
#     print("Uzur siz kimsiz tanimadim")

# #3_masala
# a = input("char code is: ")
# b = input("char code is: ")
# print(f"counterpartCharCode {b}")
# print(f"counterpartCharCode {a}")

#4_masala
# def lst(string):
#     if string.lower().count("x") == string.count("o"):
#         return True
#     return False
#
# print(lst('ooxx'))
# print(lst('xooxx'))
# print(lst('ooxXm'))
# print(lst('zpzpzpp'))
# print(lst("zzoo"))

#5_masala
# def hamming_distance(string1, string2):
#     i = 0
#     result = 0
#     while i < len(string1) and i < len(string2):
#         x = string1[i]
#         y = string2[i]
#         if x != y:
#             result += 1
#
#         i += 1
#
#     print(result)
# hamming_distance("abcde", "abcdy")

#6_masala
# def replace_vowels(string, simbol):
#     vowels = "aoueiAOUEI"
#     for vowel in vowels:
#         string = string.replace(vowel, simbol)
#     return string
# print(replace_vowels("the aardvark", "#"))