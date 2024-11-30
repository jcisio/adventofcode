import re

f = open('d07.in', 'r')


def read_rules(lines):
    rules = {}
    for line in lines:
        outer, inner = line.strip('.').split(' contain ')
        if inner == 'no other bags':
            continue
        outer = outer[:-5]# ' bags'
        rules[outer] = dict()
        for e in inner.split(', '):
            match = re.match(r'(\d+) (.+?) bags?', e)
            rules[outer][match.group(2)] = int(match.group(1))
    return rules


def find_shiny_gold(rules):
    bags = set(['shiny gold'])
    found = True
    while found:
        found = False
        for bag in rules:
            if bag not in bags and len(bags.intersection(set(rules[bag].keys()))) > 0:
                found = True
                bags.add(bag)
    return len(bags)-1


def count_bags(rules, bag):
    content = rules[bag]
    c = 0
    while content:
        bags = list(content.keys())
        for b in bags:
            c += content[b]
            if b in rules:
                for inner_bag in rules[b]:
                    count = content[b]*rules[b][inner_bag]
                    if inner_bag in content:
                        content[inner_bag] += count
                    else:
                        content[inner_bag] = count
            del content[b]
    return c


rules = read_rules(f.read().strip().split('\n'))
print("Puzzle 1: ", find_shiny_gold(rules))
print("Puzzle 2: ", count_bags(rules, 'shiny gold'))
