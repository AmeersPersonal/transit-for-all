from mta_api import *

def main():
    mta = mta_api()
  
    # print(mta.train_delay("59 St-Columbus Circle", "A"))
    print(mta.get_train_line_data("A"))


if __name__ == "__main__":
    main()  