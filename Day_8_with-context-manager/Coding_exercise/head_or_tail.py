count = 0
while True:
    data = input("Throw the coin and enter head or tail here:") + "\n"
    with open("content/sum.txt") as file:
        content = file.readlines()
        content.append(data)
    with open("content/sum.txt", "w") as file:
        file.writelines(content)
    for item in content:
        match item.strip():
            case "head":
                count += 1
            case "":
                count -= 1
    final_count = count / len(content) * 100
    print(count)
    print(f"Heads: {final_count}")
