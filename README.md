# utf16encodetamper

Just a SQLMap tamper. Tries to bypass WAF protections by encoding SQLMap payloads as utf16.

You should copy this .py file to your tampers folder. 
You can probably find that folder under sqlmap/libexec/tampers, but it's all depending on your installation.

Then, you can call it passing the --tamper utf16encode.py flag in your sqlmap.

Also you can check the tamper is working as expected by routing the requests through a local proxy like Burpsuite,
adding the --proxy http://localhost:8080 flag in your sqlmap.

I hope it's useful to you! :)
