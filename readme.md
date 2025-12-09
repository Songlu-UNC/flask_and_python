# Python and PostgreSQL
Simple flask APP to connect Pgsql through python

## Step 1: Create a new codespace use this repo
Everything should be in place, just clone it and run with code provided below

## Step 2: Before you run, set up virtual env
Run this in your IDE terminal, you can choose whatever python eversion as long as it's not older than the one below:

```
pyenv local 3.10.7
pyenv exec python -m venv.venv
sourse .venv/bin/activate
```

Don't forget to run the flask:
```
flask run
```

## Step 3: set up your database url link
in the .env file, change the link to your own database's url
```
DATABASE_URL=insert_your_url
```

## Step 4: install insomnia
Install insomnia: https://insomnia.rest/
we need this to test our app is working or not

## Step 5: How to test the app is working:
Create a new project in insomnia, in the request window(select the "post"), copy paste the url flask generated, and send this message in JSON format:
```
{
    "blog": 1
    "content": "my first blog post"
}

If the response is 201 created and had a message says: content added, then you are success.
You can combine this with your website to create a simple blog for others.

