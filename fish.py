# -*- coding: utf-8 -*-

import requests

import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from config import Config
from logics.base import *

chat_id = ""

def send_message(vk, id, text):
    vk.messages.send(
        peer_id=id,
        # attachment=','.join(attachments),
        random_id=get_random_id(),
        message=text
    )


def main():
    session = requests.Session()

    # Авторизация пользователя:
    """
    login, password = 'python@vk.com', 'mypassword'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    """

    # Авторизация группы (для групп рекомендуется использовать VkBotLongPoll):
    # при передаче token вызывать vk_session.auth не нужно
    """
    vk_session = vk_api.VkApi(token='токен с доступом к сообщениям и фото')
    """

    vk_session = vk_api.VkApi(token=Config.token)

    vk = vk_session.get_api()
    # upload = VkUpload(vk_session)  # Для загрузки изображений
    longpoll = VkBotLongPoll(vk_session, "175410603")


    for event in longpoll.listen():
        print(event)
        print(event.object.peer_id)

        if event.type == VkBotEventType.MESSAGE_NEW and event.object.text:
            # print('id{}: "{}"'.format(event.from_id, event.text), end=' ')

            # response = session.get(
            #     'http://api.duckduckgo.com/',
            #     params={
            #         'q': event.text,
            #         'format': 'json'
            #     }
            # ).json()
            #
            # text = response.get('AbstractText')
            # image_url = response.get('Image')

            # if not text:
            #     vk.messages.send(
            #         user_id=event.user_id,
            #         random_id=get_random_id(),
            #         message='No results'
            #     )
            #     print('no results')
            #     continue
            #
            # attachments = []
            #
            # if image_url:
            #     image = session.get(image_url, stream=True)
            #     photo = upload.photo_messages(photos=image.raw)[0]
            #
            #     attachments.append(
            #         'photo{}_{}'.format(photo['owner_id'], photo['id'])
            #     )
            text = ""
            print(event.object.text)
            found, text1 = hello(event.object.peer_id, event.object.text)
            if found:
                text = text1
            else:
                print("Not found")
            found, text1 = jekakill("", event.object.text)
            if found:
                text = text1
            else:
                print("Not found")

            found, text1 = writetoivan("", event.object.text)
            if found:
                text = text1
            else:
                print("Not found")
            found, text1 = check(None, event.object.text, "рыба кто уебок", "Камол, когда говорит что ты хочешь писать контрольную по КМ..")
            if found:
                text = text1
            else:
                print("Not found")
            found, text1 = check_fuck(None, event.object.text)
            if found:
                text = text1
            else:
                print("Not found")
            # if event.object.peer_id != "2000000001":
            #     hard_print(event.object.text)

            if text != "":
                send_message(vk, event.object.peer_id, text)



if __name__ == '__main__':
    main()
