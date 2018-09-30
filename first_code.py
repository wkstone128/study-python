#整数
x = 9
print("output #4: {0}".format(x))
print("output #5: {0}".format(3**4))
print("output #6: {0}".format(int(8.3)/int(2.7)))

#浮点数
print("output #7: {0:.3f}".format(8.3/2.7))
y = 2.5*4.8
print("output #8: {0:.1f}".format(y))
r = 8/float(3)
print("output #9: {0:.2f}".format(r))
print("output #10: {0:.4f}".format(8.0/3))

#math函数
from math import exp, log, sqrt
print("output #11: {0:.4f}".format(exp(3)))
print("output #12: {0:.2f}".format(log(4)))
print("output #13: {0:.1f}".format(sqrt(81)))

#字符串
print("Output #14: {0:s}".format('I\'m enjoying learning Python.'))
print("Output #15: {0:s}".format("This is a long string. Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller strings on separate lines so that the whole string is easy\
to view in the text editor."))
print("Output #16: {0:s}".format('''You can use triple single quotes
for multi-line comment strings.'''))
print("Output #17: {0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))

string1 = "this is a "
string2 = "short string."
sentence = string1 + string2
print("output #18: {0:s}".format(sentence))
print("output #19: {0:s},{1:s},{2:s}".format("she is","very " * 4,"beautiful."))
m = len(sentence)
print("output #20: {0:d}".format(m))

#split函数将一个字符串拆分成一个子字符串列表，列表中的子字符串正好可以构成原字符串
str1 = "my deliverable is due in may"
str1_list1 = str1.split()
str1_list2 = str1.split(" ",2)
print("output #21: {0}".format(str1_list1))
print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
.format(str1_list2[0], str1_list2[1], str1_list2[2]))
str2 = "you,deliverable,is,due,in,june"
str2_list = str2.split(",")
print("output #23: {0}".format(str2_list))
print("output #24: {0} {1} {2}".format(str2_list[1],str2_list[5],str2_list[-1]))

#join函数将列表中的子字符串组合成一个字符串。
print("output #25: {0}".format(',' .join(str2_list)))

#使用strip、lstrip 和rstrip 函数从字符串两端删除不想要的字符
str3 = " remove unwanted characters    from this string.\t\t    \n"
print("output #26: str3:{0:s}".format(str3))
str3_lstrip = str3.lstrip()
print("output #27: lstrip:{0:s}".format(str3_lstrip))
str3_rstrip = str3.rstrip()
print("output #28: rstrip:{0:s}".format(str3_rstrip))
str3_strip = str3.strip()
print("output #29: strip:{0:s}".format(str3_strip)) 

str4 = "$$here's another string that has unwanted characters._---++"
print("output #30: {0:s}".format(str4))
#从字符串两端删除其他字符
str4_strip = str4.strip('$_-+')
print("output #31: {0:s}".format(str4_strip))

'''
使用replace 函数将字符串中的一个或一组字符替换为另一个或
另一组字符
'''
str5 = "let's replace the spaces in this sentence with other characters."
str5_replace = str5.replace(" ","!@!")
print("output #32: {0:s}".format(str5_replace))  
str5_replace = str5.replace(" ",",")
print("output #33: {0:s}".format(str5_replace))

"""
使用lower、upper 和capitalize 函数
lower 和upper 函数分别用来将字符串中的字母转换为小写和大写。
capitalize 函数对字符串中的第一个字母应用
upper 函数，对其余的字母应用lower 函数
"""
str6 = "Here's WHAT Happens WHEN You Use lower."
print("output #34: {0:s}".format(str6.lower()))
str7 = "Here's what Happens when You Use UPPER."
print("output #35: {0:s}".format(str7.upper()))
str8 = "here's WHAT Happens WHEN you use Capitalize."
print("output #36: {0:s}".format(str8.capitalize()))
str8_list = str8.split()
print("output #37 (on each word):")
for word in str8_list:
    print("{0:s}".format(word.capitalize()))

#正则表达式与模式匹配
#re模块
import re
#计算字符串种模式出现的次数
str9 = "The quick brown fox jumps over the lazy dog."
str9_list = str9.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in str9_list:
    if pattern.search(word):
        count +=1
print("output #38: {0:d}".format(count))

#在字符串中每次找到模式时将其打印出来
str10 = "The quick brown fox jumps over the lazy dog."
str10_list = str10.split()
pattern = re.compile(r"(?P<match_word>The)",re.I) #</match_word>
print("output #39:")
for word in str10_list:
    if pattern.search(word):
        print("{:s}".format(pattern.search(word).group('match_word')))


#使用字母“a”替换字符串中的单词“the”
str11 = "The quick brown fox jumps over the lazy dog."
str11_list = str11.split()
str11_to_find = r"The"
pattern = re.compile(str11_to_find, re.I)
print("output #40: {:s}".format(pattern.sub("a",str11)))

#日期
from datetime import date, time, datetime, timedelta
today = date.today()
print("output #41: today: {0!s}".format(today))
print("output #42: {0!s}".format(today.year))
print("output #43: {0!s}".format(today.month))
print("output #44: {0!s}".format(today.day))
current_datetime = datetime.today
print("output #45: {0!s}".format(current_datetime))

#使用timedelta计算一个新日期
one_day = timedelta(day=-1)
yesterday = today + one_day
print("output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

#计算出两个日期之间的天数
date_diff = today - yesterday
print("output #48: {0!s}".format(date_diff))
print("output #49: {0!s}".format(str(date_diff).split()[0]))

#根据一个日期对象创建具有特定格式的字符串
print("output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("output #53: {:s}".format(today.strftime('%B %d, %Y')))

# 根据一个表示日期的字符串
# 创建一个带有特殊格式的datetime对象
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')
# 基于4个具有不同日期格式的字符串
# 创建2个datetime对象和2个date对象
print("output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))

# 仅显示日期部分
print("output #56: {!s}".format(datetime.date(datetime.strptime\
(date3, '%Y-%m-%d'))))
print("output #57: {!s}".format(datetime.date(datetime.strptime\
(date4, '%B %d, %Y'))))

