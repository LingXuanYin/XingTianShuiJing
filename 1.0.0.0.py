import os
import win32file
import win32api
import psutil
import time

print('''   
                        注意！！！
                本脚本涉及修改游戏文件
                不保证完全没有封号风险

            使用说明：
                将本脚本放到 游戏安装目录的上级目录 或输入 游戏安装目录 (安装目录包含YuanShen.exe)
                每次重启游戏后恢复正常
                本脚本将 角色建模 及 飞行时的模糊 恢复到2.3
                每次使用本脚本启动游戏，游戏内都将重新校验游戏资源

                本脚本完全开源
                如有顾虑请不要使用

        使用本脚本即视为同意以下条款：
            1、本脚本完全用作技术交流、学习，用作其他用途产生的一切损失由使用者承担
            2、若使用本脚本对任何集体、个人、团体、集团、公司的合法利益造成侵害，一切责任由使用者承担
            3、不合理合法合规使用本脚本，造成的一切损失均由使用者承担，与作者无关
            4、使用本脚本产生的一切损失由使用者承担
            5、如不同意以上内容，请立即退出并完全删除此脚本


交流群：777974176 (北幽冒险家公会) 

作者：南辰燏炚
            

   ''')
input("继续使用即视为完全阅读且同意以上内容\n       按 ENTER 或 ESC 以继续")

path=os.getcwd()+'\\Genshin Impact Game\\'

time_start=time.time()
if not os.path.exists(path+'YuanShen.exe'):

    while True:
        path=input("请输入原神的安装目录")+'\\'
        if not os.path.exists(path+"YuanShen.exe"):
            print ("请输入正确的路径")
        else:break
try:
    win32api.ShellExecute(0, 'open', path+"YuanShen.exe", '', '', 1) 
except:print("启动失败，请手动启动原神")

path=path+"YuanShen_Data\\Persistent\\"

path_remote=path+'silence_data_versions_remote'
path_presist=path+'silence_data_versions_persist'
file_del=[path_remote,path_presist,path+"ctable.dat"]
silence_rev=path+'silence_revision'
res_rev=path+'res_revision'
data_rev=path+'data_revision'
audio_rev=path+'audio_revision'
i=0
try:
    os.remove(silence_rev)
except:{    }
try:

    os.remove(audio_rev)
except:{    }
try:
    os.remove(res_rev)
except:{    }
try:
    os.remove(data_rev)
except:{    }
name=[]
    
while "YuanShen.exe" not in name:
    PID = psutil.pids()
    for pid in PID:
        try:
            name.append( str(psutil.Process(pid).name()))
        except:{}
    print("等待原神启动 "+str(i)+' s')
    time.sleep(3)
    i=i+1
print("原神已启动")
i=0
f=0
while True:
    if os.path.exists( path_remote):
        try:
            win32api.SetFileAttributes(path_remote,win32file.FILE_ATTRIBUTE_NORMAL )
            open( path_remote,'w+').write('')
            if i>40 and open(path_remote,'r').read()=='':break

            i=i+1
        except:print("设置remote出错")
    if os.path.exists( path_presist):
        try:
            win32api.SetFileAttributes(path_presist, win32file.FILE_ATTRIBUTE_NORMAL)
            open(path_presist,'w+').write('')
            if f>40 and open(path_presist,'r').read()=='':break
            f=f+1
        except:print("设置presist出错")
    if time_start-time.time()>90:
        print("TIME OUT")
        break
    if i>80 and f>80:
        print("END")
        break
    time.sleep(1)

