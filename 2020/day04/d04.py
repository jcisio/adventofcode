import re

f = open('d04.in', 'r')

def countValidPassport(documents):
    required_fields = 'byr iyr eyr hgt hcl ecl pid'.split()
    c = 0
    for document in documents:
        missed_fields = False
        for field in required_fields:
            if not re.search(rf'\b{field}:', document):
                missed_fields = True
                break
        if not missed_fields:
            c += 1
    return c

def countValidPassportP2(documents):
    required_fields = 'byr iyr eyr hgt hcl ecl pid'.split()
    c = 0
    for document in documents:
        kv = {}
        for e in ' '.join(document.split('\n')).strip().split():
            a,b = e.split(':')
            kv[a] = b

        missed_fields = False
        for field in required_fields:
            if field not in kv:
                missed_fields = True
                break
        if missed_fields:
            continue

        if not re.match(r'\d{4}$', kv['byr']) or kv['byr'] < '1920' or kv['byr'] > '2002':
            continue
        if not re.match(r'\d{4}$', kv['iyr']) or kv['iyr'] < '2010' or kv['iyr'] > '2020':
            continue
        if not re.match(r'\d{4}$', kv['eyr']) or kv['eyr'] < '2020' or kv['eyr'] > '2030':
            continue
        if re.match(r'\d+cm$', kv['hgt']):
            if kv['hgt'][:-2] < '150' or kv['hgt'][:-2] > '193':
                continue
        elif re.match(r'\d+in$', kv['hgt']):
            if kv['hgt'][:-2] < '59' or kv['hgt'][:-2] > '76':
                continue
        else:
            continue
        if not re.match(r'#[a-z0-9]{6}$', kv['hcl']):
            continue
        if kv['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if not re.match(r'\d{9}$', kv['pid']):
            continue

        c += 1
    return c

documents = list(f.read().strip().split('\n\n'))
print("Puzzle 1: ", countValidPassport(documents))
print("Puzzle 2: ", countValidPassportP2(documents))
