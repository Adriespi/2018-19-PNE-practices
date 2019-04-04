import json
import termcolor
import http.client

def endpoint(enpt):

    """ This is a function to get the information asked when using different endpoints. We recieve a tuple with first
     the information given by the endpoint ans second the status line of the connection."""

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection! If we do not specify the port, the standard one will be used
    conn = http.client.HTTPSConnection(HOSTNAME)
    conn.request(METHOD, enpt, None, headers)
    r1 = conn.getresponse()
    text_json = r1.read().decode("utf-8")

    # -- print status line
    status = "\nResponse received: {}{}".format(r1.status, r1.reason)
    conn.close()

    return text_json, status


HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = "Adriespi"
METHOD = "GET"
REPOS = "/repos"

enpt = ENDPOINT + GITHUB_ID
enpt1 = ENDPOINT + GITHUB_ID + REPOS

user = json.loads(endpoint(enpt)[0])
userrep = json.loads(endpoint(enpt1)[0])


def repossearch(num):
    reposname = userrep[num]['name']
    return reposname

print(user)
print(userrep)


login = user['login']
name = user['name']
bio = user['bio']
nrepos = user['public_repos']

print()
print("User: {}".format(login))
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))
print("Bio: {}\n\n".format(bio))


def repossearch(num):
    reposname = userrep[num]['name']
    return reposname
num = int(nrepos)

print("List of repositories: \n")
for i in range(num):
    print('--->',repossearch(i))