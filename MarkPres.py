html = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>presentation</title>
  <link rel="stylesheet" href="MarkPres.css"/>
</head>
<body>

<div id="splash"> 
       <p> Created with MarkPres </p>
       <div class="signal"></div>
</div> 


'''

ctr = 0

def checkstyle(text):
  if "**" in text:
    text = "<b> " + text.replace("**","").strip() + " </b>"
  if "*" in text:
    text = "<i> " + text.replace("*","").strip() + " </i>"
  if "~~" in text:
    text = "<del> " + text.replace("~~","").strip() + " </del>"
  return text

currentsection = '''<section class="s''' + str(ctr) + '''"> \n'''


markdown_path = 'presentation.md' # <| your path here
md = open(markdown_path, 'r', encoding='utf8').readlines() ## !encoding

for line in md:
  if line.isspace():
    continue
    
  if "######" in line:
    currentsection += "      <h6> " + checkstyle(line.replace("######","").strip()) + " </h6> \n"
    continue

  if "#####" in line:
    currentsection += "     <h5> " + checkstyle(line.replace("#####","").strip()) + " </h5> \n"
    continue

  if "####" in line:
    currentsection += "    <h4> " + checkstyle(line.replace("####","").strip()) + " </h4> \n"
    continue

  if "###" in line:
    currentsection += "   <h3> " + checkstyle(line.replace("###","").strip()) + " </h3> \n"
    continue

  if "##" in line:
    currentsection += "  <h2> " + checkstyle(line.replace("##","").strip()) + " </h2> \n"
    continue

  if "#" in line:
    currentsection += " <h1> " + checkstyle(line.replace("#","").strip()) + " </h1> \n"
    continue

  if "![" in line:
    [caption, path] = line.strip("![)\n").split("](")
    term = path.split('.')[-1]
    if term.upper() in ["PNG", "JPG", "JPEG", "GIF", "BMP"]:
      currentsection += ''' <figure> <img src="''' + path + '''" alt="''' + caption + "\"/> </figure> \n"
      currentsection += " <p class=\"caption\"> " + checkstyle(caption) + " </p> \n"
      continue

    if term.upper() in ["MP4", "WEBM"]:
      currentsection += ''' <video controls> <source src="''' + path + '''" type=video/''' + term + "> </video> \n"
      currentsection += " <p class=\"caption\"> " + checkstyle(caption) + " </p> \n"
      continue

    if term.upper() in ["OGG", "WAV", "FLAC"]:
      currentsection += ''' <audio controls> <source src="''' + path + '''" type=audio/''' + term + "> </audio> \n"
      currentsection += " <p class=\"caption\"> " + checkstyle(caption) + " </p> \n"
      continue

  if "---" in line:
    ctr += 1
    html += currentsection + "</section> \n \n"
    currentsection = '''<section class="s''' + str(ctr) + '''"> \n'''
    continue

  currentsection += "       <p> " + checkstyle(line.strip()) + " </p> \n"
  

html += '</body>\n<script src="MarkPres.js"></script>\n</html>'

# print(html)

save = open(markdown_path.replace("md","html"), 'w', encoding='utf8').writelines(html) ## !encoding


css = '''
:root{
  --background_color: #2D3235;
  --foreground_color: #202426;'''

for i in range(ctr):
  css+= "\n  --font_multiplier_" + str(i) + ":1.0;"
css += "\n}\n"


for i in range(ctr):
  n = str(i)
  css += f'''.s{n} {{
  font-size: calc(var(--font_multiplier_{n}) * 1vw);
}}
.s{n}>h1, .s{n}>h2, .s{n}>h3, .s{n}>h4, .s{n}>h5, .s{n}>h6 {{
  text-indent: calc(var(--font_multiplier_{n}) * 1vw);
}}
.s{n}>p {{
  text-indent: calc(var(--font_multiplier_{n}) * 2vw);
}}

'''

css += '''

/* static */


@font-face {
  font-family: Medium;
  src:url(media/Montserrat-Medium.ttf);
}

@font-face {
  font-family: Light;
  src:url(media/Montserrat-Light.ttf);
}

@font-face {
  font-family: Bold;
  src:url(media/Montserrat-Bold.ttf);
}

html, body{
  background: var(--background_color);
  color: white;
}

h1, h2, h3, h4, h5, h6 {
  font-family: Medium;
  font-size: inherit;
}

p{
  font-family: Light;
  font-size: inherit;
}

.btn{
  filter: blur(1px)
}

.btn{
  transition-property: width, left;
  transition-duration: 0.5s;
}

@keyframes op {
  from {opacity: 0;}
  to {opacity: 1;}
}

section{
  margin: auto;
  width: fit-content;
  height: fit-content;
  animation-name: op;
  animation-duration: 1s;
}

img, video, audio{
  background: white;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

@media print{
  section{
    page-break-after: always;
  }
}

.caption {
  text-align: center;
}

#splash {
  z-index: 1;
  text-align: center;
  font-family: Bold;
  background: black;
  position: fixed;
  padding-top: 30vh;
  font-size: 5vh;
  top: 0px;
  left: 0px;
  width: 100vw;
  height: 100vh;
}

.signal {
  border: 5px solid rgb(255, 255, 255);
  border-radius: 30px;
  height: 30px;
  left: 50%;
  margin: -15px 0 0 -15px;
  opacity: 0;
  position: absolute;
  top: 50%;
  width: 30px;

  animation: pulsate 1s ease-out;
  animation-iteration-count: infinite;
}

@keyframes pulsate {
  0% {
    transform: scale(.1);
    opacity: 0.0;
  }
  50% {
    opacity: 1;
  }
  100% {
    transform: scale(1.2);
    opacity: 0;
  }
}
'''

print(css)

save = open("MarkPres.css", 'w', encoding='utf8').writelines(css)