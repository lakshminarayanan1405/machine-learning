from gtts import gTTS
import os
mytext="HI you are started to learnig AI and ML"
language="en"
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")  