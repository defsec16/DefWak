import os
os.system('clear')
bannerP = ''' \033[32m
    ______             _____            
    | ___ \           |  __ \           
    | |_/ /_ _ ___ ___| |  \/ ___ _ __  
    |  __/ _` / __/ __| | __ / _ \ '_ \ 
    | | | (_| \__ \__ \ |_\ \  __/ | | |
    \_|  \__,_|___/___/\____/\___|_| |_|
    ==========Code by Alisher===========
                '''
print(bannerP)

class List:

    def __init__(self):
        self.items = []

    def __contains__(self, item):
          return item in self.items

    def __iter__(self):
        while len(self.items):
            yield self.items.pop(0)

    def __len__(self):
         return len(self.items)

    def append(self, item, front=False):
         for _ in (item, item.lower(), item.title(), item.upper()):
            if _ in self.items:
                continue

            if front:
             self.items.insert(0, _)
            else:
             self.items.append(_)


class PassGen:

    def __init__(self):
      self.words = []
      self.b_days = []
      self.is_alive = True
      self.password_list = List()
      self.suffix = [_ for _ in range(124)]

    def get_input(self):
      while self.is_alive:
          print('\033[34mВведите ключевое слово это может быть: имя, пароль, номер, символ, день рождения (мм-дд-гггг) или что-то другое...')
          print('\033[34mДля генерации списка паролей введите:\033[36m startgen ')
          print('')
          print('\033[34mEnter a keyword, it can be: name, password, number, symbol, birthday (mm-dd-yyyy) or something else ...')
          print('\033[34mTo generate a list of passwords, enter:\033[36m startgen')

          try:
            user_input = str(input('\n\033[31mPassGen\033[39m~#: ')).strip()
          except:
            self.is_alive = False

          if not self.is_alive or not user_input:
            continue

          if user_input.lower() != 'startgen':
            self.append_data(user_input)
          else:
            self.generate()
            self.is_alive = False
            continue

          print('\n')

    def append_data(self, data):
        if len(data.split('-')) == 3:  # день рождения
            if not data in self.b_days:
                self.b_days.append(data)

        elif data.isdigit():  # номер
            if not data in self.suffix:
                self.suffix.insert(0, data)
            self.password_list.append(data, front=True)

        elif len([_ for _ in data if _.isdigit()]) == (len(data) - 1):  # float
            if not data in self.suffix:
                self.suffix.insert(0, data)
                self.suffix.insert(0, ''.join(
                    [_ for _ in data if _.isdigit()]))
            self.password_list.append(data, front=True)

            self.password_list.append(''.join(
                [_ for _ in data if _.isdigit()]), front=True)

        elif data.isalpha(): 
            if not data.lower() in self.words:
                self.words.append(data)

        elif len([_ for _ in data if not _.isalpha() and not _.isdigit()]) == len(data): 
            if not data in self.suffix:
                self.suffix.insert(0, data)

        else:  # пароль
            self.password_list.append(data, front=True)

    def generate(self):
        print('\033[32mСоздание списка, это может занять некоторое время... ')
        for suffix in self.suffix:

            for word in self.words:

                self.password_list.append(word)
                self.password_list.append(f'{word}{suffix}')
                self.password_list.append(f'{suffix}{word}')
                self.password_list.append(f'{suffix}{word}{suffix}')

                for bday in self.b_days:

                    day = bday.split('-')[1]
                    month = bday.split('-')[0]
                    year = bday.split('-')[-1]
                    plain_bday = bday.replace('-', '')

                    self.password_list.append(plain_bday)
                    self.password_list.append(f'{word}{year}')
                    self.password_list.append(f'{word}{year[2:]}')
                    self.password_list.append(f'{word}{plain_bday}')

                    self.password_list.append(f'{day}{word}')
                    self.password_list.append(f'{day[-1]}{word}')

                    self.password_list.append(f'{year}{word}')
                    self.password_list.append(f'{year[2:]}{word}')

                    self.password_list.append(f'{month}{word}')
                    self.password_list.append(f'{month[-1]}{word}')

                    self.password_list.append(f'{month}{day}{word}')
                    self.password_list.append(f'{month[-1]}{day}{word}')
                    self.password_list.append(f'{month}{day[-1]}{word}')
                    self.password_list.append(f'{month[-1]}{day[-1]}{word}')

                    self.password_list.append(f'{day}{month}{word}')
                    self.password_list.append(f'{day[-1]}{month}{word}')
                    self.password_list.append(f'{day}{month[-1]}{word}')
                    self.password_list.append(f'{day[-1]}{month[-1]}{word}')

                    self.password_list.append(f'{month}{day}{word}{year}')
                    self.password_list.append(f'{month}{day}{word}{year[2:]}')

                    self.password_list.append(f'{month[-1]}{day}{word}{year}')
                    self.password_list.append(
                        f'{month[-1]}{day}{word}{year[2:]}')

                    self.password_list.append(f'{month}{day[-1]}{word}{year}')
                    self.password_list.append(
                        f'{month}{day[-1]}{word}{year[2:]}')

                    self.password_list.append(
                        f'{month[-1]}{day[-1]}{word}{year}')
                    self.password_list.append(
                        f'{month[-1]}{day[-1]}{word}{year[2:]}')

                    self.password_list.append(f'{month}{word}{suffix}')
                    self.password_list.append(f'{month[-1]}{word}{suffix}')

                    self.password_list.append(f'{day}{word}{suffix}')
                    self.password_list.append(f'{day[-1]}{word}{suffix}')

                    self.password_list.append(f'{suffix}{word}{month}')
                    self.password_list.append(f'{suffix}{word}{month[-1]}')

                    self.password_list.append(f'{suffix}{word}{day}')
                    self.password_list.append(f'{suffix}{word}{day[-1]}')

                    self.password_list.append(f'{suffix}{word}{year}')
                    self.password_list.append(f'{suffix}{word}{year[2:]}')

        with open('passwords.txt', 'wt', encoding='utf-8') as output_file:

            print(
                f'\033[32mСоздан список {len(self.password_list)} пароли ...')

            for pwd in self.password_list:
                output_file.write(f'{pwd}\n')


if __name__ == '__main__':
    PassGen().get_input()
