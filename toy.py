import hydra
from hydra.utils import call, instantiate
from omegaconf import DictConfig, OmegaConf

def function_test(x, y):
    result = x + y 
    print(f"{result = }")
    return result

class MyClass:
    def __init__(self, x):
        self.x = x

    def print_x_squared(self):
        print(f"{self.x **2 = }")


class MyComplexClass:
    def __init__(self, my_object: MyClass):
        self.obj = my_object

    def instantiate_object(self):
        self.obj = instantiate(self.obj)


@hydra.main(config_path="conf", config_name="toy", version_base=None)
def main(cfg: DictConfig):

    #Print config as yaml

    print(OmegaConf.to_yaml(cfg))

    # Easy
    print(cfg.foo)
    print(cfg.bar.bax)
    print(cfg.bar.more)
    print(cfg.bar.more.blabla)

    # Less Easy
    print("-------"*10)
    output = call(cfg.my_func)
    print(f"{output = }")

    output = call(cfg.my_func, y=100)
    print(f"{output = }")

    print("Partial")
    fn = call(cfg.my_partial_func)
    output = fn(y=1000)
    # print(f"{output = }")

    print("objects")
    obj = instantiate(cfg.my_object)  # obj type will be defined during runtime 
    # obj: MyClass = instantiate(cfg.my_object) # if in case u need to specify the object type
    obj.print_x_squared()

    print("-------"*10)
    complex_obj = instantiate(cfg.my_complex_object)  # obj type will be defined during runtime 
    # obj: MyClass = instantiate(cfg.my_object) # if in case u need to specify the object type
    print(complex_obj.obj)
    # complex_obj.obj.print_x_squared()
    complex_obj.instantiate_object()
    print(complex_obj.obj.print_x_squared())

    print("-------"*10)
    print(cfg.toy_model)
    mymodel = instantiate(cfg.toy_model)
    print(mymodel)



if __name__== "__main__":

    main()