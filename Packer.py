import threading,sys,os
def Packer(whole1):
    agents=[]
    beckup={}
    agentsNumber=[1,0]
    def agent(number,whole,thisAgent,r,l,i):
        new_agent=[]
        if not(whole is None) and len(whole) >= i:
            print("эээ 67?")
            for y in range(i,len(whole)):
                if agents == []:
                    if len(r) % 2 == 1:
                        if str(whole)[y] != " " or y == 1:
                            r+=str(whole)[y]
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
                            if len(whole) >= y+2:
                                agentsNumber[0]+=1
                                q=[whole[:],thisAgent[:],l,r]
                                beckup[number-1]=q
                                new_thisAgent=thisAgent[:]
                                k=0
                                for i in range(len(thisAgent)):
                                    if k == 1:
                                            pass
                                    elif thisAgent[i] == str(whole)[y-1]+str(whole)[y+1]:
                                        l2=str(i//2+1)
                                        k=1
                                if not(str(whole)[y-1]+str(whole)[y+1] in thisAgent):
                                    new_thisAgent.append(str(whole)[y-1]+str(whole)[y+1])
                                    new_agent.append(threading.Thread(target=agent, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},{len(new_thisAgent)}_{len(new_thisAgent)}",y+2)))
                                    new_agent[-1].start()
                                    q=beckup[number-1]
                                    whole=q[0][:]
                                    thisAgent=q[1][:]
                                    l=q[2]
                                    r=q[3]
                                else:
                                    new_agent.append(threading.Thread(target=agent, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},{l2}_{l2}",y+2)))
                                    new_agent[-1].start()
                                    q=beckup[number-1]
                                    whole=q[0][:]
                                    thisAgent=q[1][:]
                                    l=q[2]
                                    r=q[3]
                            r+=str(whole)[y]
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
                                    l+=str(y+1)
                                    k=1
                        r=""
                    else:
                        if str(whole)[y] != " " or y == 0:
                            r+=str(whole)[y]
                        else:
                            if len(whole) >= y+3:
                                agentsNumber[0]+=1
                                q=[whole[:],thisAgent[:],l,r]
                                beckup[number-1]=q
                                new_thisAgent=thisAgent[:]
                                k=0
                                for i in range(len(thisAgent)):
                                    if k == 1:
                                            pass
                                    elif thisAgent[i] == str(whole)[y+1]+str(whole)[y+2]:
                                        l2=str(i//2+1)
                                        k=1
                                if not(str(whole)[y+1]+str(whole)[y+2] in thisAgent):
                                    new_thisAgent.append(str(whole)[y+1]+str(whole)[y+2])
                                    new_agent.append(threading.Thread(target=agent, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},_{len(new_thisAgent)}",y+3)))
                                    new_agent[-1].start()
                                    q=beckup[number-1]
                                    whole=q[0][:]
                                    thisAgent=q[1][:]
                                    l=q[2]
                                    r=q[3]
                                else:
                                    new_agent.append(threading.Thread(target=agent, args=(agentsNumber[0],whole,new_thisAgent,'',f"{l},_{l2}",y+3)))
                                    new_agent[-1].start()
                                    q=beckup[number-1]
                                    whole=q[0][:]
                                    thisAgent=q[1][:]
                                    l=q[2]
                                    r=q[3]
                            r+=str(whole)[y]
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
    print('ожидаемый результат:',agents[0])
    return agents[0]
if len(sys.argv) > 1:
    input_pyt=sys.argv[1]
    with open(input_pyt,'r',encoding='latin-1', errors='ignore') as a:
        output=Packer(a.read())
    output_pyt=input_pyt+".lenu"
    with open(output_pyt,'w',encoding='latin-1', errors='ignore') as a:
        a.write(str(output))
input("нажми enter для завершения сборки...")
