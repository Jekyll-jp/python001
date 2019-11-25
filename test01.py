class test01:
    def __init__(self,name):
        self.name = name
        print("はじめ")

    def kinou(self):
        print("私" + self.name)
boy = "man="

collorlist = ["red","blue","black","white"]
humanlist = []

for x in collorlist:
    boy2 = boy + x
    humanlist.append(boy2)
else:
    boy = ""

collorlist.clear()

if not collorlist:
    print("⓵：not判定,collorlistは空です")
if len(collorlist) == 0:
    print("⓶：len判定,collorlistは空です")

humanlist.insert(1,"古")

tuikalist = [456,"削除"]
humanlist += tuikalist


humanlist.insert(5,"insertで追加")

humanlist.pop() #最後の要素【削除】を削除

humanlist.pop(1) #2番目の要素【⓷：古】を削除 delでもよい

humanliststr = map(str,humanlist)

humanlist.remove("insertで追加") #removeで要素を削除

a = "⓷："
for y in humanliststr: #map型を表示
    view = a + y
    print(view)

print("⓸：'man=blue'の場所",
+humanlist.index('man=blue',1,5))
humanliststr = ""
if '8' in humanliststr:
    print("'8'という要素がある")
else:
    print("'8'という要素はない")
if not humanliststr:
    print("humanliststrの要素はありません")
humanlist.reverse() #リストの中身を反転
humanliststr = map(str,humanlist) #再度map型を格納
a = "⓺："
for z in humanliststr:
    view = a + z
    print(view)

#コピーパターン3 
one = humanlist.copy()
two = list(humanlist)
three = humanlist[:]

if one:
    if two:
        if three:
            print("one,two,threeに要素あり")

#辞書
foo = {'tom': 20,
 'mike': 21,
  'nancy': 'unknown',
   'jenny': 12,
    'jack': 55}

ber = {'tom': 40,
 'mikef': 25,
  'nancyf': 'unknowns',
   'jennyf': 120,
    'jackf': 555}

#結合
foo.update(ber)
print(foo)

#削除
foo.pop('mike') #複数不可
del foo['nancy'] ,foo['jack'] #複数可
print(foo)

for k in foo.keys():
    print(k)

for v in foo.values():
    print(v)

for k,v in foo.items():
    print(k+"は"+str(v))

#全要素削除
foo.clear()
if not foo:
    print("'foo'の要素なし")


m = test01("⓹：▽▽")
m.kinou()