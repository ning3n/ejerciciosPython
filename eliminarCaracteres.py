def my_function(str_1, str_2):
    str_1_set = set(str_1.upper())
    str_2_set = set(str_2.upper())

    out_1 = str_1_set - str_2_set
    out_2 = str_2_set - str_1_set
    print(
        "\n· Caracteres presentes en la primera palabra, pero NO\n"
        f"presentes en la segunda, son los siguientes: {out_1}\n"
        )

    print(
        "\n· Caracteres presentes en la segunda palabra, pero NO\n"
        f"presentes en la primera, son los siguientes: {out_2}\n"
        )


my_function("Hola", "pato")