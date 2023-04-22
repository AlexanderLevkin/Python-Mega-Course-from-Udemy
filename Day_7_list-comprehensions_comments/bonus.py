filenames = ["1.doc", "1.report", "1.presentation"]
# new_list = []
# for item in filenames:
#     new_item = f"{item}.txt"
#     new_list.append(new_item.replace('.', '-', 1))
#
# print(new_list)
#
new_list = [f"{item.replace('.', '-', 1)}.txt" for item in filenames]

print(new_list)