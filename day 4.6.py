def removeChar(s, c) :

    counts = s.count(c)
 
    s = list(s)
 
    while counts :
  
        s.remove(c)
 

        counts -= 1
 

    s = '' . join(s)

    print(s)
 

if _name_ == '_main_' :    

    s = "geeksforgeeks"

    removeChar(s,'g')
