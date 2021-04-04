def extractData():
    for elem in l1:
        bag = elem.split("bags contain")[0]
        contains = elem.split("bags contain")[1]
        if contains == " no other bags.":
            bag = bag.strip()
            dic.update({bag: []})
            continue

        containList = contains.split(',')
        cleanList = []
        for item in containList:
            item = item.replace('bags', '')
            item = item.replace('bag', '')
            for char in item:
                if char.isdigit() or char == '.':
                    if char.isdigit():
                        num = char
                    item = item.replace(char, '')
            item = item.strip()
            if item == '.': continue
            cleanList.append((num, item))
        bag = bag.strip()
        dic.update({bag: cleanList})

def part1():    
    ans = 0
    for elem in dic.keys():
        if recursePart1(elem): ans += 1
    print("Part 1:", ans)

def part2():
    ans = recursePart2("shiny gold")
    print("Part 2:", ans)

def recursePart1(bag):
    if "shiny gold" in [item[1] for item in dic[bag]]: return True
    else: 
        state = False
        for x in dic[bag]:
            state |= recursePart1(x[1])
        return state

def recursePart2(bag):
    res = 0
    if bag not in dic or len(dic[bag]) == 0: return 0
    else: 
        for x in dic[bag]:
            res += int(x[0]) + (int(x[0])*recursePart2(x[1]))
    return res

# Global variables
l1 = []
dic = {}
with open("input7.txt") as f:
    l1 = f.read().splitlines()

extractData()
part1()
part2()