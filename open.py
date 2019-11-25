"""
初回ファイルが存在するときはそのファイルを複製し書き込む
上記の場合初回ファイルへの書き込みはしない

初回ファイルが存在しないときは書き込む
複製ファイルはDatetimeからstrに変換しtext(20191122135050).txtという名にする
"""
import os
import datetime
import re
class Test():
    dt_str = ""

    def __init__(self):
        # 文字列を格納するためのリストを作成
        self.testList = []; self.testList2 = []

    def main(self):
        list = []
        fileflg = True
        drive = r"C:"
        folders = r"\Users\tgl\Documents\data"
        filename = r"\test"
        dat = ".txt"
        self.testList.append(drive)
        self.testList.append(folders)
        self.testList.append(filename)
        self.testList.append(dat)
        
        #リスト内の要素を連結する
        self.testStr = "".join(self.testList)
        print(self.testStr+"が初回ファイル")

        #初回ファイル存在確認
        if not os.path.isfile(self.testStr):
            fileflg =False
            print("初回ファイルが存在しないため新規で出力")
        else:
            date = datetime.datetime.now()
            dt_str =date.strftime('%Y/%m/%d %H:%M:%S')
            dt_str = re.sub(r'[/:\s]',"",dt_str) # [/ : " "]を削除
            filename = filename+dt_str
            self.testList2.append(drive)
            self.testList2.append(folders)
            self.testList2.append(filename)
            self.testList2.append(dat)
            self.testStr2 = "".join(self.testList2)
            print(self.testStr2+"が新規書き込みファイル")
            
            print("初回ファイルが存在するため複製して出力")
            
        if fileflg:
            #初回ファイルの中身をリスト化           
            list = test.fileopen(self.testStr)
            self.testStr = self.testStr2
        else:
            pass

        #初回リストと書き込みファイル名を引数に書き込み処理      
        test.writetxt(list,self.testStr)

    def writetxt(self,list,filename):#ここがrepository
        #書き込むもの
        writeA = ["リンゴ","A","582"]
        list.extend(writeA)

        with open(filename, mode='w+',encoding='UTF-8') as f:
            for x in list:
                f.write(x)
            
    def fileopen(self,name):#ここもrepository
        #karrent = 'r'
        #names = karrent+name
        with open(name,mode='r',encoding='UTF-8') as f:
            l_strip = [s.strip() for s in f.readlines()]
            return l_strip



if __name__ == '__main__':
    test = Test()
    test.main()