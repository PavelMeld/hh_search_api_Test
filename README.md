# HH /vacancies API endpoint test

### Запуск
 * Pyhton 3.x required <br/>`$ python3.7 main.py`

### Тесты
#### Пустой запрос

|Test-case| Request | Response |
|--|--|--|
| a |empty GET request _without_ `User-agent` header|`HTTP 400(BAD REQUEST)`|
|b |empty GET request _with_ `User-agent` header|`HTTP 200(OK)`|

#### Простой запрос
Выполняется простой запрос, с заданным значением поля `text` и полем `search_field="name"` для сужения области теста.
Ответ должен содержать хотя бы одну запись `items`, в которой поле `name` содержит исхомое значение.

|Test-case| Request | Response1 |
|--|--|--|
| Cyrillic | text="Программист" & search_field="name" |items[_i_].`name` содержит текст "Программист"|
| Latin | text="Programmer" & search_field="name" |items[_i_].`name` содержит текст "Programmer"|

#### Тест длины входных данных.
Выполняется проверка ответа на запрос произвольной длины.

|Test-case| Request | Response |
|--|--|--|
| small | text= 100 x 'a' |`HTTP 200(OK)`|
| large | text= 31k x 'a' |`HTTP 200(OK)` or `414(URI TOO LONG)`|
| large+1k | text= 32k x 'a' |`HTTP 200(OK)` or `414(URI TOO LONG)`|
| huge | text= 50k x 'a' |`HTTP 200(OK)` or `414(URI TOO LONG)`|
| ddos | text= 100k x 'a' |`HTTP 200(OK)` or `414(URI TOO LONG)`|
