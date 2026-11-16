from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP Protocols</title>
</head>
<body>

    <h2>List of TCP Protocols</h2>

    <ol>
        <li>HTTP</li>
        <li>HTTPS</li>
        <li>FTP</li>
        <li>SMTP</li>
        <li>SSH</li>
        <li>Telnet</li>
        <li>POP3</li>
        <li>IMAP</li>
    </ol>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

