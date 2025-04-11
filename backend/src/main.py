from mta_api import *

def main():
    mta = mta_api()

    # n_train_stops = mta_api.get_train_stops("N")
    # for stop in n_train_stops:
    #     print(f"{stop['stop_id']}: {stop['stop_name']}")

    print(mta.stop_id_to_long_name("R45N"))


if __name__ == "__main__":
    main()  