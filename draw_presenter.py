def draw():
    import random

    members = ["서형원", "오동균", "이태경", "탁정균", "한지웅", "백승아"]
    index = random.randint(1, len(members))
    print(f"발표자: {members[index - 1]}")

if  __name__ == "__main__":
    draw()
