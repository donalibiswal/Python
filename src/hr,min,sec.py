userscnd=int(input("enter seconds:"))
hour=userscnd//3600
pscnd=hour*3600
remscnd=userscnd-pscnd
min=remscnd//60
sscnd=remscnd-(min*60)
print(userscnd,"second is",hour,"hour",min,"minutes and",sscnd,"seconds")
    
