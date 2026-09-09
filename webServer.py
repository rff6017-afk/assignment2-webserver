# import socket module
from socket import *
import os
# In order to terminate the program
import sys


def build_response(status_line, body, content_type="text/html"):
    body_bytes = body if isinstance(body, bytes) else body.encode()
    headers = (
        f"{status_line}\r\n"
        f"Server: SimplePythonServer/1.0\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {len(body_bytes)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    return headers.encode() + body_bytes

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen()
  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = socket.accept(serverSocket) # Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024)#Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1]

      file = filename[1:]
      
      #opens the client requested file. 
      if os.path.isfile(file):
        with open(file) as f:
          # fill in start 
          # Do SOmething
          data = f.read()
          # fill in end
          

        #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
        #Fill in start 
                
        #Content-Type is an example on how to send a header as bytes. There are more!
        response = build_response("HTTP/1.1 200 OK", data)
        #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html

        #Fill in end
                
        # for i in f: #for line in file
        #Fill in start - append your html file contents #Fill in end 
          
        #Send the content of the requested file to the client (don't forget the headers you created)!
        #Send everything as one send command, do not send one line/item at a time!

        # Fill in start

      else:
        body = "<html><body><h1>404 Not Found</h1></body></html>"
        response = build_response("HTTP/1.1 404 Not Found", body)

      connectionSocket.sendall(response)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      body = "<html><body><h1>404 Not Found</h1></body></html>"
      response = build_response("HTTP/1.1 404 Not Found", body)
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()

      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
