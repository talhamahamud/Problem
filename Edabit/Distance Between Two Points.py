def dict(dic, dic1):
    j=(dic["x"]-dic1["x"])**2 + (dic["y"]-dic1["y"])**2
    root=j**0.5
    print(root)

dict({"x": 10, "y": -5}, {"x": 8, "y": 16})