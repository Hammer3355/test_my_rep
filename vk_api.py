import requests
from config import access_token


class VKAPI:
    def __init__(self, user_id, count, order, fields):
        self.access_token = access_token
        self.version = 5.199
        self.user_id = user_id
        self.count = count
        self.order = order
        self.fields = fields

    def get_friends(self):
        response = requests.get(f"https://api.vk.com/method/friends.get",
                                params={"access_token": self.access_token,
                                        "v": self.version,
                                        "user_id": self.user_id,
                                        "order": self.order,
                                        "count": self.count,
                                        "fields": self.fields
                                        }
                                )
        if response.status_code != 200:
            print("Ответ не 200")
            exit()
        data = response.json()
        return data["response"]["items"]

    def get_banned_ids(self):
        friends = self.get_friends()
        banned_ids = []
        for friend in friends:
            if friend.get('deactivated') == 'banned':
                banned_ids.append(friend.get('id'))
            # print(banned_ids)
        return banned_ids

    def get_deleted_ids(self):
        friends = self.get_friends()
        deleted_ids = []
        for friend in friends:
            if friend.get('deactivated') == 'deleted':
                deleted_ids.append(friend.get('id'))
        print("Нет пользователей удаливших свой аккаунт.")
        return deleted_ids

    def get_dell_banned_ids(self):
        banned_ids = self.get_banned_ids()
        results = []
        for dell_b in banned_ids:
            response = requests.get(f"https://api.vk.com/method/friends.delete",
                                    params={"access_token": self.access_token,
                                            "user_id": dell_b,
                                            "v": self.version}
                                    )
            rez = response.json()
            results.append(rez)
        print("Нет забаненных пользователей.")

        return results

    def name(self):
        self.get_friends()
        self.get_banned_ids()
        self.get_deleted_ids()
        self.get_dell_banned_ids()



if __name__ == "__main__":
    user_id = "Заменить на свой"
    count = "Заменить на свой"
    order = "random"
    fields = "blacklisted, blacklisted_by_me"
    vk_api = VKAPI(user_id, count, order, fields)
    vk_api.name()
