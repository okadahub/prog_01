from my_module import get_filelist
from my_module import line_send_image

msg = '朝礼始まりますよ'
msg_font = 'BIZ UDゴシック'
msg_size = 25
line_send_image.send_line_ms(msg)
get_filelist.pop_msg2(msg,msg_font,msg_size)

