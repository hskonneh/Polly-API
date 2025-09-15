# API Functions Documentation

This document provides detailed information about specific API functions.

### `cast_vote`

- **Endpoint:** `POST /polls/{poll_id}/vote`
- **Headers:** `Authorization: Bearer <access_token>`
- **Body:**

```json
{
  "option_id": 1
}
```

- **Description:** Allows an authenticated user to cast a vote on a specific poll option. The `poll_id` in the path specifies the target poll, and `option_id` in the request body indicates the chosen option.

### `get_poll_results`

- **Endpoint:** `GET /polls/{poll_id}/results`
- **Authentication:** Not required
- **Response:**

```json
{
  "poll_id": 1,
  "question": "Your poll question",
  "results": [
    {
      "option_id": 1,
      "text": "Option 1",
      "vote_count": 3
    },
    {
      "option_id": 2,
      "text": "Option 2",
      "vote_count": 1
    }
  ]
}
```

- **Description:** Retrieves the current results for a specific poll, identified by `poll_id`. This endpoint does not require authentication and returns the poll question along with a list of options and their respective vote counts.