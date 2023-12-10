from config import access_token, groop_token
import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

def write_message(sender, message, token):
    authorize = vk_api.VkApi(token=token)
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

token = groop_token
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        received_message = event.text.lower()
        sender = event.user_id
        if received_message == 'привет':
            write_message(sender, 'Доброго времени суток!', token)
        elif received_message == 'пока':
            write_message(sender, 'До встречи', token)
        else:
            write_message(sender, 'Я тебя не понимаю', token)
