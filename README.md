# API Reference

## Base URL

```http
  https:127.0.0.1.8000/
```

## Get Users list

Return the list of all registered users in Database

```http
  GET /user/Users/
```

## Get user

return a specific user stored in Database

```http
  GET /user/Users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of User to fetch |

## Create User

Use a Json row params and return a confirmation message

```http
  POST /user/Users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `row params`      | `Json` | **Required**. user Description in a json format |

## Delete user

Delete a specific user stored in Database and return a confirmation.

```http
  DELETE /user/Users/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of User to delete |

## Update User

Use a Json row params and return a confirmation message

```http
  POST /user/Users/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `row params`      | `Json` | **Required**. user Description in a json format |
