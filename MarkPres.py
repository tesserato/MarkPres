html = '''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>presentation</title>
  <link rel="stylesheet" href="MarkPres.css"/>
  <script src="MarkPres.js"></script>
</head>
<body>

'''

def checkstyle(text):
  if "**" in text:
    text = "<b> " + text.replace("**","").strip() + " </b>"
  if "*" in text:
    text = "<i> " + text.replace("*","").strip() + " </i>"
  if "~~" in text:
    text = "<del> " + text.replace("~~","").strip() + " </del>"
  return text

currentsection = "<section> \n"


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
      currentsection += " <p> <em> " + checkstyle(caption) + " </em> </p> \n"
      continue

    if term.upper() in ["MP4", "WEBM"]:
      currentsection += ''' <video controls> <source src="''' + path + '''" type=video/''' + term + "> </video> \n"
      currentsection += " <p> <em> " + checkstyle(caption) + " </em> </p> \n"
      continue

    if term.upper() in ["OGG", "WAV", "FLAC"]:
      currentsection += ''' <audio controls> <source src="''' + path + '''" type=audio/''' + term + "> </audio> \n"
      currentsection += " <p> <em> " + checkstyle(caption) + " </em> </p> \n"
    

  if "---" in line:
    html += currentsection + "</section> \n \n"
    currentsection = "<section> \n"
    continue

  currentsection += "       <p> " + checkstyle(line.strip()) + " </p> \n"
  

html += '</body>\n<script src="MarkPres.js"></script>\n</html>'

print(html)

save = open(markdown_path.replace("md","html"), 'w', encoding='utf8').writelines(html) ## !encoding