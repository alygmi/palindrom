def palindrome(pal=None) :

    if pal is None:  # Jika tidak ada input dari parameter, gunakan input user
        pal = str(input("Masukkan kata untuk diputar: "))


        array = list(pal)
        reversed = array[::-1]
        rep = "" .join(reversed)

    print(rep)

palindrome()
