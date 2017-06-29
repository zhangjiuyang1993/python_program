#<pre name="code" class="html">
import re
import string

def toRgb(tmp):
    opt = re.findall(r'(.{2})',tmp)
    strs = ""
    for i in range(0,len(opt)):
        strs += str(int(opt[i],16)) + ","
    print("转换后的RGB数值为：")
    print(strs[0:-1])

def toHex(tmp):
    rgb = tmp.split(",")
    strs = "#"
    for j in range(0,len(rgb)):
        num = string.atoi(rgb[j])
        strs += str(hex(num))[-2:]
    print("转换后的16进制为：")
    print(strs)

def main():
    inColor = raw_input("输入颜色值")
    if(len(inColor) <= 11):
        if(inColor.index(",") >= 0):
            tmp = inColor
            toHex(tmp)
        elif(inColor[0] == "#"):
            tmp = inColor[1:]
            toRgb(tmp)
    else:
        print("请输入正确的数值！如\"#777bbb\"或\"123,123,123\"")

main()