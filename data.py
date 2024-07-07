class TestDataCreateOrder:
    CREATE_ORDER_BODY = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    CREATE_ORDER_NOCOLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            ""
        ]
    }

    CREATE_COURIER_DETAILS = {
            "login": "testinnng17",
            "password": "1456789",
            "firstName": "Anton"
        },


    CREATE_ORDER_EMPTY_LOGIN = {
            "login": "",
            "password": "1456789",
            "firstName": "Anton"
        },
    LOGIN = {"login": "testinnng17", "password": "1456789"}
    LOGIN_EMPY_PASSWORD = {"login": "testinnng17", "password": ""}
    LOGIN_NON_EXIST_LOGIN_PASS = {"login": "DFDDD7", "password": "14444789"}