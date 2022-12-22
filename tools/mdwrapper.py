import sys
import markdown
import codecs
import re
import os

if len(sys.argv) > 1 and sys.argv[1] == 'prepare':
    # create menu template
    with codecs.open('misc/menu.md', mode='r', encoding='utf-8') as f:
        menu = f.read()
    with codecs.open('tmp/menu-template.html', mode='w', encoding='utf-8') as f:
        f.write(markdown.markdown(menu, extensions=['extra']))
    sys.exit(0)

if len(sys.argv) > 1:
        filename = sys.argv[1]
        filename_relative = os.path.relpath(filename, 'tmp').replace('\\', '/')
        filename_no_ext = os.path.splitext(filename_relative)[0]
        with codecs.open(filename, mode='r', encoding='utf-8') as f:
                text = f.read()
else:
        filename = 'stdin'
        filename_relative = 'stdin'
        filename_no_ext = 'stdin'
        with codecs.getreader('utf-8')(sys.stdin) as f:
                text = f.read()

# load menu template
with codecs.open('tmp/menu-template.html', mode='r', encoding='utf-8') as f:
        menu = f.read()

title = text.split('\n', 1)[0]
title = re.match('#*\\s*(.+)', title).group(1)
sys.stdout.write("""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<link rel="icon" href="/favicon.ico" sizes="16x16" type="image/vnd.microsoft.icon">
<link href="/style.css" rel="stylesheet" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,800' rel='stylesheet' type='text/css'>
<style>
#menu a[href="%s.html"] {
  font-weight: bold;
}
</style>
</head>
<a name="top"></a>
<body>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-52069457-1', 'llbit.se');
  ga('send', 'pageview');
</script>
  <div class="hint">&#x1F389; Chunky 2.4.1 is out! Visit the <a href="https://chunky-dev.github.io/docs" target="_blank">new website</a> for detailed guides, downloads, plugins and more.</div>
  <table id="wrapper">
    <tr id="content">
      <td id="menu">
        <a href="/index.html" id="logo">Chunky</a>
""" % (title, filename_no_ext))
sys.stdout.write(menu)
sys.stdout.write("""
      </td>
      <!--Content goes here -->
      <td id="article">
""")
sys.stdout.write(markdown.markdown(text, extensions=['extra']))
sys.stdout.write("""
      <div id="footer"><a href="https://github.com/llbit/chunky-docs/edit/master/docs/%s">Edit page</a></div>
      </td>
    </tr>
  </table>
</body>
</html>""" % filename_relative)
sys.stdout.flush()
