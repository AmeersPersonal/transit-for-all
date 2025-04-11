from mta_api import *

def main():
    mta = mta_api()

    # n_train_stops = mta_api.get_train_stops("N")
    # for stop in n_train_stops:
    #     print(f"{stop['stop_id']}: {stop['stop_name']}")
    # print(mta.get_train_line_data("R"))
    # print(mta.get_station_coordinate("R44S"))
    print(mta.get_user_coordinate())

if __name__ == "__main__":
    main()  