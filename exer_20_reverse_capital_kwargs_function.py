def function(l,**kwargs):
    if 'reverse_str' in kwargs:
        return [i[::-1].title() for i in l]
    else:
        return [ i.title() for i in l]
    


    
user_input = ['deepak','komal']
print(function(user_input,reverse_str = True ))