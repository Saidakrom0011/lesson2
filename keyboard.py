from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 Kompaniya haqida"), KeyboardButton(text="📍 Fililallar"))
    rkm.row(KeyboardButton(text="💼 Bo'sh ish o'rinlari"))
    rkm.row(KeyboardButton(text="Menyu"), KeyboardButton(text="🗣 Yangiliklar"))
    rkm.row(KeyboardButton(text="📞 Kontaktlar/Manzil"), KeyboardButton(text="🇺🇿/🇷🇺 Til"))
    return rkm


# =================================================================


def location():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Geolokatsiyani yuboring", request_location=True))
    rkm.row(KeyboardButton(text="Ortga ↩️"), )
    return rkm


def toshkent_sh():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Samarqand Darvoza"), KeyboardButton(text="📍 Oloy bozori"))
    rkm.row(KeyboardButton(text="📍 Malika"), KeyboardButton(text="📍 Yahyo G'ulomov,94"))
    rkm.row(KeyboardButton(text="Ortga ↩️"), )
    return rkm


def filial_buttons():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="☕️ Yaqin filiallarni ko'rsatish"))
    rkm.row(KeyboardButton(text="🏢 Bosh ofis"), KeyboardButton(text="Toshkent sh."))
    rkm.row(KeyboardButton(text="Ortga ↩️"), )
    return rkm


def m_ulugbe():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Parkent"), KeyboardButton(text="📍Maksim Gorkiy"), KeyboardButton(text="📍Qorasu"))
    rkm.row(KeyboardButton(text="📍 Ekobozor savdo markazi"), KeyboardButton(text="📍Сельхоз"),
            KeyboardButton(text="📍 TTZ"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅ Ortga"))
    return rkm


def yakkasaroy():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Shota rustaveli"), KeyboardButton(text="📍 Muqimiy"),
            KeyboardButton(text="📍Next  Savdo Markazi"))
    rkm.row(KeyboardButton(text="📍Teatralny"), KeyboardButton(text="📍Южный"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅ Ortga"))
    return rkm


def sergeli():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Sergeli "), KeyboardButton(text=" 📍Sergeli Уangi Hayot"),
            KeyboardButton(text="📍 Sergeli Yarmarka"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅ Ortga"))
    return rkm


def mirobod():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Qo'yliq"), KeyboardButton(text="📍 Borovskiy"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅ Ortga"))
    return rkm


# ======================================================================================


def bosh_ish():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Toshkent"), KeyboardButton(text="Andijon"))
    rkm.row(KeyboardButton(text="Qarshi"), KeyboardButton(text="Qo'qon"))
    rkm.row(KeyboardButton(text="Namangan"), KeyboardButton(text="Toshkent viloyati"))
    rkm.row(KeyboardButton(text="Nukus"), KeyboardButton(text="Samarqand"))
    rkm.row(KeyboardButton(text="Farg'ona"), KeyboardButton(text="Shahrisabz"))
    rkm.row(KeyboardButton(text="Xorazm viloyati"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩️"))
    return rkm


def universal():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Yunusobod"), KeyboardButton(text="Mirzo Ulug'bek"))
    rkm.row(KeyboardButton(text="Yashnobod"), KeyboardButton(text="Yakkasaroy"))
    rkm.row(KeyboardButton(text="Uchtepa"), KeyboardButton(text="Sergeli"))
    rkm.row(KeyboardButton(text="Chilonzor."), KeyboardButton(text="Mirobod"))
    rkm.row(KeyboardButton(text="Bektemir"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="🔙Ortga"))
    return rkm


def toshkent():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Universal xodim"), KeyboardButton(text="Call-markaz operatori"))
    rkm.row(KeyboardButton(text="Kuryer"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩"))
    return rkm


def rus_uzb():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha"))
    rkm.row(KeyboardButton(text="Ortga ↩️"))
    return rkm


def filial():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Bahodir"), KeyboardButton(text="📍Oloy Bozori"), KeyboardButton(text="📍Yunusobod"))
    rkm.row(KeyboardButton(text="📍Universam"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga ↩"))
    return rkm


def bek():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga↩"))
    return rkm


def kuryer1():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Olmazor"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga↩"))
    return rkm


def call_():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Chilonzor"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="🔙Ortga"))
    return rkm


def chil():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="🏢 Bosh Ofis"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="Ortga↩️"))
    return rkm


def yashnobod2():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍Lisunova 2"), KeyboardButton(text="📍Lisunova"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅ Ortga"))
    return rkm


def yashnobod1():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅Ortga"))
    return rkm


# =========================================================================================


def uchtepa():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Beshqayrag'och"), KeyboardButton(text="📍Fozil Tepа"),
            KeyboardButton(text="📍Lutfiy"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅ Ortga"))
    return rkm


def f():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="↩️Ortga"))
    return rkm


def f2():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="↩Ortga"))
    return rkm


def chilonzor():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍 Chilonzor"), KeyboardButton(text="📍 Algoritm"),
            KeyboardButton(text="📍Magic City"))
    rkm.row(KeyboardButton(text="📍Katta qani"), KeyboardButton(text="📍Qatortol"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="🔙Ortga"))
    return rkm


def bektemir1():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="📍<<Compass>> savdo markazi"), KeyboardButton(text="📍Vodnik"),
            KeyboardButton(text="📍 Bektemir"))
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="⬅ Ortga"))
    return rkm


def back():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="◀️ Orqaga"))
    return rkm


def m_ulugbek_back():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="◀ Orqaga"))
    return rkm


def yakkasaroy_back():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text=" Ortga⬅"))
    return rkm


def sergeli_back():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text="ortga ⬅"))
    return rkm


def mirobod_back():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="❌ Bekor qilish ❌"), KeyboardButton(text=" ⬅Ortga"))
    return rkm