#region 全体
#改行時(下に書きたいとき)
#invalid syntaxになる
#endregion

#region print関数
print関数
print(*objects, sep=' ', end='¥n', file=sys.stdout, flush=False)
print(aaa,bbb)⇒aaa 
                bbb
print(aaa,bbb,sep="")⇒aaabbb
print(aaa,bbb,sep="+")⇒aaa+bbb

print(aaa,end='')
print(bbb,end='')
print(ccc,end="[end]\n")
⇒aaabbbccc[end]

途中は改行せず最後に改行する

myfile = open("output1_4.txt", "w")⇒ファイル読み書きで
第一引数は名、第二引数wは書き込み用という意
ファイルが存在しなければ新規作成、存在していれば上書き（既存の内容は削除）
print("Hello", file=myfile)
print("Bye", file=myfile)
myfile.close()

第四引数にあるflush=Falseは
Trueにすると即時に出力する


#endregion

#region ファイル読み書き



#endregion

#region コメントアウト
"""
現在行をコメント化
 Windows／Linux：
［Ctrl］＋［K］→［Ctrl］＋［C］キー

行コメントのコメント化を解除
Windows／Linux：
［Ctrl］＋［K］→［Ctrl］＋［U］キー

現在行のコメント化／コメント化解除をトグル
Windows／Linux：
［Ctrl］＋［/］キー

選択範囲のブロックコメント化／コメント化解除をトグル
Windows／Linux：
［Shift］＋［Alt］＋［A］キー
 """

三連引用符は変数に入る
str = """¥
ああああ
ええええ
ええ"""

¥は改行でコーディングしたい場合に最初に入れる

#endregion
#region コマンドパレット

Ctrl+Shift+Pでコマンドパレット
python select interpreterを検索して
アナコンダがえらばれてたら選ぶ


#endregion
#region 実行

左のフォルダのクラスファイルの上で右クリック
Run Python File in Terminal

#endregion

#region デバッグ
ブレークポイントを設置VSと同じ


#endregion

#region エラー

インデンドのエラー
第一引数はself固定
invalid syntax (<unknown>, line 12)
#endregion

#region リスト

変数名 = []
で実装

末尾追加
append(t)

リストの中身削除
clear()

引数と一致する要素の数
count(t)

リストが空かどうか判断２パターン
１： if not リスト:　空であればtrue
２： if len(リスト) == 0: 空であればtrue

リストの末尾にリストなどを追加
extend(t)
+= t

リストの中の要素を検索
index(x,start,end)
index(x)
例
val = ['a','b','c','d','e']
print(val.index('d',1,5))
dをindex[1]～[4]までの範囲で検索 場所
結果　3

指定した場所に要素を追加
insert(i,x)

要素の中身をStringにする
Strしたmap型を格納する変数 = map(str,リスト)
この型にした場合要素の中身を削除するには
Strしたmap型を格納する変数 = ""

pop(i)
指定したindex番号を削除
指定なしは末尾の要素を削除

remove(x)
指定した要素を削除
なければValueError

reverse()
並び順を反転

sort(key,reverse)
リスト.sort()
指定ない場合は昇順

リスト.sort(reverse = True)
この場合は降順

コピー3通り
one = humanlist.copy()
two = list(humanlist)
three = humanlist[:]

リスト複数の要素の有無は&でつなげれない
if one:
    if two:
        if three:
            print("one,two,threeに要素あり")



#endregion

#region　3項演算子

foo = if (x >= 0) ? x : -x; #c,java,jsなどの3項演算子
foo = x if (x >= 0) else -x # Pythonの3項演算子

#endregion

#region 算術演算子

整数の除算（切り捨て）
5//3 #1

べき乗
5**3　#125

#endregion

#region リスト・タプル・辞書・集合
リスト　any
タプル  重複×
辞書　　マップ
集合　　？？

#endregion

#region　多次元配列

初期
arr = [[]]

#endregion

#region　辞書
update( dict )	辞書の結合
pop( key )	指定したkeyをもつ要素の削除　単数
clear( )	全要素削除
popitem() 指定せずに削除　使わない
del リスト[key],リスト[key] 複数可 　
keys(): keyをとりだす
values():　valueをとりだす
items():　すべてとりだす　この場合valueをstrにキャスト



#endregion

#region　集合
set1.union( set2 )	和集合
{1,2,3} | {2,4,6} ⇒ {1, 2, 3, 4, 6}

set1.intersection( set2 )　積集合（共通集合）	
{1,2,3} & {2,4,6} ⇒ {2}

set1.difference( set2 )	差集合	
{1,2,3} - {2,4,6} ⇒ {1, 3}

set1.symmetric_difference( set2 )　
排他的OR（どちらか片方のみに属する）	
{1,2,3} ^ {2,4,6} ⇒ {1, 3, 4, 6}

#endregion

#region input

変数など = input('~~~~')
コンソールに引数の文字列が出力されたあと
入力状態となる　str型になる

indexで取得する場合はindexはいらず
リスト変数[i]でよい



#endregion

#region 文字列　スライス

print("abcdefg"[i])
indexの値によって取得が異なる
:4---前方から4文字 
└"abcd"
4:---前方4文字のあと
└"efg"
:----全部
└"abcdefg"
1:4--index[1]のあとからindex[4-1]まで
└"bcd"

文字列[開始インデックス:終了インデックス:ステップ数]
1:4:2
└"bd"

#endregion

#region 書式化演算子、変換指定子、制度

print("名前は%-8sです。年齢は%03d歳です。" % (name, old))
print("%〇〇,%△△" %(変数、変数))
%-10s 左詰め10桁文字列
%5d   右詰め5桁符号付10進整数

print("数値1=%d, 数値2=%*d" % (18, 5, 42))
print("%d,%*d" %(値,最小フィールド幅,値))
数値1=18, 数値2=   42

print("数値1=%f, 数値2=%.*f" % (1/3, 3, 1/3))
数値1=0.333333, 数値2=0.333

#endregion

#region formatメソッド

"名前は{:<8s}です。年齢は{:>3d}歳です。".format("Suzuki", 18)

>>> name = "Suzuki"
>>> old = 18
>>> print(f"名前は{name:<8s}です。年齢は{old:>3d}歳です。")
名前はSuzuki  です。年齢は 18歳です。



#endregion

#region 整数

8.5e+5
8.5*100000

8.5e-4
8.5*0.0001

15//2
商のみ



#endregion

#region ビット演算

OR どっちかが1なら1
10|12
10=1010
12=1100
1110 =14

AND どちらも1なら1
10 & 12 = 1010と1100
1000 =8

XOR どちらかが1の場合だけ1
10 ^ 12 = 1010と1100
0110 =6

NOT ビット反転
~10 1010
0101 = 5

左シフト
11 << 2
001011 ⇒101100
44

右シフト
11 >> 1
1011 ⇒ 0101
5




#endregion

#region パイソンではできない
インクリデクリ
++
--

#endregion

#region 変数の削除

del 変数

#endregion

#region True False

>>> bool(True)
True
>>> bool(False)
False
>>> bool(None)
False
>>> bool(NotImplemented)
True

>>> bool(0)
False
>>> bool(5)
True
>>> bool(0.0)
False
>>> bool(0.1)
True
>>> bool(0j)
False

>>> bool("")
False
>>> bool("Hello")
True

>>> bool(())
False
>>> bool(("Blue","Red"))
True
>>> bool([])
False
>>> bool(["Apple", "Orange"])
True
>>> bool({})
False
>>> bool({"A":"Apple","O":"Orage"})
True

#endregion

#region 文字列比較

Unicode のコードポイントで比較している
ord("a") = 97
ord("A") = 65

str_a = "a"
str_A = "A"

if str_a > str_A  #True
if str_a.upper == str_A #True

>>> bool("apple" in ["orange", "apple", "lemon"])
True
>>> bool("grape" in ["orange", "apple", "lemon"])
False



#endregion