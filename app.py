def rev_str(string:str,filter_list:list):
    return "".join([letter for letter in list(string) if letter not in filter_list])[::-1].capitalize()

if __name__=="__main__":
    print(rev_str(string="privet my best duck",filter_list=["b","p"]))
