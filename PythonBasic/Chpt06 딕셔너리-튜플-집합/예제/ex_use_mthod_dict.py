f = {"apple":6000, "melon":3000, "banana":5000, "orange":7000}

print("f type is {}\n".format(type(f))) # 객체 f는 키 - 값을 가지는 딕셔너리 객체이다

print(f.keys(),'\n')

f.pop("apple")
print("after (apple, 6000) value pop()\n=> {}\n".format(f))

print(f.get("grape")) # There is no key value 'grape' => print 'None'

# print(f.pop("grape")) # There is no key value 'grape' => KeyError: 'grape'

