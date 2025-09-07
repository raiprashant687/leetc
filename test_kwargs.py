test_configs = {
    "name":{"initial":None,
            "middle":None,},
    "age":None,

}



def test_kwargs(**kwargs):

    dct = test_configs.copy()

    # print(id(dct["name"]))
    # print(id(test_configs["name"]))
    for k, v in test_configs.items():
        if type(v) is dict:
            for k, v in v.items():
                


test_kwargs()