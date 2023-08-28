from random import randint as ri
import time
import sys
c=""
def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] \r" % (prefix, "#"*x, "."*(size-x)))
        file.flush()
        file.write("\n")
    show(0)
    
    for i, item in enumerate(it):
        yield item
        show(i+1)
        file.write("\n")
    file.flush()
    
def ask(c):
	if c =="Y" or c=="y":
		for i in progressbar(range(ri(15,60)), "計算中: ", 40):
			time.sleep(0.1)
		print("\n計算完成,請檢查更新\n\n")
		time.sleep(ri(0,3))
		ask(input("%s是否閃退？(Y/n) " %app))    
	elif c == "n" or c == "N":
		print("\n%s問題已解決"%app)
		sys.exit()
app = input("輸入應程式名稱： ")
nouse= input("輸入iOS或iPadOS版本(範例：iOS16.5.1)： ")
ask(input("是否閃退？(Y/n) "))
