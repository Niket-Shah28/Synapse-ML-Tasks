W=[0,0,0,0,0,0,0,0,0]
while True:
    print("1.Do you want to battle?\n2.Exit\nEnter your choice:")
    choice=int (input())
    if(choice==1):
        class Titandex:
            Titan=["Founding Titan","Attack Titan","Armored Titan","Colossal Titan","War Hammer Titan","Beast Titan",
            "Cart Titan","Female Titan","Jaw Titan"]
            Titan_Strength=[350,275,250,300,235,250,175,270,225]
            print("Titan =",Titan,"Titan_Strength =",Titan_Strength)
            print("Enter the number of Titan:")
            j=int (input())
            def TitanvsScout(a,b,c):
                Scout=["Levi","Mikasa","Eren","Armin","Erwin","Hange","Jean","Sasha","Connie"]
                Scout_Strength=[300,275,270,250,275,230,230,200,180]
                print("Scouts =",Scout,"\nScout Strength =",Scout_Strength,"\nEnter the number of Scout:")
                m=int (input())
                if(b<Scout_Strength[m-1]):
                    c=0
                    print("",Scout[m-1],"wins the match")
                elif(b>Scout_Strength[m-1]):
                    c=c+1
                    print("",a,"wins the match")
                else:
                    print("It was a tie")
                return c
            def TitanvsTitan(a,b,c,d):
                Titan=["Founding Titan","Attack Titan","Armored Titan","Colossal Titan","War Hammer Titan","Beast Titan",
                "Cart Titan","Female Titan","Jaw Titan"]
                Titan_Strength=[350,275,250,300,235,250,175,270,225]
                print("Titan =",Titan,"\nTitan Strength =",Titan_Strength,"\nEnter the other Titan:")
                l=int (input())
                if(l!=c):
                    if(b<Titan_Strength[l-1]):
                        print("",Titan[l-1],"wins the match")
                    elif(b>Titan_Strength[l-1]):
                        d=d+1
                        print("",a,"wins the match")
                    else:
                        print("It was a tie")
                else:
                    print("Titan cannot match with itself")
                return d
            print("1.Titan vs Scout\n2.Titan vs Titan\nEnter your choice:")
            choice2=int (input())
            if(choice2==1):
                W[j-1]=TitanvsScout(Titan[j-1],Titan_Strength[j-1],W[j-1])
            if(choice2==2):
                W[j-1]=TitanvsTitan(Titan[j-1],Titan_Strength[j-1],j,W[j-1])
    if(choice==2):
        break            
print("Win Streak =",W)



         
        


