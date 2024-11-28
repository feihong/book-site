import sys
import json
from pathlib import Path
import util

input_dir = Path(sys.argv[1])
output_dir = Path(__file__).parent / 'output'

def get_book():
  return json.loads((input_dir / 'book.json').read_bytes())


def generate_chapter(chapter: dict):
  template = util.get_template('site-chapter.html')
  output = template.render(title=chapter['title'], paragraphs=chapter['paragraphs'])
  output_file=(output_dir / chapter['title']).with_suffix('.html')
  output_file.write_text(output)


def generate_index(book: dict):
  template = util.get_template('site-index.html')
  output = template.render(**book)
  output_file = output_dir / 'index.html'
  output_file.write_text(output)


if __name__ == '__main__':
  book = get_book()

  for chapter in book['chapters']:
    chapter['paragraphs'] = chapter['body'].splitlines()

  generate_index(book)

  for chapter in book['chapters']:
    generate_chapter(chapter)
