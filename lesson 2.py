from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from keyboard import toshkent_sh, location, main_menu, filial_buttons, bosh_ish, toshkent, universal, rus_uzb, filial, \
    bek, kuryer1, call_, chil, yashnobod2, yashnobod1, uchtepa, f, chilonzor, f2, bektemir1, back, mirobod, sergeli, \
    yakkasaroy, m_ulugbe, m_ulugbek_back, mirobod_back, sergeli_back, yakkasaroy_back

BOT_TOKEN = "6709867527:AAEkKLI623leVohfq0gIsdwU3nOjIaXJ_Vc"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

evos_photo = "https://tashkent.hh.uz/employer-logo/4136381.jpeg"
evos_oila = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFpKI5FQi1vU-KDNnV28P_vU5kc2O00rmO17FwhALUxA&s"
evos_logo = "https://www.afisha.uz/uploads/media/2016/07/0039781.jpeg"
evos_photo2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvnm9nSpmPYTX15rRffNL2TXRoESqO6C0_c5ce7Ixq5w&s"
s_darvoza = "https://static-pano.maps.yandex.ru/v1/?panoid=1486723667_804149084_23_1571463763&size=500%2C240&azimuth=-139.4&tilt=10&api_key=maps&signature=tsrellj2DdPkv-JEFG9ojXrYn-8PMeL28xQTb3ROENg="
oloy_bozor = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMgl32zFLC0Ql6UbaU5iMSx5raKKLk9pGxuy9BZkwpwQ&s"
malika = "https://static-pano.maps.yandex.ru/v1/?panoid=1486924588_803943131_23_1571376779&size=500%2C240&azimuth=-141.7&tilt=10&api_key=maps&signature=DdlrOrOArVXDDZSkXfAWL58SjRE3slrdvJMjyF0SWN8="
yahyo_94 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRFRHov4mHtfflm9EVYkpLDtrW0ZUCaodWMMG6dhU4LQ&s"
evos1 = "https://www.afisha.uz/uploads/media/2022/12/9e2a6d8a2dda6e4d5c4f75caca7b4059_lf.jpg"
evos2 = "https://www.afisha.uz/uploads/media/2022/12/4cc430c20430ddf64df55e8206bdbbc7_l.jpg"
evos3 = "https://cachizer2.2gis.com/reviews-photos/d389feea-4a1d-4afb-a6a1-365ba8703b8b.jpg?w=1920"
# <a href='https://evos.uz/'>Evos saytiga o'tish</a>
http1 = "<a href='https://www.instagram.com/evosuzbekistan/'>Instagram</a>"
http2 = "<a href='https://t.me/evosdeliverybot'>Telegram</a>"
http3 = "<a href='https://www.facebook.com/evosuzbekistan/'>Facebook</a>"

universal_ish = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTr4nrBy5mFQ3bCqHDozBGcUt_yv1a97olafsRpdhraQg&s"
kuryer = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTixsAfGtql5eng3RkJgU0pqk-ea0bs0Y97prn_aKTkQ&s"
call = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8_zngq9JgWqTgLsvGknN84qFJ5j0ed42KrcVWCiaUmg&s"
furqat = "https://static-pano.maps.yandex.ru/v1/?panoid=1486824878_804265745_23_1572248376&size=500%2C240&azimuth=76.8&tilt=10&api_key=maps&signature=CaO7wYSx-bbtQgHXq_MiJRk-RnQb6sn7Ch4cIebYeBw="
chilonzor_p = "https://repost.uz/storage/uploads/0-1615789721-kamila-post-material.jpeg"


@dp.message_handler(commands=["start", "help"])
async def start_bot(message: types.Message):
    await message.answer("Botga xush kelibsan ukam", reply_markup=main_menu())


@dp.message_handler(commands="restart")
async def start_bot(message: types.Message):
    await message.answer("...", reply_markup=main_menu())


@dp.message_handler(Text(equals="📍 Fililallar"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo,
                               reply_markup=filial_buttons(),
                               caption="""EVOS - O'zbekistondagi eng yirik fastfud kompaniyasi. Ayni paytda 49 ta chakana savdo shoxobchasi va zamonaviy diversifikatsiyalangan ishlab chiqarish ochiq.

Kompaniya xodimlari birgalikda rivojlanib, kundan -kunga o'sib borayotgan katta oila. EVOS har kuni kengayib bormoqda, bugungi kunda bizda bir yarim mingdan ortiq odam bor. Bizning jamoamizga a'zo bo'ling, EVOS oilasiga xush kelibsiz!""")


# ======================================================================================
@dp.message_handler(Text(equals="☕️ Yaqin filiallarni ko'rsatish"))
async def orqa_bot(message: types.Message):
    await message.answer("Энг яқин филиални топиш учун жойлашувингизни юборинг", reply_markup=location())


@dp.message_handler(Text(equals="🏢 Bosh ofis"))
async def orqa_bot(message: types.Message):
    await message.answer_photo(photo=furqat, caption="""Manzil:  Furqat ko'chasi 175, 1-kirish, 4-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998712031212""")
    latitude = 41.302196
    longitude = 69.248867
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="Toshkent sh."))
async def orqa_bot(message: types.Message):
    await message.answer("Toshkent sh.", reply_markup=toshkent_sh())


@dp.message_handler(Text(equals="📍 Samarqand Darvoza"))
async def orqa_bot(message: types.Message):
    await message.answer_photo(photo=s_darvoza, caption="""Filial: "Samarqand Darvoza"
Manzil: Qoratosh, 5A""")
    latitude = 41.316428
    longitude = 69.230965
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="📍 Oloy bozori"))
async def orqa_bot(message: types.Message):
    await message.answer_photo(photo=oloy_bozor, caption="""Filial: Oloy bozori

Manzil: Amir Temur prospekti, 42

Kontakt: +998 71 203 12 12""")
    latitude = 41.32
    longitude = 69.282572
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="📍 Malika"))
async def orqa_bot(message: types.Message):
    await message.answer_photo(photo=malika, caption="""Filial: Malika

Manzil: Bog'iravon, 29

Kontakt: +998 71 203 12 12""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)


@dp.message_handler(Text(equals="📍 Yahyo G'ulomov,94"))
async def orqa_bot(message: types.Message):
    await message.answer_photo(photo=yahyo_94, caption="""Filial: Yahyo G'ulomov ko'chasi, 94

Manzil: Yahyo G'ulomov ko'chasi, 94

Kontak: +998 71 203 12 12""")
    latitude = 41.342807
    longitude = 69.264684
    await message.answer_location(latitude=latitude, longitude=longitude)


# ==============================================================================================
@dp.message_handler(Text(equals="🏢 Kompaniya haqida"))
async def start_bot(message: types.Message):
    await message.answer_photo(photo=evos_oila,
                               caption="""EVOS ® tez xizmat ko'rsatish restoranlari tarmog'i bir joyda turmaydi, siz uchun va siz bilan doimo o'sib boradi va rivojlanadi! Biz geografiyamizni kengaytiramiz va deyarli har oyda yangi filiallarni ochamiz.
Endi bizning tarmog'imizning O'zbekiston bo'ylab 50 dan ortiq filiali mavjud. Biz doimo jamoamizning bir qismi bo'lishni xohlaydigan va EVOS ® da o'z faoliyatini boshlashga tayyor bo'lgan dinamik va faol odamlarni qidiramiz.
EVOS ® –  bu ishonchli brenddir. EVOS ® da ishlash – barqaror daromad va martaba istiqbollari kafolati.
EVOS ® da o'z karyerangizni boshlang!""")


@dp.message_handler(Text(equals="Ortga ↩️"))
async def orqa1_bot(message: types.Message):
    await message.answer_photo(photo=evos_logo,
                               reply_markup=main_menu())


@dp.message_handler(Text(equals="↩️Ortga"))
async def orqa1_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?",
                         reply_markup=uchtepa())


@dp.message_handler(Text(equals="Ortga↩️"))
async def orqa1_bot(message: types.Message):
    await message.answer_photo(photo=evos_logo,
                               reply_markup=call_())


@dp.message_handler(Text(equals="🔙Ortga"))
async def orqa1_bot(message: types.Message):
    await message.answer("back", reply_markup=toshkent())


@dp.message_handler(Text(equals="Ortga ↩"))
async def orqa_bot(message: types.Message):
    await message.answer("EVOS jamoasiga qo'shiling!")
    await message.answer("📍 Shaharni tanlang",
                         reply_markup=bosh_ish())


@dp.message_handler(Text(equals="Ortga↩"))
async def orqa_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=filial())


@dp.message_handler(Text(equals=" ⬅Ortga"))
async def orqa_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=mirobod())


@dp.message_handler(Text(equals="ortga ⬅"))
async def orqa_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=sergeli())


@dp.message_handler(Text(equals="Ortga⬅"))
async def orqa_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=yakkasaroy())


@dp.message_handler(Text(equals="◀ Orqaga"))
async def orqa_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=m_ulugbe())


@dp.message_handler(Text(equals="◀️ Orqaga"))
async def orqa_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=bektemir1())


@dp.message_handler(Text(equals="❌ Bekor qilish ❌"))
async def bekor_bot(message: types.Message):
    await message.answer_photo(photo=evos_logo,
                               reply_markup=main_menu())


@dp.message_handler(Text(equals="💼 Bo'sh ish o'rinlari"))
async def ish_bot(message: types.Message):
    await message.answer("EVOS jamoasiga qo'shiling!")
    await message.answer("📍 Shaharni tanlang",
                         reply_markup=bosh_ish())


@dp.message_handler(Text(equals="Menyu"))
async def menyu_bot(message: types.Message):
    await message.answer_photo(photo=evos_photo2,
                               caption="<a href='https://evos.uz/'>Evos saytiga o'tish</a>",
                               parse_mode="HTML")
    await message.answer(f"| {http1} | {http2} | {http3} |", parse_mode="HTML")


@dp.message_handler(Text(equals="Toshkent"))
async def toshkent_bot(message: types.Message):
    await message.answer(text="💼 Sizni qiziqtirgan lavozimni tanlang",
                         reply_markup=toshkent())


@dp.message_handler(Text(equals="Universal xodim"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=universal_ish, caption="""🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 Erkin jadval (iloji bo'lsa)

✔️ Yoqimli tashqi ko'rinish

💰 Ish haqi 17228.96 dan (soliqlargacha) bir soatiga""",
                               reply_markup=universal())
    await message.answer(text="Hozirda vakansiya ochilgan tumanlardan birini tanlang")


@dp.message_handler(Text(equals="🇺🇿/🇷🇺 Til"))
async def universal_bot(message: types.Message):
    await message.answer(text="Tilni o'zgartirish", reply_markup=rus_uzb())


@dp.message_handler(Text(equals="🇷🇺 Русский"))
async def universal_bot(message: types.Message):
    await message.answer(text="Выбрано: 🇷🇺 Русский", reply_markup=main_menu())
    await message.answer_photo(photo=evos_logo)


@dp.message_handler(Text(equals="🇺🇿 O'zbekcha"))
async def universal_bot(message: types.Message):
    await message.answer(text="Tanlandi: 🇺🇿 O'zbekcha", reply_markup=main_menu())
    await message.answer_photo(photo=evos_logo)


@dp.message_handler(Text(equals="Yunusobod"))
async def universal_bot(message: types.Message):
    await message.answer(text="📍 Qaysi filialda ishlashni istaysiz?", reply_markup=filial())


@dp.message_handler(Text(equals="📍 Bahodir"))
async def universal_bot(message: types.Message):
    await message.answer("Yunusota ko'chasi, 25/24")
    await message.answer_location(41.379405, 69.305609)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=bek())


@dp.message_handler(Text(equals="📍Oloy Bozori"))
async def universal_bot(message: types.Message):
    await message.answer("Toshkent, Amir Temur shoh ko‘chasi, 42-uy")
    await message.answer_location(41.320045, 69.282388)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=bek())


@dp.message_handler(Text(equals="📍Yunusobod"))
async def universal_bot(message: types.Message):
    await message.answer("Toshkent, Mayqo‘rg‘on ko‘chasi, 11B")
    await message.answer_location(41.360131, 69.277341)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=bek())


@dp.message_handler(Text(equals="📍Universam"))
async def universal_bot(message: types.Message):
    await message.answer("Yunusobod tumani, 4-kvartal, Ahmad Donisha ko‘chasi, 1-uy")
    await message.answer_location(41.364632, 69.28619)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=bek())


# ================================
evos_ishcilar = "https://hhcdn.ru/icms/10236973.jpg"


@dp.message_handler(Text(equals="Mirobod"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=mirobod())


@dp.message_handler(Text(equals="Sergeli"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=sergeli())


@dp.message_handler(Text(equals="Yakkasaroy"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=yakkasaroy())


@dp.message_handler(Text(equals="Mirzo Ulug'bek"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=m_ulugbe())


# -----------------------------------------------------------------------------------------------
@dp.message_handler(Text(equals="📍 Parkent"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos2, caption="Toshkent, ko'ch. Parkent, 131")
    await message.answer_location(41.315319, 69.326825)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=m_ulugbek_back())


@dp.message_handler(Text(equals="📍Maksim Gorkiy"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos1, caption="51 Mirzo Ulug'bek shoh ko'chasi, Tashkent, Oʻzbekiston")
    await message.answer_location(41.325678, 69.324202)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=m_ulugbek_back())


@dp.message_handler(Text(equals="📍Qorasu"))
async def universal_bot(message: types.Message):
    await message.answer(text=" Toshkent, Mirzo-Ulug‘bek tumani, Qorasuv massivi, 3-kvartal, 14B")
    await message.answer_location(41.334534, 69.370307)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=m_ulugbek_back())


@dp.message_handler(Text(equals="📍 Ekobozor savdo markazi"))
async def universal_bot(message: types.Message):
    await message.answer(text=" Toshkent, Timur Malik koʻchasi, 3-uy")
    await message.answer_location(41.354120, 69.353765)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=m_ulugbek_back())


@dp.message_handler(Text(equals="📍Сельхоз"))
async def universal_bot(message: types.Message):
    await message.answer(text="Toshkent viloyati, Qibray tumani, Salar shaharcha qishlog‘i, Toshkent halqa yo‘li")
    await message.answer_location(41.358741, 69.339849)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=m_ulugbek_back())


@dp.message_handler(Text(equals="📍 TTZ"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos3, caption="Toshkent, Mirzo Ulug‘bek tumani, Beshkapa mahallasi")
    await message.answer_location(41.355779, 69.376185)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=m_ulugbek_back())


# --------------------------------------
@dp.message_handler(Text(equals="📍 Shota rustaveli"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos_ishcilar, caption="Shota Rustaveli ko'chasi , 36")
    await message.answer_location(41.289761, 69.25791)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=yakkasaroy_back())


evos_muqimiy = "https://lh3.googleusercontent.com/p/AF1QipNSF8E16ANKuYAZ9iEYShgYaVH7QfvBKx289Qo=s1360-w1360-h1020"


@dp.message_handler(Text(equals="📍 Muqimiy"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos_muqimiy, caption="O'zbekiston, Toshkent, ko'ch. Muqimiy, 7")
    await message.answer_location(41.280094, 69.241587)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=yakkasaroy_back())


@dp.message_handler(Text(equals="📍Next  Savdo Markazi"))
async def universal_bot(message: types.Message):
    await message.answer(text="Yakkasaroy tumani, Bobura ko‘chasi, 6-uy")
    await message.answer_location(41.297943, 69.249430)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=yakkasaroy_back())


@dp.message_handler(Text(equals="📍Teatralny"))
async def universal_bot(message: types.Message):
    await message.answer(text="Yakkasaroy tumani, Bobura ko‘chasi 40A")
    await message.answer_location(41.285577, 69.253180)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=yakkasaroy_back())


@dp.message_handler(Text(equals="📍Южный"))
async def universal_bot(message: types.Message):
    await message.answer(
        text="ТРЦ Vega Centre, ул. Шота Руставели 150 напротив Южного вокзала, 100121, Тоshkent по Zargarlik ko'chasi и Kichik Xalqa Yo'li")
    await message.answer_location(41.265794, 69.163627)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=yakkasaroy_back())


# ===================
@dp.message_handler(Text(equals="📍 Sergeli"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos_logo, caption="Toshkent, Sergeli tumani, Yangi-Sergeli mahallasiYo'nalish")
    await message.answer_location(41.223005, 69.221532)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=sergeli_back())


@dp.message_handler(Text(equals="📍Sergeli Уangi Hayot"))
async def universal_bot(message: types.Message):
    await message.answer(text="Toshkent, Mehrigiyo ko‘chasi, 84-uy")
    await message.answer_location(41.220129, 69.201101)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=sergeli_back())


@dp.message_handler(Text(equals="📍 Sergeli Yarmarka"))
async def universal_bot(message: types.Message):
    await message.answer(text="Toshkent, Yangi Sergeli ko'chasi")
    await message.answer_location(41.211754, 69.230009)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=sergeli_back())


# --------------------------------------------------

@dp.message_handler(Text(equals="📍 Qo'yliq"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos_ishcilar,
                               caption="O'zbekiston, Toshkent, Mirobod tumani, Parvona mahallasi 3-o'tish Sarbon")
    await message.answer_location(41.364632, 69.28619)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=mirobod_back())


@dp.message_handler(Text(equals="📍 Borovskiy"))
async def universal_bot(message: types.Message):
    await message.answer(text="Toshkent, Yahyo G‘ulomov ko‘chasi, 94-uy")
    await message.answer_location(41.304774, 69.284622)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=mirobod_back())


# ================================

@dp.message_handler(Text(equals="Kuryer"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=kuryer, caption="""📌 Yosh 20 dan 35 gacha

🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 Erkin jadval (iloji bo'lsa)

👨‍💼/👩‍💼 Chiroyli ko'rinish

🚘 Shaxsiy transport bo'lishligi shart

📍Oylik maosh joylashuv va regonga qarab""")
    await message.answer("Hozirda vakansiya ochilgan tumanlardan birini tanlang", reply_markup=kuryer1())


@dp.message_handler(Text(equals="Call-markaz operatori"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=call, caption="""📌 Yosh 18 dan 35 gacha

🇷🇺/🇺🇿 Rus va o'zbek tillarni bilish kerak

🕑 To'liq bandlik

👨‍💼/👩‍💼 Chiroyli ko'rinish

🧑‍💻/👩‍💻 Kompyuter yoki noutbuk bo'lishi kerak
Biz taqdim etamiz:
- Rasmiy ish
- Kompaniya tomonidan taqdim etiladigan ovqatlanish
- Birinchi ish kuningizdan hisoblanadigan  ish xaqi
- Soatlik ish haqi""")
    await message.answer("Hozirda vakansiya ochilgan tumanlardan birini tanlang", reply_markup=call_())


@dp.message_handler(Text(equals="🏢 Bosh Ofis"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=furqat, caption="Furqat ko'chasi 175")
    await message.answer_location(41.302196, 69.248867)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=bek())


@dp.message_handler(Text(equals="🔙Ortga"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=chil())


@dp.message_handler(Text(equals="Chilonzor"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=chil())


@dp.message_handler(Text(equals="Chilonzor."))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=chilonzor())


@dp.message_handler(Text(equals="Yashnobod"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=yashnobod2())


@dp.message_handler(Text(equals="⬅Ortga"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=yashnobod2())


@dp.message_handler(Text(equals="⬅ Ortga"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=universal())


@dp.message_handler(Text(equals="🔙 Ortga"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=universal())


@dp.message_handler(Text(equals=" ⬅Ortga"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=universal())


@dp.message_handler(Text(equals="↩Ortga"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=chilonzor())


@dp.message_handler(Text(equals="📍Lisunova"))
async def universal_bot(message: types.Message):
    await message.answer("Aviasozlar 3, 21-bino")
    await message.answer_location(41.291741, 69.340696)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=yashnobod1())


@dp.message_handler(Text(equals="📍 Chilonzor"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=chilonzor_p,
                               caption="Toshkent, Chilonzor tumani, Chilonzor massivi, 10-kvartal, 17-uy")
    await message.answer_location(41.279398, 69.197988)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f2())


@dp.message_handler(Text(equals="📍Lisunova 2"))
async def universal_bot(message: types.Message):
    await message.answer("Toshkent, Aviasozlar 9/3")
    await message.answer_location(41.290595, 69.342981)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=yashnobod1())


@dp.message_handler(Text(equals="Uchtepa"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=uchtepa())


@dp.message_handler(Text(equals="📍 Beshqayrag'och"))
async def universal_bot(message: types.Message):
    await message.answer("Toshkent, Ko'kcha Darvoza ko'chasi, 622")
    await message.answer_location(41.310653, 69.166091)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f())


@dp.message_handler(Text(equals="📍Fozil Tepа"))
async def universal_bot(message: types.Message):
    await message.answer("Uchtepa tumani, Fozil tepa ko‘chasi, 25-uy, 12 B-uy")
    await message.answer_location(41.283575, 69.164983)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f())


@dp.message_handler(Text(equals="📍Lutfiy"))
async def universal_bot(message: types.Message):
    await message.answer("Chilonzor massivi, 12-kvartal, 41")
    await message.answer_location(41.281626, 69.181078)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f())


@dp.message_handler(Text(equals="📍 Algoritm"))
async def universal_bot(message: types.Message):
    await message.answer("O'zbekiston, Toshkent, Sugalli ota ko'chasi")
    await message.answer_location(41.272316, 69.160647)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f2())


@dp.message_handler(Text(equals="📍Magic City"))
async def universal_bot(message: types.Message):
    await message.answer("Magic City Park Chilonzor tumani, Olmazor massivi, 183a")
    await message.answer_location(41.303477, 69.245444)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f2())


@dp.message_handler(Text(equals="📍Katta qani"))
async def universal_bot(message: types.Message):
    await message.answer("Chilonzor tumani, 20-kvartal, Katta-qаni ko‘chasi.")
    await message.answer_location(41.268828, 69.172708)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f2())


@dp.message_handler(Text(equals="📍Qatortol"))
async def universal_bot(message: types.Message):
    await message.answer("Chilonzor tumani, Chilonzor massivi, 8-uy, 21A 1-qavat")
    await message.answer_location(41.262328, 69.164708)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=f2())


@dp.message_handler(Text(equals="Bektemir"))
async def universal_bot(message: types.Message):
    await message.answer("📍 Qaysi filialda ishlashni istaysiz?", reply_markup=bektemir1())


@dp.message_handler(Text(equals="📍<<Compass>> savdo markazi"))
async def universal_bot(message: types.Message):
    await message.answer("Toshkent halqa yo‘li, 17-uy")
    await message.answer_location(41.262328, 69.164708)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=back())


@dp.message_handler(Text(equals="📍Vodnik"))
async def universal_bot(message: types.Message):
    await message.answer("Husayn Boyqoro ko‘chasi, 37A/1")
    await message.answer_location(41.262328, 69.164708)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=back())


@dp.message_handler(Text(equals="📍 Bektemir"))
async def universal_bot(message: types.Message):
    await message.answer("Toshkent, Bektemir yo‘li ko‘chasi")
    await message.answer_location(41.262328, 69.164708)
    await message.answer("👤 Ism sharifingizni kiriting?", reply_markup=back())


# ------------------------------------------------------------------------------------------------------------


@dp.message_handler(Text(equals="🗣 Yangiliklar"))
async def universal_bot(message: types.Message):
    await message.answer("""Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""")


@dp.message_handler(Text(equals="📞 Kontaktlar/Manzil"))
async def universal_bot(message: types.Message):
    await message.answer_photo(photo=evos_logo, caption="""Manzil: Furqat ko'chasi 175, kirish 1, 
2-qavat.
Mo'ljal: MAKRO THE TOWER

Kontakt: +998 71 203 12 12""")
    await message.answer_location(41.302196, 69.248867)


if __name__ == '__main__':
    executor.start_polling(dp)
