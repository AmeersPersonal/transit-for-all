from mta_api import *

def main():
    mta = mta_api()
    # print(mta.get_train_line_data("A"))
    # print(mta.stop_id_to_long_name("G05N"))
    # print(mta.long_name_to_id("Howard Beach-JFK Airport"))
    # print(mta.station_lines( "G05N"))4
    # print(mta.station_train_info("G05N"))
    print(mta.accessible("59 St-Columbus Circle"))
    #"59 St-Columbus Circle",

if __name__ == "__main__":
    main()  