## Request all boards from
https://api.trello.com/1/members/me/boards

Trello requires your API Key and token be submitted as paramters with every request.
Using the webrequests module this is best done by passing a dictionary to the params arg, like {'key': 'xxx', 'token': 'zzzz'}. You can set each item in the dictionary as a variable, or create a dictionary seperately that you call in requests.get() function.

