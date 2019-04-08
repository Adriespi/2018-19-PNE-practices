import http.server
import socketserver
import termcolor
from seq6 import Seq

PORT = 8005

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/" or self.path.startswith("/seq") :
            termcolor.cprint(self.requestline, 'green')
            print(self.path)
            f = open("menu.html", "r")
            content = f.read()
        elif self.path.startswith("/myserver") :
            print("hola")
            listinfo = self.path.split("&")
            option_list = []
            for element in listinfo:
                print(element)
                if element.startswith("chk"):
                    option_list.append(1)
            hey = listinfo[0].index("=")
            message = listinfo[0][(hey+1):]
            list_work = []
            list_work.append(message)
            message = Seq(message)
            for letter in message.strbases :
                if letter != "A" and letter != "C" and letter != "G" and letter != "T" :
                    f = open("error.html", "r")
                    content = f.read()
                    list_work.append("Sorry, wrong sequence")
            if "incorrect sequence" not in list_work :
                if 1 in option_list :
                    list_work.append(message.len())
                for element in listinfo :
                    if element.startswith("operation") :
                        number = listinfo.index(element)
                        operation = listinfo[number]
                        hey2 = operation.index("=")
                        operation = operation[(hey2 + 1):]
                    elif element.startswith("base") :
                        number = listinfo.index(element)
                        base = listinfo[number]
                        hey3 = base.index("=")
                        base = base[(hey3 + 1) :]
                if operation == "count":
                    string_1 = "The operation done is : count and {}".format(base)
                    list_work.append(string_1)
                    list_work.append(message.count(base))
                elif operation == "perc":
                    string_2 = "The operation done is : percentage and {}".format(base)
                    list_work.append(string_2)
                    list_work.append(message.perc(base))
                f = open("sequence.html" , "w")
                if 1 in option_list :
                    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sequence information</title>
</head>
<body> 
 Sequence : {} <br>
 Length : {} <br>
 {} <br>
 Result : {} <br>
</body>
</html>'''.format(list_work[0] , list_work[1] , list_work[2] , list_work[3]))
                else :
                    f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sequence information</title>
</head>
<body> 
 Sequence : {} <br>
 {} <br>
 Result : {} <br>
</body>
</html>'''.format(list_work[0], list_work[1], list_work[2]))
                f.close()
                f = open("sequence.html", "r")
                content = f.read()
                print(list_work)
        else :
            f = open("error1.html" , "r")
            content = f.read()
            f.close()






        self.send_response(200)

        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))


with socketserver.TCPServer(("", PORT), TestHandler) as httpd:

    print("Serving at PORT : {}".format(PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()