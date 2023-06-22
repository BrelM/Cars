
# Market Announce Place Project

an efficient solution for creating, viewing, updating and deleting car sales ads

## Deployment

To deploy this project run you need to:

1- install a Virtual Environment

```bash
  python -m venv mkPlace
```

2- Enter the Virtual Environment 

```bash
  cd .\mkPlace\
```
3- now activate Virtual Environment

```bash
  source Scripts/activate.bat
```

4- Install Django in your virtual Environment

```bash
  pip install django
```

5- clone the git project in your Virtual  Environment

```bash
  git clone https://github.com/BrelM/Cars.git
```

6- install required dependencies

- mysqlclient

  ```bash
    pip install mysqlclient
  ```

- pillow

  ```bash
    pip install pillow
  ```

7- path to manage.py

```bash
  cd .\Cars\Cars
```

8- Start the Server

```bash
  python manage.py runserver
```

The project is now setup!

## API Reference

### Base URL

```http
  https:127.0.0.1.8000/
```

### Get Users list

Return the list of all registered users in Database

```http
  GET /user/Users/
```

### Get user

return a specific user stored in Database

```http
  GET /user/Users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of User to fetch |

### Create User

Use a Json row params and return a confirmation message

```http
  POST /user/Users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `row params`      | `Json` | **Required**. user Description in a json format |

### Delete user

Delete a specific user stored in Database and return a confirmation.

```http
  DELETE /user/Users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of User to delete |

### Update User

Use a Json row params and return a confirmation message

```http
  POST /user/Users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `row params`      | `Json` | **Required**. user Description in a json format |

## Authors

- [@junssashu](https://www.github.com/junssashu)
- [@junssashu2](https://www.github.com/junssashu2)
- [@BrelM](https://www.github.com/BrelM)
- [@MurphyUser022](https://www.github.com/MurphyUser022)

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

## Licence

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
