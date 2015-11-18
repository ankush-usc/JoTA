import webbrowser
import sys

f = open('helloworld.html','w')
count = 1
for line in sys.stdin:
  line = line.strip()
  line = line.split('#')
  score = line[0]
  message = """<!DOCTYPE html>
  <html lang="en">
  <head>
    <title>Bootstrap Example</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  </head>
  <body>

  <div class="container">
    <h2 align=\"center\">JoTA score: """+score+"""</h2>
    <table class="table">
      <thead>
        <tr class = \"warning\">
          <th>Company</th>
          <th>Skills</th>
          <th>Day since posting</th>
          <th>Position</th>
          <th>Link to website</th>
        </tr>
      </thead>
      <tbody>"""
  f.write(message)

  
  line = eval(line[1])
  for entry in line:
    input_value = entry
    count = count+1
    company = input_value['Company']
    skills = input_value['skills']
    days = input_value['days']
    title = input_value['title']
    link = input_value['link']
    message = """<tr class=\"success\"> <td>"""+company+ """</td>
    <td>"""+skills+"""</td>
    <td>"""+days+"""</td>
    <td>"""+title+"""</td>
    <td><a href='https://www.indeed.com/"""+link+"""'>Link</a></td></tr>"""
    f.write(message)
message = """</tbody>
  </table>
</div>

</body>
</html>
"""
f.write(message)
f.close()

filename = 'file:///Users/meerapatil/JoTA/firstscraper/' + 'helloworld.html'
webbrowser.open_new_tab(filename)
