from emoji import emojize

calendar = emojize(":spiral_calendar_pad:", use_aliases=True)
hand = emojize(":v:", use_aliases=True)
bell = emojize(":bell:", use_aliases=True)
weather = emojize(":sunny: ", use_aliases=True)
clock = emojize(":clock2:", use_aliases=True)
description = emojize(":page_with_curl:", use_aliases=True)
idk = emojize(":man_shrugging:", use_aliases=True)
more = emojize(":mag_right:", use_aliases=True)

def num_to_emoji(num):
    """Format got number of event and format it to emoji"""
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'keycap_ten']
    for n in range(10):
        if n == num:
            emoji = ":" + numbers[n-1] + ":"
            return emojize(emoji, use_aliases=True)
