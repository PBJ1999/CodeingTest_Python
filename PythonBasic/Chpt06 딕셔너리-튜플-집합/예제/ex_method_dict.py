# keys(), values() , items()

p = {"name":"park", "age":15, "sex":'m'}

print(p.keys())
print(p.values())
print(p.items())

# output

# dict_keys(['name', 'age', 'sex'])
# dict_values(['park', 15, 'm'])
# dict_items([('name', 'park'), ('age', 15), ('sex', 'm')])

# get(키) , pop(키)

# 해당 키의 값을 반환한다, 하지만 pop은 해당 키의 값을 반환 및 삭제하고, 정해진 키가 없으면 error

print(p.get("name"))
print(p.pop("age"))

print("after pop() ={}".format(p))
# age 키 값의 15 반환 밎 항목 삭제

# popitems() 매개변수는 없으며(self) 랜덤한 항목 삭제

print(p.popitem())

print("after popitems() = {}".format(p))

# clear() => 문자그대로 딕 안의 모든 내용 삭제

p.clear()
print("after clear() = {}".format(p))