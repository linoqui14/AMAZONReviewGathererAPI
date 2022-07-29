


 

class Deepy:
    def asciisize(message):
        code = ''
        for x in message:
            code+=(str(ord(x))+"-")
        return code

    def deasciisize(message):
        result = ''
        for x in message.split('-'):
            if x=='':continue
            result+=(chr(int(x)))
        return result

