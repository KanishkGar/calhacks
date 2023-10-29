

url_list = [
    "",
    "https://youtu.be/pPzVV2kkGHc?si=yfebQtVs6moW-byY",
    "https://youtu.be/4FpG1DcvHzc?si=kLYa-wjTn9-Gzqsu",
    "https://youtu.be/QSep-J6vtdc?si=J902GmZkzH2B1tQZ",
    "https://youtu.be/WHmmT_syaG8?si=ccDOgotL5Br_-u6p",
    "https://youtu.be/MKcSCaP0ZrQ?si=w4-mes-fBVlpgZwv",
    "https://youtu.be/5uyGn147rr0?si=t7fxuPfwcL3IphUs",
    "https://youtu.be/gRX-YxdFQzk?si=k7J8FDpJ9BxC2idM",
    "https://youtu.be/yqsqjqLGMe4?si=C-R83Ux8y4lw3pCv",
    "https://youtu.be/snp580kqCto?si=aB8m61_4u9FtgKx2",
    "https://youtu.be/U7P4FbrraYs?si=WwoGoaE0s6gVql_F",
    "https://youtu.be/v388OYBkfME?si=WyJ9Yvpb7UlEt67p",
    "https://youtu.be/FDwJ6EW4dCM?si=q4KnJDwzqcjb_7oU",
    "https://youtu.be/1SJeLcI8otk?si=Gf3TsfpjWYK2PtSF",
    "https://youtu.be/aaCeY4YCCmM?si=_0A-N9GFbaJYCRXN",
    "https://youtu.be/IBgkKX6DUTM?si=cBtGl_Rw6r0R0F_4",
    "https://youtu.be/THoYkBItSkk?si=l36nU6pdxOM4ohlc",
    "https://youtu.be/5pXaixRmj8U?si=1WSO7YI5INcmGiF5",
    "https://youtu.be/obZ3HQaDly4?si=TpZDm-iJP15QNIUp",
    "https://youtu.be/CrpLw5s2HQs?si=hkJNP7evlhq2yJPJ",
    "https://youtu.be/9UQza7XNt6M?si=PCy2_mAq1OHFWpRE",
    "https://youtu.be/NpM0n6xBbrA?si=LrF_nn6Xx2x7xn58",
    "https://youtu.be/50IU9PwlKas?si=IFA0iMt5C9oSBw6S",
    "https://youtu.be/DDmExpQj1VI?si=UZb5EewCLRdF1lQ0",
    "https://youtu.be/nKqqtV-33k0?si=zeUWJxG9lYm2cb7p",
    "https://youtu.be/ROq0rGmR3GE?si=duizHw13eGv_PnkC",
    "https://youtu.be/cgsU5R5dY2Y?si=hTTSy3_u2zjzfcwv"
]

def format_time(total_seconds):
    # Get the hours, minutes and seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Format the result as hh:mm:ss
    return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

"""
return url of video, timestamped
start time
end time
"""
def process_key_tuple(key: str):
    lecture_num, start_seconds, end_seconds = map(int, key.split(":")[1:])
    return f"{url_list[lecture_num]}&t={start_seconds}s", format_time(start_seconds), format_time(end_seconds)
    