#Q1:-
print("#The apps.twitter.com application interface offers the ability to generate an access token and secret for the owner of the application. This is useful if:")
print("*Your application only needs to make requests on behalf of a single user.(for example, establishing a connection to the Streaming API).")
print("*You wish to test API functionality from a single account before building out the 3-Legged OAuth flow.")
print("#Generating access tokens:-")
print("*Login to the apps.twitter.com interface using your Twitter credentials.")
print("*Create an app or open an existing app that you would like to create access tokens for.")
print("*Navigate to the 'Keys and Access Tokens' page.")
print("*Scroll down and click on the 'Create my access token' button.")
print("*Take note of your access token as you will use in to access certain API endpoints.")
print("#Next Steps:-")
print("*Start with the OAuth basics.")
print("*Generate a bearer token for application authentication (app-only auth).")
print("*Securing Keys and Access Tokens.")

#Q2:-
import socket
print("Twitter IP-address:- ",socket.gethostbyname("www.twitter.com"))
print("Facebook IP-address:- ",socket.gethostbyname("www.facebook.com"))
print("Yahoo IP-address:- ",socket.gethostbyname("www.yahoo.com"))
print("Google IP-address:- ",socket.gethostbyname("www.google.com"))


#Q4:-What is the difference between library and API.Figure it out with an example.
print('''Libray:- A library contains re-usable chunks of code (a software program).

    These re-usable codes of library is linked to your program through APIs (Application Programming Interfaces). 
    That is, API is interface to library through which re-usable codes are linked to an application program.
    In simple term it can be said that an API is an interface between two software programs which facilitates the interaction between them.
    For example, in procedural languages like C, the library math.c contains the implementations of mathematical function, 
    such as sqrt, exp, log etc. It contains the definition of all these functions.

    These function can be referenced by using the API math.h which describes and prescribes the expected behavior.
    Library is written in same language which is a collection of all the functionalities required for the use case.
    For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, 
    along with a large collection of high-level mathematical functions to operate on these arrays.

API:- API is a part of library which defines how an application communicates with external code.
    API can be written in any language.
    API is part of library that defines how it will interact with external code. 
    Every library has API, API is sum of all public/exported stuff. Nowadays meaning of API is widened. 
    we might call the way web site/service interact with code as API also. 
    You can also tell that some device has API - the set of commands you can call.

    Sometimes this terms can be mixed together. 
    For example, you have some server app (like TFS for example). 
    It has API with it, and this API is implemented as a library. 
    But this library is just a middle layer between you and not the one who executes your calls. 
    But if library itself contains all action code then we can't say that this library is API.
''')

