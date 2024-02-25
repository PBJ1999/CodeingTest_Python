p = {"name":"park", "age":15, "sex":'m'}

p["college"] = "Pusan.Catholic" # 새로은 키:값 추가 => list()는 append()메소드 필요함

print('before del:{}'.format(p))

# 제거? = del p[키](존재하지 않는 키 값은 x)

if(p["age"] <20):
    del p["age"]

print('after del: {}'.format(p))