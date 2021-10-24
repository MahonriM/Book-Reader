import pyttsx3
import PyPDF2
Libro=input("Ingresa el nombre del libro con el .pdf")
pdfReader = PyPDF2.PdfFileReader(open(Libro , 'rb'))
speaker=pyttsx3.init()
voices = speaker.getProperty('voices')
print(voices)
speaker.setProperty('voice', voices[2].id)
speaker.setProperty('rate', 120)
rate = speaker.getProperty('rate')
volume = speaker.getProperty('volume')
print(volume)
print(pdfReader.numPages)
print(pdfReader.isEncrypted)
for num in range(6,pdfReader.numPages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    print(text)
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

