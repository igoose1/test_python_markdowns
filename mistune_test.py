import mistune
import sys


text = sys.stdin.read()
html = mistune.markdown(text)
html = html.encode('utf-8', "xmlcharrefreplace")
sys.stdout.buffer.write(html)
