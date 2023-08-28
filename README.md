# iOS-troubleshooter
![image](https://github.com/proton-penguin/iOS-troubleshooter/assets/142492829/d49112e6-2ee3-4adf-a7fe-54b0538e41fd)
這個專案是用來解決iOS應用程式的閃退問題
![image](https://github.com/proton-penguin/iOS-troubleshooter/assets/142492829/543c0a87-a5b4-4017-9975-78c0db42b856)

` These commands were last tested on Aug 2023 on Debian 12. `

## Prerequisites
### For GNU/Linux user
```bash
# Update your software repositories.
sudo apt-get update
sudo apt-get upgrade

# Install Git.
sudo apt-get install -y git

# Install Python3.
sudo apt-get install -y python3
```

### For Windows user
Download and install Python 3 at [this website](https://www.python.org/downloads/).

### For macOS user
You don't need to do anything.


## Download the script

### Download directly
[![image](https://github.com/proton-penguin/iOS-troubleshooter/assets/142492829/31b3595b-36cc-4e4d-923b-c7ce396aca44)](https://github.com/proton-penguin/iOS-troubleshooter/archive/refs/heads/main.zip)

Once [download](https://github.com/proton-penguin/iOS-troubleshooter/archive/refs/heads/main.zip)ed, exract the zip.

### Clone this repository
```bash
git clone https://github.com/proton-penguin/iOS-troubleshooter.git
```



### Copy the python script directly
```python
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
```
Paste these codes in Notepad++ then save as main.py

## Run the script

```bash
# 進入iOS-troubleshooter directory
cd iOS-troubleshooter-main
```

```bash
# 以python執行程式
python3 main.py
```



## 斗內我
想打我都來不急了
怎麼可能有人斗內
連結還是不放囉
