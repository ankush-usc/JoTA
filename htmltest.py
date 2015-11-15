__author__ = 'meerapatil'
import webbrowser
f = open('helloworld.html','w')
file=open('myInput.txt','r')
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
  <h2 align=\"center\">Listings based on Location</h2>
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
for line in file:
    job = line.split('::')
    company = job[1]
    skills = job[2]
    days = job[3]
    title = job[4]
    link = job[5]
    print link
    message = """<tr class=\"success\"> <td>"""+company+ """</td>
    <td>"""+skills+"""</td>
    <td>"""+days+"""</td>
    <td>"""+title+"""</td>
    <td><a href=\"https://www.google.com/?gws_rd=ssl\">"""+link+"""</td></tr>"""
    f.write(message)
message = """</tbody>
  </table>
</div>

</body>
</html>
"""
f.write(message)
f.close()

filename = 'file:///Users/meerapatil/JoTA/' + 'helloworld.html'
webbrowser.open_new_tab(filename)
