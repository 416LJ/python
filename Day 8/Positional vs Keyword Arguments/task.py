def calculate_love_score(input1,input2):
    input1 = input1.lower()
    input2 = input2.lower()
    new_name = input1+input2
    t = new_name.count("t")
    r = new_name.count("r")
    u = new_name.count("u")
    e = new_name.count("e")

    l = new_name.count("l")
    o = new_name.count("o")
    v = new_name.count("v")
    e = new_name.count("e")

    total_score = str(t+r+u+e)+str(l+o+v+e)
    print(total_score)


calculate_love_score("Kanye West", "Kim Kardashian")