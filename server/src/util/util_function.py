

url_list = [
    "",
    "https://www.youtube.com/embed/pPzVV2kkGHc?si=P6Ubs8mnnHyuNfoU",
    "https://www.youtube.com/embed/4FpG1DcvHzc?si=pbrFQW6JL0DS4Kks",
    "https://www.youtube.com/embed/QSep-J6vtdc?si=6G0-NobUninonQCu",
    "https://www.youtube.com/embed/WHmmT_syaG8?si=GJcu17k5GhOaREaX",
    "https://www.youtube.com/embed/MKcSCaP0ZrQ?si=ADn8qTi2DlkThXoI",
    "https://www.youtube.com/embed/5uyGn147rr0?si=M2V5shXcIHvq1SmY",
    "https://www.youtube.com/embed/gRX-YxdFQzk?si=xrfeqtKOs67tnB5I",
    "https://www.youtube.com/embed/yqsqjqLGMe4?si=8-4jXmV4NjrgLlEr",
    "https://www.youtube.com/embed/snp580kqCto?si=Al_s2cz0Ia18rLI3",
    "https://www.youtube.com/embed/U7P4FbrraYs?si=7hMjQDQVjRHHKsyE",
    "https://www.youtube.com/embed/v388OYBkfME?si=q9yMGOpkLfgjbbZP",
    "https://www.youtube.com/embed/FDwJ6EW4dCM?si=z1IYj-pyX6V86yIK",
    "https://www.youtube.com/embed/1SJeLcI8otk?si=2diIbiQbPJHIwEmT",
    "https://www.youtube.com/embed/aaCeY4YCCmM?si=-MKkqwmPPnzHhuCw",
    "https://www.youtube.com/embed/IBgkKX6DUTM?si=XiXh7VwvA4zWwSbd",
    "https://www.youtube.com/embed/THoYkBItSkk?si=JD--j6GWuFBkN3Y0",
    "https://www.youtube.com/embed/THoYkBItSkk?si=L47bylhUdto72leK",
    "https://www.youtube.com/embed/obZ3HQaDly4?si=X6vWe-hFi6AdMg57",
    "https://www.youtube.com/embed/CrpLw5s2HQs?si=cA8zjVIxLAe4_40A",
    "https://www.youtube.com/embed/9UQza7XNt6M?si=DCw2ScgPaUtZnXy1",
    "https://www.youtube.com/embed/NpM0n6xBbrA?si=Fxjgfb5RBNUY48Z8",
    "https://www.youtube.com/embed/50IU9PwlKas?si=jptdAnFW7MFE-KXk",
    "https://www.youtube.com/embed/DDmExpQj1VI?si=j3pXaktl-OMxhGxh",
    "https://www.youtube.com/embed/nKqqtV-33k0?si=e3ibsoRtLLBD6mvU",
    "https://www.youtube.com/embed/ROq0rGmR3GE?si=SGwkjlWeczBQTvVD",
    "https://www.youtube.com/embed/cgsU5R5dY2Y?si=LndLlWOgOdTOzrZ7"
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
    return f"{url_list[lecture_num]}&amp;start=282={start_seconds}", format_time(start_seconds), format_time(end_seconds)
    