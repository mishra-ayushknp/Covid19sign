import os
os.chdir('C:\\Users\\AYUSH MISHRA\\Desktop\\im')
print(os.getcwd())
c =0 
def increment():
    global c
    c = c+1

for i in os.listdir():
    f_name,f_ext = os.path.splitext(i)
    f_name = str(c)
    increment()
new_name = '{}{}'.format(f_name,".png")
os.rename(i,new_name)