def main():
    # Given and derived ages
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen

    # Printing results exactly as expected
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))


# Required line to call main
if __name__ == "__main__":
    main()
