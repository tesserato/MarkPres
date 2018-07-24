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

currentsection = "<section> \n"


markdown_path = 'presentation.md' # <| your path here
md = open(markdown_path, 'r', encoding='utf8').readlines() ## !encoding

for line in md:
  if line.isspace():
    continue
    
  if "######" in line:
    currentsection += "<h6> " + line.replace("######","").strip() + " </h6> \n"
    continue

  if "#####" in line:
    currentsection += "<h5> " + line.replace("#####","").strip() + " </h5> \n"
    continue

  if "####" in line:
    currentsection += "<h4> " + line.replace("####","").strip() + " </h4> \n"
    continue

  if "###" in line:
    currentsection += "<h3> " + line.replace("###","").strip() + " </h3> \n"
    continue

  if "##" in line:
    currentsection += "<h2> " + line.replace("##","").strip() + " </h2> \n"
    continue

  if "#" in line:
    currentsection += "<h1> " + line.replace("#","").strip() + " </h1> \n"
    continue

  if "![" in line:
    [caption, path] = line.strip("![)\n").split("](")
    term = path.split('.')[-1]
    if term.upper() in ["PNG", "JPG", "JPEG"]:
      currentsection += '''<figure> <img src="''' + path + '''" alt="''' + caption + "\"/> </figure> \n"
      continue
    if term.upper() in ["MP4", "WEBM"]:
      currentsection += '''<video controls> <source src="''' + path + '''" type=video/''' + term + "> </video> \n"


    # print(caption, path)
    continue




  if "---" in line:
    html += currentsection + "</section> \n \n"
    currentsection = "<section> \n"
    continue

  currentsection += "<p> " + line.strip() + " </p> \n"
  

html += '</body>\n<script src="MarkPres.js"></script>\n</html>'


print(html)

save = open(markdown_path.replace("md","html"), 'w', encoding='utf8').writelines(html) ## !encoding








# filenames = [f for f in os.listdir('./') if '.md' in f]