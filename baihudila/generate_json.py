"""
Source: https://annas-archive.org/md5/a8e1dfe801e44a6c6c06d1020bfc4021

"""

import re
from pathlib import Path
import json


title = '白狐迪拉与月亮石'
author = '陈佳同'
input_file = Path('book.txt')
output_file = Path('book.json')


class Chapter:
  def __init__(self, title):
    self.title = title
    self.body = []

  def append(self, line):
    self.body.append(line)

def get_lines():
  with input_file.open('r') as fp:
    for line in fp:
      line = line.strip()
      if line:
        yield line

def get_chapters(lines):
  chapter = None

  for line in lines:
    if line == '（全书完）':
      break

    if re.match(r'文前辅文|第[一二三四五六七八九十]{1,2}章 ', line):
      if chapter is not None:
        yield chapter
      chapter = Chapter(line)
    else:
      if chapter is not None:
        chapter.append(line)

  if chapter is not None:
    yield chapter


if __name__ == '__main__':
  lines = get_lines()
  # Ignore chapters that contain no content
  chapters = [chapter for chapter in get_chapters(lines) if len(chapter.body) > 1]

  with output_file.open('w') as fp:
    obj = dict(
      title=title,
      author=author,
      chapters=[dict(title=c.title, body='\n'.join(c.body)) for c in chapters],
    )
    json.dump(obj, fp, indent=2, ensure_ascii=False)
    print(f'Generated {output_file}')
