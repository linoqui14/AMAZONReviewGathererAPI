


 

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
            try:
                result+=(chr(int(x)))
            except:
                continue
        return result

