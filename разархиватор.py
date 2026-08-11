from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import threading
def Packer(whole1):
    agents=[]
    beckup={}
    agentsNumber=[1,0]
    def agent(number,whole,thisAgent,r,l,y):
        new_agent=[]
        if not(whole is None) and len(whole) >= y:
            print("эээ 67?")
            for i in range(y,len(whole)):
                if agents == []:
                    if len(r) % 2 == 1:
                        if str(whole)[i] != " ":
                            r+=str(whole)[i]
                            if not(r in thisAgent):
                                thisAgent.append(r)
                            if l[-1] == '|':
                                pass
                            else:
                                l+=','
                            k=0
                            for i in range(len(thisAgent)):
                                if k == 1:
                                    pass
                                elif thisAgent[i] == r:
                                    l+=str(i+1)
                                    k=1
                        else:
                            if len(whole) >= i+2:
                                agentsNumber[0]+=1
                                q=[whole[:],thisAgent[:],l,r,y]
                                beckup[number-1]=q
                                new_thisAgent=thisAgent
                                new_thisAgent.append(r+str(whole)[i+1])
                                new_agent.append(threading.Thread(target=agent, args=(agentsNumber[0]+1,whole,new_thisAgent,'',f"{l},{len(new_thisAgent)}_{len(new_thisAgent)}",y+3)))
                                q=beckup[number-1]
                                whole=q[0]
                                thisAgent=q[1]
                                l=q[2]
                                r=q[3]
                                y=q[4]
                                new_agent[-1].start()
                            r+=str(whole)[i]
                            if not(r in thisAgent):
                                thisAgent.append(r)
                            if l[-1] == "|":
                                pass
                            else:
                                l+=','
                            k=0
                            for i in range(len(thisAgent)):
                                if k == 1:
                                    pass
                                elif thisAgent[i] == r:
                                    l+=str(i+1)
                                    k=1
                        r=""
                    else:
                        if str(whole)[i] != " ":
                            r+=str(whole)[i]
                        else:
                            if len(whole) >= i+3:
                                agentsNumber[0]+=1
                                q=[whole[:],thisAgent[:],l,r,y]
                                beckup[number-1]=q
                                new_thisAgent=thisAgent
                                k=0
                                for i in range(len(thisAgent)):
                                    if k == 1:
                                            pass
                                    elif thisAgent[i] == str(whole)[i+1]+str(whole)[i+2]:
                                        l2=str(i)
                                        k=1
                                if not(str(whole)[i+1]+str(whole)[i+2] in thisAgent):
                                    new_thisAgent.append(str(whole)[i+1]+str(whole)[i+2])
                                    new_agent.append(threading.Thread(target=agent, args=(agentsNumber[0]+1,whole,new_thisAgent,'',f"{l},_{len(new_thisAgent)}",y+2)))
                                    q=beckup[number-1]
                                    whole=q[0]
                                    thisAgent=q[1]
                                    l=q[2]
                                    r=q[3]
                                    y=q[4]
                                    new_agent[-1].start()
                                else:
                                    new_agent.append(threading.Thread(target=agent, args=(agentsNumber[0]+1,whole,new_thisAgent,'',f"{l},_{l2}",y+2)))
                                    q=beckup[number-1]
                                    whole=q[0]
                                    thisAgent=q[1]
                                    l=q[2]
                                    r=q[3]
                                    y=q[4]
                                    new_agent[-1].start()
                            r+=str(whole)[i]
                    y=i
                    print("номер агента: ",number)
                    print("целое: ",whole)
                    print("Len: ",thisAgent)
                    print("Num: ",l)
                    print("буфер: ",r)
                    print("интерация: ",y)
            if agents == []:
                agentsNumber[1]=number
            if r != "":
                y+=1
                r+=" "
                thisAgent.append(r)
                l+=','
                k=0
                for i in range(len(thisAgent)):
                    if k == 1:
                        pass
                    elif thisAgent[i] == r:
                        l+=str(i+1)
                        k=1
                l+="-"
            r=l
            thisAgent.append(r)
            agents.append(thisAgent)
        print(f"агент {number} завершил работу")
        if new_agent != []:
            for i in range(len(new_agent)):
                new_agent[i].join()
    agent(1,whole1,[],'','|',0)
    print('пул агентов:',agents)
    print('всего агентов:',agentsNumber[0])
    print('результат от агента №',agentsNumber[1])
    return agents[0]
def Unpacker(whole):
    per_len,per_int=whole.replace("'","").replace("[","").replace("]","").split("|")
    strs= per_len.split(", ")
    nums= per_int.split(",")
    result =[]
    for num in nums:
        if "_" in num:
            if num[0] == "_":
                if num[-1] == "-":
                    whole=strs[int(num.replace("-","").replace("_",""))-1]
                    lens=whole[0]
                    result.append(" "+lens)
                elif num[-1] == "+":
                    whole=strs[int(num.replace("+","").replace("_",""))-1]
                    lens=whole[1]
                    result.append(" "+lens)
                else:
                    result.append(" "+strs[int(num.replace("_",""))-1])
            else:
                lens1,crop1=num.split("_")
                if lens1[-1] == "+":
                    whole1=strs[int(lens1.replace("+",""))-1]
                    lens2=whole1[1]
                else:
                    whole1=strs[int(lens1.replace("-",""))-1]
                    lens2=whole1[0]
                if crop1[-1] == "-":
                    whole2=strs[int(crop1.replace("-",""))-1]
                    crop2=whole2[0]
                else:
                    whole2=strs[int(crop1.replace("+",""))-1]
                    crop2=whole2[1]
                result.append(lens2+" "+crop2)
        else:
            if num[-1] == "-":
                    whole=strs[int(num.replace("-",""))-1]
                    lens=whole[0]
                    result.append(lens)
            elif num[-1] == "+":
                    whole=strs[int(num.replace("+",""))-1]
                    lens=whole[1]
                    result.append(lens)
            else:
                result.append(strs[int(num)-1])
    return "".join(result)
#a=Packer(input())
#print("результат архивации:",a)
print("результат разархивации:",input())